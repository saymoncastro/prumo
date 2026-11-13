# Fontes, qualidade e proveniência dos dados

> **Natureza:** patrimônio de dados e evidências que fundamenta o PRUMO, com cobertura **comprovada** (verificada em 11/11/2026), limitações e linhagem.
> **Relacionados:** [data/README.md](../../data/README.md) (obtenção e checksums da PNP) · [referencias/README.md](../../referencias/README.md) (arquivos preservados) · [PNP](../inteligencia/exploracao-estrategica-pnp.md) · [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) · [diretrizes SaaS](../arquitetura/diretrizes-saas.md)

## 1. Princípios

1. **Todo número carrega natureza e origem:** fonte, edição ou versão, ano-base, definição, fórmula e limitação.
2. **Só dados públicos entram no Git.** Dado privado de instituição e fontes não públicas ficam fora.
3. **Nenhuma fonte tem cobertura ou definição estável presumida.** Cobertura é verificada arquivo a arquivo, e quebras são metadado.
4. **O dado bruto não é reescrito.** Transformações são scripts reproduzíveis, e os resultados guardam a versão de entrada.

## 2. Inventário das fontes

Identificadores herdados da fonte canônica da matriz (§ 0.1) e dos manifestos de evidência.

| ID | Fonte | Versão / data | Finalidade | Formato | Pública? | No pacote? |
|---|---|---|---|---|---|---|
| PNP | Indicadores de Gestão da Plataforma Nilo Peçanha (MEC/Setec), exportação | Anos-base 2016–2025 conforme arquivo (§ 3); obtida antes de 10/11/2026 | Série longitudinal da Rede | 18 CSV, 97.030.642 bytes | Sim | **Não** (externa; manifesto em [data/README.md](../../data/README.md)) |
| C9 | Guia de Referência Metodológica da PNP (MEC/Setec), cópia no repositório do Cefet-MG | 2018, 98 p. | Definições de matrícula equivalente | PDF | Sim | Sim, [referencias/normas/](../../referencias/README.md) |
| — | Guia PNP atual | Consultado em espelho; endereço oficial retornou 403 | Definição vigente da ME | Web | Sim | **Não preservado**; pendência |
| N1 | Decreto 7.313/2010 (Planalto) | 22/09/2010 | Base legal da matriz | HTML | Sim | Não (URL) |
| N2 | Portaria MEC 646/2022, republicação no DOU de 21/09/2022, Seção 1, pp. 122–125, via espelho do Cefet-MG | Revogada por N3 | Regime anterior | PDF | Sim; assinatura não validada | Sim |
| N3 | Portaria MEC 243, de 10/03/2026, DOU de 12/03/2026, Seção 1, p. 63; impressão da página web | Vigente | Regime vigente | PDF | Sim; **não substitui a versão certificada** | Sim |
| — | Lei 11.892/2008, art. 8º | — | Metas legais de oferta | HTML | Sim | Não (URL) |
| — | Portaria Setec/MEC 146/2021 | — | Matrícula equivalente | — | Sim | Não; não lida diretamente |
| — | Portaria MEC 357/2026 | — | Citada no documento fundador como metas de oferta técnica por campus | — | Sim | **Não verificada** |
| A | Livro da Matriz Orçamentária, nova configuração (IFSertãoPE, ISBN 978-65-89380-47-4) | 2025, 65 p. | Método e história | PDF | Registro editorial público; cópia local não versionada | **Não**; obter pelo ISBN |
| B | Planilha da matriz do Ifes, 6ª fase (dados de 2024) | Metadado de 25/02/2026 | Caso do Ifes; reprodução da MT | XLSX | **Não pública** | **Não** |
| C5 | Demonstrativo da matriz 2026 do IFMT (PLOA 2026), exportação pública | Consulta de 08/11/2026 | Indicadores da Rede; reprodução da MT; RAP | XLSX | Sim (link institucional) | Sim |
| C6 | Cadastro público de cursos (IFMT) | Aba PLOA 2025 | Cotejo de peso e bônus | XLSX | Sim; não homologado | Não (URL) |
| C7 | Guia de orçamento da RFEPCT (EduCAPES) | 2025, 16 MB | Apoio metodológico | PDF | Sim | Não (URL) |
| C8 | Página "Orçamento 2026" da PROAD/Ifes | Publicada em 01/04/2026, atualizada em 05/08/2026; baixada em 09/11/2026 | Distribuição interna do Ifes | HTML + extrato JSON | Sim | Sim |
| C1–C4 | Páginas institucionais (IFMT, IFPB, Protocolo Integrado, Conif) | Consulta de 08/11/2026 | Pistas e tramitação | URL | Sim | Não (URL na fonte canônica) |

URLs e checksums de cada arquivo preservado: [referencias/README.md](../../referencias/README.md). URLs de fontes apenas citadas: fonte canônica § 0.1.

## 3. PNP: cobertura comprovada

Verificada em 11/11/2026 sobre a exportação usada nos estudos. Todos os 18 arquivos: UTF-8 sem BOM, separador `;`, decimal com vírgula, coluna de ano `Ano` (= ano-base).

| Arquivo | Anos | Granularidade | Instituições por ano |
|---|---|---|---|
| DadosGerais | 2017–2025 | Curso × tipo × oferta × modalidade × unidade | 64; 63 em 2025 |
| dados-academicos/CassificacaoRacialRendaSexo | 2017–2025 | Instituição × cor × renda × idade × sexo | 64; 63 |
| dados-academicos/SituacaoMatricula | 2017–2025 | Unidade × situação | 64; 63 |
| indicadores-academicos/EficienciaAcademica | 2017–2025 | Unidade (**inclui FIC**) | 62–64 |
| indicadores-academicos/IndiceVerticalizacao | 2017–2025 | Unidade | 64 (inclui em 2025 uma instituição ausente dos demais) |
| indicadores-academicos/RelacaoAlunoProfessorRAP | 2017–2025 | Unidade | 64; 63 |
| indicadores-academicos/TaxaEvasao | 2017–2025 | Curso × eixo × oferta × turno × modalidade × programa × unidade | 64; 63 |
| indicadores-academicos/TaxaOcupacao | 2017–2025 | Instituição (**retirado da PNP**) | 63–64 |
| indicadores-gastos/IndicadoresGastos | 2017–2025 | Instituição (valores nominais) | 41 |
| indicadores-gastos/PanoramaOrcamentario | **2013–2025** | Instituição × órgão | **40** (sem IFAC) |
| CargosCarreira | **2016–2023** | Instituição × carreira | **40** (sem IFAC) + linhas sem instituição |
| indicadores-pessoal/ProfessoresPorInstituicao | 2017–2025 | Instituição × titulação × jornada | 62–64 |
| indicadores-pessoal/TecnicosAdmNivel | 2017–2025 | Instituição × titulação | 62–64 |
| indicadores-pessoal/TitulacaoDocente | 2017–2025 | Instituição | 64; 63 |
| percentuais-legais/OfertaVagasNoturnas | 2017–2025 | Unidade | **43 (2017–2019), 44 (2020–2025)** |
| percentuais-legais/PercentuaisLegais | 2017–2025 | Unidade (ME × 100) | 64; 63 |
| percentuais-legais/RelacaoInscritosVagas | 2017–2025 | Unidade | 62–64 |
| percentuais-legais/ReservaVagas | **2019–2025** | Unidade × cota | 61–64 |

**Portanto, "PNP 2017–2025" vale para 14 dos 18 arquivos**, e nem todos cobrem todas as instituições em todos os anos.

**Coerência interna verificada** (estudo, T2): matrículas fecham exatamente entre DadosGerais, TaxaEvasao, SituacaoMatricula e CassificacaoRacialRendaSexo em todos os anos; a ME de DadosGerais é igual à de PercentuaisLegais ÷ 100. **Lacunas:** em DadosGerais há células vazias em vagas (24%), inscritos (24%), ingressantes (21%) e concluintes (25%).

## 4. Definições das variáveis-chave

| Variável | Definição operacional | Fonte da definição | Limitação |
|---|---|---|---|
| Matrícula | Ciclos de matrícula ativos no ano-base | PNP | Soma ciclos, não pessoas |
| Matrícula equivalente (ME) | Matrícula × fatores de carga horária e esforço (guia atual: M × FECH × FEC) | Guia PNP; Portaria Setec/MEC 146/2021 | Fórmula mudou 2020/2021 |
| Ingressantes, vagas, concluintes | Contagens do ano-base | PNP | Células vazias (§ 3) |
| Evasão (no simulador) | Evadidos ÷ matrículas da oferta | TaxaEvasao | Agregado anual, não coorte |
| Ocupação (no simulador) | Ingressantes ÷ vagas | DadosGerais | O indicador oficial foi retirado |
| M/I | Matrículas ÷ ingressantes do mesmo ano | Construção do estudo | **Não mede permanência** |
| Percentuais legais | ME da classe ÷ ME total, por soma dos campi | PercentuaisLegais | Classificação de formação de professores não é por curso |
| Professor-equivalente | Conforme PNP | RelacaoAlunoProfessorRAP | Sem área de formação |
| RAP | Matrículas ÷ professor-equivalente, conforme a fonte | PNP / matriz | Numerador não reconcilia com a matriz |

## 5. Qualidade, comparabilidade e divergências

Quebras metodológicas da PNP: [PNP](../inteligencia/exploracao-estrategica-pnp.md) § 3. Divergências PNP × matriz: [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) § 8. Em resumo:

| Tema | Situação |
|---|---|
| Matrícula equivalente 2017–2020 × 2021–2025 | Não comparável |
| Pandemia 2020–2022 | Evasão subnotificada, retenção inflada |
| Rótulos de programa e forma | Instáveis |
| Identidade de unidade | Inexistente na fonte |
| Taxa de ocupação, inscritos por vaga, gastos | Não utilizáveis para conclusões |
| Numerador da RAP | Irreconciliável (20,11 / 17,56 / 18,148 no Ifes) |
| Eficiência acadêmica | Não reproduz a da matriz (FIC) |
| Formação de professores | Provável reclassificação 2024–2025 |

## 6. Linhagem

```text
PNP (18 CSV, externos) ─┬─> scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py ─> resultado-estudo-pnp.txt (T1–T14)
C5 (referencias/normas) ┘                                     (verificado byte a byte em 11/11/2026)

PNP + C5 ─> extratores das POCs (não transportados) ─> dados-recomposicao.json, dados-poc002.json
           ─> scripts/analises/motores-coortes-poc/*/testar_*.cjs (6 e 16 verificações passam)

B (não pública) + C5 + C8 ─> testes de auditoria da matriz e reproduzir_revisao_critica.py
           (permanecem no laboratório; não rodam sem B)
```

| Valor de referência | Fonte | Produzido por | Reproduzível no repositório novo? |
|---|---|---|---|
| Percentuais legais do Ifes 2024 (0,4403 / 0,1206 / 0,0186) | PNP PercentuaisLegais | Portão de dados; estudo T7/T13 | Sim, com a PNP externa |
| Valores da matriz 2026 (0,44 / 0,1206 / 0,0186; RAP 18,148) | C5 | Leitura direta | Sim |
| Tabelas T1–T14 | PNP + C5 | `reproduzir_estudo_pnp.py` | Sim, com a PNP externa |
| Erros dos motores de coortes | dados derivados versionados | `testar_coortes.cjs`, `testar_poc002.cjs` | Sim, sem dados externos |
| RO-MT 2.322/2.322 e 1.086/1.086; 32 testes da matriz | B + C5 | `tests/auditoria_matriz/` (laboratório) | **Não** (B não é pública) |
| Distribuição interna PROAD × planilha | C8 + B | `reproduzir_revisao_critica.py` (laboratório) | **Não** |

## 7. Dados públicos, privados e sensíveis

| Categoria | Exemplos | Tratamento |
|---|---|---|
| **Público compartilhado** | PNP, normas, demonstrativos públicos | Pode ser versionado se pequeno; a PNP fica externa por tamanho |
| **Não público institucional** | Planilha da matriz do Ifes, fixtures de teste derivados dela | Fora do Git |
| **Privado da instituição cliente** | Objetivos pactuados, premissas, propostas, compromissos, dados por turma | Separado por construção; nunca visível a outra instituição |
| **Pessoal** | Dados por estudante ou servidor | **Fora do núcleo.** Agregados bastam |

**Atenção:**

- `CassificacaoRacialRendaSexo.csv` traz cor/raça, renda, idade e sexo como contagens por instituição; 29,7% das linhas têm 1 ou 2 matrículas (células pequenas). É publicado pelo MEC e o risco de reidentificação é baixo nesse nível, mas **não cruzar com campus ou curso nem publicar recortes finos**.
- A fonte canônica da matriz e as regras de produto contêm **agregados derivados da planilha não pública do Ifes** (inventário de B, § 9, verificações V-01 a V-12, RMO-075). Já estavam publicados no repositório exploratório, que é público. Antes de mudar a visibilidade do repositório novo, confirmar com o responsável que esses agregados podem ser divulgados.
- A Lei Geral de Proteção de Dados (LGPD) não é citada pelos documentos do laboratório; eles falam em minimização, agregação e acesso por finalidade. Qualquer especificação que traga dado pessoal precisa de base legal explícita.

## 8. Atualização e versionamento

- **Edição como versão.** Cada exportação da PNP é uma versão identificada por data de obtenção e checksums ([data/README.md](../../data/README.md)). Uma série observada no produto sabe de qual edição veio.
- **Atualização manual, uma vez por edição** da PNP, até haver demanda para automatizar.
- **Mapeamento de unidades** nome-na-fonte → identidade estável, versionado a cada edição.
- **Normas:** cada nova portaria entra como fonte com ID, data, URL, checksum e condição (certificada ou não).
- **Responsável:** não há. É a hipótese H10 da [visão](../produto/visao.md) e um risco: sem dono, o produto envelhece em um ciclo.
