"""Extrai, somente leitura, o fixture `ro_mt_casos.json` usado por `test_ro_mt.py`.

Requer openpyxl e os arquivos originais/preservados. Confirma SHA-256 antes e
depois da leitura. Não recalcula nem salva planilhas. Executar da raiz:

    python3 tests/auditoria_matriz/extrair_ro_mt.py
"""
import datetime as dt
import hashlib
import json
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[2]
B = RAIZ / "6ª Fase - Participação matrículas totais 2026 IFES - cópia.xlsx"
C5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
SAIDA = Path(__file__).with_name("ro_mt_casos.json")
HASH = {
    B: "7f62a6ebcf6fac12a7b63805e6f936a68469d2e13e3f71759c7d550cb5de5d33",
    C5: "b341f7a1e8a92bc510abd75058ec4396369d9725654c0d11e2e7e740bb66b9f3",
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def iso(x):
    return x.date().isoformat() if isinstance(x, dt.datetime) else None


def main():
    for p, h in HASH.items():
        assert sha(p) == h, f"SHA-256 divergente: {p}"

    wb = openpyxl.load_workbook(B, data_only=True, read_only=True)
    par = wb["Parâmetros"]
    ciclos_b = []
    for i, r in enumerate(wb["CICLOS"].iter_rows(min_row=7, max_row=2328, values_only=True), start=7):
        ciclos_b.append({
            "row": i, "I": r[8], "J": r[9], "AG": r[32],
            "P": iso(r[15]), "Q": iso(r[16]), "R": iso(r[17]),
            "S": r[18], "U": r[20], "W": r[22], "Y": r[24], "AC": r[28],
        })

    wc = openpyxl.load_workbook(C5, data_only=True)
    ws = wc["Ciclos"]
    ciclos_c5 = []
    for i in range(6, ws.max_row + 1):
        g = lambda c: ws[f"{c}{i}"].value
        if not isinstance(g("K"), dt.datetime) or g("AL") is None:
            continue
        ciclos_c5.append({
            "row": i, "D": g("D"), "G": g("G"),
            "P": iso(g("K")), "Q": iso(g("L")), "R": iso(g("M")),
            "S": g("N"), "U": g("P"), "W": g("Q"), "Y": g("AA"), "AL": g("AL"),
        })
    ind = wc["Indicadores"]
    indicadores = []
    for i in range(8, 49):
        g = lambda c: ind[f"{c}{i}"].value
        if g("C"):
            indicadores.append({k: g(k) for k in "CEFGHILMNRTV"})
    cc = wc["Cálculo Custeio"]

    fixture = {
        "fontes": {"B": HASH[B], "C5": HASH[C5]},
        "periodo": ["2024-01-01", "2024-12-31"],
        "parametros_B": {c: par[c].value for c in ("D7", "D9", "D10", "D11", "D12")},
        "submontantes_QE_C5": {"IEA": cc["E46"].value, "RAP": cc["E50"].value, "CT": cc["E54"].value,
                               "FP": cc["E56"].value, "EJA": cc["E58"].value},
        "valores_rede_C5": {"pres": cc["C39"].value, "ead": cc["D39"].value,
                            "mooc": cc["F39"].value, "fp": cc["H39"].value},
        "ciclos_B": ciclos_b,
        "ciclos_C5": ciclos_c5,
        "indicadores_C5": indicadores,
    }
    SAIDA.write_text(json.dumps(fixture, ensure_ascii=False, separators=(",", ":")))

    for p, h in HASH.items():
        assert sha(p) == h, f"Arquivo alterado durante a leitura: {p}"
    print(f"{SAIDA.name}: {len(ciclos_b)} ciclos B, {len(ciclos_c5)} ciclos C5, {len(indicadores)} instituições")


if __name__ == "__main__":
    main()
