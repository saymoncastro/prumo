"""Extrai os dados públicos da POC 0.0.2 do Prumo (somente leitura).

POC 0.0.2: jornada Comparar → Simular → Compor com evidência histórica da PNP, em dois campi do Ifes
(Vitória e Serra) escolhidos pela auditoria longitudinal: oferta técnica concomitante com vagas
preenchidas e perda de matrículas e concluintes depois do ingresso.

Fontes:
  - PNP, exportação de Indicadores de Gestão (`indicadores-gestao/`, não versionada; Ano = ano-base);
  - C5, demonstrativo IFMT da matriz 2026 (indicadores da Rede e submontantes de Qualidade).
Saída: poc/dados-poc002.json. Executar da raiz:
    python3 poc/extrair_poc002.py [caminho/indicadores-gestao]     (ou variável PNP_DIR)

Classes de oferta (mesma regra de poc/extrair_recomposicao.py, conciliada com PercentuaisLegais):
técnico = tipoCurso "Técnico"; EJA = tipoOferta contém "PROEJA";
formação de professores = Licenciatura ou nome com "Pedagóg".
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
PNP = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PNP_DIR", RAIZ / "indicadores-gestao"))
C5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
SAIDA = Path(__file__).with_name("dados-poc002.json")
CAMPI = {"Campus Vitória": "Vitória", "Campus Serra": "Serra"}
ANOS = [str(a) for a in range(2017, 2026)]
ETV = "Escola Técnica Vinculada"
GRUPOS = {  # oferta técnica e graduação presenciais, para as trajetórias da etapa Comparar
    "integrado": lambda r: r["tipoCurso"] == "Técnico" and r["tipoOferta"] == "Integrado",
    "concsub": lambda r: r["tipoCurso"] == "Técnico" and r["tipoOferta"] in ("Concomitante", "Subsequente"),
    "proeja": lambda r: r["tipoCurso"] == "Técnico" and "PROEJA" in r["tipoOferta"],
    "graduacao": lambda r: r["tipoCurso"] in ("Bacharelado", "Licenciatura", "Tecnologia"),
}


def num(x):
    x = (x or "").strip()
    return float(x.replace(".", "").replace(",", ".")) if x else 0.0  # ponto = milhar, como nos demais extratores


def ler(rel):
    with open(PNP / rel, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter=";") if r["Ano"] in ANOS]


def classe(r):
    return {"tec": r["tipoCurso"] == "Técnico", "eja": "PROEJA" in r["tipoOferta"],
            "fp": r["tipoCurso"] == "Licenciatura" or "Pedagóg" in r["nomeIdCurso"]}


def nome_base(s):
    return re.sub(r"\s*\(.*$", "", s).strip()


def main():
    if not PNP.exists():
        sys.exit(f"Pasta PNP não encontrada: {PNP}")
    dg = ler("DadosGerais.csv")
    pl = ler("percentuais-legais/PercentuaisLegais.csv")
    ev = ler("indicadores-academicos/TaxaEvasao.csv")
    rapf = ler("indicadores-academicos/RelacaoAlunoProfessorRAP.csv")
    pres = lambda r: r["ModalidadeEnsino"] == "Educação Presencial"

    # 1. Indicadores legais do Ifes e por campus (PercentuaisLegais está ×100 em relação a DadosGerais)
    ifes = {a: {"meq": 0, "ct": 0, "fp": 0, "eja": 0} for a in ANOS}
    por_campus = defaultdict(lambda: {a: {"meq": 0, "ct": 0, "fp": 0, "eja": 0} for a in ANOS})
    for r in pl:
        if r["Instituicao"] != "IFES":
            continue
        v = {"meq": num(r["Matrícula Equivalente | Geral"]) / 100, "ct": num(r["Matrícula Equivalente | Técnicos"]) / 100,
             "fp": num(r["Matrícula Equivalente | Formação de Professores"]) / 100, "eja": num(r["Matrícula Equivalente | Proeja"]) / 100}
        for k in v:
            ifes[r["Ano"]][k] += v[k]
            por_campus[r["nomeUnidadeRecente"]][r["Ano"]][k] += v[k]

    # 2. Trajetórias: Ifes e Rede41 por grupo de oferta presencial (vagas, ingressantes, matrículas, concluintes)
    traj = {"IFES": {g: {a: [0, 0, 0, 0] for a in ANOS} for g in GRUPOS}, "Rede41": {g: {a: [0, 0, 0, 0] for a in ANOS} for g in GRUPOS}}
    campus_grupo = defaultdict(lambda: {g: {a: [0, 0, 0, 0] for a in ANOS} for g in GRUPOS})
    for r in dg:
        if not pres(r) or r["Organização Acadêmica PNP"] == ETV:
            continue
        v = [num(r["Número de vagas"]), num(r["Número de ingressantes"]), num(r["Número de Matrículas"]), num(r["Número de concluintes"])]
        for g, f in GRUPOS.items():
            if f(r):
                alvos = [traj["Rede41"][g][r["Ano"]]]
                if r["Instituicao"] == "IFES":
                    alvos += [traj["IFES"][g][r["Ano"]], campus_grupo[r["nomeUnidadeRecente"].replace("Campus ", "")][g][r["Ano"]]]
                for alvo in alvos:
                    for i in range(4):
                        alvo[i] += v[i]
    # evasão anual por grupo (TaxaEvasao): evadidos ÷ matrículas
    evg = {k: {g: {a: [0, 0] for a in ANOS} for g in GRUPOS} for k in ("IFES", "Rede41")}
    for r in ev:
        if not pres(r) or r["Organização Acadêmica PNP"] == ETV:
            continue
        for g, f in GRUPOS.items():
            if f(r):
                for k in ("Rede41", "IFES") if r["Instituicao"] == "IFES" else ("Rede41",):
                    evg[k][g][r["Ano"]][0] += num(r["Matrículas | Número de Evadidos"])
                    evg[k][g][r["Ano"]][1] += num(r["Número de Matrículas"])
    evasao_grupo = {k: {g: {a: round(x[0] / x[1], 4) if x[1] else None for a, x in v.items()} for g, v in d.items()} for k, d in evg.items()}

    # 3. Ofertas dos campi simulados: série por oferta [vagas, inscritos, ingressantes, matrículas, concluintes, ME]
    evm = defaultdict(lambda: {"turnos": set(), "evadidos": defaultdict(float), "mat": defaultdict(float)})
    for r in ev:
        if r["Instituicao"] != "IFES" or r["nomeUnidadeRecente"] not in CAMPI:
            continue
        e = evm[(r["nomeUnidadeRecente"], r["nomeCurso"].strip().lower(), r["tipoOferta"], r["ModalidadeEnsino"])]
        e["turnos"].add(r["turnoCurso"])
        e["evadidos"][r["Ano"]] += num(r["Matrículas | Número de Evadidos"])
        e["mat"][r["Ano"]] += num(r["Número de Matrículas"])

    def achar_ev(unid, curso, oferta, modal):
        nb = nome_base(curso).lower()
        alvo = [k for k in evm if k[0] == unid and k[2] == oferta and k[3] == modal]
        for k in alvo:
            if k[1] == nb:
                return evm[k]
        for k in alvo:
            if k[1].endswith(nb) or nb.endswith(k[1]):
                return evm[k]
        return None

    campi = {}
    for unid, curto in CAMPI.items():
        of = {}
        for r in dg:
            if r["Instituicao"] != "IFES" or r["nomeUnidadeRecente"] != unid:
                continue
            k = (r["nomeIdCurso"], r["tipoOferta"], r["ModalidadeEnsino"])
            o = of.setdefault(k, {"id": " | ".join(k), "curso": nome_base(r["nomeIdCurso"]), "tipo": r["tipoCurso"],
                                  "oferta": r["tipoOferta"], "presencial": pres(r), "classe": classe(r), "serie": {}})
            o["serie"][r["Ano"]] = [num(r["Número de vagas"]), num(r["Número de inscritos"]), num(r["Número de ingressantes"]),
                                   num(r["Número de Matrículas"]), num(r["Número de concluintes"]),
                                   round(num(r["Matrícula Equivalente | Geral"]), 3)]
        lista = []
        for o in of.values():
            e = achar_ev(unid, o["curso"], o["oferta"], "Educação Presencial" if o["presencial"] else "Educação a Distância")
            o["turno"] = ", ".join(sorted(t for t in e["turnos"] if t)) if e else ""
            o["evasao"] = {a: round(e["evadidos"][a] / e["mat"][a], 4) for a in ANOS if e and e["mat"][a] > 0} if e else {}
            lista.append(o)
        lista.sort(key=lambda o: -max(v[3] for v in o["serie"].values()))
        prof = {r["Ano"]: num(r["RAP | Professor Equivalente"]) for r in rapf if r["Instituicao"] == "IFES" and r["nomeUnidadeRecente"] == unid}
        campi[curto] = {"unidade": unid, "pl": por_campus[unid], "professores_equivalentes": prof, "ofertas": lista,
                        "trajetoria": campus_grupo[curto]}

    # 4. Contexto de todos os campi do Ifes: técnico concomitante+subsequente e integrado, médias trienais
    def media(serie, anos, i):
        return sum(serie[a][i] for a in anos) / len(anos)
    A3, B3 = ANOS[:3], ANOS[-3:]
    contexto = []
    for c, gr in campus_grupo.items():
        linha = {"campus": c}
        for g in ("concsub", "integrado"):
            s = gr[g]
            linha[g] = {"A": [round(media(s, A3, i), 1) for i in range(4)], "B": [round(media(s, B3, i), 1) for i in range(4)]}
        if any(linha[g]["B"][2] > 0 or linha[g]["A"][2] > 0 for g in ("concsub", "integrado")):
            contexto.append(linha)
    contexto.sort(key=lambda x: -(x["concsub"]["A"][2] + x["integrado"]["A"][2]))

    # 5. Matriz 2026 (C5): percentuais legais da Rede e submontantes de Qualidade
    wb = openpyxl.load_workbook(C5, data_only=True)
    ind, cc = wb["Indicadores"], wb["Cálculo Custeio"]
    rede = [{"nome": ind[f"C{i}"].value, "ct": ind[f"R{i}"].value, "fp": ind[f"T{i}"].value, "eja": ind[f"V{i}"].value}
            for i in range(8, 49) if ind[f"C{i}"].value]
    sub = {"CT": cc["E54"].value, "FP": cc["E56"].value, "EJA": cc["E58"].value}

    dados = {
        "gerado_por": "poc/extrair_poc002.py",
        "fontes": {"pnp": "PNP, Indicadores de Gestão (exportação local); Ano = ano-base",
                   "matriz_2026": "C5, demonstrativo IFMT PLOA 2026 (docs/dominio/evidencias/2026-11-08)",
                   "auditoria": "docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md (PR #1)"},
        "anos": ANOS, "ifes": ifes, "campi": campi, "trajetorias": traj, "evasao_grupo": evasao_grupo,
        "contexto_campi": contexto, "matriz_2026": {"rede": rede, "submontantes": sub},
    }
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, separators=(",", ":")))
    print(SAIDA.name, f"{SAIDA.stat().st_size / 1024:.0f} KB")
    for c, v in campi.items():
        print(" ", c, len(v["ofertas"]), "ofertas")
    t = traj["IFES"]["concsub"]
    print("  Ifes concomitante+subsequente, médias A×B [vagas, ingr, mat, conc]:",
          [round(media(t, A3, i)) for i in range(4)], [round(media(t, B3, i)) for i in range(4)])


if __name__ == "__main__":
    main()
