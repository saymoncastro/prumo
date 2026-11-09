"""Extrai os dados públicos usados pela prova de conceito do Prumo (somente leitura).

Fontes:
  - PNP, pasta `indicadores-gestao/` (exportação de Indicadores de Gestão, todas as
    instituições; não versionada no repositório por tamanho);
  - C5, demonstrativo IFMT da matriz 2026 (evidência pública preservada).

Saída: poc/dados-poc.json. Executar da raiz:  python3 poc/extrair_dados.py

Unidades: em PercentuaisLegais.csv as matrículas equivalentes estão multiplicadas
por 100 em relação a DadosGerais.csv (verificado campus a campus); aqui tudo é
convertido para a escala de DadosGerais.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
PNP = RAIZ / "indicadores-gestao"
C5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
SAIDA = Path(__file__).with_name("dados-poc.json")
ANOS = ("2024", "2025")


def num(x):
    x = (x or "").strip()
    return float(x.replace(".", "").replace(",", ".")) if x else 0.0


def ler(rel):
    with open(PNP / rel, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter=";") if r["Ano"] in ANOS]


def main():
    pl = ler("percentuais-legais/PercentuaisLegais.csv")
    rap = ler("indicadores-academicos/RelacaoAlunoProfessorRAP.csv")
    dg = ler("DadosGerais.csv")

    inst = defaultdict(lambda: defaultdict(float))
    meta_inst = {}
    for r in pl:
        k = (r["Ano"], r["Instituicao"])
        meta_inst[r["Instituicao"]] = {"nome": r["Instituição (Nome)"], "org": r["Organização Acadêmica PNP"],
                                      "uf": r["UF"], "regiao": r["Região"]}
        a = inst[k]
        a["ct"] += num(r["Matrícula Equivalente | Técnicos"]) / 100
        a["fp"] += num(r["Matrícula Equivalente | Formação de Professores"]) / 100
        a["eja"] += num(r["Matrícula Equivalente | Proeja"]) / 100
        a["meq"] += num(r["Matrícula Equivalente | Geral"]) / 100
        a["unidades"] += 1
    for r in rap:
        a = inst[(r["Ano"], r["Instituicao"])]
        a["rap_m"] += num(r["RAP | Matrículas RAP"])
        a["rap_p"] += num(r["RAP | Professor Equivalente"])

    instituicoes = {ano: [] for ano in ANOS}
    for (ano, sig), a in inst.items():
        if a["meq"] <= 0:
            continue
        instituicoes[ano].append({"sigla": sig, **meta_inst.get(sig, {}),
                                  **{k: round(v, 2) for k, v in a.items()}})

    campi = defaultdict(lambda: defaultdict(lambda: {"cursos": [], "meq": 0, "ct": 0, "fp": 0, "eja": 0,
                                                     "rap_m": 0, "rap_p": 0, "me_pres": 0, "mat_pres": 0}))
    for r in pl:
        if r["Instituicao"] != "IFES":
            continue
        c = campi[r["Ano"]][r["nomeUnidadeRecente"]]
        c["meq"] = num(r["Matrícula Equivalente | Geral"]) / 100
        c["ct"] = num(r["Matrícula Equivalente | Técnicos"]) / 100
        c["fp"] = num(r["Matrícula Equivalente | Formação de Professores"]) / 100
        c["eja"] = num(r["Matrícula Equivalente | Proeja"]) / 100
    for r in rap:
        if r["Instituicao"] != "IFES":
            continue
        c = campi[r["Ano"]][r["nomeUnidadeRecente"]]
        c["rap_m"], c["rap_p"] = num(r["RAP | Matrículas RAP"]), num(r["RAP | Professor Equivalente"])
    for r in dg:
        if r["Instituicao"] != "IFES":
            continue
        c = campi[r["Ano"]][r["nomeUnidadeRecente"]]
        mat, me = num(r["Número de Matrículas"]), num(r["Matrícula Equivalente | Geral"])
        pres = "Presencial" in r["ModalidadeEnsino"]
        if pres:
            c["me_pres"] += me
            c["mat_pres"] += mat
        c["cursos"].append({"curso": r["nomeIdCurso"], "tipo": r["tipoCurso"], "oferta": r["tipoOferta"],
                            "presencial": pres, "matriculas": mat, "me": round(me, 3),
                            "vagas": num(r["Número de vagas"]), "ingressantes": num(r["Número de ingressantes"]),
                            "concluintes": num(r["Número de concluintes"])})

    ws = openpyxl.load_workbook(C5, data_only=True)
    ind = ws["Indicadores"]
    matriz_2026 = []
    for i in range(8, 49):
        g = lambda col: ind[f"{col}{i}"].value
        if g("C"):
            matriz_2026.append({"nome": g("C"), "uf": g("B"), "iea": g("H"), "iea_pond": g("I"), "rap": g("L"),
                                "meq_rap": g("M"), "prof": g("N"), "ct": g("R"), "fp": g("T"), "eja": g("V")})
    cc = ws["Cálculo Custeio"]
    submontantes = {"IEA": cc["E46"].value, "RAP": cc["E50"].value, "CT": cc["E54"].value,
                    "FP": cc["E56"].value, "EJA": cc["E58"].value}

    dados = {
        "gerado_por": "poc/extrair_dados.py",
        "fontes": {
            "pnp": "Indicadores de Gestão PNP (exportação local indicadores-gestao/); Ano = ano-base",
            "matriz_2026": "C5 — demonstrativo IFMT PLOA 2026 (docs/dominio/evidencias/2026-11-08)",
        },
        "conciliacao": {
            "ifes_2024_ct": "0,4403 (PNP por campus) = 0,44 (matriz 2026)",
            "ifes_2024_fp": "0,1206 = 0,1206", "ifes_2024_eja": "0,0186 = 0,0186",
            "ifes_2024_prof_eq": "1.520 (PNP) × 1.517,5 (matriz)",
            "ifes_2024_rap": "20,11 (PNP) × 18,148 (matriz): numerador da matriz não reconciliado (L-25)",
        },
        "instituicoes": instituicoes,
        "ifes_campi": {ano: {k: dict(v) for k, v in campi[ano].items()} for ano in ANOS},
        "matriz_2026": {"instituicoes": matriz_2026, "submontantes": submontantes},
    }
    SAIDA.write_text(json.dumps(dados, ensure_ascii=False, separators=(",", ":")))
    print(SAIDA.name, {a: len(instituicoes[a]) for a in ANOS}, {a: len(campi[a]) for a in ANOS},
          f"{SAIDA.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
