/* Simulação do protótipo conceitual (2ª rodada, 12/11/2026; operações e capacidade datada na 3ª rodada, 13/11/2026). Usa o motor poc/coortes002.js sem alteração.
   Reproduz os resultados da POC 0.0.2 (Vitória e Serra, alternativas A, B e C) e acrescenta alavancas combináveis,
   horizonte até 2035, capacidade por turno, laboratório e área docente (ilustrativa) e matrícula total por premissa. */
const OBS = 2025, FIM = 2035, HIST = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025];
const FUT = []; for (let t = OBS + 1; t <= FIM; t++) FUT.push(t);
const PREM = { turma: 40, aulas_int: 30, aulas_naoint: 20, aulas_proeja: 25, horas_prof: 14, ch_int: 800, ch_naoint: 600, peso_int: 1.5, peso_naoint: 1.5, rs_mt: 1324 };
const CAMPI = { vitoria: 'Vitória', serra: 'Serra' };
const curto = of => of.curso.replace(/^Técnico em /, '') + ' · ' + of.oferta.replace('PROEJA - ', 'PROEJA ').toLowerCase();
const ehNaoInt = of => of.oferta === 'Concomitante' || of.oferta === 'Subsequente';

/* Capacidade (ilustrativa): turno principal de cada oferta, laboratório crítico e área docente.
   As quantidades disponíveis são calibradas para 2025 (uso entre 80% e 95%) e marcadas como ilustrativas. */
const CAPCFG = {
  vitoria: { lab: { nome: 'Oficinas de mecânica e metalurgia', re: /Mecânica|Metalurgia/, aulas: 8 },
             areas: [['Mecânica e metalurgia', /Mecânica|Metalurgia/], ['Eletrotécnica e automação', /Eletro|Automação/], ['Demais áreas técnicas', /./]] },
  serra: { lab: { nome: 'Laboratórios de informática', re: /Informática/, aulas: 10 },
           areas: [['Informática', /Informática/], ['Automação e mecatrônica', /Automação|Mecatrônica/], ['Demais áreas técnicas', /./]] },
};
function turnoDe(of, i) {
  if (!ehNaoInt(of)) return i % 2 ? 'V' : 'M';
  return /Noturno/.test(of.turno || '') ? 'N' : 'V';
}

function prepararCampus(chave) {
  const c = D.campi[CAMPI[chave]];
  const ofs = c.ofertas.filter(o => o.presencial && o.tipo === 'Técnico' && o.serie[OBS] && (o.serie[OBS][0] > 0 || o.serie[OBS][3] >= 10));
  const evMed = C.media(ofs.map(o => o.evasao && o.evasao['2024']).filter(x => x != null)) || 0.2;
  const lista = ofs.map(o => {
    const k = C.calibrar(o, evMed), s = o.serie[OBS];
    const banda = { mat: Math.max(k.erro.mat ?? 0.15, k.teste?.mat ?? 0, 0.05), conc: Math.min(0.6, Math.max(k.erro.conc ?? 0.3, k.teste?.conc ?? 0, 0.1)) };
    return { of: o, id: o.id, nome: curto(o), k, banda, vagas: s[0], insc: s[1], ing: s[2], mat: s[3], conc: s[4], me: s[5], naoInt: ehNaoInt(o),
      ocup: k.ocup ?? 1, demandaExtra: Math.max(0, s[1] - s[2]) };
  }).sort((a, b) => b.mat - a.mat);
  for (const o of lista.filter(x => !x.k.cFato)) {
    const pares = lista.filter(x => x.k.cFato && x.naoInt === o.naoInt).map(x => x.k.c).sort((a, b) => a - b);
    o.k.c = pares.length ? pares[Math.floor(pares.length / 2)] : 0.6; o.k.emprestado = true;
    o.banda = { mat: 0.25, conc: 0.6 };
  }
  const cfg = CAPCFG[chave];
  let ii = 0;
  for (const o of lista) {
    o.turno = turnoDe(o.of, o.naoInt ? 0 : ii++);
    o.lab = cfg.lab.re.test(o.of.curso);
    o.area = cfg.areas.find(([, re]) => re.test(o.of.curso))[0];
  }
  return { chave, nome: CAMPI[chave], dados: c, lista, cfg };
}
const achar = (cp, curso, oferta) => cp.lista.find(o => o.of.curso === curso && o.of.oferta === oferta);
const ocupNovas = (o, n) => Math.min(o.ocup, o.demandaExtra / Math.max(n, 1));

/* Alavancas compostas. Cada uma pode ser ligada sozinha ou junto com as outras. */
function alavancasPadrao(cp) {
  const v = cp.chave === 'vitoria';
  const amp = v ? achar(cp, 'Técnico em Mecânica', 'Concomitante') : achar(cp, 'Técnico em Informática', 'Concomitante');
  const de = v ? achar(cp, 'Técnico em Eletrotécnica', 'Concomitante') : achar(cp, 'Técnico em Informática', 'Concomitante');
  const para = v ? achar(cp, 'Técnico em Eletrotécnica', 'Integrado') : achar(cp, 'Técnico em Informática para Internet', 'Integrado');
  return {
    ampliar: { on: false, oferta: amp.id, n: v ? 36 : 40, desde: 2027, ocup: +ocupNovas(amp, v ? 36 : 40).toFixed(2) },
    migrar: { on: false, de: de.id, para: para.id, n: v ? 32 : 40, desde: 2027, ocup: +ocupNovas(para, v ? 32 : 40).toFixed(2), turno: null },
    preencher: { on: false, alvo: 0.95, desde: 2027 },
    evasao: { on: false, red: 0.30, desde: 2027 },
  };
}
const PRESETS = {
  M: { nome: 'Manter', liga: [] },
  A: { nome: 'A · Ampliar vagas', liga: ['ampliar'] },
  B: { nome: 'B · Aproveitar melhor', liga: ['preencher', 'evasao'] },
  C: { nome: 'C · Reorganizar', liga: ['migrar'] },
  R: { nome: 'Reorganizar + preencher + evasão −20%', liga: ['migrar', 'preencher', 'evasao'], red: 0.20 },
};
function aplicarPreset(cp, letra) {
  const a = alavancasPadrao(cp), p = PRESETS[letra];
  for (const k of p.liga) a[k].on = true;
  if (p.red) a.evasao.red = p.red;
  return a;
}

const turmasDe = v => v > 0 ? Math.ceil(v / PREM.turma - 0.05) : 0;
const aulasDe = o => o.of.oferta === 'Integrado' ? PREM.aulas_int : o.of.oferta.includes('PROEJA') ? PREM.aulas_proeja : PREM.aulas_naoint;

/* Operações elementares (3ª rodada). As alavancas da bancada viram uma lista de operações; os itens da pauta
   usam a mesma lista, inclusive no nível do curso. Tipos:
     ampliar   {oferta, n, desde, ocup, turno, fp, fo}  turmas novas na oferta (fp/fo: fator de ocupação pess./otim.)
     reduzir   {oferta, n, desde}                       menos vagas (lado "de" da reorganização)
     pausar    {oferta, desde}                          nenhuma entrada a partir de "desde"; turmas em andamento seguem
     evasao    {red, desde, ofertas}                    redução da evasão; ofertas null = todos os não integrados
     preencher {alvo, desde, ofertas}                   ocupação-alvo onde a procura comporta; ofertas null = não integrados */
function opsDe(alav) {
  if (!alav) return [];
  if (Array.isArray(alav)) return alav;
  const A = alav.ampliar, M = alav.migrar, P = alav.preencher, E = alav.evasao, ops = [];
  if (A.on) ops.push({ t: 'ampliar', oferta: A.oferta, n: A.n, desde: A.desde, ocup: A.ocup, turno: null, fp: 0.7, fo: 1.2 });
  if (M.on) { ops.push({ t: 'reduzir', oferta: M.de, n: M.n, desde: M.desde }); ops.push({ t: 'ampliar', oferta: M.para, n: M.n, desde: M.desde, ocup: M.ocup, turno: M.turno, fp: 0.85, fo: 1 }); }
  if (E.on) ops.push({ t: 'evasao', red: E.red, desde: E.desde, ofertas: null });
  if (P.on) ops.push({ t: 'preencher', alvo: P.alvo, desde: P.desde, ofertas: null });
  return ops;
}
const alcanca = (op, o) => op.ofertas ? op.ofertas.includes(o.id) : o.naoInt;
const ofertasDe = op => op.oferta ? [op.oferta] : (op.ofertas || ['*naoInt']);

/* Simula um campus com alavancas (objeto da bancada) ou com uma lista de operações.
   varr: central | pess | otim (sensibilidade das hipóteses). */
function simular(cp, alav, varr = 'central') {
  const fator = { central: 1, pess: 0.5, otim: 1.5 }[varr];
  const ops = opsDe(alav);
  const linhas = [];
  for (const o of cp.lista) {
    const vg = {}, oc = {}, eF = {};
    for (const t of FUT) { vg[t] = o.vagas; oc[t] = o.ocup; }
    let nNovas = 0, ocupN = 0, desdeN = 9999, turnoNovas = null;
    const red = {}, alvo = {};
    for (const op of ops) {
      if (op.t === 'ampliar' && op.oferta === o.id) { nNovas += op.n; ocupN = Math.min(1.05, op.ocup * (varr === 'pess' ? op.fp : varr === 'otim' ? op.fo : 1)); desdeN = op.desde; if (op.turno) turnoNovas = op.turno; }
      if (op.t === 'reduzir' && op.oferta === o.id) for (const t of FUT) if (t >= op.desde) vg[t] = Math.max(0, vg[t] - op.n);
      if (op.t === 'evasao' && alcanca(op, o)) for (const t of FUT) if (t >= op.desde) red[t] = 1 - (1 - (red[t] || 0)) * (1 - Math.min(0.9, op.red * fator));
      if (op.t === 'preencher' && alcanca(op, o) && o.insc >= o.vagas * op.alvo) for (const t of FUT) if (t >= op.desde) alvo[t] = Math.max(alvo[t] || 0, op.alvo);
    }
    for (const t of FUT) {
      if (red[t] != null) eF[t] = o.k.e * (1 - red[t]);
      if (alvo[t] != null) oc[t] = Math.max(o.ocup, alvo[t]);
    }
    if (nNovas) for (const t of FUT) if (t >= desdeN) { oc[t] = (vg[t] * oc[t] + nNovas * ocupN) / Math.max(1, vg[t] + nNovas); vg[t] += nNovas; }
    for (const op of ops) if (op.t === 'pausar' && op.oferta === o.id) for (const t of FUT) if (t >= op.desde) vg[t] = 0;
    const p = C.projetar({ hist: o.of, D: o.k.D, e: o.k.e, c: o.k.c, meRatio: o.k.meRatio, vagas: vg, ocup: oc, eFut: eF }, FIM);
    for (const t of FUT) {
      let tur = 0, turNovas = 0;
      for (let k = 0; k < o.k.D; k++) {
        const y = t - k, v = y <= OBS ? C.vagas(o.of, y) : vg[y];
        tur += turmasDe(v);
        if (turnoNovas && y > OBS && y >= desdeN) turNovas += turmasDe(v) - turmasDe(v - nNovas);
      }
      p[t].turmas = tur; p[t].turNovas = turNovas; p[t].horas = tur * aulasDe(o);
    }
    linhas.push({ o, p, vg, turnoNovas });
  }
  return agregar(cp, linhas);
}

function agregar(cp, linhas) {
  const anos = {};
  const z = () => ({ vagas: 0, ing: 0, mat: 0, prazo: 0, ret: 0, conc: 0, evad: 0, me: 0, ct: 0, fp: 0, eja: 0, horas: 0, banda: 0, bandaC: 0, mt: 0, turno: { M: 0, V: 0, N: 0 }, lab: { M: 0, V: 0, N: 0 }, area: {} });
  const obs = anos[OBS] = z();
  for (const { o } of linhas) {
    obs.vagas += o.vagas; obs.ing += o.ing; obs.mat += o.mat; obs.conc += o.conc; obs.me += o.me;
    if (o.of.classe.tec) obs.ct += o.me; if (o.of.classe.eja) obs.eja += o.me;
    obs.mt += mtDe(o, o.mat, 0);
  }
  for (const t of FUT) {
    const a = anos[t] = z();
    for (const { o, p, turnoNovas } of linhas) {
      const x = p[t];
      a.vagas += x.vagas; a.ing += x.ing; a.mat += x.mat; a.prazo += x.prazo; a.ret += x.ret; a.conc += x.conc; a.evad += x.evad; a.me += x.me; a.horas += x.horas;
      if (o.of.classe.tec) a.ct += x.me; if (o.of.classe.eja) a.eja += x.me; if (o.of.classe.fp) a.fp += x.me;
      a.banda += x.mat * o.banda.mat; a.bandaC += x.conc * o.banda.conc;
      a.mt += mtDe(o, x.prazo, x.ret);
      const tNov = turnoNovas ? x.turNovas : 0, tBase = x.turmas - tNov;
      a.turno[o.turno] += tBase; if (tNov) a.turno[turnoNovas] += tNov;
      if (o.lab) { a.lab[o.turno] += tBase * cp.cfg.lab.aulas; if (tNov) a.lab[turnoNovas] += tNov * cp.cfg.lab.aulas; }
      const hTec = o.of.oferta === 'Integrado' ? x.horas / 2 : x.horas;
      a.area[o.area] = (a.area[o.area] || 0) + hTec;
      if (o.of.oferta === 'Integrado') a.area['Núcleo comum'] = (a.area['Núcleo comum'] || 0) + x.horas / 2;
    }
    a.prof = a.horas / PREM.horas_prof;
  }
  // 2025 também precisa de turmas e uso para a verificação da capacidade
  const a0 = anos[OBS];
  for (const { o } of linhas) {
    let tur = 0; for (let k = 0; k < o.k.D; k++) tur += turmasDe(C.vagas(o.of, OBS - k));
    a0.turno[o.turno] += tur; if (o.lab) a0.lab[o.turno] += tur * cp.cfg.lab.aulas;
    const h = tur * aulasDe(o); a0.horas += h;
    a0.area[o.area] = (a0.area[o.area] || 0) + (o.of.oferta === 'Integrado' ? h / 2 : h);
    if (o.of.oferta === 'Integrado') a0.area['Núcleo comum'] = (a0.area['Núcleo comum'] || 0) + h / 2;
  }
  a0.prof = a0.horas / PREM.horas_prof;
  return { cp, anos, linhas };
}
// Matrícula total estimada por premissa: ativos no prazo × CH anual ÷ 800 × peso; retidos valem ¼ (RMO-066).
function mtDe(o, prazo, ret) {
  const int = !o.naoInt, ch = int ? PREM.ch_int : PREM.ch_naoint, peso = int ? PREM.peso_int : PREM.peso_naoint;
  return (prazo + ret / 4) * ch / 800 * peso;
}

/* Capacidade disponível ilustrativa: ajustada para que manter a oferta caiba no horizonte (pico de uso de
   ~90% em salas, ~92% em laboratório e ~95% em docentes). Serve para mostrar o mecanismo, não o campus real. */
function capacidadePadrao(base) {
  const anos = [OBS, ...FUT].map(t => base.anos[t]);
  const mx = f => Math.max(...anos.map(f));
  const salas = Math.ceil(mx(a => Math.max(a.turno.M, a.turno.V, a.turno.N)) / 0.9);
  const lab = Math.ceil(mx(a => Math.max(a.lab.M, a.lab.V, a.lab.N)) / 0.92 / 10) * 10;
  const areas = {};
  for (const k of Object.keys(base.anos[OBS].area)) areas[k] = Math.max(1, Math.ceil(mx(a => a.area[k] || 0) / PREM.horas_prof / 0.95));
  return { salas, lab, areas };
}
/* Acréscimos datados à capacidade: cap.adds = [{ rec: 'lab' | 'salas' | 'area', area, desde, v }]. */
function capEm(cap, t) {
  if (!cap.adds || !cap.adds.length) return cap;
  const c = { salas: cap.salas, lab: cap.lab, areas: { ...cap.areas } };
  for (const a of cap.adds) if (t >= a.desde) { if (a.rec === 'lab') c.lab += a.v; else if (a.rec === 'salas') c.salas += a.v; else c.areas[a.area] = (c.areas[a.area] || 0) + a.v; }
  return c;
}
function usoCapacidade(sim, capBase, t) {
  const a = sim.anos[t], r = [], cap = capEm(capBase, t);
  for (const tu of ['M', 'V', 'N']) r.push({ rec: 'Salas · ' + { M: 'matutino', V: 'vespertino', N: 'noturno' }[tu], uso: a.turno[tu] / cap.salas, dem: a.turno[tu], cap: cap.salas, un: 'turmas' });
  const lt = ['M', 'V', 'N'].reduce((m, tu) => a.lab[tu] > a.lab[m] ? tu : m, 'M');
  r.push({ rec: sim.cp.cfg.lab.nome + ' · ' + { M: 'matutino', V: 'vespertino', N: 'noturno' }[lt], uso: a.lab[lt] / cap.lab, dem: a.lab[lt], cap: cap.lab, un: 'aulas/sem' });
  for (const [k, n] of Object.entries(cap.areas)) r.push({ rec: 'Docentes · ' + k, uso: (a.area[k] || 0) / PREM.horas_prof / n, dem: (a.area[k] || 0) / PREM.horas_prof, cap: n, un: 'prof.-eq.' });
  return r;
}
function primeiraRestricao(sim, cap) {
  for (const t of FUT) { const r = usoCapacidade(sim, cap, t).filter(x => x.uso > 1.0001); if (r.length) return { ano: t, rec: r }; }
  return null;
}

/* Ifes: percentuais legais de 2025 mais a variação dos campi simulados (demais constantes). */
function ifesEm(t, sims, extras = []) {
  const I = D.ifes[OBS], o = { meq: I.meq, ct: I.ct, fp: I.fp, eja: I.eja };
  for (const s of sims) { const a = s.anos[t], b = s.anos[OBS]; o.meq += a.me - b.me; o.ct += a.ct - b.ct; o.fp += a.fp - b.fp; o.eja += a.eja - b.eja; }
  for (const e of extras) { const d = e(t); o.meq += d.meq || 0; o.ct += d.ct || 0; o.fp += d.fp || 0; o.eja += d.eja || 0; }
  return { ...o, pct: { ct: o.ct / o.meq, fp: o.fp / o.meq, eja: o.eja / o.meq } };
}
// Referência condicional de Qualidade (F-23/F-29): Rede 2026 constante, ponderado = valor × peso da faixa.
function refQualidade(pct) {
  const R = D.matriz_2026.rede, S = D.matriz_2026.submontantes;
  const W = { ct: v => v < .5 ? 0 : v < .6 ? v : 2 * v, fp: v => v < .1 ? 0 : v < .15 ? v : v < .2 ? 2 * v : 2.5 * v, eja: v => v < .025 ? 0 : v < .05 ? v : v < .1 ? 2 * v : 2.5 * v };
  const ifesR = R.find(r => r.nome.includes('ESPIRITO SANTO')), out = {};
  for (const k of ['ct', 'fp', 'eja']) {
    const soma = R.reduce((s, r) => s + W[k](r[k] || 0), 0), w = W[k](pct[k]);
    out[k] = w ? w / (soma - W[k](ifesR[k]) + w) * S[k.toUpperCase()] : 0;
  }
  return out;
}
