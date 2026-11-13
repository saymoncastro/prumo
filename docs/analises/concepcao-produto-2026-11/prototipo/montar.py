"""Monta o protótipo conceitual (2ª rodada, 12/11/2026; 3ª rodada, 13/11/2026).

  prumo-conceito.html ← prumo-conceito.template.html
                        + recorte de poc/dados-poc002.json (só dados públicos da PNP e do demonstrativo da matriz 2026)
                        + poc/coortes002.js (motor de coortes da POC 0.0.2, sem alteração)
                        + simulacao.js (alavancas, operações, capacidade e matriz do protótipo)
                        + pauta.js (desafio da Reitoria, pauta de decisões, composição e participação na matriz)

Uso, a partir da raiz do repositório:  python3 docs/analises/concepcao-produto-2026-11/prototipo/montar.py
Não altera nada em poc/.
"""
import json
from pathlib import Path

aqui = Path(__file__).parent
raiz = aqui.parents[3]
dados = json.loads((raiz / "poc" / "dados-poc002.json").read_text())

CAMPOS = ("id", "curso", "tipo", "oferta", "presencial", "classe", "turno", "evasao", "serie")


def recorte_campus(c):
    ofertas = [
        {k: o[k] for k in CAMPOS}
        for o in c["ofertas"]
        if o["presencial"] and o["tipo"] == "Técnico" and o["serie"].get("2025")
    ]
    return {"unidade": c["unidade"], "pl": c["pl"], "professores_equivalentes": c["professores_equivalentes"], "ofertas": ofertas}


recorte = {
    "fontes": dados["fontes"],
    "anos": dados["anos"],
    "ifes": dados["ifes"],
    "campi": {nome: recorte_campus(c) for nome, c in dados["campi"].items()},
    "matriz_2026": dados["matriz_2026"],
}

seguro = lambda s: s.replace("</", "<\\/")
html = (aqui / "prumo-conceito.template.html").read_text()
html = html.replace("/*DADOS*/", seguro(json.dumps(recorte, ensure_ascii=False)), 1)
html = html.replace("/*COORTES*/", seguro((raiz / "poc" / "coortes002.js").read_text()), 1)
html = html.replace("/*SIMULACAO*/", seguro((aqui / "simulacao.js").read_text()), 1)
html = html.replace("/*PAUTA*/", seguro((aqui / "pauta.js").read_text()), 1)
(aqui / "prumo-conceito.html").write_text(html)
print(f"prumo-conceito.html: {len(html) / 1024:.0f} KB")
