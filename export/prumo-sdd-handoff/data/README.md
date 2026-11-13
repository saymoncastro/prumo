# Dados

> **Nada desta pasta é versionado, exceto este arquivo e `samples/`** (quando existir). Os dados históricos ficam fora do Git por tamanho e para que cada edição seja conferida por checksum. Fontes, cobertura e limitações: [fontes, qualidade e proveniência](../docs/dados/fontes-qualidade-e-proveniencia.md).

## 1. Exportação dos Indicadores de Gestão da PNP

| | |
|---|---|
| **Fonte oficial** | Plataforma Nilo Peçanha (MEC/Setec), painel de Indicadores de Gestão, exportação de dados por indicador |
| **Local esperado** | `data/pnp/indicadores-gestao/` (ignorado pelo Git) |
| **Edição usada nos estudos** | Anos-base 2017–2025 (cobertura por arquivo em [fontes](../docs/dados/fontes-qualidade-e-proveniencia.md) § 3). Data exata da obtenção não registrada; anterior a 10/11/2026 |
| **Tamanho** | 18 CSV, 97.030.642 bytes |
| **Formato** | UTF-8 sem BOM, separador `;`, decimal com vírgula, cabeçalho na primeira linha |

**Como obter:** pedir a cópia ao responsável pelo projeto (é a mesma usada nos estudos e confere com os checksums abaixo) ou exportar novamente da PNP, arquivo por arquivo, mantendo os nomes e a estrutura de pastas. **Uma exportação nova é outra edição:** os checksums não vão bater, e os resultados de referência podem mudar. Registre-a como nova versão (§ 3).

### Manifesto da edição usada nos estudos

| Caminho relativo | Bytes | Linhas (sem cabeçalho) | sha256 |
|---|---:|---:|---|
| `CargosCarreira.csv` | 39.352 | 409 | `740b9a55040b955e28f38a0a4de827f92d830fc98705d5b14b7d0bbd589a0f78` |
| `DadosGerais.csv` | 20.354.885 | 86.330 | `c6dd576549193afd86aa68b171cf13a0a63d5c80444eda9a6528707b75ed35a7` |
| `dados-academicos/CassificacaoRacialRendaSexo.csv` | 33.207.850 | 244.006 | `98e31323a40354131d1026653d5d7063298b9c51b9330e0a01c55d9bdef1de94` |
| `dados-academicos/SituacaoMatricula.csv` | 5.556.966 | 40.404 | `4da7f60d55c814b975f84b8db7ce99d24b4457fd79cb612d78092a328c4d1e22` |
| `indicadores-academicos/EficienciaAcademica.csv` | 795.570 | 5.774 | `2bdc2f4a7c5cbf688dd4978bff8601b185bd69907c9107c1c5baca45eed0481b` |
| `indicadores-academicos/IndiceVerticalizacao.csv` | 748.657 | 5.883 | `74f43a3cb0f01f64481e864de1e04cbf93ed36d941a5fe0a99daa7d798c5ab1a` |
| `indicadores-academicos/RelacaoAlunoProfessorRAP.csv` | 708.619 | 5.966 | `7ce1a87e57fcec3f778fc6924adfafaeb39385eb6f98aa5d803889344afe58cb` |
| `indicadores-academicos/TaxaEvasao.csv` | 30.581.288 | 109.396 | `e30f714b5ad4e275e7093b3f4779d1ffb5e9b6c300d515fe1bd2bb5af04e8113` |
| `indicadores-academicos/TaxaOcupacao.csv` | 62.837 | 574 | `1005cb2d3d949460bbe83b0fc295ef791639a28aab248e150a119cea5d4cbb2e` |
| `indicadores-gastos/IndicadoresGastos.csv` | 73.169 | 369 | `3a4a1b4ea14af372c083e01750d56b78c4f938656484677c5193fb01c4ebee18` |
| `indicadores-gastos/PanoramaOrcamentario.csv` | 836.188 | 4.509 | `92e2d279c16c3d9d2f0d1d9b151845d0a9107ca1959e4d3e4b7c04a22f2edea0` |
| `indicadores-pessoal/ProfessoresPorInstituicao.csv` | 604.792 | 5.612 | `efb32acea3ff9d4303ec71c37d321161b315da2fcda28d00383cb5d5afc5625d` |
| `indicadores-pessoal/TecnicosAdmNivel.csv` | 328.761 | 3.048 | `90977c9678390016a28c9a00a6181e6e8588ce54fe98dbfc6ca56ab584009aac` |
| `indicadores-pessoal/TitulacaoDocente.csv` | 62.361 | 575 | `564e4112a07b4eb24f8c13ee810a2a858740fa1cbf689ea9eb14db048c49f756` |
| `percentuais-legais/OfertaVagasNoturnas.csv` | 501.820 | 4.337 | `5579e2022c75818027b99faa43b3e84b28d9cf0d93d005df62018515b06a9cb0` |
| `percentuais-legais/PercentuaisLegais.csv` | 758.151 | 5.877 | `a93c8921e8eeb19531ce12b66b43e5fddcccf8c327adbde48c599cd4075073af` |
| `percentuais-legais/RelacaoInscritosVagas.csv` | 695.079 | 5.847 | `5cfff9d37f9f15edfde473e075d3ca9cbd1b18dad8ee29fbfb2411f841b4ca36` |
| `percentuais-legais/ReservaVagas.csv` | 1.114.297 | 8.800 | `64bac999c1cae9cfbb4dce55cd25c96ed41bd2e65423f18edea68b639c135fa4` |

Conferir:

```bash
cd data/pnp/indicadores-gestao && find . -name '*.csv' -exec shasum -a 256 {} + | sort -k2
```

## 2. Amostras (`samples/`)

**Ainda não há amostra.** Quando uma especificação precisar de dados de teste, crie-a **filtrando linhas reais** de uma edição identificada (ex.: as unidades de uma instituição em dois anos-base), com o script de filtragem versionado e um README que diga edição, filtro e checksum de origem. **Nunca invente dados com aparência de dados oficiais.** Os dados derivados já versionados em `scripts/analises/motores-coortes-poc/*/dados-*.json` são exemplos reais de recorte por oferta.

## 3. Convenções de atualização

- Cada edição da PNP vai para uma pasta própria (ex.: `data/pnp/<data-de-obtenção>/`) com um manifesto de checksums como o do § 1.
- "Ano" nos arquivos é o **ano-base**. A matriz do exercício N usa a PNP do ano N−1, que retrata o ano-base N−2 (regra de 2026; ver [Matriz CONIF](../docs/dominio/matriz-conif-e-indicadores.md) § 6).
- Não editar arquivos da fonte. Correções e mapeamentos (ex.: nome de unidade → identidade estável) ficam em arquivos próprios, versionados.
- Dados não públicos (planilha da matriz de uma instituição, dados por turma) **nunca** vão para esta pasta versionados.
