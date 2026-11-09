"""Monta as páginas da prova de conceito a partir dos templates e dos dados extraídos.

  prumo-poc.html            ← prumo-poc.template.html + dados-poc.json            (v2, meta de 50%)
  prumo-recomposicao.html   ← prumo-recomposicao.template.html + dados-recomposicao.json + coortes.js
"""
from pathlib import Path

aqui = Path(__file__).parent


def json_seguro(nome):
    return (aqui / nome).read_text().replace("</", "<\\/")


def montar(template, saida, dados, coortes=False):
    html = (aqui / template).read_text().replace("/*DADOS*/", json_seguro(dados), 1)
    if coortes:
        html = html.replace("/*COORTES*/", (aqui / "coortes.js").read_text().replace("</", "<\\/"), 1)
    (aqui / saida).write_text(html)
    print(f"{saida}: {len(html)/1024:.0f} KB")


montar("prumo-poc.template.html", "prumo-poc.html", "dados-poc.json")
montar("prumo-recomposicao.template.html", "prumo-recomposicao.html", "dados-recomposicao.json", coortes=True)
