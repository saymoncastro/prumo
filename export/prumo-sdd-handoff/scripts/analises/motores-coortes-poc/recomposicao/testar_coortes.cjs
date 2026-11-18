/* Validação histórica do motor de coortes (§ 15.5 do documento fundador).
   Calibra com 2017–2021, prevê 2022–2025 com os ingressos observados e compara com a PNP.
   Executar da raiz:  node poc/testar_coortes.cjs  (requer poc/dados-recomposicao.json) */
const assert = require('assert');
const C = require('./coortes.js');
const D = require('./dados-recomposicao.json');

let falhas = 0;
const linhas = [];
for (const [campus, v] of Object.entries(D.campi)) {
  for (const of of v.ofertas) {
    if (!C.REGULARES.includes(of.tipo) || !of.serie['2025']) continue;
    const val = C.validar(of);
    linhas.push([campus, of.curso, of.oferta, val ? `D=${val.D} r=${val.r.toFixed(2)} erro ${(100 * val.erro).toFixed(1)}%` : 'sem série suficiente']);
  }
}
console.table(linhas);

function erroDe(campus, curso, oferta) {
  const of = D.campi[campus].ofertas.find(o => o.curso === curso && o.oferta === oferta);
  assert(of, `oferta ausente: ${curso}`);
  return C.validar(of);
}
function checar(nome, cond) { if (!cond) { falhas++; console.error('FALHOU:', nome); } else console.log('ok:', nome); }

// técnicos integrados de Itapina: o modelo simples reproduz o passado com erro médio abaixo de 5%
for (const c of ['Técnico em Agropecuária', 'Técnico em Zootecnia', 'Técnico em Alimentos']) {
  const v = erroDe('Itapina', c, 'Integrado');
  checar(`${c} integrado, erro ${(100 * v.erro).toFixed(1)}% < 5%`, v && v.erro < 0.05);
}
// projeção ancorada: sem decisão, o primeiro ano projetado parte da matrícula observada em 2025
const of = D.campi.Itapina.ofertas.find(o => o.curso === 'Técnico em Alimentos' && o.oferta === 'Integrado');
const cal = C.calibrar(of);
const p = C.projetar({ hist: of, D: cal.D, T: cal.T, r: cal.r, phi: cal.phi, meRatio: 1, vagasFut: {}, ocup: {}, turma: 40 }, 2029);
checar('suspensão de ingressos: matrícula decresce e zera quando a última coorte conclui', p[2026].mat < C.matr(of, 2025) && p[2028].mat < 1e-9 && p[2029].mat < 1e-9);
const ampl = C.projetar({ hist: of, D: cal.D, T: cal.T, r: cal.r, phi: cal.phi, meRatio: 1,
  vagasFut: { 2026: 36, 2027: 72, 2028: 72, 2029: 72 }, ocup: { 2026: 1, 2027: 1, 2028: 1, 2029: 1 }, turma: 40 }, 2029);
checar('ampliação: turmas simultâneas crescem de 3 para 6', ampl[2026].turmas === 3 && ampl[2029].turmas === 6);
checar('nenhum valor negativo', Object.values(ampl).every(x => x.mat >= 0 && x.ing >= 0 && x.conc >= 0));

if (falhas) { console.error(`${falhas} verificação(ões) falharam`); process.exit(1); }
console.log('todas as verificações passaram');
