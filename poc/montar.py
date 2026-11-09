"""Monta poc/prumo-poc.html a partir do template e de poc/dados-poc.json."""
from pathlib import Path
aqui = Path(__file__).parent
dados = (aqui / "dados-poc.json").read_text().replace("</", "<\\/")
html = (aqui / "prumo-poc.template.html").read_text().replace("/*DADOS*/", dados, 1)
(aqui / "prumo-poc.html").write_text(html)
print(f"prumo-poc.html: {len(html)/1024:.0f} KB")
