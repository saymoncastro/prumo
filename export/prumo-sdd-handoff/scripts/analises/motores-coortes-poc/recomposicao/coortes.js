/* Motor de coortes do Prumo (demonstração de recomposição de oferta).
   Determinístico e anual. Cada coorte de ingresso permanece D + T anos (T = anos de retenção além da
   duração), com permanência anual r. Matrículas do ano = soma das coortes ativas.
   Usado pela página (inlinado por poc/montar.py) e por poc/testar_coortes.mjs (validação histórica). */
const Coortes = (() => {
  const PRIMEIRO = 2017, ULTIMO = 2025;
  const REGULARES = ['Técnico', 'Bacharelado', 'Licenciatura', 'Tecnologia', 'Mestrado Profissional', 'Mestrado', 'Doutorado'];

  function padrao(of) {
    const t = of.tipo, o = of.oferta || '';
    if (t === 'Técnico') return o.includes('Integrado') || o.includes('PROEJA') ? { D: 3, T: 0 } : { D: 2, T: 0 };
    if (t === 'Bacharelado') return { D: 5, T: 1 };
    if (t === 'Licenciatura' || t === 'Tecnologia') return { D: 4, T: 1 };
    if (t.startsWith('Mestrado')) return { D: 2, T: 0 };
    if (t === 'Doutorado') return { D: 4, T: 0 };
    return { D: 1, T: 0 };
  }
  const campo = i => (of, a) => (of.serie[a] ? of.serie[a][i] : 0);
  const vagas = campo(0), ingr = campo(2), matr = campo(3), conc = campo(4), meq = campo(5);

  // estoque de um ano a partir dos ingressos, com permanência constante
  function estoque(ing, t, D, T, r) {
    let s = 0;
    for (let k = 0; k < D + T; k++) s += (ing[t - k] || 0) * Math.pow(r, k);
    return s;
  }
  const serieIng = of => { const o = {}; for (let a = PRIMEIRO; a <= ULTIMO; a++) o[a] = ingr(of, a); return o; };

  // anos utilizáveis: todas as coortes ativas conhecidas e matrícula observada. Oferta que surge depois
  // de 2017 não tem coortes anteriores; oferta já existente em 2017 só é usável quando as coortes
  // anteriores a 2017 já saíram do estoque.
  function anosUteis(of, D, T, ate) {
    const anos = Object.keys(of.serie).map(Number).sort((a, b) => a - b);
    const inicio = anos[0] > PRIMEIRO ? anos[0] : PRIMEIRO + D + T - 1;
    const r = [];
    for (let t = inicio; t <= ate; t++) if (of.serie[t] && matr(of, t) > 0) r.push(t);
    return r;
  }
  function ajustar(of, D, T, ate) {
    const ing = serieIng(of), anos = anosUteis(of, D, T, ate);
    if (anos.length < 2) return null;
    let melhor = null;
    for (let i = 50; i <= 100; i++) {
      const r = i / 100;
      let sse = 0;
      for (const t of anos) sse += (estoque(ing, t, D, T, r) - matr(of, t)) ** 2;
      if (!melhor || sse < melhor.sse) melhor = { r, sse };
    }
    return { r: melhor.r, pontos: anos.length };
  }

  // calibração da permanência com a duração padrão do tipo de oferta (a PNP não informa a duração;
  // escolher a duração pelo ajuste, com poucos pontos, produziu sobreajuste no teste histórico)
  function calibrar(of, ate = ULTIMO) {
    const p = padrao(of), D = p.D;
    const f = ajustar(of, D, p.T, ate);
    if (!f) return { D, T: p.T, r: null, erro: null, calibrado: false };
    const ing0 = serieIng(of), anos = anosUteis(of, D, p.T, ate);
    const erro = anos.reduce((s, t) => s + Math.abs(estoque(ing0, t, D, p.T, f.r) - matr(of, t)) / matr(of, t), 0) / anos.length;
    const melhor = { D, T: p.T, r: f.r, erro, pontos: f.pontos, calibrado: true };
    // fração de concluintes sobre a coorte que chega à última série
    let num = 0, den = 0;
    const ing = serieIng(of);
    for (let t = PRIMEIRO + melhor.D - 1; t <= ate; t++) {
      const base = (ing[t - melhor.D + 1] || 0) * Math.pow(melhor.r, melhor.D - 1);
      if (base > 0 && of.serie[t]) { num += conc(of, t); den += base; }
    }
    melhor.phi = den > 0 ? Math.min(1.2, num / den) : 0.8;
    return melhor;
  }

  // validação histórica: calibra até 2021 e prevê 2022–2025 com os ingressos observados
  function validar(of) {
    const c = calibrar(of, 2021);
    if (!c.calibrado) return null;
    const ing = serieIng(of), pontos = [];
    for (let t = 2022; t <= ULTIMO; t++) if (of.serie[t] && matr(of, t) > 0)
      pontos.push({ ano: t, observado: matr(of, t), previsto: estoque(ing, t, c.D, c.T, c.r) });
    if (!pontos.length) return null;
    const erro = pontos.reduce((s, p) => s + Math.abs(p.previsto - p.observado) / p.observado, 0) / pontos.length;
    return { D: c.D, r: c.r, pontos, erro };
  }

  /* Projeção de uma oferta.
     spec: { hist: oferta com série (ou null para oferta nova), D, T, r, phi, meRatio,
             vagasFut: {ano: vagas}, ocup: {ano: ocupação}, rFut: {ano: permanência}, turma }
     Coortes até 2025 usam ingressos observados e são ancoradas na matrícula de 2025. */
  function projetar(spec, ate) {
    const { D, T, phi, meRatio, turma } = spec;
    const rDe = t => (spec.rFut && spec.rFut[t] != null ? spec.rFut[t] : spec.r);
    const coortes = [];
    if (spec.hist) {
      for (let y = Math.max(PRIMEIRO, ULTIMO - D - T + 1); y <= ULTIMO; y++) {
        const i = ingr(spec.hist, y);
        if (i > 0) coortes.push({ y, ing: i, vagas: Math.max(vagas(spec.hist, y), i), velha: true });
      }
    }
    for (let y = ULTIMO + 1; y <= ate; y++) {
      const v = spec.vagasFut[y] || 0, o = spec.ocup[y] != null ? spec.ocup[y] : 0;
      if (v > 0 && o > 0) coortes.push({ y, ing: v * o, vagas: v, velha: false });
    }
    const tam = (c, t) => { let s = c.ing; for (let u = c.y + 1; u <= t; u++) s *= rDe(u); return s; };
    let ancora = 1;
    if (spec.hist) {
      const m25 = coortes.filter(c => c.velha).reduce((s, c) => s + tam(c, ULTIMO), 0);
      const obs = matr(spec.hist, ULTIMO);
      ancora = m25 > 0 ? obs / m25 : 0;
    }
    const out = {};
    for (let t = ULTIMO + 1; t <= ate; t++) {
      let mat = 0, cn = 0, turmas = 0, ing = 0;
      for (const c of coortes) {
        const k = t - c.y;
        if (k < 0 || k >= D + T) continue;
        const s = tam(c, t) * (c.velha ? ancora : 1);
        mat += s;
        if (k === 0) ing += s;
        if (k === D - 1) cn += s * phi;
        if (k < D && s > 0.5) turmas += Math.max(1, Math.round(c.vagas / turma)); // 42 vagas = 1 turma; 72 = 2
      }
      out[t] = { ing, mat, conc: cn, me: mat * meRatio, turmas };
    }
    return out;
  }

  return { PRIMEIRO, ULTIMO, REGULARES, padrao, calibrar, validar, projetar, estoque, serieIng, vagas, ingr, matr, conc, meq };
})();
if (typeof module !== 'undefined') module.exports = Coortes;
