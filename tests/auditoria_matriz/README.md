# Referências de auditoria da Matriz Orçamentária

Suíte de auditoria, sem código de produto e sem alteração de planilhas. A fonte canônica é [matriz-orcamentaria.md](../../docs/dominio/matriz-orcamentaria.md), **versão 1.2.0**. Os resultados e limites estão no [relatório complementar](../../docs/dominio/auditoria-complementar-matriz-orcamentaria.md) (v1.1.0) e na [revisão crítica](../../docs/dominio/revisao-critica-regras-prumo.md) (v1.2.0).

Execute a partir da raiz:

```sh
python3 -m unittest discover -s tests/auditoria_matriz -v
python3 tests/auditoria_matriz/verificar_fontes.py
python3 tests/auditoria_matriz/extrair_ro_mt.py
```

O primeiro comando usa somente a biblioteca padrão e não precisa de rede nem de Excel. O segundo e o terceiro requerem `openpyxl` e os arquivos originais ou preservados; fazem apenas leitura e confirmam o SHA-256 antes e depois. Não recalculam nem salvam planilhas. O terceiro regenera `ro_mt_casos.json`.

**Dados não publicados:** `referencias.json` e `ro_mt_casos.json` reproduzem dados da planilha do Ifes e estão no `.gitignore`, assim como a própria planilha e o livro. Em um clone do repositório, os testes só rodam depois de obter esses arquivos com o responsável pelo projeto; `ro_mt_casos.json` pode ser regenerado com `extrair_ro_mt.py` a partir da planilha original.

São **32 testes** em dois arquivos.

`test_referencia.py` (v1.1.0, 19 testes):

- **O01–O08:** reprodução operacional de preços, classificação, monetização de 23 amostras, somas de 22 campi, denominador Ifes, fronteiras ICQA, ano bissexto e diagnóstico. Não certificam legalidade.
- **M01–M06:** texto e metodologia identificados de N2/C5. Inclui 12 amostras de MT sem AC como entrada, cinco divergências do **texto**, faixas contínuas, conflito IEA, duas metades de retenção e fórmula RIP. M01 compara a quatro casas com HALF_UP. **v1.2.0:** M02 continua válido como prova de que o texto N2/N3 diverge da prática; os mesmos cinco casos são positivos em R03.
- **H01–H05:** cenários declarados, não parâmetros oficiais.

`test_ro_mt.py` (v1.2.0, 13 testes), sobre `ro_mt_casos.json` (todos os ciclos de B e C5, indicadores de Qualidade C5 2026, parâmetros de B; SHA-256 das fontes registrados):

- **R01–R06:** a regra operacional RO-MT (RMO-066) reproduz 2.322/2.322 ciclos de B e 1.086/1.086 de C5. Os antigos contraexemplos são positivos. O bônus agro inferido coincide com 13 cursos agrários. FIC retido vale zero. Empates exatos na 5ª casa são indeterminados (L-17).
- **T01–T02:** o texto N2/N3 reproduz só 1.300 (B) e 993 (C5), divergência L-24. Valor de Funcionamento do Ifes com os fatores de N3 (EAD 25%, MOOC 8%).
- **C01–C02:** bolo F de B igual ao de C5; base nacional MOOC idêntica; fatores de 2026 em C5.
- **Q01–Q03:** C5 aplica 0,5×IEA no primeiro ramo (L-23); IEA = conclusão ÷ (conclusão + evasão); degraus do Ifes (CT, RAP).

A função `mt` de `test_ro_mt.py` foi escrita somente para auditoria. Aprovar R não torna RO-MT normativa: N2 e N3 escrevem outra regra. Não deve ser importada pelo produto como implementação oficial. Agro de B é identificado por inferência (lista explícita no teste), não por cadastro homologado.

Nenhum tratamento de denominador zero é atribuído à norma. `ValueError` é validação proposta, enquanto B usa `IFERROR` em expressões específicas. Nenhum teste transforma ausência de fonte em zero ou pressupõe conversão integral de vagas em matrículas.

Resultados: [v1.1.0](../../docs/dominio/evidencias/2026-11-08/resultado-validacao.json); [v1.2.0](../../docs/dominio/evidencias/2026-11-09/resultado-testes-1.2.0.txt). A conferência das 49.583 fórmulas permanece registro da v1.0.0.
