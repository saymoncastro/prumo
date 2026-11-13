/* Pauta de decisões, desafio da Reitoria e participação na matriz (3ª rodada, 13/11/2026).
   Depende de simulacao.js (simular, capacidade, ifesEm, refQualidade) e dos objetos CP, BASE e CAP.
   Nada aqui decide: compõe itens, sinaliza conflitos e traduz trajetórias acadêmicas em referência na matriz. */

/* ---------- matriz: partida, total de referência e cenário da Rede ---------- */
const MATRIZ = {
  total: 2205.8e6,             // remanescente do exercício 2026 sem assistência estudantil (fato da fonte)
  ifes0: 73.2e6,               // Funcionamento 62,8 + Reitoria ≈ 7,7 + Qualidade 2,65 (estimado)
  ex0: 2026,                   // último exercício observado; lê o ano-base 2024
  fpDegrau: 1.27e6,            // formação de professores ≥ 20% a partir do exercício 2027, se a reclassificação de 2025 se confirmar
};
MATRIZ.part0 = MATRIZ.ifes0 / MATRIZ.total;
const REDE = {
  junto: { n: 'Rede e Ifes no mesmo ritmo', f: () => 1, nat: 'prem' },
  cresce: { n: 'Rede cresce 1% a.a. a mais', f: ex => Math.pow(0.99, Math.max(0, ex - MATRIZ.ex0)), nat: 'il' },
};
const EXS = []; for (let e = MATRIZ.ex0; e <= FIM; e++) EXS.push(e);
const ANOS4 = [2028, 2029, 2030, 2031];   // os quatro anos letivos do plano de oferta 2028

const DESAFIO = { meta: 0.039, ex: 2030, rede: 'junto', fp: false, publicado: false, macro: { red: 0.2, preencher: true, amplia: 0 } };

function partBase(ex, cen = DESAFIO) {
  return (MATRIZ.part0 + (cen.fp && ex >= 2027 ? MATRIZ.fpDegrau / MATRIZ.total : 0)) * REDE[cen.rede].f(ex);
}
/* Efeito em reais na parcela simulada para o ano-base t (exercício t + 2), comparado a manter.
   MT: marginal de 2026 (R$ 1.324 por MT). Qualidade: percentuais legais pela razão das somas, Rede 2026 constante. */
function dReais(t, sims, extras = []) {
  if (t <= OBS) return { mt: 0, rmt: 0, rq: 0, r: 0 };
  let mt = 0;
  for (const k of Object.keys(sims)) mt += sims[k].anos[t].mt - BASE[k].anos[t].mt;
  for (const e of extras) mt += e(t).mt || 0;
  const pS = ifesEm(t, Object.values(sims), extras).pct, pB = ifesEm(t, Object.keys(sims).map(k => BASE[k])).pct;
  const qS = refQualidade(pS), qB = refQualidade(pB);
  const rq = (qS.ct - qB.ct) + (qS.fp - qB.fp) + (qS.eja - qB.eja);
  return { mt, rmt: mt * PREM.rs_mt, rq, r: mt * PREM.rs_mt + rq };
}
function participacao(ex, sims, extras = [], cen = DESAFIO) {
  return partBase(ex, cen) + dReais(ex - 2, sims, extras).r / MATRIZ.total * REDE[cen.rede].f(ex);
}

/* ---------- itens da pauta ---------- */
const UNID = { vitoria: 'Vitória', serra: 'Serra', itapina: 'Itapina', barra: 'Barra de São Francisco', cefor: 'Cefor (EaD)', reitoria: 'Reitoria' };
const TIPOS = { pausa: 'Pausa de entradas', expansao: 'Expansão', reorganizacao: 'Reorganização', permanencia: 'Permanência', ocupacao: 'Ocupação de vagas', recurso: 'Recurso', proposta: 'Proposta combinada' };
const ESTADOS = { hipotese: 'hipótese simulada', proposta: 'proposta do campus', pactuada: 'contribuição pactuada', observado: 'resultado observado' };
const rampa = (t, de, ate, v) => t < de ? 0 : t >= ate ? v : v * (t - de + 1) / (ate - de + 1);

function idOf(k, curso, oferta) { const o = achar(CP[k], curso, oferta); return o ? o.id : null; }
function nomeOf(k, id) { const o = CP[k].lista.find(x => x.id === id); return o ? o.nome : '?'; }

function criarPauta() {
  const V = (c, o) => idOf('vitoria', c, o), S = (c, o) => idOf('serra', c, o);
  const mecC = V('Técnico em Mecânica', 'Concomitante'), edS = V('Técnico em Edificações', 'Subsequente');
  const elC = V('Técnico em Eletrotécnica', 'Concomitante'), elI = V('Técnico em Eletrotécnica', 'Integrado');
  const estC = V('Técnico em Estradas', 'Concomitante');
  const infI = S('Técnico em Informática para Internet', 'Integrado'), autC = S('Técnico em Automação Industrial', 'Concomitante');
  const amp = (oferta, n, desde, ocup, turno) => ({ t: 'ampliar', oferta, n, desde, ocup, turno, fp: 0.7, fo: 1.2 });
  return [
    { id: 'pausa-edif', un: 'vitoria', curso: edS, tipo: 'pausa', origem: 'Campus', estado: 'proposta', incluir: true,
      titulo: 'Pausar novas entradas em Edificações subsequente (turmas em andamento seguem)',
      motivo: 'Ocupação de 85% e evasão anual de 33% na média 2023–2025; o campus quer rever o projeto do curso antes de reabrir.',
      vars: { base: { n: 'Pausa em 2028', ops: [{ t: 'pausar', oferta: edS, desde: 2028 }] } }, var: 'base',
      acompanhar: { ind: 'Turmas de 2026 e 2027 concluindo no prazo; proposta de novo projeto de curso', resp: 'Direção de ensino de Vitória' } },
    { id: 'exp-mec', un: 'vitoria', curso: mecC, tipo: 'expansao', origem: 'Campus', estado: 'proposta', incluir: true,
      titulo: 'Abrir mais uma turma de Mecânica concomitante (+36 vagas por ano)',
      motivo: '461 inscritos para 144 vagas em 2025. A procura é noturna, e as oficinas já estão em 91% de uso à noite.',
      vars: {
        noturno: { n: 'Noturno, sem obra', ops: [amp(mecC, 36, 2028, 1, 'N')], nota: 'Turno da procura. Oficinas passam de 100% à noite em 2029.' },
        tarde: { n: 'Vespertino, sem obra', ops: [amp(mecC, 36, 2028, 0.7, 'V')], nota: 'Oficinas livres à tarde. Ocupação das novas vagas de 70% (premissa): o público do concomitante estuda de manhã ou trabalha.' },
        bloco: { n: 'Noturno, com bloco de oficinas', ops: [amp(mecC, 36, 2030, 1, 'N')], adds: [{ rec: 'lab', desde: 2030, v: 40 }], nota: 'Bloco pronto para o ano letivo de 2030 (premissa: obra em 2027–2029). Turma nova só entra em 2030.' },
      }, var: 'noturno',
      acompanhar: { ind: 'Vagas ofertadas e ocupação da turma nova', resp: 'Coordenação de Mecânica' } },
    { id: 'reorg-eletro', un: 'vitoria', curso: elI, tipo: 'reorganizacao', origem: 'Campus', estado: 'proposta', incluir: true, requer: 'cod1',
      titulo: 'Transferir 32 vagas de Eletrotécnica concomitante para Eletrotécnica integrado',
      motivo: '600 inscritos para 64 vagas no integrado; evasão de 32% no concomitante. O integrado amplia o núcleo comum.',
      vars: { base: { n: 'A partir de 2028', ops: [{ t: 'reduzir', oferta: elC, n: 32, desde: 2028 }, { ...amp(elI, 32, 2028, 1, null), fp: 0.85, fo: 1 }] } }, var: 'base',
      acompanhar: { ind: 'Ocupação e permanência no 1º ano do integrado', resp: 'Coordenação de Eletrotécnica' } },
    { id: 'exp-info', un: 'serra', curso: infI, tipo: 'expansao', origem: 'Campus', estado: 'proposta', incluir: true, requer: 'cod1',
      titulo: 'Abrir mais uma turma de Informática para Internet integrado (+36 vagas por ano)',
      motivo: '1.765 inscritos para 74 vagas em 2025, a maior procura por vaga entre as ofertas dos dois campi.',
      vars: {
        manha: { n: 'Matutino', ops: [{ ...amp(infI, 36, 2028, 1, null), fp: 0.85, fo: 1 }], nota: 'Turno atual do curso. Laboratório de informática passa de 100% de manhã em 2029.' },
        tarde: { n: 'Vespertino', ops: [{ ...amp(infI, 36, 2028, 1, 'V'), fp: 0.85, fo: 1 }], nota: 'Laboratório livre à tarde. Procura igual (premissa: integrado atrai nos dois turnos).' },
      }, var: 'tarde',
      acompanhar: { ind: 'Ocupação da turma nova e docentes em exercício', resp: 'Direção de ensino de Serra' } },
    { id: 'cod1', un: 'reitoria', tipo: 'recurso', origem: 'Reitoria', estado: 'proposta', incluir: true,
      titulo: 'Código de vaga docente liberado por aposentadoria (um código, dois pedidos)',
      motivo: 'Vitória e Serra contam com o mesmo código para viabilizar seus itens. Só um campus pode recebê-lo.',
      opcoes: { '': 'A decidir', vitoria: 'Vitória · núcleo comum', serra: 'Serra · Informática', nenhum: 'Não alocar agora' }, escolha: '',
      add: { vitoria: { rec: 'area', area: 'Núcleo comum', desde: 2028, v: 1 }, serra: { rec: 'area', area: 'Informática', desde: 2028, v: 1 } },
      tempo: 'Concurso e nomeação em ≈ 12 a 18 meses (premissa): docente em sala no ano letivo de 2028.',
      acompanhar: { ind: 'Nomeação e entrada em exercício', resp: 'Pró-reitoria de gestão de pessoas' } },
    { id: 'ocup-estradas', un: 'vitoria', curso: estC, tipo: 'ocupacao', origem: 'Curso', estado: 'proposta', incluir: true,
      titulo: 'Preencher as vagas de Estradas concomitante antes de abrir turma nova',
      motivo: '633 inscritos, mas só 75% das vagas ocupadas: as chamadas terminam antes de esgotar a lista.',
      vars: { base: { n: 'Ocupação de 75% para 95%', ops: [{ t: 'preencher', alvo: 0.95, desde: 2028, ofertas: [estC] }] } }, var: 'base',
      acompanhar: { ind: 'Ocupação das vagas no início do semestre', resp: 'Coordenação de Estradas e registro acadêmico' } },
    { id: 'perm-autom', un: 'serra', curso: autC, tipo: 'permanencia', origem: 'Curso', estado: 'hipotese', incluir: true,
      titulo: 'Ação de permanência no 1º ano de Automação Industrial concomitante',
      motivo: 'Evasão anual de 38%, a maior entre as ofertas de Serra. A coordenação ainda está desenhando a ação.',
      vars: { base: { n: 'Evasão −25%', ops: [{ t: 'evasao', red: 0.25, desde: 2028, ofertas: [autC] }] } }, var: 'base',
      acompanhar: { ind: 'Evasão no 1º ano (sistema acadêmico)', resp: 'Coordenação de Automação Industrial' } },
    { id: 'il-itapina', un: 'itapina', tipo: 'expansao', origem: 'Campus', estado: 'proposta', incluir: true, ilus: true,
      titulo: 'Expansão em Alimentos', motivo: 'Trajetória inventada para mostrar uma unidade sem simulação.',
      delta: t => ({ ct: rampa(t, 2028, 2031, 100), meq: rampa(t, 2028, 2031, 100), mat: rampa(t, 2028, 2031, 110), conc: t >= 2031 ? 22 : 0, prof: rampa(t, 2028, 2031, 6), mt: rampa(t, 2028, 2031, 140) }),
      rest: 2030, acompanhar: { ind: 'Vagas ofertadas e ocupação', resp: 'Direção de Itapina' } },
    { id: 'il-cefor', un: 'cefor', tipo: 'reorganizacao', origem: 'Reitoria', estado: 'hipotese', incluir: false, ilus: true,
      titulo: 'Reorientar parte da EaD de formação de professores para técnico', motivo: 'Maior alavanca isolada para o degrau de 50% em técnico, ao custo de formação de professores.',
      delta: t => ({ ct: rampa(t, 2028, 2030, 860), meq: 0, fp: -rampa(t, 2028, 2030, 860), mat: 0, conc: 0, prof: 0, mt: 0 }),
      rest: null, acompanhar: { ind: 'Matrículas técnicas EaD e formação de professores', resp: 'Direção do Cefor' } },
  ];
}

/* Item de curso criado pela coordenação ou pelo convite do desafio. O mesmo id converge os dois caminhos. */
function itemCurso(k, ofId, tipo, p, origem, estado) {
  const o = CP[k].lista.find(x => x.id === ofId), id = `cur-${tipo}-${ofId}`;
  const ops = tipo === 'permanencia' ? [{ t: 'evasao', red: p.red, desde: 2028, ofertas: [ofId] }]
    : tipo === 'ocupacao' ? [{ t: 'preencher', alvo: p.alvo, desde: 2028, ofertas: [ofId] }]
    : tipo === 'pausa' ? [{ t: 'pausar', oferta: ofId, desde: 2028 }]
    : [{ t: 'ampliar', oferta: ofId, n: p.n, desde: 2028, ocup: ocupNovas(o, p.n), turno: null, fp: 0.7, fo: 1.2 }];
  const titulo = { permanencia: `Ação de permanência no 1º ano de ${o.nome}`, ocupacao: `Preencher as vagas de ${o.nome}`, pausa: `Pausar novas entradas em ${o.nome}`, expansao: `Ampliar ${o.nome} (+${p.n} vagas)` }[tipo];
  const n = { permanencia: `Evasão −${Math.round(p.red * 100)}%`, ocupacao: `Ocupação até ${Math.round(p.alvo * 100)}%`, pausa: 'Pausa em 2028', expansao: `+${p.n} vagas` }[tipo];
  return { id, un: k, curso: ofId, tipo, origem, estado, incluir: true, titulo, motivo: p.motivo || '', vars: { base: { n, ops } }, var: 'base',
    acompanhar: { ind: { permanencia: 'Evasão no 1º ano (sistema acadêmico)', ocupacao: 'Ocupação das vagas no início do semestre', pausa: 'Conclusão das turmas em andamento', expansao: 'Ocupação da turma nova' }[tipo], resp: 'Coordenação do curso' }, p };
}

/* ---------- pauta de teste de legibilidade (36 itens, todos ilustrativos) ---------- */
function itensTeste() {
  const un = ['Alegre', 'Aracruz', 'Cachoeiro', 'Cariacica', 'Colatina', 'Guarapari', 'Linhares', 'Montanha', 'Nova Venécia', 'Santa Teresa', 'São Mateus', 'Venda Nova'];
  const mod = [['expansao', 'Ampliar vagas em curso com procura', 1], ['permanencia', 'Ação de permanência no 1º ano', 0.4], ['pausa', 'Pausar entradas em curso com baixa procura', -0.8], ['ocupacao', 'Preencher vagas ociosas', 0.3]];
  const r = [];
  for (let i = 0; i < 27; i++) {
    const u = un[i % un.length], [tipo, t, s] = mod[i % mod.length], v = Math.round((20 + (i * 37) % 60) * s);
    r.push({ id: 'teste-' + i, un: 'teste', unNome: u, tipo, origem: i % 3 ? 'Campus' : 'Curso', estado: i % 5 ? 'proposta' : 'hipotese', incluir: true, ilus: true, teste: true,
      titulo: t, motivo: 'Item gerado para testar a leitura de uma pauta longa. Não representa o campus.',
      delta: tt => ({ ct: rampa(tt, 2028, 2030, v), meq: rampa(tt, 2028, 2030, v), mat: rampa(tt, 2028, 2030, v), conc: tt >= 2031 ? Math.round(v / 4) : 0, prof: rampa(tt, 2028, 2030, v / 30), mt: rampa(tt, 2028, 2030, v * 1.3) }),
      rest: i % 7 === 0 ? 2030 : null, acompanhar: { ind: '—', resp: u } });
  }
  return r;
}

/* ---------- composição ---------- */
const varDe = it => it.vars ? it.vars[it.var] : null;
const tocadas = it => { const v = varDe(it); if (!v) return []; const ni = CP[it.un].lista.filter(o => o.naoInt).map(o => o.id); return [...new Set(v.ops.flatMap(op => ofertasDe(op).flatMap(x => x === '*naoInt' ? ni : [x])))]; };
function addsPara(k, itens, cod) {
  const a = [];
  for (const it of itens) { const v = varDe(it); if (it.un === k && v && v.adds) a.push(...v.adds); }
  if (cod && cod.escolha === k) a.push(cod.add[k]);
  return a;
}
/* Sinais de cada item: sobreposição (mesma oferta em dois itens incluídos: o segundo não é somado),
   disputa (dois campi contam com o mesmo código) e falta do recurso (o código foi para o outro campus). */
function sinais(itens) {
  const cod = itens.find(i => i.id === 'cod1'), out = {}, vistos = {};
  const ativos = itens.filter(i => i.incluir && !i.ilus && i.vars);
  for (const it of ativos) {
    out[it.id] = [];
    const ofs = tocadas(it), v = vistos[it.un] || (vistos[it.un] = []);
    const choque = v.find(([, o]) => o.some(x => ofs.includes(x)));
    if (choque) out[it.id].push({ k: 'sobreposto', t: `Mexe na mesma oferta que "${choque[0].titulo}". Não é somado ao conjunto para não contar o mesmo efeito duas vezes.` });
    else v.push([it, ofs]);
  }
  const pedem = ativos.filter(i => i.requer === 'cod1');
  if (cod && cod.incluir) {
    if (!cod.escolha && new Set(pedem.map(i => i.un)).size > 1) for (const i of pedem) out[i.id].push({ k: 'disputa', t: 'Conta com o mesmo código de vaga docente que outro campus. Escolha o destino do código.' });
    if (cod.escolha) for (const i of pedem) if (cod.escolha !== i.un) out[i.id].push({ k: 'semrecurso', t: `O código foi para ${cod.escolha === 'nenhum' ? 'nenhum campus' : UNID[cod.escolha]}. Sem ele, ver a restrição de docentes.` });
  } else for (const i of pedem) out[i.id].push({ k: 'semrecurso', t: 'Depende de um código de vaga docente que não está na pauta.' });
  return out;
}
const CACHE = new Map();
function simCache(k, ops, varr) {
  const key = k + '|' + varr + '|' + JSON.stringify(ops);
  if (!CACHE.has(key)) CACHE.set(key, simular(CP[k], ops, varr));
  return CACHE.get(key);
}
/* Compõe os itens incluídos. Unidades calculadas: um único motor por campus com todas as operações juntas.
   Unidades ilustrativas: deltas declarados, sempre em linha separada. */
function compor(itens, varr = 'central', soCalc = false) {
  const sg = sinais(itens), cod = itens.find(i => i.id === 'cod1');
  const sims = {}, caps = {}, restr = {};
  for (const k of Object.keys(CP)) {
    const its = itens.filter(i => i.incluir && i.un === k && i.vars && !(sg[i.id] || []).some(s => s.k === 'sobreposto'));
    const ops = its.flatMap(i => varDe(i).ops);
    sims[k] = ops.length ? simCache(k, ops, varr) : BASE[k];
    caps[k] = { ...CAP[k], adds: addsPara(k, its, cod && cod.incluir ? cod : null) };
    restr[k] = primeiraRestricao(sims[k], caps[k]);
  }
  const ilus = soCalc ? [] : itens.filter(i => i.incluir && i.ilus).map(i => i.delta);
  return { sims, caps, restr, extras: ilus, sinais: sg };
}
/* Efeito de um item sozinho, comparado a manter. */
function efeitoItem(it, itens, varKey) {
  const cod = itens.find(i => i.id === 'cod1');
  if (it.ilus) {
    const d = {}; for (const t of [OBS, ...FUT]) { const x = it.delta(t); d[t] = { ing: 0, mat: x.mat || 0, conc: x.conc || 0, mt: x.mt || 0, prof: x.prof || 0, ct: x.ct || 0, meq: x.meq || 0 }; }
    return { d, rest: it.rest ? { ano: it.rest, rec: [{ rec: 'capacidade (ilustr.)', uso: 1.1 }] } : null, sims: null, extras: [it.delta] };
  }
  if (!it.vars) return null;
  const v = it.vars[varKey || it.var], k = it.un;
  const s = simCache(k, v.ops, 'central'), b = BASE[k];
  const cap = { ...CAP[k], adds: [...(v.adds || []), ...(cod && cod.incluir && cod.escolha === k && it.requer === 'cod1' ? [cod.add[k]] : [])] };
  const d = {};
  for (const t of [OBS, ...FUT]) d[t] = { ing: s.anos[t].ing - b.anos[t].ing, mat: s.anos[t].mat - b.anos[t].mat, conc: s.anos[t].conc - b.anos[t].conc, mt: s.anos[t].mt - b.anos[t].mt, prof: (s.anos[t].prof || 0) - (b.anos[t].prof || 0), ct: s.anos[t].ct - b.anos[t].ct, meq: s.anos[t].me - b.anos[t].me };
  const sims = { ...BASE }; sims[k] = s;
  return { d, rest: primeiraRestricao(s, cap), sims, extras: [], cap };
}
/* Quando o efeito aparece: primeiro ano com efeito visível em matrículas ou concluintes, e ano em que estabiliza. */
function quando(d) {
  const anos = FUT.filter(t => t >= 2027), fim = d[FIM].mat, mx = Math.max(...anos.map(t => Math.abs(d[t].mat)), 1);
  const aparece = anos.find(t => Math.abs(d[t].mat) >= 3 || Math.abs(d[t].conc) >= 3);
  const conc = anos.find(t => Math.abs(d[t].conc) >= 3);
  const pleno = aparece ? anos.find(t => t >= aparece && Math.abs(d[t].mat - fim) <= 0.05 * mx) : null;
  return { aparece, conc, pleno };
}

/* ---------- hipóteses macro (exploração a partir do desafio) ---------- */
function macroOps(cp, h) {
  const ops = [];
  if (h.red) ops.push({ t: 'evasao', red: h.red, desde: 2028, ofertas: null });
  if (h.preencher) ops.push({ t: 'preencher', alvo: 0.95, desde: 2028, ofertas: null });
  if (h.amplia) for (const o of cp.lista) { const n = Math.round(o.vagas * h.amplia / 4) * 4; if (n > 0 && o.demandaExtra >= n) ops.push({ t: 'ampliar', oferta: o.id, n, desde: 2028, ocup: ocupNovas(o, n), turno: null, fp: 0.7, fo: 1.2 }); }
  return ops;
}
/* Extrapolação para o Ifes: efeito em Vitória e Serra multiplicado pela razão entre a matrícula equivalente técnica
   do Ifes e a dos dois campi (2025). Hipótese exploratória, não contribuição de ninguém. */
function escalaIfes() { return D.ifes[OBS].ct / (BASE.vitoria.anos[OBS].ct + BASE.serra.anos[OBS].ct); }
function macroExtra(h, varr = 'central') {
  const f = escalaIfes(), s = {};
  for (const k of Object.keys(CP)) s[k] = simCache(k, macroOps(CP[k], h), varr);
  const extra = t => {
    if (t <= OBS) return {};
    let mt = 0, ct = 0, meq = 0, eja = 0, mat = 0, conc = 0;
    for (const k of Object.keys(CP)) { const a = s[k].anos[t], b = BASE[k].anos[t]; mt += a.mt - b.mt; ct += a.ct - b.ct; meq += a.me - b.me; eja += a.eja - b.eja; mat += a.mat - b.mat; conc += a.conc - b.conc; }
    return { mt: mt * f, ct: ct * f, meq: meq * f, eja: eja * f, mat: mat * f, conc: conc * f };
  };
  return extra;
}
/* Ofertas onde uma hipótese macro tem base nos dados. Ordem: campus e nome. Não é ranking. */
function ondeTemBase(h) {
  const r = [];
  for (const k of Object.keys(CP)) for (const o of CP[k].lista) {
    if (h === 'red' && o.naoInt && o.k.e >= 0.25 && o.mat >= 60) r.push({ k, o, tipo: 'permanencia', porque: `evasão anual de ${Math.round(o.k.e * 100)}% com ${o.mat} matrículas` });
    if (h === 'preencher' && o.naoInt && o.ocup < 0.9 && o.insc >= o.vagas * 0.95 && o.vagas > 0) r.push({ k, o, tipo: 'ocupacao', porque: `ocupação de ${Math.round(o.ocup * 100)}% com ${o.insc} inscritos para ${o.vagas} vagas` });
    if (h === 'amplia' && o.demandaExtra >= Math.max(36, o.vagas * 0.5)) r.push({ k, o, tipo: 'expansao', porque: `${o.insc} inscritos para ${o.vagas} vagas` });
  }
  return r.sort((a, b) => a.k.localeCompare(b.k) || a.o.nome.localeCompare(b.o.nome));
}

/* ---------- peças para fechar a distância (partir da meta) ---------- */
function pecas() {
  const I = D.ifes[OBS], p0 = { ct: I.ct / I.meq, fp: I.fp / I.meq, eja: I.eja / I.meq }, q0 = refQualidade(p0);
  const q50 = refQualidade({ ...p0, ct: 0.5 }).ct - q0.ct, q60 = refQualidade({ ...p0, ct: 0.6 }).ct - q0.ct, qe = refQualidade({ ...p0, eja: 0.025 }).eja - q0.eja;
  return [
    { n: 'Formação de professores ≥ 20%', v: MATRIZ.fpDegrau, ex: 2027, nat: 'hip', obs: 'Já no ano-base 2025, se a reclassificação se confirmar. Entra no cenário de referência, não é decisão.' },
    { n: 'Formação técnica ≥ 50%', v: q50, ex: null, nat: 'est', obs: '≈ +3.800 matrículas equivalentes técnicas. Fora do alcance de decisões de oferta até o ano letivo de 2028.' },
    { n: 'Formação técnica ≥ 60%', v: q60, ex: null, nat: 'est', obs: 'Inclui o degrau de 50%. Prazo longo.' },
    { n: 'RAP de 18,15 para 20', v: 0.85e6, ex: 2029, nat: 'est', obs: '≈ +2.800 matrículas equivalentes presenciais com o mesmo quadro. Indicador de guarda: não perseguir à custa de qualidade.' },
    { n: 'IEA: próximo degrau', v: 0.51e6, ex: 2030, nat: 'est', obs: 'Permanência e conclusão. Valor da matriz não reproduzível pela PNP.' },
    { n: 'EJA ≥ 2,5%', v: qe, ex: 2029, nat: 'est', obs: 'Oferta PROEJA. Hoje 1,98%.' },
    { n: 'Cada +1.000 MT presenciais', v: 1000 * PREM.rs_mt, ex: null, nat: 'est', obs: '≈ 2% da MT do Ifes. Vem de vagas ocupadas e de estudantes que permanecem.' },
  ];
}
