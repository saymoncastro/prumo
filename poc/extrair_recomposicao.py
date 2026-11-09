"""Extrai os dados públicos da demonstração de recomposição de oferta (Itapina e Barra de São Francisco).

Fonte: PNP, exportação de Indicadores de Gestão em `indicadores-gestao/` (não versionada);
demonstrativo IFMT da matriz 2026 (C5) para os indicadores da Rede e os submontantes de Qualidade.
Saída: poc/dados-recomposicao.json. Executar da raiz:  python3 poc/extrair_recomposicao.py

Classes de oferta, conferidas com PercentuaisLegais.csv (ver `conciliacao` na saída):
  técnico  = tipoCurso "Técnico";
  EJA      = tipoOferta contém "PROEJA";
  formação de professores = tipoCurso "Licenciatura" ou nome com "Pedagóg" (formação pedagógica).
A regra de formação de professores fecha com a PNP nos dois campi em 2024 e 2025, mas não no Ifes
inteiro: a PNP marca como formação de professores outros cursos (especializações, oferta do Cefor) que
o nome não identifica. Por isso o total do Ifes vem sempre de PercentuaisLegais.csv.
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
PNP = RAIZ / "indicadores-gestao"
C5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
SAIDA = Path(__file__).with_name("dados-recomposicao.json")
CAMPI = {"Campus Itapina": "Itapina", "Campus Barra de São Francisco": "Barra de São Francisco"}
ANOS = [str(a) for a in range(2017, 2026)]


def num(x):
    x = (x or "").strip()
    return float(x.replace(".", "").replace(",", ".")) if x else 0.0


def ler(rel, inst="IFES"):
    with open(PNP / rel, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter=";") if r["Ano"] in ANOS and (inst is None or r["Instituicao"] == inst)]


def classe(r):
    tec = r["tipoCurso"] == "Técnico"
    return {"tec": tec, "eja": "PROEJA" in r["tipoOferta"],
            "fp": r["tipoCurso"] == "Licenciatura" or "Pedagóg" in r["nomeIdCurso"]}


def nome_base(s):
    return re.sub(r"\s*\(.*$", "", s).strip()


def main():
    dg = ler("DadosGerais.csv")
    pl = ler("percentuais-legais/PercentuaisLegais.csv")
    ev = ler("indicadores-academicos/TaxaEvasao.csv")

    # Ifes e campi pelos percentuais legais (escala de DadosGerais: PL está ×100)
    ifes = {a: {"meq": 0, "ct": 0, "fp": 0, "eja": 0} for a in ANOS}
    por_campus = defaultdict(lambda: {a: {"meq": 0, "ct": 0, "fp": 0, "eja": 0} for a in ANOS})
    for r in pl:
        v = {"meq": num(r["Matrícula Equivalente | Geral"]) / 100, "ct": num(r["Matrícula Equivalente | Técnicos"]) / 100,
             "fp": num(r["Matrícula Equivalente | Formação de Professores"]) / 100,
             "eja": num(r["Matrícula Equivalente | Proeja"]) / 100}
        for k in v:
            ifes[r["Ano"]][k] += v[k]
            por_campus[r["nomeUnidadeRecente"]][r["Ano"]][k] += v[k]

    # conciliação das classes por curso com os percentuais legais, Ifes inteiro, por ano
    soma = {a: defaultdict(float) for a in ANOS}
    for r in dg:
        me, c = num(r["Matrícula Equivalente | Geral"]), classe(r)
        s = soma[r["Ano"]]
        s["meq"] += me
        for k, kk in (("tec", "ct"), ("fp", "fp"), ("eja", "eja")):
            if c[k]:
                s[kk] += me
    conc = {a: {k: [round(soma[a][k], 1), round(ifes[a][k], 1)] for k in ("meq", "ct", "fp", "eja")} for a in ANOS}

    # turno, eixo e evasão por oferta (nome do curso sem o sufixo de tipo)
    evm = defaultdict(lambda: {"turnos": set(), "eixo": "", "evasao": {}})
    for r in ev:
        if r["nomeUnidadeRecente"] not in CAMPI:
            continue
        k = (r["nomeUnidadeRecente"], r["nomeCurso"].strip().lower(), r["tipoOferta"])
        e = evm[k]
        e["turnos"].add(r["turnoCurso"])
        e["eixo"] = r["tipoEixoTecnologico"]
        if r["Matrículas | Taxa de Evasão %"]:
            e["evasao"][r["Ano"]] = round(num(r["Matrículas | Taxa de Evasão %"]), 3)

    def achar_ev(unid, curso, oferta, tipo):
        nb = nome_base(curso).lower()
        alvo = [k for k in evm if k[0] == unid and k[2] == oferta]
        for k in alvo:
            if k[1] == nb:
                return evm[k]
        # ex.: "Agronomia" × "bacharelado em agronomia"; "Ciências Agrárias" × "licenciatura em ciências agrárias"
        for k in alvo:
            if k[1].endswith(nb) or nb.endswith(k[1]):
                return evm[k]
        return None

    campi = {}
    for unid, curto in CAMPI.items():
        of = {}
        for r in dg:
            if r["nomeUnidadeRecente"] != unid:
                continue
            k = (r["nomeIdCurso"], r["tipoOferta"], r["ModalidadeEnsino"])
            o = of.setdefault(k, {"id": " | ".join(k), "curso": nome_base(r["nomeIdCurso"]), "tipo": r["tipoCurso"],
                                  "oferta": r["tipoOferta"], "presencial": "Presencial" in r["ModalidadeEnsino"],
                                  "classe": classe(r), "serie": {}})
            o["serie"][r["Ano"]] = [num(r["Número de vagas"]), num(r["Número de inscritos"]), num(r["Número de ingressantes"]),
                                   num(r["Número de Matrículas"]), num(r["Número de concluintes"]),
                                   round(num(r["Matrícula Equivalente | Geral"]), 3)]
        lista = []
        for o in of.values():
            e = achar_ev(unid, o["curso"], o["oferta"], o["tipo"])
            o["turno"] = ", ".join(sorted(e["turnos"])) if e else ""
            o["eixo"] = e["eixo"] if e else ""
            o["evasao"] = e["evasao"] if e else {}
            lista.append(o)
        lista.sort(key=lambda o: -max(v[3] for v in o["serie"].values()))
        rap = {r["Ano"]: num(r["RAP | Professor Equivalente"]) for r in ler("indicadores-academicos/RelacaoAlunoProfessorRAP.csv")
               if r["nomeUnidadeRecente"] == unid}
        campi[curto] = {"unidade": unid, "pl": por_campus[unid], "professores_equivalentes": rap, "ofertas": lista}

    # parâmetros emprestados de ofertas equivalentes no Ifes (2024–2025)
    ev_all = ler("indicadores-academicos/TaxaEvasao.csv")
    emprestimos = {"agroindustria": [], "proeja_tecnico": []}
    for r in dg:
        if r["Ano"] not in ("2024", "2025") or r["tipoCurso"] != "Técnico":
            continue
        mat, me = num(r["Número de Matrículas"]), num(r["Matrícula Equivalente | Geral"])
        if mat <= 0:
            continue
        item = {"ano": r["Ano"], "campus": r["nomeUnidadeRecente"].replace("Campus ", ""), "curso": nome_base(r["nomeIdCurso"]),
                "oferta": r["tipoOferta"], "matriculas": mat, "me": round(me, 3)}
        if "Agroindústria" in r["nomeIdCurso"]:
            emprestimos["agroindustria"].append(item)
        if "PROEJA" in r["tipoOferta"]:
            emprestimos["proeja_tecnico"].append(item)
    evasao_proeja = [{"ano": r["Ano"], "campus": r["nomeUnidadeRecente"].replace("Campus ", ""), "curso": r["nomeCurso"],
                      "turno": r["turnoCurso"], "matriculas": num(r["Número de Matrículas"]),
                      "evasao": round(num(r["Matrículas | Taxa de Evasão %"]), 3)}
                     for r in ev_all if r["Ano"] in ("2024", "2025") and "PROEJA" in r["tipoOferta"]
                     and r["tipoCurso"] == "Técnico" and r["Matrículas | Taxa de Evasão %"]]
    emprestimos["evasao_proeja"] = evasao_proeja

    gastos = {r["Ano"]: {"gasto_corrente_por_me": round(num(r["Gastos Correntes por matrícula equivalente"]), 2),
                         "outros_custeios": round(num(r["Gastos Correntes | Outros Custeios"]), 2)}
              for r in ler("indicadores-gastos/IndicadoresGastos.csv") if r["Ano"] in ("2023", "2024", "2025")}

    wb = openpyxl.load_workbook(C5, data_only=True)
    ind, cc = wb["Indicadores"], wb["Cálculo Custeio"]
    rede = [{"nome": ind[f"C{i}"].value, "ct": ind[f"R{i}"].value, "fp": ind[f"T{i}"].value, "eja": ind[f"V{i}"].value}
            for i in range(8, 49) if ind[f"C{i}"].value]
    sub = {"CT": cc["E54"].value, "FP": cc["E56"].value, "EJA": cc["E58"].value}

    dados = {
        "gerado_por": "poc/extrair_recomposicao.py",
        "fontes": {"pnp": "PNP, Indicadores de Gestão (exportação local); Ano = ano-base",
                   "matriz_2026": "C5, demonstrativo IFMT PLOA 2026 (docs/dominio/evidencias/2026-11-08)"},
        "anos": ANOS, "ifes": ifes, "conciliacao": conc, "campi": campi, "emprestimos": emprestimos,
        "gastos": gastos, "matriz_2026": {"rede": rede, "submontantes": sub},
    }
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, separators=(",", ":")))
    print(SAIDA.name, f"{SAIDA.stat().st_size/1024:.0f} KB")
    for a in ("2024", "2025"):
        print(" conciliação", a, conc[a])
    for c, v in campi.items():
        sem = [o["curso"] for o in v["ofertas"] if not o["turno"] and o["tipo"] in ("Técnico", "Bacharelado", "Licenciatura")
               and "2025" in o["serie"]]
        print(" ", c, len(v["ofertas"]), "ofertas; sem turno:", sem)


if __name__ == "__main__":
    main()
