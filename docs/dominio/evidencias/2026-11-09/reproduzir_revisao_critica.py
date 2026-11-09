"""Reprodução das evidências quantitativas da revisão crítica de 09/11/2026.

Script de auditoria, somente leitura. NÃO é código de produto.
Executar a partir da raiz do projeto:

    python3 docs/dominio/evidencias/2026-11-09/reproduzir_revisao_critica.py

Requer openpyxl. Lê B (planilha Ifes, 6ª fase) e C5 (demonstrativo IFMT 2026)
e imprime um JSON com:
  1. cobertura da regra operacional de MT (RO-MT) versus a leitura literal de N2,
     em B (2.322 ciclos) e em C5 (ciclos IFMT, com flags agro do próprio IFMT);
  2. conciliação do bolo de Funcionamento e da base MOOC entre B e C5;
  3. posição do Ifes nas faixas de Qualidade e Eficiência (C5, aba Indicadores)
     e valores condicionais de cenários de faixa, com os demais participantes constantes.
"""
import datetime as dt
import json
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[4]
B = RAIZ / "6ª Fase - Participação matrículas totais 2026 IFES - cópia.xlsx"
C5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
T0, T1 = dt.date(2024, 1, 1), dt.date(2024, 12, 31)
NP = (T1 - T0).days + 1  # 366 em 2024


def _d(x):
    return x.date() if isinstance(x, dt.datetime) else x


def mt_sem_agro(P, Q, R, CHC, CHM, PC, QTM, variante):
    """MT sem bônus agro. variante='RO' (regra operacional) ou 'N2' (literal)."""
    q = (Q - P).days + 1
    if variante == "RO":
        longo = q >= 365
        ch = min(CHC, CHM) if longo else CHM
    else:
        longo = q > 365
        ch = CHM if longo else CHC
    fator_ret = 1.0
    if Q < T0:  # ciclo encerrado antes do período: retido
        if R < T0:  # além da data de jubilamento (FIC: R = Q)
            return 0.0
        dacp, fator_ret = NP / 2, 0.5
    else:
        a, b = max(P, T0), min(Q, T1)
        dacp = max(0, (b - a).days + 1)
    if longo:
        fechda = (ch / q * 365 / 800) * (dacp / NP)
    elif variante == "RO":
        fechda = (ch / 800) * (dacp / q)  # fração do ciclo dentro do período
    else:
        fechda = (ch / 800) * (dacp / NP)
    return fechda * QTM * PC * fator_ret


def coincide(prev, real, agro=None):
    fatores = (1.5 if agro == "SIM" else 1.0,) if agro in ("SIM", "NÃO") else (1.0, 1.5)
    if prev == 0:
        return abs(real) < 6e-5
    return any(abs(round(prev * k, 4) - real) <= 0.00011 for k in fatores)


def cobertura_B():
    ws = openpyxl.load_workbook(B, data_only=True, read_only=True)["CICLOS"]
    res = {"RO": 0, "N2": 0, "total": 0, "agro_inferido_1_5": {}}
    for r in ws.iter_rows(min_row=7, max_row=2328, values_only=True):
        P, Q, R = _d(r[15]), _d(r[16]), _d(r[17])
        S, U, W, Y, AC = (float(r[i] or 0) for i in (18, 20, 22, 24, 28))
        res["total"] += 1
        for v in ("RO", "N2"):
            if coincide(mt_sem_agro(P, Q, R, S, U, W, Y, v), AC):
                res[v] += 1
        base = mt_sem_agro(P, Q, R, S, U, W, Y, "RO")
        if base and abs(round(base * 1.5, 4) - AC) <= 0.00011 and abs(round(base, 4) - AC) > 0.00011:
            res["agro_inferido_1_5"][r[9]] = res["agro_inferido_1_5"].get(r[9], 0) + 1
    return res


def cobertura_C5():
    ws = openpyxl.load_workbook(C5, data_only=True)["Ciclos"]
    res = {"RO": 0, "N2": 0, "total": 0}
    for i in range(6, ws.max_row + 1):
        g = lambda c: ws[f"{c}{i}"].value
        P, Q, R = _d(g("K")), _d(g("L")), _d(g("M"))
        if not isinstance(P, dt.date) or g("AL") is None:
            continue
        try:
            S, U, W, Y, AL = (float(g(c)) for c in ("N", "P", "Q", "AA", "AL"))
        except (TypeError, ValueError):
            continue
        res["total"] += 1
        for v in ("RO", "N2"):
            if coincide(mt_sem_agro(P, Q, R, S, U, W, Y, v), AL, agro=g("G")):
                res[v] += 1
    return res


def conciliacao_bolo():
    pb = openpyxl.load_workbook(B, data_only=True)["Parâmetros"]
    cc = openpyxl.load_workbook(C5, data_only=True)["Cálculo Custeio"]
    rede = {k: cc[c].value for k, c in (("pres", "C39"), ("ead", "D39"), ("mooc", "F39"), ("fp", "H39"))}
    return {
        "B_D7_funcionamento": pb["D7"].value,
        "C5_pres_mais_ead_mais_fp": rede["pres"] + rede["ead"] + rede["fp"],
        "C5_mooc_rede_fora_do_bolo": rede["mooc"],
        "B_D11_base_mooc_nacional": pb["D11"].value,
        "C5_base_mooc_implicita": rede["mooc"] / cc["E30"].value,
        "C5_preco_ead_sobre_presencial": cc["E28"].value / cc["E4"].value,
        "C5_preco_mooc_sobre_presencial": cc["E30"].value / cc["E4"].value,
    }


def funcionamento_ifes_por_regime():
    """Valor de Funcionamento do Ifes com as MT de B sob três regimes de fatores.

    B: fatores observados na planilha (EAD 0,0625; MOOC 0).
    N3_mooc_no_denominador: Portaria 243/2026 (EAD 0,25; FP 0,8; MOOC 0,08), MOOC dentro de F.
    N3_mooc_fora_de_F: mesmos fatores, MOOC pago à parte (prática observada em C5 para 2026).
    Bases nacionais e F de B mantidos; não é previsão de exercício futuro.
    """
    wb = openpyxl.load_workbook(B, data_only=True, read_only=True)
    par = wb["Parâmetros"]
    F = par["D7"].value
    N = {k: par[c].value for k, c in (("PRESENCIAL", "D9"), ("EAD", "D10"), ("EAD MOOC", "D11"), ("EAD FP", "D12"))}
    mt = {k: 0.0 for k in N}
    for r in wb["CICLOS"].iter_rows(min_row=7, max_row=2328, values_only=True):
        mt[r[32]] += float(r[28] or 0)
    regimes = {
        "B": ({"PRESENCIAL": 1, "EAD": 0.25, "EAD MOOC": 0, "EAD FP": 0.8},
              {"PRESENCIAL": 1, "EAD": 0.0625, "EAD MOOC": 0, "EAD FP": 0.8}, False),
        "N3_mooc_no_denominador": ({"PRESENCIAL": 1, "EAD": 0.25, "EAD MOOC": 0.08, "EAD FP": 0.8}, None, False),
        "N3_mooc_fora_de_F": ({"PRESENCIAL": 1, "EAD": 0.25, "EAD MOOC": 0, "EAD FP": 0.8}, None, True),
    }
    out = {"mt_ifes_por_situacao": {k: round(v, 4) for k, v in mt.items()}}
    for nome, (w_den, w_preco, mooc_fora) in regimes.items():
        p = F / sum(N[k] * w_den[k] for k in N)
        w_preco = w_preco or dict(w_den, **({"EAD MOOC": 0.08} if mooc_fora else {}))
        out[nome] = {"preco_base": p, "valor_ifes": round(sum(p * w_preco[k] * mt[k] for k in mt), 2)}
    return out


def distribuicao_interna_vs_matriz():
    """Custeio 2026 publicado pela PROAD × contribuição de Funcionamento por campus em B."""
    proad = json.loads((Path(__file__).with_name("distribuicao-interna-ifes-2026.json")).read_text())["unidades"]
    soma_b = {}
    for r in openpyxl.load_workbook(B, data_only=True, read_only=True)["CICLOS"].iter_rows(
            min_row=7, max_row=2328, values_only=True):
        nome = r[4].replace("CAMPUS ", "").title().replace(" De ", " de ").replace(" Do ", " do ")
        soma_b[nome] = soma_b.get(nome, 0) + float(r[30] or 0)
    norm = lambda x: x.lower().replace("ó", "o")
    proad_n = {norm(k): v["custeio"] for k, v in proad.items()}
    linhas = {k: {"matriz_B": round(v, 2), "proad": proad_n.get(norm(k)),
                  "razao": round(proad_n[norm(k)] / v, 3) if proad_n.get(norm(k)) and v else None}
              for k, v in sorted(soma_b.items())}
    comuns = [x for x in linhas.values() if x["proad"]]
    razoes = [x["razao"] for x in comuns if x["razao"]]
    # Tabela por campus não é exportada: valores derivados de B são resultado de auditoria local.
    return {
        "custeio_total_proad": round(sum(v["custeio"] for v in proad.values()), 2),
        "campi_pareados": len(comuns),
        "faixas_de_razao": {"<0,90": sum(r < 0.90 for r in razoes), "0,90–0,98": sum(0.90 <= r < 0.98 for r in razoes),
                            "0,98–1,02": sum(0.98 <= r <= 1.02 for r in razoes), "1,02–1,10": sum(1.02 < r <= 1.10 for r in razoes),
                            ">1,10": sum(r > 1.10 for r in razoes)},
        "dentro_2pct": sum(1 for x in comuns if x["razao"] and 0.98 <= x["razao"] <= 1.02),
        "soma_proad_campi_comuns": round(sum(x["proad"] for x in comuns), 2),
        "soma_matriz_campi_comuns": round(sum(x["matriz_B"] for x in comuns), 2),
    }


def qualidade_ifes():
    ws = openpyxl.load_workbook(C5, data_only=True)["Indicadores"]
    inst = []
    for i in range(8, 49):
        g = lambda c: ws[f"{c}{i}"].value
        if g("C"):
            inst.append({k: g(k) for k in "CHILMNRTV"})
    num = lambda x: x if isinstance(x, (int, float)) else 0
    w_rap = lambda x: 0 if x < 18 else x if x < 20 else 2 * x if x < 22 else 2.5 * x
    w_ct = lambda x: 0 if x < 0.5 else x if x < 0.6 else 2 * x
    w_fp = lambda x: 0 if x < 0.10 else x if x < 0.15 else 2 * x if x < 0.20 else 2.5 * x
    w_eja = lambda x: 0 if x < 0.025 else x if x < 0.05 else 2 * x if x < 0.10 else 2.5 * x
    sub = {"IEA": 55149450.54, "RAP": 55149450.54, "CT": 77209230.76, "FP": 22059780.22, "EJA": 11029890.11}
    soma = {
        "IEA": sum(num(x["I"]) for x in inst), "RAP": sum(w_rap(x["L"]) for x in inst),
        "CT": sum(w_ct(x["R"]) for x in inst), "FP": sum(w_fp(x["T"]) for x in inst),
        "EJA": sum(w_eja(x["V"]) for x in inst),
    }
    ifes = next(x for x in inst if "ESPIRITO" in x["C"])
    atual = {"IEA": ifes["I"], "RAP": w_rap(ifes["L"]), "CT": w_ct(ifes["R"]), "FP": w_fp(ifes["T"]), "EJA": w_eja(ifes["V"])}

    def valor(k, novo):
        return 0 if not novo else novo / (soma[k] - atual[k] + novo) * sub[k]

    base = {k: round(valor(k, atual[k])) for k in sub}
    cen = {
        "RAP_abaixo_18": ("RAP", 0), "RAP_20": ("RAP", w_rap(20)), "RAP_22": ("RAP", w_rap(22)),
        "CT_50": ("CT", w_ct(0.5)), "CT_60": ("CT", w_ct(0.6)), "FP_15": ("FP", w_fp(0.15)),
        "FP_20": ("FP", w_fp(0.20)), "EJA_2_5": ("EJA", w_eja(0.025)), "EJA_5": ("EJA", w_eja(0.05)),
        "IEA_peso_2": ("IEA", 2 * ifes["H"]),
    }
    delta = {n: round(valor(k, v)) - base[k] for n, (k, v) in cen.items()}
    pesos_iea = sorted((x["H"], round(x["I"] / x["H"], 2)) for x in inst if x["H"] and x["I"])
    return {
        "ifes_indicadores": {"IEA": ifes["H"], "RAP": ifes["L"], "MEq_RAP": ifes["M"], "prof_eq": ifes["N"],
                             "CT": ifes["R"], "FP": ifes["T"], "EJA": ifes["V"]},
        "valor_atual_por_subcomponente": base, "valor_atual_total": sum(base.values()),
        "delta_por_cenario_isolado": delta,
        "primeiro_ramo_iea_aplicado_C5": [p for p in pesos_iea if p[1] == 0.5][:3],
    }


if __name__ == "__main__":
    print(json.dumps({
        "cobertura_MT_B": cobertura_B(),
        "cobertura_MT_C5": cobertura_C5(),
        "conciliacao_bolo_e_mooc": conciliacao_bolo(),
        "funcionamento_ifes_por_regime": funcionamento_ifes_por_regime(),
        "distribuicao_interna_vs_matriz": distribuicao_interna_vs_matriz(),
        "qualidade_ifes_C5": qualidade_ifes(),
    }, ensure_ascii=False, indent=2, default=str))
