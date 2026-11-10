"""Reproduz as tabelas do estudo exploratório de inteligência comparativa longitudinal da PNP.

Relatório: docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md

Somente leitura. T1–T12 usam apenas a biblioteca padrão (csv, sqlite3 em memória).
T13 é opcional e usa openpyxl (já usado em poc/extrair_dados.py) para ler o demonstrativo C5 da matriz 2026.
Fonte: exportação local dos Indicadores de Gestão da PNP (pasta `indicadores-gestao/`,
não versionada; 19 CSV, anos-base 2017–2025, 64 instituições).

Uso, da raiz do repositório:
    python3 docs/dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py [caminho/indicadores-gestao]
Também aceita a variável de ambiente PNP_DIR. Tempo típico: < 30 s.

Convenções:
  - "Ano" nos arquivos = ano-base (não a edição PNP). Verificado na v1 do protótipo contra a matriz 2026.
  - Rede41 = Institutos Federais + Cefets + Colégio Pedro II (universo da Matriz CONIF, 41 instituições);
    exclui as 23 Escolas Técnicas Vinculadas.
  - "Regular presencial" = presencial, excluídos cursos FIC (Qualificação Profissional).
  - ME = Matrícula Equivalente | Geral de DadosGerais.csv (= PercentuaisLegais.csv ÷ 100).
  - Médias trienais: A = 2017–2019 (pré-pandemia), B = 2023–2025 (pós-normalização).
"""
import csv
import math
import os
import re
import sqlite3
import statistics as st
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
PNP = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PNP_DIR", RAIZ / "indicadores-gestao"))
ANOS = [str(a) for a in range(2017, 2026)]
A3, B3 = ("2017", "2018", "2019"), ("2023", "2024", "2025")
R41 = "Organizacao_Academica_PNP<>'Escola Técnica Vinculada'"
PRES = "ModalidadeEnsino='Educação Presencial'"
EAD = "ModalidadeEnsino='Educação a Distância'"
REG = "tipoCurso NOT LIKE 'Qualifica%'"
GRAD = "tipoCurso IN ('Tecnologia','Bacharelado','Licenciatura')"
POS = "(tipoCurso LIKE 'Especializa%' OR tipoCurso LIKE 'Mestrado%' OR tipoCurso LIKE 'Doutorado%')"
BAS = "tipoCurso IN ('Ensino Médio','Ensino Fundamental I','Ensino Fundamental II','Educação Infantil','ABI')"
FIC = "tipoCurso LIKE 'Qualifica%'"
TEC = "tipoCurso='Técnico'"


def carregar(pasta):
    con = sqlite3.connect(":memory:")
    num = re.compile(r"^-?[0-9]+(,[0-9]+)?$")
    inv = []
    for dp, _, fs in sorted(os.walk(pasta)):
        for f in sorted(fs):
            if not f.endswith(".csv"):
                continue
            with open(os.path.join(dp, f), encoding="utf-8") as fh:
                rd = csv.reader(fh, delimiter=";")
                cols = next(rd)
                rows = list(rd)
            ncols = {i for i, c in enumerate(cols) if c != "Ano"
                     and any(r[i].strip() for r in rows) and all(num.match(r[i]) for r in rows if r[i].strip())}
            safe = [re.sub(r"[^A-Za-z0-9]+", "_", unicodedata.normalize("NFKD", c.replace("%", "pct"))
                           .encode("ascii", "ignore").decode()).strip("_") for c in cols]
            t = f[:-4]
            con.execute(f'CREATE TABLE "{t}" (' + ",".join(
                f'"{s}" {"REAL" if i in ncols else "TEXT"}' for i, s in enumerate(safe)) + ")")
            con.executemany(f'INSERT INTO "{t}" VALUES ({",".join("?" * len(cols))})',
                            [[(float(v.replace(",", ".")) if i in ncols else v) if v.strip() else None
                              for i, v in enumerate(r)] for r in rows])
            inv.append((os.path.relpath(os.path.join(dp, f), pasta), os.path.getsize(os.path.join(dp, f)), len(rows)))
    return con, inv


def titulo(s):
    print("\n" + "=" * 100 + "\n" + s + "\n" + "=" * 100)


def painel(con, sql, args=()):
    d = {}
    for *k, a, v in con.execute(sql, args):
        d.setdefault(k[0] if len(k) == 1 else tuple(k), {})[a] = v or 0
    return d


def media(d, anos):
    return sum(d.get(a, 0) for a in anos) / len(anos)


def corr(x, y):
    mx, my = st.mean(x), st.mean(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / math.sqrt(
        sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))


def linha(rot, vals, fmt="{:9.0f}", w=34):
    print(f"{rot[:w-1]:{w}}" + "".join(fmt.format(v or 0) for v in vals))


def main():
    if not PNP.exists():
        sys.exit(f"Pasta PNP não encontrada: {PNP}")
    con, inv = carregar(PNP)

    titulo("T1. Inventário: arquivos, linhas, anos-base, instituições e unidades")
    for rel, tam, n in inv:
        t = Path(rel).stem
        cols = [r[1] for r in con.execute(f'PRAGMA table_info("{t}")')]
        anos = [r[0] for r in con.execute(f'SELECT DISTINCT Ano FROM "{t}" ORDER BY 1')]
        ni = con.execute(f'SELECT COUNT(DISTINCT Instituicao) FROM "{t}" WHERE Instituicao IS NOT NULL').fetchone()[0]
        nu = (con.execute(f'SELECT COUNT(DISTINCT Instituicao||nomeUnidadeRecente) FROM "{t}" WHERE Ano="2025"').fetchone()[0]
              if "nomeUnidadeRecente" in cols else "-")
        print(f"{rel:52} {tam/1e6:6.1f} MB {n:8} linhas  anos {anos[0]}–{anos[-1]}  inst {ni:3}  unid(2025) {nu}")

    titulo("T2. Coerência do universo de matrículas entre arquivos e escala da ME (64 instituições)")
    print("ano    mat DadosGerais  mat TaxaEvasao  mat SituacaoMatr  mat Racial  ME DadosGerais  ME PercLegais/100")
    for a in ANOS:
        v = [con.execute(f'SELECT SUM(Numero_de_Matriculas) FROM "{t}" WHERE Ano=?', (a,)).fetchone()[0]
             for t in ("DadosGerais", "TaxaEvasao", "SituacaoMatricula", "CassificacaoRacialRendaSexo")]
        me = con.execute("SELECT SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE Ano=?", (a,)).fetchone()[0]
        pl = con.execute("SELECT SUM(Matricula_Equivalente_Geral)/100 FROM PercentuaisLegais WHERE Ano=?", (a,)).fetchone()[0]
        print(f"{a} {v[0]:15,.0f} {v[1]:15,.0f} {v[2]:17,.0f} {v[3]:11,.0f} {me:15,.0f} {pl:18,.0f}")

    titulo("T3. Quebra metodológica: razão ME/matrícula por tipo e modalidade (64 instituições)")
    print("Salto entre os anos-base 2020 e 2021, coerente com a Portaria Setec/MEC 146/2021 (ME = M × FECH × FEC).")
    print(" " * 34 + "".join(f"{a:>9}" for a in ANOS))
    for t in ("Técnico", "Tecnologia", "Bacharelado", "Licenciatura", "Especialização (Lato Sensu)", "Qualificação Profissional (FIC)"):
        for m in ("Educação Presencial", "Educação a Distância"):
            d = dict(con.execute("SELECT Ano, SUM(Matricula_Equivalente_Geral)/SUM(Numero_de_Matriculas) FROM DadosGerais "
                                 "WHERE tipoCurso=? AND ModalidadeEnsino=? GROUP BY Ano", (t, m)).fetchall())
            linha(f"{t[:22]} {'pres' if 'Presencial' in m else 'EaD'}", [d.get(a, 0) for a in ANOS], "{:9.3f}")

    titulo("T4. Rede41: ME por grupo de oferta (mil) e contribuição ao crescimento 2021→2025")
    grupos = {"Técnico presencial": f"{TEC} AND {PRES}", "Graduação presencial": f"{GRAD} AND {PRES}",
              "Pós-graduação presencial": f"{POS} AND {PRES}", "Básica/ABI presencial": f"{BAS} AND {PRES}",
              "FIC presencial": f"{FIC} AND {PRES}", "Técnico EaD": f"{TEC} AND {EAD}", "Graduação EaD": f"{GRAD} AND {EAD}",
              "Pós-graduação EaD": f"{POS} AND {EAD}", "FIC EaD (inclui MOOC)": f"{FIC} AND {EAD}"}
    res = {k: dict(con.execute(f"SELECT Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE {R41} AND {c} GROUP BY Ano").fetchall())
           for k, c in grupos.items()}
    tot = {a: sum(res[k].get(a, 0) for k in res) for a in ANOS}
    dt = tot["2025"] - tot["2021"]
    print(" " * 34 + "".join(f"{a:>9}" for a in ANOS) + "   Δ21-25   % do Δ")
    for k, v in res.items():
        d = v.get("2025", 0) - v.get("2021", 0)
        print(f"{k:34}" + "".join(f"{v.get(a, 0)/1000:9.1f}" for a in ANOS) + f" {d/1000:+8.1f} {d/dt*100:7.1f}%")
    print(f"{'Total':34}" + "".join(f"{tot[a]/1000:9.1f}" for a in ANOS) + f" {dt/1000:+8.1f}")
    print("\nQuatro grupos mutuamente exclusivos (regular/FIC × presencial/EaD); a soma deve igualar o Δ total:")
    soma = 0
    for rot, c in (("Regular presencial", f"{REG} AND {PRES}"), ("Regular EaD", f"{REG} AND {EAD}"),
                   ("FIC presencial", f"{FIC} AND {PRES}"), ("FIC EaD", f"{FIC} AND {EAD}")):
        v = dict(con.execute(f"SELECT Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE {R41} AND {c} GROUP BY Ano").fetchall())
        d = v["2025"] - v["2021"]
        soma += d
        print(f"  {rot:20} 2021 {v['2021']:10,.0f}  2025 {v['2025']:10,.0f}  Δ {d:+9,.0f}  ({d/dt*100:5.1f}% do Δ)")
    print(f"  {'Soma dos grupos':20} Δ {soma:+,.0f}  ×  Δ total {dt:+,.0f}")
    mat = {k: dict(con.execute(f"SELECT Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE {R41} AND {c} GROUP BY Ano").fetchall())
           for k, c in grupos.items()}
    print("\nMatrículas (mil), mesmo recorte:")
    for k, v in mat.items():
        print(f"{k:34}" + "".join(f"{v.get(a, 0)/1000:9.1f}" for a in ANOS))

    titulo("T5. Participação na ME sem FIC da Rede41, 2021→2025: efeito numerador × denominador (p.p.)")
    print("Δparticipação = (x25−x21)/X25 [numerador]  +  x21/X25 − x21/X21 [denominador]")
    reg = painel(con, f"SELECT Instituicao, Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE {R41} AND {REG} GROUP BY 1,2")
    regp = painel(con, f"SELECT Instituicao, Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2")
    tme = painel(con, f"SELECT Instituicao, Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE {R41} GROUP BY 1,2")
    X = {a: sum(reg[i].get(a, 0) for i in reg) for a in ANOS}
    out = []
    for i in reg:
        x0, x1 = reg[i]["2021"], reg[i]["2025"]
        s0, s1 = x0 / X["2021"], x1 / X["2025"]
        nume = (x1 - x0) / X["2025"]
        out.append((i, x0, x1, x1 / x0 * 100, regp[i]["2025"] / regp[i]["2021"] * 100, tme[i]["2025"] / tme[i]["2021"] * 100,
                    s0 * 100, s1 * 100, (s1 - s0) * 100, nume * 100, (s1 - s0 - nume) * 100))
    print(f"{'inst':15}{'ME21':>8}{'ME25':>8}{'idx':>7}{'idxPres':>8}{'idxTot':>8}{'part21':>8}{'part25':>8}{'Δpp':>8}{'num':>8}{'den':>8}")
    for r in sorted(out, key=lambda r: -r[3]):
        print(f"{r[0]:15}{r[1]:8.0f}{r[2]:8.0f}{r[3]:7.1f}{r[4]:8.1f}{r[5]:8.1f}{r[6]:8.2f}{r[7]:8.2f}{r[8]:+8.3f}{r[9]:+8.3f}{r[10]:+8.3f}")

    titulo("T6. Matrículas regulares presenciais: médias 2017–19 (A) × 2023–25 (B), fluxo e campi (Rede41)")
    m = painel(con, f"SELECT Instituicao, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2")
    tec = painel(con, f"SELECT Instituicao, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE {R41} AND {TEC} AND {PRES} GROUP BY 1,2")
    gra = painel(con, f"SELECT Instituicao, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE {R41} AND {GRAD} AND {PRES} GROUP BY 1,2")
    ing = painel(con, f"SELECT Instituicao, Ano, SUM(Numero_de_ingressantes) FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2")
    vag = painel(con, f"SELECT Instituicao, Ano, SUM(Numero_de_vagas) FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2")
    cam = painel(con, f"SELECT Instituicao, nomeUnidadeRecente, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2,3")
    pe = painel(con, f"SELECT Instituicao, Ano, SUM(RAP_Professor_Equivalente) FROM RelacaoAlunoProfessorRAP WHERE {R41} GROUP BY 1,2")
    I = sorted(m)
    MA, MB = sum(media(m[i], A3) for i in I), sum(media(m[i], B3) for i in I)
    IA, IB = sum(media(ing[i], A3) for i in I), sum(media(ing[i], B3) for i in I)
    VA, VB = sum(media(vag[i], A3) for i in I), sum(media(vag[i], B3) for i in I)
    PA, PB = sum(media(pe[i], A3) for i in I), sum(media(pe[i], B3) for i in I)
    print(f"Rede41: matrículas {MA:,.0f} → {MB:,.0f} (idx {MB/MA*100:.1f}); ingressantes {IA:,.0f} → {IB:,.0f} (idx {IB/IA*100:.1f}); "
          f"vagas idx {VB/VA*100:.1f}; M/I {MA/IA:.2f} → {MB/IB:.2f}; professor-equivalente idx {PB/PA*100:.1f}")
    print("M/I = matrículas ÷ ingressantes do mesmo ano (anos de permanência por ingressante, proxy de estoque/fluxo)")
    print(f"{'inst':15}{'matA':>8}{'matB':>8}{'idx':>7}{'ΔTec':>7}{'ΔGrad':>7}{'idxVag':>7}{'idxIng':>7}{'M/I A':>7}{'M/I B':>7}"
          f"{'top3%':>7}{'cam+':>5}{'cam-':>5}{'partA':>7}{'partB':>7}")
    linhas, gm, gi, gr, gp = [], [], [], [], []
    for i in I:
        a, b = media(m[i], A3), media(m[i], B3)
        dc = [media(v, B3) - media(v, A3) for k, v in cam.items() if k[0] == i]
        pos = sorted([x for x in dc if x > 0], reverse=True)
        up = sum(1 for k, v in cam.items() if k[0] == i and media(v, A3) > 0 and media(v, B3) / media(v, A3) > 1.05)
        dn = sum(1 for k, v in cam.items() if k[0] == i and media(v, A3) > 0 and media(v, B3) / media(v, A3) < 0.95)
        ia, ib = media(ing[i], A3), media(ing[i], B3)
        linhas.append((i, a, b, b / a * 100, media(tec[i], B3) - media(tec[i], A3), media(gra[i], B3) - media(gra[i], A3),
                       media(vag[i], B3) / media(vag[i], A3) * 100, ib / ia * 100, a / ia, b / ib,
                       sum(pos[:3]) / sum(pos) * 100 if pos else 0, up, dn, a / MA * 100, b / MB * 100))
        gm.append(math.log(b / a)); gi.append(math.log(ib / ia)); gr.append(math.log((b / ib) / (a / ia)))
        gp.append(media(pe[i], B3) / media(pe[i], A3) - 1)
    for r in sorted(linhas, key=lambda r: -r[3]):
        print(f"{r[0]:15}{r[1]:8.0f}{r[2]:8.0f}{r[3]:7.1f}{r[4]:+7.0f}{r[5]:+7.0f}{r[6]:7.1f}{r[7]:7.1f}{r[8]:7.2f}{r[9]:7.2f}"
              f"{r[10]:7.0f}{r[11]:5}{r[12]:5}{r[13]:7.2f}{r[14]:7.2f}")
    cv = lambda x, y: sum((p - st.mean(x)) * (q - st.mean(y)) for p, q in zip(x, y)) / (len(x) - 1)
    print(f"\nn={len(I)} instituições. corr(Δlog ingressantes, Δlog matrículas) = {corr(gi, gm):.2f}; "
          f"corr(Δlog M/I, Δlog matrículas) = {corr(gr, gm):.2f}; corr(Δ% prof.-equivalente, Δlog matrículas) = {corr(gp, gm):.2f}")
    print(f"Decomposição da variância de Δlog matrículas: ingressantes {cv(gi, gm)/st.variance(gm):.2f}; M/I {cv(gr, gm)/st.variance(gm):.2f}")
    ev = painel(con, f"SELECT Instituicao, Ano, SUM(Matriculas_Numero_de_Evadidos)*100.0/SUM(Numero_de_Matriculas) FROM TaxaEvasao WHERE {R41} AND {REG} AND {PRES} GROUP BY 1,2")
    dev = [media(ev[i], B3) - media(ev[i], A3) for i in I]
    print(f"corr(Δ evasão anual média, p.p., Δlog matrículas) = {corr(dev, gm):.2f}; corr(Δ evasão, Δlog M/I) = {corr(dev, gr):.2f}")

    titulo("T7. Percentual de ME em cursos técnicos (%CT, PercentuaisLegais) por instituição — Rede41")
    ct = painel(con, f"SELECT Instituicao, Ano, SUM(Matricula_Equivalente_Tecnicos)*100/SUM(Matricula_Equivalente_Geral) FROM PercentuaisLegais WHERE {R41} GROUP BY 1,2")
    fp = painel(con, f"SELECT Instituicao, Ano, SUM(Matricula_Equivalente_Formacao_de_Professores)*100/SUM(Matricula_Equivalente_Geral) FROM PercentuaisLegais WHERE {R41} GROUP BY 1,2")
    print(" " * 15 + "".join(f"{a:>7}" for a in ANOS) + "   FP21   FP25")
    for i in sorted(ct, key=lambda i: -ct[i]["2025"]):
        print(f"{i:15}" + "".join(f"{ct[i].get(a, 0):7.1f}" for a in ANOS) + f"{fp[i]['2021']:7.1f}{fp[i]['2025']:7.1f}")
    r = con.execute(f"SELECT Ano, SUM(Matricula_Equivalente_Tecnicos)*100/SUM(Matricula_Equivalente_Geral) FROM PercentuaisLegais WHERE {R41} GROUP BY Ano").fetchall()
    print(f"{'Rede41':15}" + "".join(f"{v:7.1f}" for _, v in r))
    print("Instituições com %CT ≥ 50%: " + ", ".join(f"{a}: {sum(1 for i in ct if ct[i].get(a, 0) >= 50)}" for a in ANOS))

    titulo("T8. Ifes por campus: matrículas regulares presenciais 2017–2025 e variações")
    cm = painel(con, f"SELECT nomeUnidadeRecente, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE Instituicao='IFES' AND {REG} AND {PRES} GROUP BY 1,2")
    ct_ = painel(con, f"SELECT nomeUnidadeRecente, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE Instituicao='IFES' AND {TEC} AND {PRES} GROUP BY 1,2")
    cg = painel(con, f"SELECT nomeUnidadeRecente, Ano, SUM(Numero_de_Matriculas) FROM DadosGerais WHERE Instituicao='IFES' AND {GRAD} AND {PRES} GROUP BY 1,2")
    ci = painel(con, f"SELECT nomeUnidadeRecente, Ano, SUM(Numero_de_ingressantes) FROM DadosGerais WHERE Instituicao='IFES' AND {REG} AND {PRES} GROUP BY 1,2")
    print(f"{'campus':32}" + "".join(f"{a:>7}" for a in ANOS) + "  ΔA→B  ΔTec ΔGrad idxIng  M/I A  M/I B")
    for u in sorted(cm, key=lambda u: -cm[u].get("2025", 0)):
        if media(cm[u], B3) < 1:
            continue
        ia, ib = media(ci.get(u, {}), A3), media(ci.get(u, {}), B3)
        print(f"{u.replace('Campus ', '')[:31]:32}" + "".join(f"{cm[u].get(a, 0):7.0f}" for a in ANOS) +
              f"{media(cm[u], B3)-media(cm[u], A3):+6.0f}{media(ct_.get(u, {}), B3)-media(ct_.get(u, {}), A3):+6.0f}"
              f"{media(cg.get(u, {}), B3)-media(cg.get(u, {}), A3):+6.0f}{(ib/ia*100 if ia else 0):7.0f}"
              f"{(media(cm[u], A3)/ia if ia else 0):7.2f}{(media(cm[u], B3)/ib if ib else 0):7.2f}")

    titulo("T9. Ifes × Rede41: vagas, ingressantes, matrículas, concluintes e evasão anual por oferta (presencial)")
    for nome, filt, args in (("IFES", "Instituicao=?", ("IFES",)), ("Rede41", R41, ())):
        for rot, c in (("Técnico integrado", f"{TEC} AND tipoOferta='Integrado'"),
                       ("Técnico concomitante+subsequente", f"{TEC} AND tipoOferta IN ('Concomitante','Subsequente')"),
                       ("Graduação", GRAD)):
            r = con.execute(f"SELECT Ano, SUM(Numero_de_vagas), SUM(Numero_de_ingressantes), SUM(Numero_de_Matriculas), SUM(Numero_de_concluintes) "
                            f"FROM DadosGerais WHERE {filt} AND {PRES} AND {c} GROUP BY Ano", args).fetchall()
            e = dict(con.execute(f"SELECT Ano, SUM(Matriculas_Numero_de_Evadidos)*100.0/SUM(Numero_de_Matriculas) FROM TaxaEvasao "
                                 f"WHERE {filt} AND {PRES} AND {c} GROUP BY Ano", args).fetchall())
            print(f"\n{nome} — {rot}\n{'ano':6}{'vagas':>8}{'ingr':>8}{'mat':>9}{'concl':>8}{'evas%':>7}{'M/I':>6}")
            for a, v, i, mm, cc in r:
                print(f"{a:6}{v or 0:8.0f}{i or 0:8.0f}{mm:9.0f}{cc or 0:8.0f}{e.get(a, 0):7.1f}{(mm/i if i else 0):6.2f}")

    print("\nMédias trienais A (2017–19) × B (2023–25) por tipo/oferta, regular presencial")
    ofertas = (("Técnico integrado", f"{TEC} AND tipoOferta='Integrado'"),
               ("Técnico concomitante+subsequente", f"{TEC} AND tipoOferta IN ('Concomitante','Subsequente')"),
               ("Técnico subsequente", f"{TEC} AND tipoOferta='Subsequente'"),
               ("Técnico PROEJA integrado", f"{TEC} AND tipoOferta='PROEJA - Integrado'"),
               ("Graduação", GRAD), ("Bacharelado", "tipoCurso='Bacharelado'"),
               ("Licenciatura", "tipoCurso='Licenciatura'"), ("Tecnologia", "tipoCurso='Tecnologia'"))
    print(f"{'recorte':10}{'oferta':34}{'vagA':>8}{'vagB':>8}{'ingA':>8}{'ingB':>8}{'matA':>9}{'matB':>9}{'M/I A':>7}{'M/I B':>7}{'i/v A':>7}{'i/v B':>7}")
    for nome, filt, args in (("IFES", "Instituicao=?", ("IFES",)), ("Rede41", R41, ())):
        for rot, c in ofertas:
            q = lambda col, anos: con.execute(f"SELECT SUM({col})/3.0 FROM DadosGerais WHERE {filt} AND {PRES} AND {c} "
                                              f"AND Ano IN ({','.join('?' * 3)})", args + anos).fetchone()[0] or 0
            va, vb, ia, ib = q("Numero_de_vagas", A3), q("Numero_de_vagas", B3), q("Numero_de_ingressantes", A3), q("Numero_de_ingressantes", B3)
            ma, mb = q("Numero_de_Matriculas", A3), q("Numero_de_Matriculas", B3)
            print(f"{nome:10}{rot:34}{va:8.0f}{vb:8.0f}{ia:8.0f}{ib:8.0f}{ma:9.0f}{mb:9.0f}"
                  f"{(ma/ia if ia else 0):7.2f}{(mb/ib if ib else 0):7.2f}{(ia/va if va else 0):7.2f}{(ib/vb if vb else 0):7.2f}")

    titulo("T10. Efeitos da pandemia e de fluxo (Rede41, regular presencial)")
    print("ano   evasão anual %   %retidos entre 'em curso' (todas as ofertas)   inscritos/vaga   ingressantes/vaga")
    for a in ANOS:
        e = con.execute(f"SELECT SUM(Matriculas_Numero_de_Evadidos)*100.0/SUM(Numero_de_Matriculas) FROM TaxaEvasao WHERE {R41} AND {REG} AND {PRES} AND Ano=?", (a,)).fetchone()[0]
        rt = con.execute(f"SELECT SUM(CASE WHEN FluxoRetido='Retido' THEN Numero_de_Matriculas END)*100.0/SUM(Numero_de_Matriculas) FROM SituacaoMatricula "
                         f"WHERE {R41} AND categoriaSituacao='Em curso' AND Ano=?", (a,)).fetchone()[0]
        iv, gv = con.execute(f"SELECT SUM(Numero_de_inscritos)*1.0/SUM(Numero_de_vagas), SUM(Numero_de_ingressantes)*1.0/SUM(Numero_de_vagas) "
                             f"FROM DadosGerais WHERE {R41} AND {REG} AND {PRES} AND Numero_de_vagas>0 AND Ano=?", (a,)).fetchone()
        print(f"{a}  {e:14.1f}  {rt:44.1f}  {iv:15.2f}  {gv:17.3f}")

    titulo("T11. Casos: séries de apoio")
    for inst in ("IFMA", "IFPE", "IFRS", "IFES"):
        print(f"\n{inst}")
        for rot, c in (("ME técnico presencial", f"{TEC} AND {PRES}"), ("ME graduação presencial", f"{GRAD} AND {PRES}"),
                       ("ME técnico EaD", f"{TEC} AND {EAD}"), ("ME pós EaD", f"{POS} AND {EAD}"), ("ME FIC EaD", f"{FIC} AND {EAD}")):
            d = dict(con.execute(f"SELECT Ano, SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE Instituicao=? AND {c} GROUP BY Ano", (inst,)).fetchall())
            linha(rot, [d.get(a, 0) for a in ANOS], "{:8.0f}", 26)
        d = dict(con.execute("SELECT Ano, SUM(CASE WHEN FluxoRetido='Retido' THEN Numero_de_Matriculas END)*100.0/SUM(Numero_de_Matriculas) "
                             "FROM SituacaoMatricula WHERE Instituicao=? AND categoriaSituacao='Em curso' GROUP BY Ano", (inst,)).fetchall())
        linha("% retidos entre em curso", [d.get(a, 0) for a in ANOS], "{:8.1f}", 26)
        d = dict(con.execute(f"SELECT Ano, SUM(Numero_de_ingressantes)*1.0/SUM(Numero_de_vagas) FROM DadosGerais WHERE Instituicao=? AND {PRES} "
                             f"AND {TEC} AND tipoOferta='Subsequente' AND Numero_de_vagas>0 GROUP BY Ano", (inst,)).fetchall())
        linha("ingr/vaga técn. subseq.", [d.get(a, 0) for a in ANOS], "{:8.2f}", 26)
        d = dict(con.execute(f"SELECT Ano, SUM(Numero_de_ingressantes)*1.0/SUM(Numero_de_vagas) FROM DadosGerais WHERE Instituicao=? AND {PRES} "
                             f"AND {GRAD} AND Numero_de_vagas>0 GROUP BY Ano", (inst,)).fetchall())
        linha("ingr/vaga graduação", [d.get(a, 0) for a in ANOS], "{:8.2f}", 26)
    print("\nIfes: %CT com e sem o Cefor, e sem a especialização EaD de Colatina (pulso de 2021 e 2023)")
    for a in ANOS:
        t, g = con.execute("SELECT SUM(Matricula_Equivalente_Tecnicos)/100, SUM(Matricula_Equivalente_Geral)/100 FROM PercentuaisLegais WHERE Instituicao='IFES' AND Ano=?", (a,)).fetchone()
        tc, gc = con.execute("SELECT SUM(Matricula_Equivalente_Tecnicos)/100, SUM(Matricula_Equivalente_Geral)/100 FROM PercentuaisLegais WHERE Instituicao='IFES' "
                             "AND nomeUnidadeRecente NOT LIKE 'Centro de Refer%' AND Ano=?", (a,)).fetchone()
        col = con.execute(f"SELECT COALESCE(SUM(Matricula_Equivalente_Geral),0) FROM DadosGerais WHERE Instituicao='IFES' AND nomeUnidadeRecente='Campus Colatina' "
                          f"AND tipoCurso LIKE 'Especializa%' AND {EAD} AND Ano=?", (a,)).fetchone()[0]
        print(f"{a}  com Cefor {t/g*100:5.1f}%   sem Cefor {tc/gc*100:5.1f}%   especialização EaD Colatina {col:6.0f} ME   "
              f"%CT sem esse pulso {t/(g-col)*100:5.1f}%")

    titulo("T12. Indicadores de capacidade e gastos (nominais) — Rede41")
    for a in ANOS:
        rap = con.execute(f"SELECT SUM(RAP_Matriculas_RAP)/SUM(RAP_Professor_Equivalente), SUM(RAP_Professor_Equivalente) FROM RelacaoAlunoProfessorRAP WHERE {R41} AND Ano=?", (a,)).fetchone()
        g = con.execute("SELECT SUM(Gastos_Correntes_Gastos_Correntes)/1e9 FROM IndicadoresGastos WHERE Ano=?", (a,)).fetchone()[0]
        print(f"{a}  RAP {rap[0]:6.2f}  professor-equivalente {rap[1]:8,.0f}  gastos correntes R$ {g:6.2f} bi (nominal)")

    titulo("T13. Numerador da RAP da matriz 2026 (C5, 'MEq-RAP Pres') × candidatos PNP, ano-base 2024")
    c5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
    try:
        import openpyxl
    except ImportError:
        print("openpyxl ausente: seção opcional não executada.")
        return
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[^A-Z ]", " ", unicodedata.normalize("NFKD", s.upper())
                                                .encode("ascii", "ignore").decode())).strip()
    extra = {"CEFET MG": "CEFET-MG", "CEFET RJ": "CEFET-RJ", "INSTITUTO FEDERAL DE MATO GROSSO DO SUL": "IFMS",
             "INSTITUTO FEDERAL DE MATO GROSSO": "IFMT", "INSTITUTO FEDERAL DE TOCANTINS": "IFTO", "INSTITUTO FEDERAL DO SUL MINAS GERAIS": "IFSULDEMINAS"}
    sig = {norm(n): s for n, s in con.execute(f"SELECT DISTINCT Instituicao_Nome, Instituicao FROM DadosGerais WHERE {R41}")}
    wb = openpyxl.load_workbook(c5, data_only=True, read_only=True)
    pares = []
    for r in wb["Indicadores"].iter_rows(min_row=8, max_row=60, values_only=True):
        if not (r[2] and isinstance(r[12], (int, float))):
            continue
        s = sig.get(norm(r[2])) or extra.get(norm(r[2]))
        if not s:
            print("sem par:", r[2])
            continue
        q = lambda cond: con.execute(f"SELECT SUM(Matricula_Equivalente_Geral) FROM DadosGerais WHERE Instituicao=? AND Ano='2024' AND {cond}", (s,)).fetchone()[0] or 0
        mr, pe = con.execute("SELECT SUM(RAP_Matriculas_RAP), SUM(RAP_Professor_Equivalente) FROM RelacaoAlunoProfessorRAP WHERE Instituicao=? AND Ano='2024'", (s,)).fetchone()
        pares.append((s, r[12], r[13], q(PRES), q(f"{PRES} AND {REG}"), mr, pe))
    print(f"{len(pares)} instituições pareadas. Razão candidato ÷ MEq-RAP da matriz:")
    for rot, j in (("ME presencial (com FIC) — via ALRAPE do guia", 3), ("ME presencial sem FIC", 4), ("Matrículas RAP (arquivo PNP)", 5)):
        r = [p[j] / p[1] for p in pares]
        print(f"  {rot:46} mediana {st.median(r):.3f}  mín {min(r):.3f}  máx {max(r):.3f}  ±1%: {sum(abs(x-1) <= .01 for x in r):2}  ±3%: {sum(abs(x-1) <= .03 for x in r):2}")
    r = [p[6] / p[2] for p in pares]
    print(f"  {'Professor-equivalente (PNP ÷ matriz)':46} mediana {st.median(r):.3f}  mín {min(r):.3f}  máx {max(r):.3f}")
    for p in pares:
        if p[0] == "IFES":
            print(f"  Ifes: matriz {p[1]:,.2f} / {p[2]} = {p[1]/p[2]:.3f}; ME presencial {p[3]:,.0f} / {p[6]:,.0f} = {p[3]/p[6]:.2f}; "
                  f"Matrículas RAP {p[5]:,.0f} / {p[6]:,.0f} = {p[5]/p[6]:.2f}")


if __name__ == "__main__":
    main()
