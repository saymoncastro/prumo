# Scripts de análise e reprodução

> **Não é código de produção.** Estes scripts reproduzem resultados quantitativos citados em `docs/`. Ficam separados de `src/` e **não devem ser importados, adaptados ou promovidos a módulos do produto** sem nova especificação. Os motores de coortes são **referência de comportamento** para a especificação do motor do produto.

## Estudo da PNP (`estudo-pnp/`)

Reproduz as 14 tabelas (T1–T14) do [estudo da PNP](../../referencias/estudos/estudo-pnp-2026-11-10.md). Somente leitura; escreve só na saída padrão.

```bash
python3 scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py data/pnp/indicadores-gestao > /tmp/saida.txt
cmp /tmp/saida.txt scripts/analises/estudo-pnp/resultado-estudo-pnp.txt
```

| | |
|---|---|
| **Entrada** | Exportação da PNP (18 CSV) passada como argumento, pela variável `PNP_DIR` ou em `data/pnp/indicadores-gestao/` ([data/README.md](../../data/README.md)); `referencias/normas/ifmt-matriz-2026.xlsx` para T13 |
| **Dependências** | Python 3 (biblioteca padrão); `openpyxl` só para T13 (sem ele, T13 é pulada e a saída difere) |
| **Saída esperada** | `resultado-estudo-pnp.txt`, sha256 `3eab12c57fba14d69e40de220710d60b90eb8a8e5740109d3efabbe357c14281` |
| **Verificado** | 11/11/2026, Python 3.9.6, openpyxl 3.1.5: saída idêntica byte a byte, cerca de 5 s |
| **Adaptação** | Única mudança em relação ao original: caminhos (raiz do repositório, pasta padrão da PNP, local do demonstrativo C5 e duas linhas da documentação). Diff no [manifesto](../../migracao/manifesto-transferencia.md) |
| **Inconsistências conhecidas** | A documentação interna diz "19 CSV" (são 18) e "< 30 s"; a T6 rotula M/I como "anos de permanência" (termo abandonado). Não corrigidas, para preservar a saída de referência |

## Motores de coortes das POCs (`motores-coortes-poc/`)

Cópias **sem alteração** dos motores, dados derivados e testes de dois protótipos. Rodam sem dados externos (os dados derivados da PNP estão versionados ao lado).

```bash
node scripts/analises/motores-coortes-poc/recomposicao/testar_coortes.cjs
node scripts/analises/motores-coortes-poc/poc-002/testar_poc002.cjs
```

| Pasta | Motor | O que o teste verifica | Resultado em 11/11/2026 |
|---|---|---|---|
| `recomposicao/` | `coortes.js`: permanência única, duração fixa | Erro fora do ajuste (ajuste 2017–2021, teste 2022–2025) abaixo de 5% em três técnicos integrados; suspensão zera; ampliação dobra turmas; sem negativos. Imprime a tabela de erros de todas as ofertas | 6 de 6 passam |
| `poc-002/` | `coortes002.js`: evasão, conclusão e retenção separadas | Números conferem com o estudo da PNP; calibração 2023–2025; teste de um ano | 16 de 16 passam |

**Limites:** os erros de graduação de 8%, 15% e 19% citados nos documentos do laboratório não são reproduzidos por `coortes.js` (o teste retorna "sem série suficiente"). Ver [simulação](../../docs/simulacao/modelos-premissas-e-validacao.md) § 6.2. O comentário de `coortes.js` cita `testar_coortes.mjs`; o arquivo real é `.cjs`.

## O que não veio

Ficaram no repositório exploratório, por depender de fonte não pública ou por serem exploratórios:

| Script | Motivo |
|---|---|
| `tests/auditoria_matriz/` (32 testes) | Dependem da planilha não pública do Ifes e de arquivos derivados dela |
| `reproduzir_revisao_critica.py` | Depende da planilha não pública |
| `poc/extrair_*.py`, `poc/montar.py`, templates | Geram dados e páginas das POCs; código exploratório com o Ifes fixo |
