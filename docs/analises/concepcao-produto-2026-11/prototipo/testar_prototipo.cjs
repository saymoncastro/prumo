/* Verificações do protótipo conceitual (3ª rodada, 13/11/2026). Uso, a partir da raiz do repositório:
     node docs/analises/concepcao-produto-2026-11/prototipo/testar_prototipo.cjs
   Carrega poc/dados-poc002.json, poc/coortes002.js, simulacao.js e pauta.js como a página faz e confere
   as regras que a mesa promete: mesmos resultados da bancada, tempo das coortes, nada contado duas vezes. */
const fs = require('fs'), vm = require('vm'), path = require('path');
const aqui = __dirname, raiz = path.resolve(aqui, '../../../..');
const ctx = { console, Math, JSON, Map, Set, Object }; vm.createContext(ctx);
const v = s => s.replace(/^const /gm, 'var ').replace(/^let /gm, 'var ');
ctx.D = JSON.parse(fs.readFileSync(path.join(raiz, 'poc/dados-poc002.json')));
vm.runInContext(fs.readFileSync(path.join(raiz, 'poc/coortes002.js'), 'utf8') + '\nvar C = Coortes2;', ctx);
vm.runInContext(v(fs.readFileSync(path.join(aqui, 'simulacao.js'), 'utf8')), ctx);
vm.runInContext(`var CP = { vitoria: prepararCampus('vitoria'), serra: prepararCampus('serra') };
var BASE = { vitoria: simular(CP.vitoria, null), serra: simular(CP.serra, null) };
var CAP = { vitoria: capacidadePadrao(BASE.vitoria), serra: capacidadePadrao(BASE.serra) };`, ctx);
vm.runInContext(v(fs.readFileSync(path.join(aqui, 'pauta.js'), 'utf8')), ctx);
const X = ctx;
let falhas = 0;
const ok = (c, m) => { console.log((c ? 'ok: ' : 'FALHOU: ') + m); if (!c) falhas++; };
const igual = (a, b) => JSON.stringify(a) === JSON.stringify(b);

// 1. Alavancas da bancada e lista de operações dão o mesmo resultado
for (const k of ['vitoria', 'serra']) for (const p of ['A', 'B', 'C', 'R']) {
  const a = X.aplicarPreset(X.CP[k], p);
  ok(igual(X.simular(X.CP[k], a).anos, X.simular(X.CP[k], X.opsDe(a)).anos), `${k} ${p}: alavancas = operações`);
}
// 2. Pausa respeita as turmas em andamento: ingresso zera no ano, matrícula cai aos poucos, concluintes depois
const it = X.criarPauta(), pausa = X.efeitoItem(it.find(i => i.id === 'pausa-edif'), it).d;
ok(pausa[2027].mat === 0 && pausa[2028].ing < 0 && pausa[2029].mat < pausa[2028].mat && pausa[2028].conc === 0 && pausa[2030].conc < 0, 'pausa: entrada some em 2028, matrícula cai até 2030, concluintes caem depois');
// 3. Nenhuma decisão do ciclo 2028 mexe nos exercícios até 2029 (ano-base ≤ 2027)
const comp = X.compor(it);
ok([2026, 2027, 2028, 2029].every(e => Math.abs(X.participacao(e, comp.sims) - X.partBase(e)) < 1e-12), 'atraso da matriz: exercícios até 2029 não mudam com a pauta');
// 4. Disputa pelo código: os dois pedidos sinalizados até haver destino; depois só o outro campus fica sem
ok(['reorg-eletro', 'exp-info'].every(id => comp.sinais[id].some(s => s.k === 'disputa')), 'código a decidir: os dois pedidos aparecem em disputa');
it.find(i => i.id === 'cod1').escolha = 'serra';
const c2 = X.compor(it);
ok(c2.caps.serra.adds.filter(a => a.rec === 'area').length === 1 && c2.caps.vitoria.adds.filter(a => a.rec === 'area').length === 0, 'código para Serra: um docente a mais em Serra e nenhum em Vitória');
ok(c2.sinais['reorg-eletro'].some(s => s.k === 'semrecurso') && !c2.sinais['exp-info'].length, 'código para Serra: só Vitória fica sem o recurso');
// 5. Sobreposição: a mesma oferta em dois itens não é somada duas vezes
const it3 = X.criarPauta();
it3.push({ id: 'dup', un: 'serra', curso: it3.find(i => i.id === 'exp-info').curso, tipo: 'expansao', origem: 'teste', estado: 'proposta', incluir: true, titulo: 'duplicado', vars: { base: { n: 'x', ops: X.varDe(it3.find(i => i.id === 'exp-info')).ops } }, var: 'base' });
const c3 = X.compor(it3), c3s = X.compor(X.criarPauta());
ok(c3.sinais.dup.some(s => s.k === 'sobreposto') && igual(c3.sims.serra.anos, c3s.sims.serra.anos), 'item repetido fica fora da soma');
// 6. Os dois caminhos convergem: convite da Reitoria e proposta do curso geram o mesmo item
const met = X.idOf('vitoria', 'Técnico em Metalurgia', 'Concomitante');
const a1 = X.itemCurso('vitoria', met, 'permanencia', { red: 0.25 }, 'Reitoria', 'hipotese'), a2 = X.itemCurso('vitoria', met, 'permanencia', { red: 0.25 }, 'Curso', 'proposta');
ok(a1.id === a2.id && igual(a1.vars, a2.vars), 'convite e proposta do curso convergem no mesmo item');
// 7. Bloco: a variante com obra não muda nada antes de 2030
const mec = it.find(i => i.id === 'exp-mec'), bl = X.efeitoItem(mec, it, 'bloco').d;
ok(bl[2028].mat === 0 && bl[2029].mat === 0 && bl[2030].mat > 0 && !X.efeitoItem(mec, it, 'bloco').rest, 'bloco: efeito só a partir de 2030 e sem restrição de oficina');
ok(X.efeitoItem(mec, it, 'noturno').rest?.ano === 2029, 'sem obra e no turno da procura: oficinas passam de 100% em 2029');
// 8. Ifes pela razão das somas: o percentual do conjunto não é a soma das contribuições por campus
const ct = t => X.ifesEm(t, Object.values(comp.sims)).pct.ct - X.ifesEm(t, Object.values(X.BASE)).pct.ct;
const porCampus = t => ['vitoria', 'serra'].reduce((s, k) => { const o = k === 'vitoria' ? X.BASE.serra : X.BASE.vitoria; return s + X.ifesEm(t, [comp.sims[k], o]).pct.ct - X.ifesEm(t, [X.BASE[k], o]).pct.ct; }, 0);
ok(Math.abs(ct(2031) - porCampus(2031)) > 1e-7, `formação técnica do Ifes recomposta pela razão das somas (${(100 * ct(2031)).toFixed(4)} p.p. × soma das partes ${(100 * porCampus(2031)).toFixed(4)} p.p.)`);

console.log(falhas ? `${falhas} verificação(ões) falharam` : 'todas as verificações passaram');
process.exit(falhas ? 1 : 0);
