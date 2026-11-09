"""Referências da versão 1.2.0: regra operacional de MT (RO-MT), N3 e degraus.

Somente biblioteca padrão; lê `ro_mt_casos.json` (gerado por `extrair_ro_mt.py`).
R = reprodução operacional de 2026 (B e C5); T = texto normativo N2/N3;
Q = Qualidade e Eficiência com dados C5 2026. Aprovar R não torna RO-MT
normativa: N2 e N3 têm outro texto (L-24). Não importar como código de produto.
"""
import json
import unittest
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

FIX = json.loads(Path(__file__).with_name("ro_mt_casos.json").read_text())
D = lambda x: Decimal(str(x))
T0, T1 = (date.fromisoformat(x) for x in FIX["periodo"])
NP = (T1 - T0).days + 1
# Identificados por inferência do fator 1,5 em B (RMO-066/011); cadastro a homologar.
AGRO_B = {"AGRONOMIA", "TECNICO EM AGROPECUARIA", "TECNICO EM AGRICULTURA", "TECNICO EM AGROINDUSTRIA",
          "ENGENHARIA DE PESCA", "CAFEICULTURA", "TECNICO EM FLORESTAS", "TECNICO EM ZOOTECNIA",
          "TECNICO EM PESCA", "ENGENHARIA DE AQUICULTURA", "ZOOTECNIA", "TECNICO EM AQUICULTURA",
          "CIENCIAS AGRARIAS"}


def quatro_casas(x):
    """Convenção de comparação, NÃO regra oficial de precisão (L-17)."""
    return x.quantize(D(".0001"), rounding=ROUND_HALF_UP)


def mt(c, agro, variante):
    """MT de um ciclo. variante='RO' (prática 2026) ou 'TEXTO' (N2 = N3 literal).

    Retidos: elegibilidade pela data de jubilamento R (RMO-073), sem recalcular
    1.095 dias. Não usa AC/AL como entrada.
    """
    P, Q, R = (date.fromisoformat(c[k]) for k in "PQR")
    qtdc = (Q - P).days + 1
    if qtdc <= 0:
        raise ValueError("Ciclo inválido")
    if variante == "RO":
        longo = qtdc >= 365
        ch = min(D(c["S"]), D(c["U"])) if longo else D(c["U"])
    else:
        longo = qtdc > 365
        ch = D(c["U"]) if longo else D(c["S"])
    fator_ret = D(1)
    if Q < T0:
        if R < T0:
            return D(0)
        dacp, fator_ret = D(NP) / 2, D(".5")
    else:
        dacp = D(max(0, (min(Q, T1) - max(P, T0)).days + 1))
    if longo:
        fechda = ch / qtdc * 365 / 800 * dacp / NP
    elif variante == "RO":
        fechda = ch / 800 * dacp / qtdc
    else:
        fechda = ch / 800 * dacp / NP
    return fechda * D(c["Y"]) * D(c["W"]) * fator_ret * (D("1.5") if agro else 1)


def coincide(valor, esperado):
    """Igualdade a quatro casas; empate exato na 5ª casa aceita os dois lados.

    B e C5 arredondam em ponto flutuante binário: o empate da linha 173 sobe e o
    da linha 1080 desce (L-17). Não é política oficial de precisão.
    """
    esperado = D(esperado)
    if quatro_casas(valor) == esperado:
        return True
    return (valor * 10000) % 1 == D(".5") and abs(valor - esperado) == D(".00005")


def cobertura(ciclos, chave, agro_de, variante):
    return sum(coincide(mt(c, agro_de(c), variante), c[chave]) for c in ciclos)


B, C5 = FIX["ciclos_B"], FIX["ciclos_C5"]
agro_b = lambda c: c["J"] in AGRO_B
agro_c5 = lambda c: c["G"] == "SIM"


class ReproducaoOperacional(unittest.TestCase):
    def test_R01_ro_mt_reproduz_todos_os_ciclos_de_B(self):
        falhas = [c["row"] for c in B if not coincide(mt(c, agro_b(c), "RO"), c["AC"])]
        self.assertEqual(falhas, [])
        self.assertEqual(len(B), 2322)

    def test_R02_ro_mt_reproduz_todos_os_ciclos_de_C5_com_flags_proprias(self):
        falhas = [c["row"] for c in C5 if not coincide(mt(c, agro_c5(c), "RO"), c["AL"])]
        self.assertEqual(falhas, [])
        self.assertEqual(len(C5), 1086)

    def test_R03_antigos_contraexemplos_sao_casos_positivos(self):
        por_linha = {c["row"]: c for c in B}
        for r in (99, 284, 511, 585, 586):
            with self.subTest(row=r):
                c = por_linha[r]
                self.assertTrue(coincide(mt(c, agro_b(c), "RO"), c["AC"]))

    def test_R04_agro_inferido_coincide_com_cursos_agrarios(self):
        precisa_bonus = set()
        for c in B:
            if not coincide(mt(c, False, "RO"), c["AC"]) and coincide(mt(c, True, "RO"), c["AC"]):
                precisa_bonus.add(c["J"])
        self.assertEqual(precisa_bonus, AGRO_B)

    def test_R06_empates_de_quinta_casa_sao_indeterminados(self):
        por_linha = {c["row"]: c for c in B}
        subiu, desceu = por_linha[173], por_linha[1080]
        for c in (subiu, desceu):
            self.assertEqual((mt(c, agro_b(c), "RO") * 10000) % 1, D(".5"))
        self.assertEqual(quatro_casas(mt(subiu, agro_b(subiu), "RO")), D(subiu["AC"]))
        self.assertNotEqual(quatro_casas(mt(desceu, agro_b(desceu), "RO")), D(desceu["AC"]))

    def test_R05_fic_retido_sem_tolerancia(self):
        fic_retidos = [c for c in B if "FIC" in c["I"] and date.fromisoformat(c["Q"]) < T0]
        self.assertTrue(fic_retidos)
        self.assertTrue(all(c["R"] == c["Q"] and D(c["AC"]) == 0 for c in fic_retidos))


class TextoNormativo(unittest.TestCase):
    def test_T01_texto_n2_n3_diverge_da_pratica_L24(self):
        # Texto de N3 é idêntico ao de N2 para a cadeia de MT.
        self.assertEqual(cobertura(C5, "AL", agro_c5, "TEXTO"), 993)
        self.assertEqual(cobertura(B, "AC", agro_b, "TEXTO"), 1300)
        por_linha = {c["row"]: c for c in B}
        for r in (99, 284, 511, 585, 586):
            self.assertNotEqual(quatro_casas(mt(por_linha[r], agro_b(por_linha[r]), "TEXTO")),
                                D(por_linha[r]["AC"]))

    def test_T02_fatores_funcionamento_n3_e_valor_ifes(self):
        p = FIX["parametros_B"]
        mt_sit = {}
        for c in B:
            mt_sit[c["AG"]] = mt_sit.get(c["AG"], D(0)) + D(c["AC"])
        N = {"PRESENCIAL": D(p["D9"]), "EAD": D(p["D10"]), "EAD MOOC": D(p["D11"]), "EAD FP": D(p["D12"])}
        fat_n3 = {"PRESENCIAL": D(1), "EAD": D(".25"), "EAD MOOC": D(".08"), "EAD FP": D(".8")}
        preco = D(p["D7"]) / sum(N[k] * fat_n3[k] for k in N)
        valor = sum(preco * fat_n3[k] * mt_sit[k] for k in mt_sit)
        self.assertEqual(valor.quantize(D(".01")), D("63873167.58"))
        mooc = preco * D(".08") * mt_sit["EAD MOOC"]
        self.assertLess(mooc, D(75000))  # MOOC deixa de ser alavanca relevante sob N3


class ConciliacaoC5(unittest.TestCase):
    def test_C01_bolo_F_de_B_igual_ao_de_C5(self):
        r = FIX["valores_rede_C5"]
        self.assertAlmostEqual(FIX["parametros_B"]["D7"], r["pres"] + r["ead"] + r["fp"], delta=0.02)

    def test_C02_base_mooc_identica_e_fatores_2026(self):
        r, p = FIX["valores_rede_C5"], FIX["parametros_B"]
        preco_c5 = r["pres"] / (r["pres"] / 1220.3527)  # preço presencial publicado em C5
        self.assertAlmostEqual(r["mooc"] / (0.8 * preco_c5), p["D11"], delta=0.01)
        self.assertAlmostEqual(r["ead"] / p["D10"] / preco_c5, 0.25, delta=0.001)


class QualidadeC5(unittest.TestCase):
    def setUp(self):
        self.inst = FIX["indicadores_C5"]
        self.ifes = next(x for x in self.inst if "ESPIRITO" in x["C"])
        self.sub = FIX["submontantes_QE_C5"]

    def test_Q01_primeiro_ramo_iea_aplicado_como_meio_iea(self):
        baixos = [x for x in self.inst if x["H"] and x["I"] and x["H"] < 0.4146]
        self.assertEqual(len(baixos), 13)
        for x in baixos:
            self.assertAlmostEqual(x["I"], 0.5 * x["H"], delta=0.0006)

    def test_Q02_iea_e_conclusao_sobre_conclusao_mais_evasao(self):
        for x in self.inst:
            if x["E"] is not None and x["F"]:
                self.assertAlmostEqual(x["H"], x["E"] / (x["E"] + x["F"]), delta=0.0006)

    def test_Q03_degraus_do_ifes(self):
        ct = lambda v: 0 if v < 0.5 else v if v < 0.6 else 2 * v
        rap = lambda v: 0 if v < 18 else v if v < 20 else 2 * v if v < 22 else 2.5 * v
        s_ct = sum(ct(x["R"]) for x in self.inst)
        s_rap = sum(rap(x["L"]) for x in self.inst)
        self.assertEqual(ct(self.ifes["R"]), 0)  # 44% < 50%: participação CT zero
        ganho_ct50 = 0.5 / (s_ct + 0.5) * self.sub["CT"]
        self.assertAlmostEqual(ganho_ct50, 2055405, delta=1)
        atual_rap = rap(self.ifes["L"]) / s_rap * self.sub["RAP"]
        self.assertAlmostEqual(atual_rap, 726914, delta=1)
        self.assertAlmostEqual(self.ifes["M"] - 18 * self.ifes["N"], 224.39, delta=0.01)


if __name__ == "__main__":
    unittest.main()
