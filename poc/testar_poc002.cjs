/* Verificações do motor de coortes e dos dados da POC 0.0.2.
   Executar da raiz:  node poc/testar_poc002.cjs  (requer poc/dados-poc002.json) */
const C = require('./coortes002.js');
const D = require('./dados-poc002.json');

let falhas = 0;
const checar = (nome, cond) => { if (cond) console.log('ok:', nome); else { falhas++; console.error('FALHOU:', nome); } };
const oferta = (campus, curso, of) => D.campi[campus].ofertas.find(o => o.curso === curso && o.oferta === of && o.presencial);
const media = (s, anos, i) => anos.reduce((x, a) => x + s[a][i], 0) / anos.length;

// 1. Dados conferem com a auditoria longitudinal (T9/T14: Ifes, técnico concomitante+subsequente presencial)
const g = D.trajetorias.IFES.concsub, A = ['2017', '2018', '2019'], B = ['2023', '2024', '2025'];
checar('matrículas Ifes concomitante+subsequente 5.881 → 4.409', Math.round(media(g, A, 2)) === 5881 && Math.round(media(g, B, 2)) === 4409);
checar('concluintes Ifes concomitante+subsequente 1.460 → 798', Math.round(media(g, A, 3)) === 1460 && Math.round(media(g, B, 3)) === 798);
checar('formação técnica do Ifes 2025 = 45,1% (PNP)', Math.abs(D.ifes['2025'].ct / D.ifes['2025'].meq - 0.451) < 0.001);

// 2. Calibração: ofertas usadas nas alternativas reproduzem as matrículas de 2023–2025
const tab = [];
for (const [campus, curso, of, lim] of [
  ['Vitória', 'Técnico em Mecânica', 'Concomitante', 0.10], ['Vitória', 'Técnico em Eletrotécnica', 'Concomitante', 0.10],
  ['Vitória', 'Técnico em Eletrotécnica', 'Integrado', 0.10], ['Serra', 'Técnico em Informática', 'Concomitante', 0.15],
  ['Serra', 'Técnico em Informática para Internet', 'Integrado', 0.10]]) {
  const o = oferta(campus, curso, of), k = C.calibrar(o, 0.2);
  tab.push({ campus, curso, of, D: k.D, e: +k.e.toFixed(2), c: k.c, erroMat: +(100 * k.erro.mat).toFixed(1), erroConc: +(100 * k.erro.conc).toFixed(1), teste2025: k.teste && +(100 * k.teste.mat).toFixed(1) });
  checar(`${campus}, ${curso} ${of}: erro de matrículas ${(100 * k.erro.mat).toFixed(1)}% < ${100 * lim}%`, k.erro.mat < lim);
}
console.table(tab);
// integrados de Vitória ajustam melhor com 4 anos do que com 3
const ei = oferta('Vitória', 'Técnico em Eletrotécnica', 'Integrado');
checar('integrado de Vitória: prazo efetivo de 4 anos', C.calibrar(ei, 0.2).D === 4);

// 3. Propriedades da projeção
const mec = oferta('Vitória', 'Técnico em Mecânica', 'Concomitante'), k = C.calibrar(mec, 0.2);
const anos = [2026, 2027, 2028, 2029, 2030, 2031, 2032], cte = v => Object.fromEntries(anos.map(t => [t, v]));
const base = { hist: mec, D: k.D, e: k.e, c: k.c, meRatio: k.meRatio, vagas: cte(144), ocup: cte(k.ocup) };
const P = (extra) => C.projetar({ ...base, ...extra }, 2032);
const m0 = P({});
checar('ancoragem: 2026 sem mudança fica a menos de 15% da matrícula observada em 2025', Math.abs(m0[2026].mat / C.matr(mec, 2025) - 1) < 0.15);
checar('nenhum valor negativo', anos.every(t => ['ing', 'mat', 'prazo', 'ret', 'conc', 'evad'].every(x => m0[t][x] >= 0)));
checar('matrículas = no prazo + retidos', anos.every(t => Math.abs(m0[t].mat - m0[t].prazo - m0[t].ret) < 1e-6));
const amp = P({ vagas: Object.fromEntries(anos.map(t => [t, t >= 2027 ? 180 : 144])) });
checar('ampliar 36 vagas com ocupação 100%: +36 ingressantes por ano', Math.abs(amp[2028].ing - m0[2028].ing - 36 * k.ocup) < 1e-6);
const menosEv = P({ eFut: cte(k.e * 0.7) });
checar('reduzir evasão aumenta matrículas e concluintes', menosEv[2030].mat > m0[2030].mat && menosEv[2030].conc > m0[2030].conc);
const menosRet = P({ cFut: cte(Math.min(1, k.c + 0.3)) });
checar('reduzir retenção reduz retidos e matrículas, sem reduzir concluintes em regime',
  menosRet[2032].ret < m0[2032].ret && menosRet[2032].mat < m0[2032].mat && menosRet[2032].conc >= m0[2032].conc - 1e-6);
const susp = P({ vagas: cte(0) });
checar('suspender ingressos: estoque zera quando a última coorte sai', susp[2026 + k.D + 1].mat < 1e-9);

if (falhas) { console.error(`${falhas} verificação(ões) falharam`); process.exit(1); }
console.log('todas as verificações passaram');
