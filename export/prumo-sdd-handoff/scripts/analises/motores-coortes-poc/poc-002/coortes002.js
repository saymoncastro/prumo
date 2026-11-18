/* Motor de coortes da POC 0.0.2 do Prumo.
   Anual, determinístico e explícito. Separa os quatro mecanismos que o gestor pode querer mudar:
     ocupação  o   = ingressantes ÷ vagas                          (fato PNP: média 2023–2025)
     evasão    e   = evadidos ÷ matrículas no ano                   (fato PNP: TaxaEvasao, média 2023–2025)
     conclusão c   = fração do último ano que conclui no prazo       (estimada: ajuste a matrículas e concluintes)
     retenção      = quem não conclui no prazo fica 1 ano a mais e então conclui ou evade
   Coorte que ingressa no ano y, com N₀ = ingressantes:
     anos k = 0..D−1 (no prazo):  N_k = N₀ (1−e)^k
     concluem no prazo (k = D−1): N_{D−1} (1−e) c
     retidos (k = D):             R = N_{D−1} (1−e) (1−c);  concluem depois: R (1−e)
   Matrículas do ano = soma das coortes ativas (a PNP conta quem esteve ativo ao menos um dia).
   Usado pela página (inlinado por poc/montar.py) e por poc/testar_poc002.cjs. */
const Coortes2 = (() => {
  const PRIMEIRO = 2017, ULTIMO = 2025;
  const campo = i => (of, a) => (of.serie[a] ? of.serie[a][i] : 0);
  const vagas = campo(0), inscritos = campo(1), ingr = campo(2), matr = campo(3), conc = campo(4), meq = campo(5);

  // prazos candidatos em anos (a PNP não informa a duração). O prazo efetivo é escolhido entre dois valores
  // plausíveis pelo ajuste à série; integrados de Vitória e Serra ajustam com 4 anos (3–10% de erro contra 27–31% com 3).
  function prazos(of) {
    if (of.tipo !== 'Técnico') return of.tipo === 'Bacharelado' ? [5] : of.tipo.startsWith('Mestrado') ? [2] : [4];
    if ((of.oferta || '').includes('PROEJA')) return [3, 4];
    return of.oferta === 'Integrado' ? [3, 4] : [2, 3];
  }
  const prazo = of => prazos(of)[prazos(of).length - 1];

  // contribuição de uma coorte no ano t (k = t − y)
  function coorte(N0, k, D, e, c) {
    const z = { mat: 0, prazo: 0, ret: 0, conc: 0, evad: 0 };
    if (k < 0 || k > D || N0 <= 0) return z;
    if (k < D) {
      const N = N0 * Math.pow(1 - e, k);
      z.mat = z.prazo = N; z.evad = N * e;
      if (k === D - 1) z.conc = N * (1 - e) * c;
      return z;
    }
    const R = N0 * Math.pow(1 - e, D) * (1 - c);
    z.mat = z.ret = R; z.evad = R * e; z.conc = R * (1 - e);
    return z;
  }

  const media = (xs) => { const v = xs.filter(x => x != null && isFinite(x)); return v.length ? v.reduce((a, b) => a + b, 0) / v.length : null; };

  // estoque e concluintes modelados com ingressos observados (para calibrar e testar)
  function modelar(of, t, D, e, c) {
    const s = { mat: 0, conc: 0 };
    for (let y = t - D; y <= t; y++) {
      const z = coorte(ingr(of, y), t - y, D, e, c);
      s.mat += z.mat; s.conc += z.conc;
    }
    return s;
  }
  // anos em que todas as coortes ativas são conhecidas (ingresso ≥ 2017)
  const anosCompletos = (of, D, de, ate) => {
    const r = [];
    for (let t = Math.max(de, PRIMEIRO + D); t <= ate; t++) if (of.serie[t] && matr(of, t) > 0) r.push(t);
    return r;
  };

  function ajustarC(of, D, e, anos) {
    let melhor = null;
    for (let i = 0; i <= 100; i++) {
      const c = i / 100;
      let q = 0;
      for (const t of anos) {
        const m = modelar(of, t, D, e, c);
        q += ((m.mat - matr(of, t)) / matr(of, t)) ** 2 + ((m.conc - conc(of, t)) / Math.max(conc(of, t), 10)) ** 2;
      }
      if (!melhor || q < melhor.q) melhor = { c, q };
    }
    return melhor.c;
  }
  function erros(of, D, e, c, anos) {
    const em = media(anos.map(t => Math.abs(modelar(of, t, D, e, c).mat - matr(of, t)) / matr(of, t)));
    const ec = media(anos.map(t => Math.abs(modelar(of, t, D, e, c).conc - conc(of, t)) / Math.max(conc(of, t), 10)));
    return { mat: em, conc: ec };
  }

  /* Calibração de uma oferta com série. Devolve parâmetros com origem declarada. */
  function calibrar(of, evPadrao) {
    const evs = ['2023', '2024', '2025'].map(a => of.evasao && of.evasao[a]).filter(x => x != null);
    const e = evs.length ? media(evs) : evPadrao;
    const oc = ['2023', '2024', '2025'].filter(a => vagas(of, a) > 0).map(a => ingr(of, a) / vagas(of, a));
    const ocup = oc.length ? Math.min(1.05, media(oc)) : null;
    const s25 = of.serie[ULTIMO];
    const base = { e, eFato: evs.length > 0, ocup, meRatio: s25 && s25[3] > 0 ? s25[5] / s25[3] : 1 };
    let melhor = null;
    for (const D of prazos(of)) {
      const anos = anosCompletos(of, D, 2023, ULTIMO);
      if (anos.length < 2 || e == null) continue; // um ano só não identifica a conclusão
      const c = ajustarC(of, D, e, anos), err = erros(of, D, e, c, anos);
      const nota = err.mat + 0.5 * err.conc;
      if (!melhor || nota < melhor.nota) melhor = { D, c, erro: err, anos, nota };
    }
    if (!melhor) return { ...base, D: prazo(of), c: 0.6, cFato: false, erro: { mat: null, conc: null }, teste: null, candidatos: prazos(of) };
    const { D, c, anos } = melhor;
    // teste fora da amostra: calibra com 2023–2024 e prevê 2025 com os ingressos observados
    const an = anos.filter(t => t < ULTIMO);
    let teste = null;
    if (an.length && of.serie[ULTIMO] && matr(of, ULTIMO) > 0) {
      const e2 = media(['2023', '2024'].map(a => of.evasao && of.evasao[a]).filter(x => x != null)) ?? e;
      const c2 = ajustarC(of, D, e2, an), p = modelar(of, ULTIMO, D, e2, c2);
      teste = { mat: Math.abs(p.mat - matr(of, ULTIMO)) / matr(of, ULTIMO), conc: Math.abs(p.conc - conc(of, ULTIMO)) / Math.max(conc(of, ULTIMO), 10) };
    }
    return { ...base, D, c, cFato: true, erro: melhor.erro, teste, anos, candidatos: prazos(of) };
  }

  /* Projeção de uma oferta, de 2026 até `ate`.
     p: { hist (oferta com série ou null), D, e, c, meRatio,
          vagas: {ano: vagas}, ocup: {ano: ocupação}, eFut: {ano: evasão}, cFut: {ano: conclusão} }
     Coortes até 2025 usam ingressos observados e são ancoradas na matrícula observada em 2025.
     Mudanças de evasão e conclusão valem para todas as coortes ativas no ano em que entram em vigor. */
  function projetar(p, ate) {
    const coortes = [];
    if (p.hist) for (let y = ULTIMO - p.D; y <= ULTIMO; y++) { const i = ingr(p.hist, y); if (i > 0) coortes.push({ y, N0: i, velha: true }); }
    for (let y = ULTIMO + 1; y <= ate; y++) {
      const v = (p.vagas && p.vagas[y]) || 0, o = p.ocup && p.ocup[y] != null ? p.ocup[y] : 0;
      if (v > 0 && o > 0) coortes.push({ y, N0: v * o, vagas: v, velha: false });
    }
    const eDe = t => (p.eFut && p.eFut[t] != null ? p.eFut[t] : p.e);
    const cDe = t => (p.cFut && p.cFut[t] != null ? p.cFut[t] : p.c);
    // trajetória ano a ano de uma coorte com parâmetros que podem mudar no tempo
    function passo(c, t) {
      const k = t - c.y; if (k < 0 || k > p.D) return null;
      let N = c.N0;
      for (let u = c.y; u < c.y + Math.min(k, p.D - 1); u++) N *= 1 - eDe(u);
      const e = eDe(t);
      if (k < p.D) return { mat: N, prazo: N, ret: 0, evad: N * e, conc: k === p.D - 1 ? N * (1 - e) * cDe(t) : 0 };
      const ultimo = c.y + p.D - 1;
      const R = N * (1 - eDe(ultimo)) * (1 - cDe(ultimo));
      return { mat: R, prazo: 0, ret: R, evad: R * e, conc: R * (1 - e) };
    }
    let ancora = 1;
    if (p.hist) {
      const m25 = coortes.filter(c => c.velha).reduce((s, c) => s + (passo(c, ULTIMO)?.mat || 0), 0);
      ancora = m25 > 0 ? matr(p.hist, ULTIMO) / m25 : 0;
    }
    const out = {};
    for (let t = ULTIMO + 1; t <= ate; t++) {
      const a = { ing: 0, mat: 0, prazo: 0, ret: 0, conc: 0, evad: 0, vagas: (p.vagas && p.vagas[t]) || 0 };
      for (const c of coortes) {
        const z = passo(c, t); if (!z) continue;
        const f = c.velha ? ancora : 1;
        for (const k of ['mat', 'prazo', 'ret', 'conc', 'evad']) a[k] += z[k] * f;
        if (t === c.y) a.ing += c.N0;
      }
      a.me = a.mat * p.meRatio;
      out[t] = a;
    }
    return out;
  }

  return { PRIMEIRO, ULTIMO, prazo, prazos, coorte, modelar, calibrar, projetar, vagas, inscritos, ingr, matr, conc, meq, media };
})();
if (typeof module !== 'undefined') module.exports = Coortes2;
