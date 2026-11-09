"""Confronto somente de leitura com originais; requer openpyxl.

Executar a partir da raiz. Não baixa nem salva planilhas. Os testes de
referência usam apenas a biblioteca padrão e permanecem independentes.
"""
import collections
import hashlib
import json
from pathlib import Path
import sys

import openpyxl
from test_referencia import REF, D, precos_operacionais, mt_literal_n2, quatro_casas

raiz = Path(__file__).resolve().parents[2]
origem = raiz / REF['source']
antes = hashlib.sha256(origem.read_bytes()).hexdigest()
assert antes == REF['sha256'], 'Versão do arquivo diferente da referência'
b = openpyxl.load_workbook(origem, data_only=True)
f = openpyxl.load_workbook(origem, data_only=False)
s = b['CICLOS']
assert f['CLASSIFICAÇÕES'].auto_filter.ref == 'B6:J6'
assert f['CURSOS'].auto_filter.ref == 'A6:J6'
assert f['CICLOS'].auto_filter.ref == 'A6:AS2328'
assert f['CURSOS']['H4'].value is None
assert f['CURSOS']['E6'].value == 'Tipo de Oferta'
assert 'CICLOS!$I$7:$I$2328,E7' in f['CURSOS']['G7'].value
assert all(s[f'L{r}'].value == 'SIM' for r in range(7,2329))
for chave, esperado in REF['formulas'].items():
    aba, celula = chave.split('!')
    assert f[aba][celula].value == esperado, chave
for c in REF['cycles']:
    for coluna, esperado in c.items():
        if coluna == 'row': continue
        atual = s[f"{coluna}{c['row']}"].value
        if hasattr(atual,'date'): atual = atual.date().isoformat()
        assert atual == esperado, (coluna,c['row'])
precos = precos_operacionais()
campi = collections.defaultdict(lambda:dict(Y=D(0),AA=D(0),AC=D(0),AE=D(0)))
max_erro = D(0)
for r in range(7,2329):
    categoria=s[f'AG{r}'].value
    esperado=precos[categoria]*D(s[f'AC{r}'].value)
    max_erro=max(max_erro,abs(esperado-D(s[f'AE{r}'].value)))
    for col in ['Y','AA','AC','AE']:
        campi[s[f'E{r}'].value][col]+=D(s[f'{col}{r}'].value)
assert max_erro < D('.00000001'), max_erro
for campus, valores in campi.items():
    for col, valor in valores.items():
        assert abs(valor-D(REF['campus'][campus][col])) < D('.000001')
apos = hashlib.sha256(origem.read_bytes()).hexdigest()
assert antes == apos
evidencias=raiz/'docs/dominio/evidencias/2026-11-08'
manifesto=json.loads((evidencias/'manifesto.json').read_text())
for fonte in manifesto['arquivos']:
    if 'arquivo' in fonte:
        assert hashlib.sha256((evidencias/fonte['arquivo']).read_bytes()).hexdigest()==fonte['sha256']
c5=openpyxl.load_workbook(evidencias/'ifmt-matriz-2026.xlsx',data_only=True)
assert c5['Cálculo AE RIP']['K4'].value == 713072.9061
assert c5['Cálculo AE PRESENCIAL']['O4'].value == 3408275.869
# Cadastro C6: não usar AC para selecionar bônus. Ausência/ambiguidade
# permanece sem previsão. O rótulo PLOA2025 limita a comparabilidade.
import unicodedata
def chave(x):
    return ''.join(a for a in unicodedata.normalize('NFD',str(x).strip().upper()) if unicodedata.category(a)!='Mn')
cadastro=openpyxl.load_workbook(evidencias/'cadastro-publico.xlsx',data_only=True)['PLOA 2025']
agro=collections.defaultdict(set)
for linha in list(cadastro.values)[1:]:
    agro[tuple(chave(linha[i]) for i in [1,3,2])].add(chave(linha[7]))
mt=collections.Counter()
for r in range(7,2329):
    if s[f'I{r}'].value=='QUALIFICACAO PROFISSIONAL (FIC)': continue
    flags=agro[tuple(chave(s[f'{col}{r}'].value) for col in ['J','I','K'])]
    if len(flags)!=1:
        mt['cadastro_ambiguo_ou_ausente']+=1
        continue
    c={k:s[f'{k}{r}'].value for k in ['P','Q','S','U','W','Y']}
    c.update({k:c[k].date().isoformat() for k in ['P','Q']})
    calculado=quatro_casas(mt_literal_n2(c,flags=={'SIM'}))
    mt['coincide' if calculado==D(s[f'AC{r}'].value) else 'diverge']+=1
resultado={'original_sha256_preservado':apos,'ciclos_monetizados':2322,
           'max_erro_reais':str(max_erro),'campi_conferidos':len(campi),
           'amostras_conferidas':len(REF['cycles']), 'mt_nao_fic_literal_N2_C5_cadastro_C6':dict(mt),
           'limite':'Contagens exploratórias; cadastro PLOA2025; não certifica edição de B nem norma vigente.'}
print(json.dumps(resultado,ensure_ascii=False,indent=2))
