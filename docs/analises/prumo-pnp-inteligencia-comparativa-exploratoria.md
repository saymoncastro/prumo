# PNP como inteligência comparativa longitudinal: auditoria e estudo exploratório

> **Data:** 10/11/2026 · **Natureza:** descoberta de produto e auditoria analítica. Nada foi implementado no simulador, nos protótipos ou nos dados de origem.
> **Fonte de dados:** exportação local dos Indicadores de Gestão da PNP (`indicadores-gestao/`, 93 MB, 19 CSV, não versionada), anos-base 2017–2025.
> **Reprodução:** [`reproduzir_estudo_pnp.py`](../dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py) (somente leitura, ~4 s; T1–T12 usam só a biblioteca padrão, T13 usa openpyxl) e [saída completa](../dominio/evidencias/2026-11-10/resultado-estudo-pnp.txt). As referências "T1"–"T14" apontam para as tabelas dessa saída. A T14 reúne as séries de apoio citadas nos casos e no § 2.4, para que cada número do texto tenha origem na saída.
> **Local:** o pedido sugeria `docs/estudos/`. Segui o padrão do repositório: análises em `docs/analises/` e scripts de evidência em `docs/dominio/evidencias/<data>/`.
> **Revisão (10/11/2026, após avaliação externa):**
> 1. M/I passou a se chamar "anos de vínculo por ingressante", porque mistura progressão regular, duração do curso e retenção. O texto deixou de tratá-lo como permanência.
> 2. Entrou a decomposição em quatro grupos mutuamente exclusivos, sem dupla contagem (§ 5.1).
> 3. Ficou explícito que, no técnico do Ifes, o gargalo está depois do ingresso, e que a queda de ocupação das vagas ocorre na graduação (§ 5.4).
> 4. Foi testado o numerador da RAP pela definição do guia, nas 41 instituições (§ 5.5, T13).

**Convenções usadas em todo o texto**

- **Ano** é o **ano-base**, não a edição da PNP. Pela N3, a matriz do exercício N usa a PNP N−1, que retrata o ano-base N−2 ([RMO-070](../dominio/matriz-orcamentaria.md#rmo-070)).
- **Rede41** reúne 38 IFs, 2 Cefets e o Colégio Pedro II, que formam o universo da Matriz CONIF. Exclui as 23 Escolas Técnicas Vinculadas, presentes na exportação.
- **Regular presencial** são os cursos presenciais, exceto FIC (qualificação profissional).
- **ME** é a matrícula equivalente da PNP. **MT** é a matrícula total da matriz. As duas não são a mesma medida (§ 4).
- Médias trienais: **A = 2017–2019** (antes da pandemia) e **B = 2023–2025** (depois da normalização).
- **M/I — anos de vínculo por ingressante** = matrículas ÷ ingressantes do mesmo ano (relação estoque/fluxo). Não é medida oficial da PNP. **Não é medida de permanência.** Um M/I maior pode vir de três causas, com sentidos educacionais opostos:
  - progressão regular em cursos mais longos;
  - menos evasão;
  - **retenção** (reprovação, atraso, vínculo além do prazo), que é resultado indesejável.

  Sem dados por turma de ingresso, essas causas não se separam.

---

## 1. Resumo executivo

**Oportunidade.** A exportação local cobre **64 instituições, cerca de 660 unidades e 9 anos-base (2017–2025)**, no nível de curso × campus × ano. Ela tem vagas, inscritos, ingressantes, matrículas, concluintes, evadidos e ME. Os quatro arquivos com matrículas fecham exatamente entre si em todos os anos (T2). A base sustenta comparações longitudinais **desde que se respeitem duas quebras**:

- a mudança da fórmula da ME entre os anos-base 2020 e 2021 (T3);
- a distorção da pandemia em 2020–2022 (T10).

**Achados com base suficiente (fatos observados):**

1. **O crescimento recente da Rede veio quase todo de FIC e EaD.** De 2021 a 2025, a ME da Rede41 cresceu 12,0% (+122 mil). Em quatro grupos mutuamente exclusivos, cuja soma fecha exatamente com o total:
   - regular a distância: 55,1%;
   - FIC presencial: 23,0%;
   - FIC a distância: 16,7%;
   - regular presencial: **5,3%**. Dentro dela, a ME de técnico presencial caiu 0,8% e a de graduação presencial subiu 1,8% (T4). Por isso, uma instituição de perfil presencial perde participação pelo denominador mesmo crescendo. O Ifes perdeu 0,15 p.p. na ME sem FIC. O próprio crescimento somou +0,12 p.p., e o crescimento da Rede tirou −0,26 p.p. (T5).
2. **Matrícula cresce por duas vias, e elas pesam igual.** Entre as médias A e B, as matrículas regulares presenciais da Rede cresceram 10,4%, **com 2,3% menos ingressantes**. O crescimento veio de mais anos de vínculo por ingressante (M/I de 3,17 para 3,59). Isso não é, por si, melhora: no mesmo período, a fatia de retidos entre os matriculados em curso subiu de 21–22% para 25–30%. Entre as 41 instituições, a variação das matrículas se divide em partes iguais entre ingresso e tempo de vínculo (T6).
3. **O Ifes inverte esse padrão, e o gargalo do técnico está depois do ingresso.** Vagas regulares presenciais +9,7%, ingressantes +4,6%, matrículas +0,7% e M/I de 3,30 para 3,18 (T6). No técnico concomitante/subsequente, as vagas continuam preenchidas (0,99 → 0,93 ingressante por vaga), mas as matrículas caem 25% com ingressantes −6%, e os concluintes caem à metade em alguns campi. A diferença entre vagas e ingressantes vem sobretudo da graduação, onde os ingressantes por vaga caem de 1,03 para 0,92 (§ 5.4).
4. **A Rede se afastou da meta de 50% técnico.** O %CT caiu de 61,5% (2017) para 47,8% (2025). As instituições com %CT ≥ 50% passaram de 35 para 24. Parte da queda é metodológica (2021). Parte vem de FIC e pós-graduação EaD no denominador. Parte é reconfiguração real de portfólio, de técnico para graduação, em IFPE, IFBA, IF Goiano, IFTO e Cefet-MG (T6, T7).
5. **Uma única oferta em pulso pode mover o indicador institucional.** Em 2023, as especializações EaD registradas em Colatina somaram 6.454 ME, quase todas de um único curso. Elas tiraram 6,3 p.p. do %CT do Ifes, que ficou em 36,8%. Com a especialização do Cefor, o efeito chega a ~10 p.p. Pelo calendário de RMO-070, o ano-base 2023 alimenta a matriz 2025 (T11).

**Limites.** Esta exportação não reproduz o IEA da matriz, porque o arquivo de eficiência inclui FIC. A RAP da PNP não reconcilia com a da matriz. A definição do guia aproxima, mas também não fecha: mediana −2,9% nas 41 instituições (T13). A Taxa de Ocupação foi retirada da PNP para revisão. Não há planilhas oficiais da matriz da Rede para exercícios anteriores a 2026. Por isso, **nenhum resultado aqui é estimativa orçamentária**: são proxies acadêmicas.

**Recomendação.** Vale incorporar a inteligência longitudinal ao PRUMO, mas como **fonte de premissas fundamentadas e de comparação contextual para o simulador e para o pacto de metas**. Não deve virar painel de desempenho nem ranking. A primeira pergunta de alto valor que já é possível responder bem está no § 10: **quanto cada vaga nova, por tipo de oferta e por campus, se converte em matrícula ativa ao longo do ciclo, e por que essa conversão está caindo no Ifes enquanto sobe na Rede?**

---

## 2. Inventário dos dados

### 2.1. Arquivos (T1)

| Arquivo | Linhas | Anos-base | Granularidade | Conteúdo útil |
|---|---:|---|---|---|
| `DadosGerais.csv` | 86.330 | 2017–2025 | curso × tipo × oferta × modalidade × **campus** | nº de cursos, vagas, inscritos, ingressantes, matrículas, concluintes, **ME** |
| `indicadores-academicos/TaxaEvasao.csv` | 109.396 | 2017–2025 | curso × turno × **programa** × campus | matrículas, evadidos, evasão anual; eixo/subeixo; programa (UAB, MOOC etc.) |
| `percentuais-legais/PercentuaisLegais.csv` | 5.877 | 2017–2025 | campus | ME técnicos, formação de professores, Proeja, geral (×100) |
| `percentuais-legais/RelacaoInscritosVagas.csv` | 5.847 | 2017–2025 | campus | inscritos, vagas |
| `percentuais-legais/ReservaVagas.csv` | 8.800 | **2019**–2025 | campus × cota/ampla | vagas |
| `percentuais-legais/OfertaVagasNoturnas.csv` | 4.337 | 2017–2025 | campus (44 instituições) | vagas noturnas e de graduação |
| `indicadores-academicos/EficienciaAcademica.csv` | 5.774 | 2017–2025 | campus | concluídos, evadidos e retidos por ciclo; **inclui FIC** |
| `indicadores-academicos/RelacaoAlunoProfessorRAP.csv` | 5.966 | 2017–2025 | campus | matrículas RAP, **professor-equivalente**, RAP |
| `indicadores-academicos/TaxaOcupacao.csv` | 574 | 2017–2025 | instituição | indicador **retirado da PNP** (ver 2.4) |
| `indicadores-academicos/IndiceVerticalizacao.csv` | 5.883 | 2017–2025 | campus | vagas por nível e eixo |
| `dados-academicos/SituacaoMatricula.csv` | 40.404 | 2017–2025 | campus × situação × fluxo/retido | em curso, concluintes, evadidos, retidos |
| `dados-academicos/CassificacaoRacialRendaSexo.csv` | 244.006 | 2017–2025 | instituição × cor × renda × idade × sexo | matrículas, ingressantes, concluintes, vagas |
| `indicadores-pessoal/*` (3) | 575–5.612 | 2017–2025 | instituição | docentes por titulação/jornada, TAE, ITCD |
| `indicadores-gastos/IndicadoresGastos.csv` | 369 | 2017–2025 | instituição (41) | gastos correntes, pessoal, custeio, gasto/ME (**nominais**) |
| `indicadores-gastos/PanoramaOrcamentario.csv` | 4.509 | **2013**–2025 | instituição (40) × resultado primário | dotação, empenhado, liquidado, pago |
| `CargosCarreira.csv` | 409 | **2016–2023** | instituição | servidores por carreira (Siafi) |

### 2.2. Cobertura e chaves

- **Instituições:** 64 por ano (38 IFs, 2 Cefets, CPII e 23 ETVs). Em 2025 são 63: a UFMG‑TU não aparece. Os arquivos de gastos cobrem só as 41 (ETVs não têm gasto segregável, segundo o guia).
- **Unidades:** de 642 (2017) a 661 (2025). A chave é `Instituicao` + `nomeUnidadeRecente`. O campo já traz o **nome mais recente** da unidade, então mudanças de nome não quebram a série. Por outro lado, não há código estável de unidade e o histórico de renomeações e incorporações fica invisível. No Ifes, Presidente Kennedy aparece a partir de 2022, sem matrícula regular presencial.
- **Ligação entre arquivos:** no nível campus × ano, a ligação é direta. No nível de curso, `DadosGerais` e `TaxaEvasao` só se ligam por nome, tipo, oferta e modalidade. `TaxaEvasao` ainda separa turno e programa. Não há chave de curso ou de ciclo.
- **Coerência interna:** as matrículas somam exatamente o mesmo total em `DadosGerais`, `TaxaEvasao`, `SituacaoMatricula` e `CassificacaoRacialRendaSexo`, em todos os anos. A ME de `DadosGerais` é igual à de `PercentuaisLegais` ÷ 100 (T2). Não há valores com separador de milhar ambíguo.
- **Lacunas:** vagas, inscritos e ingressantes ficam vazios em cerca de 20–25% das linhas de curso. Isso corresponde a cursos sem ciclo iniciado no ano, o que é esperado. Já a evasão fica vazia em 21% das linhas de `TaxaEvasao`.

### 2.3. Natureza dos dados

Todos os arquivos trazem **indicadores agregados já calculados**, como os do Extrator PNP. Não há microdados de matrícula ou de servidor, nem ciclo ou coorte individual. **A série histórica mostra cada ano com a metodologia da sua edição**: a mudança da fórmula da ME em 2021 aparece intacta (T3), em vez de recalculada para trás. O guia registra que, desde 2022, o modelo em Power BI "consolida dados de diferentes anos em um único modelo".

### 2.4. Mudanças metodológicas e anos atípicos (verificados)

| Efeito | Evidência | Consequência |
|---|---|---|
| **Fórmula da ME (anos-base 2020 → 2021)** | A razão ME/matrícula cai de 1,21 para 1,08 no técnico presencial, de 1,17 para 1,05 em tecnologia e de 1,13 para 1,09 em bacharelado. Na EaD, sobe de 0,15–0,65 para ~1,0 (T3). O guia PNP atual define ME = M × FECH × FEC, com FECH = carga mínima regulamentada ÷ 800 e FEC pelo Anexo II da Portaria Setec/MEC 146/2021. O guia de 2018 usava fator de nível de curso e contava só matrículas "sem programa associado". | **A ME não forma série contínua entre 2017–2020 e 2021–2025.** Para comparar a ME, usei apenas o bloco 2021–2025. Para séries longas, usei matrículas físicas da oferta regular presencial. A edição exata em que a mudança foi adotada não foi confirmada; o salto coincide com o ano-base 2021. |
| **MOOC e programas** | A FIC EaD salta de 91 mil para 642 mil matrículas em 2020, ainda como "Sem Programa Associado". Os rótulos MOOC só aparecem a partir de 2021. PROEJA, Bolsa Formação e PARTIUIF só aparecem como programa em 2025 (T14; 64 instituições). | Matrícula total e FIC não são comparáveis ao longo da série. **O rótulo de programa não serve para série histórica.** |
| **Pandemia (2020–2022)** | Na Rede41, a evasão anual da oferta regular presencial cai de 18,5% (2017) para 9,1% (2021) e volta a 16,0% em 2022. A fatia de retidos entre os matriculados "em curso" passa de 21% para 46,6% (2021) e volta a 24,9% (2025). As vagas regulares presenciais caem 20% em 2020 (T10, T14). | As matrículas de 2021–2022 estão infladas por vínculos prolongados e retenção, e 2023 mostra a "queda" de normalização. **Melhoras de evasão em 2020–2021 são artefato.** Por isso usei médias trienais antes e depois. |
| **Inscritos** | Inscritos por vaga (Rede41, regular presencial): 6,5 (2017), 4,2 (2022–2023), 6,1 (2025) (T10). Em 2025 há saltos atípicos; no IFPE, por exemplo, vai de 3,50 para 8,13 (T14). | Indicador de demanda de **baixa confiabilidade** para série. A contagem depende do processo seletivo, já que o mesmo candidato pode se inscrever em várias opções. |
| **Taxa de Ocupação** | O guia PNP atual informa: "Este indicador foi removido da PNP para reanálise de seu modelo matemático". A exportação mostra 144 linhas acima de 100% e um outlier (IFG 2020: 321,5%) (T14). | Não usar. |
| **Eficiência acadêmica** | O arquivo por campus inclui FIC, e com isso o IEA da Rede41 vai de 46,8% para 77,9% puxado por MOOCs (T14). O IEA da matriz exclui qualificação profissional ([RMO-068](../dominio/matriz-orcamentaria.md#rmo-068)). | Não serve como proxy do IEA da matriz. O IEA sem FIC não pode ser reconstruído com esta exportação. |
| **Gastos** | Valores nominais. Os gastos correntes da Rede41 vão de R$ 13,2 bi para R$ 23,6 bi (T12). | Sem deflator e sem rateio por campus. Não sustenta conclusões sobre eficiência. |
| **Tipo de oferta** | O Ifes registra quase toda a oferta técnica não integrada como "Concomitante" (30 linhas curso × campus em 2025), ao contrário da Rede, onde predomina "Subsequente". As linhas "Subsequente" do Ifes passam de 4–6 (2017–2022) para 13, 16 e 26 (2023–2025) (T14). | Mudança de classificação. Concomitante e subsequente devem ser analisados juntos. |

---

## 3. Mapa de variáveis × perguntas de gestão

| Pergunta de gestão | Variáveis | Disponibilidade | Observação |
|---|---|---|---|
| A instituição/campus cresceu? | matrículas, ME por tipo/modalidade/campus | **confirmado** | ME comparável só em 2021–2025. Matrículas regulares presenciais servem para 2017–2025, com ressalva da pandemia. |
| Cresceu por ingresso ou por tempo de vínculo? | vagas, ingressantes, matrículas, concluintes, evadidos | **confirmado** (agregado) | Sem coorte, o M/I não separa progressão regular de retenção. |
| O estoque cresceu por retenção? | retidos × em fluxo (`SituacaoMatricula`) | **parcial** | Disponível por campus, mas inclui FIC e EaD. Não há separação por tipo de curso. |
| A composição do portfólio mudou? | tipo de curso, oferta, modalidade, eixo, turno | **confirmado** | Mudanças de classificação, como concomitante → subsequente, exigem checagem. |
| A expansão foi absorvida? | ingressantes/vaga, inscritos/vaga | **parcial** | Ingressantes/vaga é confiável. Inscritos/vaga não é, e a Taxa de Ocupação foi retirada. |
| Permanência e êxito melhoraram? | evasão anual por curso; IEA por campus | **parcial** | A evasão anual por curso é utilizável. O IEA de ciclo sem FIC está ausente. A pandemia distorce 2020–2022. |
| Percentuais legais (técnico, formação de professores, EJA) | ME por categoria e campus | **confirmado** | Reconcilia com a matriz 2026 ([portão de dados](prumo-poc-portao-dados.md)). Não há classificação de formação de professores por curso. |
| Capacidade docente | professor-equivalente por campus, docentes por titulação/jornada | **parcial** | O professor-equivalente reconcilia com a matriz (±1%). O numerador da RAP não. Não há docente por área. |
| Infraestrutura (salas, laboratórios) | — | **ausente** | A PNP não substitui inventário físico. |
| Demanda territorial | — | **ausente** | Só há inscritos, que são institucionais e pouco confiáveis. Faltam Censo Escolar e dados de território. |
| Custo por campus | gastos por instituição | **ausente** no nível de campus | Valores nominais e só por instituição. |
| Intenção ou decisão de gestão | — | **ausente** | Exige PDI, atas, portarias e entrevistas. |

---

## 4. Relação com a Matriz CONIF

A tabela separa os cinco níveis pedidos. A fonte canônica é [`matriz-orcamentaria.md`](../dominio/matriz-orcamentaria.md), v1.2.2.

| Nível | O que existe | Situação nesta base |
|---|---|---|
| **1. Indicador PNP** | ME, %CT, %FP, %EJA, RAP, professor-equivalente, evasão, eficiência | Disponível 2017–2025, com as quebras do § 2.4. |
| **2. Variável elegível e ponderada pela matriz** | Funcionamento: **MT** = matrículas ativas × horas do curso no ano ÷ 800 × peso (×1,5 agro); retidos valem ¼ por até 3 anos; FIC entra; fatores N3: EaD próprio 0,8, EaD externo 0,25, MOOC 0,08 ([RMO-066](../dominio/matriz-orcamentaria.md#rmo-066), [RMO-067](../dominio/matriz-orcamentaria.md#rmo-067)). Qualidade: IEA sem FIC, RAP e %CT/%FP/%EJA em faixas ([RMO-021](../dominio/matriz-orcamentaria.md#rmo-021), [RMO-068](../dominio/matriz-orcamentaria.md#rmo-068)). | **%CT, %FP e %EJA: proxy oficial.** Reconcilia com 2026 (Ifes 0,4403 × 0,44). **Professor-equivalente:** reconcilia (±1%). **RAP:** não reconcilia. Ifes: 20,11 na PNP, 17,56 pela definição do guia, 18,148 na matriz (T13). **IEA:** não reproduzível (arquivo com FIC). **MT:** não derivável da ME, porque usa carga transcorrida, peso de curso, retidos a ¼ e fatores de financiamento. |
| **3. Participação relativa no montante** | Para 2026, o demonstrativo C5 traz indicadores e submontantes de Qualidade das 41 instituições ([RMO-072](../dominio/matriz-orcamentaria.md#rmo-072)). | **Não calculável** para outros exercícios. A "participação na ME da PNP" (§ 5.1) é proxy acadêmica: não pondera EaD, MOOC e retidos como a MT. |
| **4. Dotação em reais** | Depende do montante distribuível, da separação de assistência e de 80/10/10 ([RMO-006](../dominio/matriz-orcamentaria.md#rmo-006)). | **Não calculado.** |
| **5. Distribuição interna aos campi** | Ifes 2026: critérios próprios com piso e teto, sem fórmula publicada ([RMO-075](../dominio/matriz-orcamentaria.md#rmo-075), HIPÓTESE). | **Fora do alcance da PNP.** |

**Regras por exercício.** Esta exportação (anos-base 2017–2025) alimentaria, pelo calendário de RMO-070, as matrizes de 2019 a 2027. A matriz 2026 usou a prática anterior à N3 (Portaria MEC 646/2022 como texto, com a prática divergente em L-24). A N3 (Portaria MEC 243/2026) vale a partir de 2027. Para 2019–2025, o repositório tem apenas descrições históricas do livro ([RMO-028 a RMO-032](../dominio/matriz-orcamentaria.md#rmo-028)), sem planilhas oficiais. **Não presumo a mesma fórmula na série toda.**

**Três consequências diretas para leitura dos dados:**

- **Crescer em ME não equivale a crescer na matriz.** O caso extremo é o IFRS: a ME de FIC EaD (MOOC) passa de 184 para 55.726 e a ME total dobra de 2021 a 2025 (índice 249,5; T5). Na N3, MOOC pesa 0,08 no Funcionamento. Ao mesmo tempo, o %CT do IFRS cai de 55% para 16,9%, abaixo da primeira faixa de Qualidade.
- **Crescer em matrículas por retenção rende pouco na MT.** Um retido conta ¼ na MT e não entra no IEA. Instituições cujo estoque cresce por vínculo além do prazo previsto (§ 5.4, caso IFMA) teriam ganho de MT menor que o aumento de matrículas. Além disso, esse crescimento seria piora acadêmica, não melhora.
- **A participação relativa reage ao denominador.** O Ifes cresceu 3,5% na ME sem FIC de 2021 a 2025 e ainda assim perdeu participação, porque a Rede cresceu 7,9%, sobretudo em EaD (§ 5.1). Na matriz, o efeito depende dos fatores de EaD de cada exercício e não é calculável aqui. Isso é distributivo e não mede qualidade educacional.

---

## 5. Análises exploratórias verificáveis

### 5.1. Crescimento da Rede e participação relativa (perguntas A e G)

**ME da Rede41 por grupo de oferta (mil), 2021–2025 (bloco metodológico comparável; T4)**

| Grupo | 2021 | 2023 | 2025 | Δ 2021→25 | % do Δ total |
|---|---:|---:|---:|---:|---:|
| Técnico presencial | 486,6 | 470,2 | 482,6 | −3,9 | −3% |
| Graduação presencial | 316,9 | 329,2 | 322,7 | +5,7 | 5% |
| Pós-graduação presencial | 27,9 | 30,5 | 30,4 | +2,5 | 2% |
| Básica/ABI presencial | 14,7 | 15,2 | 16,8 | +2,1 | 2% |
| FIC presencial | 9,4 | 16,1 | 37,4 | +28,0 | 23% |
| Técnico EaD | 34,2 | 42,8 | 62,3 | +28,1 | 23% |
| Graduação EaD | 27,9 | 32,3 | 40,5 | +12,6 | 10% |
| Pós-graduação EaD | 29,4 | 42,1 | 55,8 | +26,5 | 22% |
| FIC EaD (inclui MOOC) | 71,0 | 49,8 | 91,3 | +20,4 | 17% |
| **Total** | **1.017,8** | **1.028,2** | **1.139,8** | **+122,0** | 100% |

*Fórmula:* soma de `Matrícula Equivalente | Geral` (`DadosGerais.csv`) por grupo (tipo de curso × modalidade). Nível: instituição agregada à Rede41.

**Verificação de dupla contagem (T4).** As mesmas linhas, agrupadas em quatro grupos mutuamente exclusivos:

| Grupo | ME 2021 | ME 2025 | Δ | % do Δ |
|---|---:|---:|---:|---:|
| Regular presencial | 846.106 | 852.551 | +6.444 | 5,3% |
| Regular EaD | 91.409 | 158.599 | +67.191 | 55,1% |
| FIC presencial | 9.358 | 37.367 | +28.009 | 23,0% |
| FIC EaD | 70.971 | 91.323 | +20.352 | 16,7% |
| **Soma = Δ total da Rede41** | | | **+121.996** | 100% |

Cada linha de `DadosGerais` tem um único tipo de curso e uma única modalidade. Por isso os grupos não se sobrepõem, e a soma reproduz o total. Destaque: a ME de FIC presencial quase quadruplicou (9,4 mil → 37,4 mil). Tudo isso é ME da PNP, não MT da matriz (§ 4).

**Participação na ME sem FIC da Rede41, 2021 → 2025, com decomposição (T5).** Δparticipação = (x₂₅ − x₂₁)/X₂₅ [efeito numerador] + (x₂₁/X₂₅ − x₂₁/X₂₁) [efeito denominador], onde x é a ME da instituição e X a da Rede.

| Instituição | ME 2021 | ME 2025 | Índice | Índice presencial | Partic. 2021 | Partic. 2025 | Δ p.p. | Numerador | Denominador |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IF Goiano | 18.087 | 24.578 | 135,9 | 101,4 | 1,93% | 2,43% | +0,50 | +0,64 | −0,14 |
| IFPI | 29.074 | 37.533 | 129,1 | 105,5 | 3,10% | 3,71% | +0,61 | +0,84 | −0,23 |
| IFMA | 38.386 | 45.204 | 117,8 | 106,0 | 4,09% | 4,47% | +0,38 | +0,67 | −0,30 |
| IFPR | 29.230 | 34.911 | 119,4 | 111,4 | 3,12% | 3,45% | +0,34 | +0,56 | −0,23 |
| IFSC | 37.344 | 37.776 | 101,2 | 97,0 | 3,98% | 3,74% | −0,25 | +0,04 | −0,29 |
| **Ifes** | **33.980** | **35.161** | **103,5** | **96,7** | **3,62%** | **3,48%** | **−0,15** | **+0,12** | **−0,26** |
| IFRN | 37.789 | 36.564 | 96,8 | 94,3 | 4,03% | 3,62% | −0,41 | −0,12 | −0,29 |
| IFPB | 39.931 | 34.857 | 87,3 | 87,6 | 4,26% | 3,45% | −0,81 | −0,50 | −0,31 |
| **Rede41** | 937.515 | 1.011.150 | 107,9 | 100,8 | | | | | |

**Leitura:**

- Entre os que mais ganharam participação, o motor foi EaD. No IF Goiano, a ME de técnico EaD vai de 57 para 4.589. No IFPI, a de graduação e pós EaD vai de ~1,0 mil para 7,8 mil. A oferta presencial regular desses institutos ficou quase estável.
- Nas instituições de perfil presencial, a perda de participação é sobretudo efeito do denominador, e o próprio crescimento é modesto.
- Os resultados de todas as 41 estão em T5.

### 5.2. Portfólio e percentuais legais (pergunta B)

**%CT da Rede41:** 61,5% (2017), 55,7% (2020), 51,2% (2021), 49,9% (2023), 47,8% (2025). As instituições com %CT ≥ 50% são 35 em 2017, 25 em 2021 e 24 em 2025 (T7). No bloco comparável (2021–2025), a queda é de 3,4 p.p. Ela se explica por FIC e EaD não técnica no denominador, já que a ME de técnico presencial ficou estável (§ 5.1).

**Reconfiguração técnico → graduação presencial** (matrículas regulares presenciais, médias A → B; T6). Uso matrículas físicas porque a ME não atravessa 2021.

| Instituição | Δ técnico | Δ graduação | %CT 2017 → 2025 | Índice ingressantes |
|---|---:|---:|---|---:|
| IFBA | −4.123 | +1.576 | 74,9 → 54,8 | 89,9 |
| IFPE | −3.521 | +2.732 | 83,1 → 60,2 | 93,7 |
| IF Goiano | −1.693 | +2.143 | 56,7 → 43,1 | 82,4 |
| IFTO | −1.662 | +1.132 | 54,7 → 52,1 | 91,1 |
| Cefet-MG | −1.284 | +1.289 | 55,7 → 43,4 | 90,8 |
| *Contraexemplos: as duas ofertas cresceram* | | | | |
| IFMA | +4.055 | +3.140 | 69,5 → 59,9 | 98,5 |
| IFCE | +3.563 | +4.542 | 45,7 → 40,8 | 91,9 |
| IFPB | +2.786 | +2.153 | 53,2 → 50,7 | 100,1 |
| IFPR | +1.223 | +4.141 | 69,5 → 60,2 | 113,2 |
| **Ifes** | **−768** | **+587** | **65,7 → 45,1** | **104,6** |

**Leitura.** Expandir a graduação não implicou, por si só, reduzir o técnico: há institutos que expandiram as duas ofertas. Os dados não mostram se a redução do técnico foi decisão, perda de demanda ou reclassificação.

### 5.3. Demanda e preenchimento (pergunta C)

- **Ingressantes por vaga** (regular presencial, Rede41) ficam estáveis, entre 0,88 e 0,97. Por tipo de oferta, a média A → B cai em vários casos (T9, médias trienais): subsequente de 0,91 para 0,83, licenciatura de 0,93 para 0,79 e PROEJA integrado de 0,86 para 0,71. **Há ociosidade crescente concentrada em subsequente, licenciatura e PROEJA.**
- No IFPE, o técnico subsequente passa de 0,94 (média A) para 0,76 (média B) ingressante por vaga, com 0,71 em 2025. A graduação vai de 0,99 (2017) para 0,84 (2025) (T11).
- Inscritos por vaga tem baixa confiabilidade (§ 2.4) e não foi usado em conclusões.

### 5.4. Ingresso, tempo de vínculo e estoque (perguntas A, C e D)

**Rede41, oferta regular presencial, médias A → B (T6):**

| Medida | Valor |
|---|---|
| Matrículas | 713.784 → 788.014 (+10,4%) |
| Ingressantes | 224.921 → 219.678 (−2,3%) |
| Vagas | +0,7% |
| M/I | 3,17 → 3,59 |
| Professor-equivalente | +9,9% |

**Variação entre as 41 instituições (n = 41, medidas A → B):**

- **Ingresso e tempo de vínculo pesam igual.** Na decomposição da variância de Δlog matrículas, 0,50 vem dos ingressantes e 0,50 do M/I.
- **Ambos se associam positivamente ao crescimento.** A correlação entre Δlog matrículas e Δlog ingressantes é 0,52, e com Δlog M/I também é 0,52.
- **A evasão anual não explica o crescimento.** A correlação entre Δ evasão anual média (p.p.) e Δlog matrículas é **−0,00**; com Δlog M/I, é −0,10.
- **O crescimento acompanha o professor-equivalente.** A correlação com Δ% professor-equivalente é 0,43. É associação, não causalidade: docentes podem seguir a matrícula ou precedê-la.
- *Fórmulas (T6):* correlação de Pearson entre instituições (n = 41). As variações comparam as médias trienais A e B. A evasão é a média das taxas anuais de cada triênio.

**Interpretação (associação plausível, não causal).** O aumento do M/I da Rede tem pelo menos três explicações possíveis, que os dados agregados não separam:

1. uma composição mais longa, com mais integrado e bacharelado e menos subsequente;
2. mais retenção: a fatia de retidos entre os matriculados "em curso" passa de 21–22% para 25–30%;
3. efeitos residuais da pandemia.

Por isso, **"crescer em matrícula" pode significar mais acesso, cursos mais longos ou mais estudantes retidos**, e cada uma dessas vias tem efeito diferente na MT (retido conta ¼) e no IEA. **Crescimento do estoque por retenção é resultado acadêmico indesejável**, mesmo quando eleva contagens. Nenhum M/I maior deve ser lido como sucesso de permanência sem separar retidos de estudantes em fluxo regular.

**Ifes × Rede, médias A → B (T9, médias trienais):**

| Oferta | | Vagas | Ingressantes | Ingressantes/vaga | Matrículas | M/I |
|---|---|---|---|---|---|---|
| Técnico integrado | Ifes | +19% | +18% | 1,02 → 1,01 | +10% | 3,50 → 3,27 |
| | Rede41 | +16% | +19% | 0,96 → 0,98 | +21% | 3,34 → 3,39 |
| Técnico concomitante + subsequente | Ifes | −1% | −6% | 0,99 → 0,93 | −25% | 2,82 → 2,26 |
| | Rede41 | −20% | −27% | 0,91 → 0,83 | −20% | 2,69 → 2,93 |
| Graduação | Ifes | +7% | −4% | 1,03 → 0,92 | +8% | 3,62 → 4,07 |
| | Rede41 | +5% | +1% | 0,91 → 0,88 | +23% | 3,55 → 4,34 |

**Leitura: no técnico do Ifes, o gargalo está depois do ingresso.**

- **Técnico.** As vagas do Ifes se preenchem: 0,93–1,01 ingressante por vaga, acima da Rede. A perda no concomitante/subsequente ocorre na trajetória da turma: o estoque cai 25% com ingressantes −6%, e os concluintes também caem (Vitória 410 → 231/ano; Serra 152 → 53; Vila Velha 134 → 17). Para esse problema, a alavanca é a trajetória da turma (evasão precoce, duração, retenção, reclassificação), não a ocupação das vagas.
- **Graduação.** É aqui que está a queda de ocupação: licenciatura de 1,03 para 0,86 e tecnologia de 1,08 para 0,78 ingressante por vaga (T9). A distância entre vagas (+9,7%) e ingressantes (+4,6%) na oferta regular presencial vem principalmente daí.
- **Integrado.** Parte da diferença pode ser defasagem: os ingressantes do Ifes crescem sobretudo em 2023–2025, e o estoque de cursos de 3–4 anos ainda não acompanhou.
- **Classificação.** No Ifes, "subsequente" sozinho não forma série estável (as linhas "Subsequente" passam de 5 em 2022 para 26 em 2025; T14). As duas formas devem ser analisadas juntas.

### 5.5. Capacidade institucional (pergunta E)

- Na Rede41, o professor-equivalente cresce de 37.979 para 43.237 entre 2017 e 2025 (+13,8%). A RAP da PNP oscila entre 22,6 e 25,4 (T12).
- No Ifes, o professor-equivalente vai de 1.452 para 1.589 (+9,4%), contra matrículas regulares presenciais +0,7% (médias A → B).
- **Não interpreto RAP maior ou menor como eficiência.** O numerador da RAP não reconcilia com a matriz, os gastos são nominais e só existem por instituição, e não há docente por área nem inventário físico.

**Teste do numerador da RAP (T13).** O guia PNP define a "relação entre matrícula equivalente presencial e professor equivalente" (ALRAPE). Comparei três candidatos ao numerador da matriz 2026 ("MEq-RAP Pres (5.6b PNP)" no demonstrativo C5), ano-base 2024, nas 41 instituições:

| Candidato (PNP, ano-base 2024) | Razão ÷ numerador da matriz: mediana (mín–máx) | Dentro de ±1% | Dentro de ±3% |
|---|---|---:|---:|
| ME presencial, com FIC (definição ALRAPE do guia) | 0,971 (0,942–1,032) | 6 | 21 |
| ME presencial, sem FIC | 0,949 (0,851–1,019) | 1 | 7 |
| "Matrículas RAP" do arquivo PNP | 1,066 (1,001–2,567) | 8 | 14 |
| *Denominador: professor-equivalente PNP ÷ matriz* | *1,002 (1,000–1,005)* | | |

Para o Ifes, a RAP é 17,56 pela definição ALRAPE do guia (26.689 ÷ 1.520), contra 18,148 na matriz (27.539 ÷ 1.517,5) e 20,11 no arquivo RAP da PNP (30.574 ÷ 1.520).

**Leitura:**

- O denominador fecha.
- A definição do guia é a mais próxima, mas fica sistematicamente cerca de 3% abaixo. É provável que a matriz use outro recorte ou outra versão do cálculo, por exemplo com algum ajuste ou edição distinta. A diferença não parece ruído.
- **Continua não reconciliado.** A RAP da matriz não deve ser estimada a partir da PNP sem a documentação do cálculo 5.6b.

### 5.6. Contribuição dos campi (pergunta F)

Nas 41 instituições, os três campi que mais cresceram concentram de 25% (IFPR) a 100% (IFRR) do crescimento positivo (T6, coluna top3%).

**No Ifes (T8):**

- 10 campi cresceram mais de 5% e 5 encolheram mais de 5%.
- Os três maiores crescimentos concentram 61% do ganho positivo: Vila Velha (+590 matrículas regulares presenciais, sobretudo graduação +344), Barra de São Francisco (+242) e Guarapari (+162).
- As maiores quedas foram em Colatina (−342), Vitória (−232), Cariacica (−228) e Nova Venécia (−228). Nos quatro, o técnico cai.
- O M/I diverge entre campi. Cai em Cariacica (4,18 → 2,95), Piúma (3,49 → 2,72), São Mateus (3,76 → 3,03) e Vitória (3,27 → 2,92). Sobe em Barra de São Francisco (1,82 → 3,26, maturação de campus novo) e Venda Nova (2,79 → 3,67).

**Leitura:** a estabilidade agregada do Ifes esconde contribuições opostas entre campi, que é exatamente o objeto da governança distribuída.

### 5.7. Resiliência e picos (pergunta H)

- **Pulsos de oferta EaD.**
  - **Colatina:** as especializações EaD registradas no campus somam 2.992 ME em 2021, 202 em 2022, 6.454 em 2023 e 54 em 2024 (T11). Quase tudo vem de um único curso, "Desenvolvimento Educacional e Social", com 2.934 matrículas em 2021 e 6.313 em 2023 (T14).
  - **Cefor:** o mesmo curso soma 4.304 matrículas em 2023. Em 2024, outra especialização EaD, de docência para a educação profissional, soma 3.499 (T14).
  - **Efeito:** esses pulsos explicam o %CT de 36,8% em 2023 (T11).
- **MOOC sem continuidade.** A FIC EaD do IFSUL sobe de 489 ME (2019) para 36.178 (2021) e cai para 9.993 (2022). O %CT do IFSUL vai de 68% para 23% e depois para 41%.
- **Sem picos isolados no total institucional.** Nenhuma instituição tem alta acima de 20% seguida de queda acima de 15% na ME total ou na ME sem FIC de 2021 a 2025. Os picos ficam no nível de componente ou de campus.
- **Crescimento sustentado:** IFSP, IFRJ, IFPR, IFPI, IFPA, IFMS, IFMG, Ifes, IFC e IFB cresceram em 6 dos 8 anos nas matrículas regulares presenciais. O critério é pouco discriminante por causa da pandemia.

---

## 6. Insights candidatos (priorizados)

### I-1. Conversão de vaga em matrícula ativa: ingresso × trajetória da turma
*Prioridade 1: alto impacto decisório, solidez média-alta, viável já.*

1. **O que os dados mostram.**
   - **Rede41:** de A para B, cresceu 10,4% em matrículas regulares presenciais com 2,3% menos ingressantes (M/I de 3,17 para 3,59), enquanto a retenção subiu.
   - **Ifes:** ampliou vagas (+9,7%) e ingressantes (+4,6%), mas as matrículas ficaram estáveis (+0,7%) e o M/I caiu de 3,30 para 3,18.
   - **Técnico concomitante/subsequente do Ifes:** as vagas se preenchem (0,93 ingressante por vaga), mas o estoque cai 25% e os concluintes caem.
   - **Onde:** Cariacica, Vitória, Piúma e São Mateus.

   Fonte: `DadosGerais.csv`, T6, T8, T9.
2. **Por que interessa.** "Abrir mais vagas" é a alavanca mais citada nas metas, mas no técnico do Ifes ela não se converteu em estoque, e o motivo não é falta de candidatos. O gestor precisa saber se o problema é evasão precoce, curso mais curto, menos retidos (o que seria bom) ou classificação. Cada causa pede uma decisão diferente.
3. **Relação com metas.** Metas de matrícula e de %CT dependem do estoque, não das vagas. Cada campus contribui de forma diferente: um pode precisar reduzir evasão mais do que abrir vagas.
4. **Uso no simulador.** A decisão do gestor passa a ser **vagas**, não matrículas. O simulador converte vagas em matrículas ativas por ano com quatro parâmetros separados, cada um com faixa empírica do próprio campus e dos pares:
   - ingressantes por vaga;
   - evasão;
   - **retenção**;
   - conclusão.

   Um M/I único não serve, porque esconderia a retenção.
5. **Dados que faltam.** Coortes do qAcadêmico (situação por ano desde o ingresso), duração prevista dos PPCs, histórico de reclassificação concomitante/subsequente e de jubilamentos.
6. **Confiabilidade.** **Alta** para os fatos agregados. **Média** para a interpretação, pois o M/I não separa progressão regular de retenção.

### I-2. O denominador da Rede cresce por FIC e EaD; a oferta presencial regular está estável
*Prioridade 2.*

1. **O que os dados mostram.** De 2021 a 2025, 94,7% do crescimento da ME da Rede41 veio de FIC e EaD, em quatro grupos mutuamente exclusivos: regular EaD 55,1%, FIC presencial 23,0% e FIC EaD 16,7%. A presencial regular contribuiu com 5,3%. O Ifes perdeu 0,15 p.p. de participação, sendo −0,26 p.p. de efeito denominador (T4, T5).
2. **Por que interessa.** Cenários de matriz que projetam "a Rede cresce X%" de forma uniforme ([RMO-057](../dominio/matriz-orcamentaria.md#rmo-057)) erram o sinal da competição relevante. A disputa ocorre em EaD e FIC, que têm fatores próprios na N3.
3. **Relação com metas.** Mostra que uma meta institucional de participação pode ser inalcançável só com oferta presencial, e que perder participação não significa piorar.
4. **Uso no simulador.** Premissa de **crescimento da Rede por modalidade e por tipo**, com tendência 2021–2025 e intervalos, aplicada separadamente a presencial, EaD e MOOC.
5. **Dados que faltam.** A MT da Rede por modalidade em cada exercício (planilhas oficiais) e a separação EaD próprio/externo na PNP.
6. **Confiabilidade.** **Alta** como fato sobre a ME. **Baixa** como estimativa de efeito na matriz, porque ME não é MT.

### I-3. O %CT institucional é sensível a ofertas não técnicas em pulso e a decisões de poucos campi
*Prioridade 3.*

1. **O que os dados mostram.** Em 2023, uma especialização EaD de Colatina tirou 6,3 p.p. do %CT do Ifes. Sem o Cefor, o Ifes fica em 50,8% em 2025 contra 45,1% com ele (T11). Na Rede, o número de instituições na faixa ≥ 50% caiu de 35 para 24 entre 2017 e 2025 (T7).
2. **Por que interessa.** A faixa de %CT pesa na Qualidade ([RMO-021](../dominio/matriz-orcamentaria.md#rmo-021)), e o ano-base 2023 alimenta a matriz 2025. Uma decisão local de oferta EaD tem efeito institucional dois anos depois.
3. **Relação com metas.** É o argumento central do pacto de metas: o campus que oferta formação de professores sustenta o %FP e reduz o %CT. Os efeitos precisam ser negociados juntos.
4. **Uso no simulador.** Uma **restrição/alerta**: toda oferta não técnica acima de um limiar de ME mostra o efeito no %CT e no %FP do Ifes e o exercício afetado.
5. **Dados que faltam.** Classificação oficial de formação de professores por curso (L-25) e calendário das ofertas em pulso.
6. **Confiabilidade.** **Alta.**

### I-4. Crescimento não é sinônimo de expansão de acesso: três trajetórias diferentes
*Prioridade 4: valor para a UX conceitual de "comparáveis".*

1. **O que os dados mostram.** Matrículas regulares presenciais semelhantes escondem trajetórias diferentes:
   - **IFPR:** ingresso +13%, professor-equivalente +30% e matrículas +33%. Expansão com capacidade.
   - **IFMA:** ingresso −1,5%, M/I de 3,23 para 4,15 e matrículas +27%, com 31–46% de retidos entre os matriculados em curso. Crescimento do estoque com retenção elevada. Até prova em contrário, isso é resultado acadêmico indesejável, não estratégia de permanência.
   - **IFPE:** técnico −3.521, graduação +2.732 e ingressantes/vaga em queda. Reconfiguração com ociosidade.
2. **Por que interessa.** Comparar o Ifes com "quem cresceu mais" levaria a copiar o IFMA, cujo crescimento de matrícula tem pouco efeito na MT e no IEA.
3. **Relação com metas.** Metas de matrícula precisam vir acompanhadas de metas de ingresso e de conclusão.
4. **Uso no simulador.** O **parâmetro de comparação** deve ser a trajetória decomposta (ingresso, evasão, retenção, conclusão, composição), não o índice de matrículas. Um par só serve de referência para premissas de "crescimento saudável" se o crescimento dele não vier de retenção.
5. **Dados que faltam.** IEA sem FIC por instituição e por ano; documentos institucionais (PDI, relatórios de gestão).
6. **Confiabilidade.** **Média.**

---

## 7. Estudos de caso

Cada caso separa **fato observado**, **associação plausível** e **hipótese a verificar**.

### Caso 1 — Ifes: mais vagas, mesmo estoque (caso central)

| Medida (regular presencial) | A (2017–19) | B (2023–25) | Rede41 A → B |
|---|---:|---:|---:|
| Vagas | 7.451 | 8.171 (+9,7%) | +0,7% |
| Ingressantes | 7.514 | 7.862 (+4,6%) | −2,3% |
| Matrículas | 24.791 | 24.973 (+0,7%) | +10,4% |
| M/I (anos de vínculo por ingressante) | 3,30 | 3,18 | 3,17 → 3,59 |
| Participação na Rede (matrículas) | 3,47% | 3,17% | |

- **Fatos (T6, T8, T9).**
  - A queda está concentrada no técnico concomitante/subsequente: matrículas de 5.881 para 4.409, com ingressantes −6%. As vagas seguem preenchidas: 0,99 → 0,93 ingressante por vaga.
  - A diferença entre vagas e ingressantes vem da graduação, com ingressantes por vaga de 1,03 para 0,92.
  - Os concluintes dessa oferta também caem (Vitória 410 → 231/ano; Serra 152 → 53; Vila Velha 134 → 17).
  - A evasão anual dessa oferta é parecida nos dois períodos (~23–25%).
  - A fatia de retidos entre os matriculados em curso é menor que a da Rede (Ifes 17–27%; Rede 25–30% em B).
- **Associação plausível.** Os cursos de duração menor (subsequente) ganham peso e as coortes de integrado ampliadas em 2023–2025 ainda não maturaram. As duas coisas reduzem o M/I sem implicar piora.
- **Explicações alternativas.**
  - Reclassificação concomitante → subsequente (linhas "Subsequente": 5 em 2022, 26 em 2025; T14).
  - Saneamento de registros de retidos antigos.
  - Encurtamento de PPCs.
  - Evasão nos primeiros meses, não captada pela taxa anual.
- **Perguntas que exigem documentos ou entrevistas.** Houve redesenho de carga horária dos subsequentes? Houve jubilamentos em lote entre 2019 e 2022? Por que Serra e Vila Velha reduziram concluintes? A Proen/Prodi reclassificou a oferta em 2023?

### Caso 2 — IFMA: estoque cresce com retenção elevada (contraponto)

- **Fatos.**
  - Matrículas regulares presenciais +26,6% (A → B) com ingressantes −1,5% e vagas +1,2%. O M/I vai de 3,23 para 4,15.
  - A fatia de retidos entre os matriculados em curso fica entre 31% e 46%, contra 21–30% na Rede.
  - Participação na ME sem FIC: +0,38 p.p. (2021 → 2025), com crescimento também em técnico EaD (1.645 → 3.984) e pós EaD (1.957 → 4.029).
  - %CT de 69,5% para 59,9% (T5, T6, T11).
- **Associação plausível.** Parte do crescimento do estoque é retenção. Pelas regras documentadas, o retido conta ¼ na MT após o fim previsto e não entra no IEA. **Este caso não deve ser apresentado como estratégia de permanência a seguir.** Estudantes retidos por reprovação ou atraso elevam a contagem de matrículas, mas representam piora acadêmica.
- **Explicações alternativas.** Cursos efetivamente mais longos (bacharelados novos); evasão de fato menor (a evasão anual do IFMA, 6–12%, é baixa); registro tardio de evasão.
- **Para confirmar.** Fluxo por coorte do IFMA; política de jubilamento; composição por duração.

### Caso 3 — IFPR: expansão com ingresso e docentes (trajetória positiva)

- **Fatos.**
  - Matrículas regulares presenciais +32,6%, vagas +24,6%, ingressantes +13,2% e professor-equivalente +30,1% (1.105 → 1.547 entre 2017 e 2025).
  - Graduação +4.141 matrículas e técnico +1.223. O %CT fica em 60,2% em 2025.
  - O crescimento é distribuído: 21 campi crescem, 1 diminui, e os três maiores concentram 25% do ganho (T6, T11).
- **Associação plausível.** Expansão acompanhada de provimento docente e com contribuição de muitos campi.
- **Explicações alternativas.** Maturação de campi criados na expansão; inscritos por vaga baixos (2,2–2,6 entre 2021 e 2025; T14) sugerem demanda menos folgada; os ingressantes cresceram menos que as vagas (+13,2% × +24,6%; T6).
- **Para confirmar.** Cronologia de provimentos e de autorização de cursos no IFPR; inscritos por campus.

### Caso 4 — IFPE: reconfiguração com ociosidade (caso negativo)

- **Fatos.**
  - Técnico presencial: matrículas −26% entre 2017 e 2025 (20.111 → 14.846). O subsequente cai de 4.018 para 2.671 ingressantes/ano (médias A → B), e sua relação ingressantes/vaga vai de 0,94 para 0,76 (0,71 em 2025).
  - Graduação presencial: matrículas +80% (3.771 → 6.801), com ingressantes/vaga de 0,99 para 0,84.
  - %CT de 83,1% para 60,2%. A evasão anual da oferta regular presencial cai de 23,5% para 14,7% (T6, T11).
- **Associação plausível.** A substituição de subsequente por graduação veio com vagas menos preenchidas nas duas pontas. Não há ganho líquido de matrícula: índice 97,5.
- **Explicações alternativas.** Queda de demanda por subsequente na região (a Rede inteira perdeu 27% dos ingressantes nessa oferta); vagas de graduação abertas antes da demanda maturar; mudança de processo seletivo.
- **Para confirmar.** Atas de criação e extinção de cursos; demanda territorial do Censo Escolar; vagas remanescentes e chamadas.

---

## 8. Riscos de interpretação e dados complementares

**Riscos:**

- **Atravessar 2020/2021 com a ME.** Produz quedas de técnico e saltos de EaD artificiais. Mitigação: usar a ME só em 2021–2025, e matrículas para séries longas.
- **Ler 2020–2022 como desempenho.** A evasão subnotificada e a retenção inflada são artefato.
- **Tratar programa ou tipo de oferta como série.** Os rótulos mudam (MOOC, PROEJA, concomitante/subsequente).
- **Confundir ME, MT e participação na matriz** (§ 4).
- **Ler tempo de vínculo como permanência saudável.** Um M/I maior pode ser retenção. Toda comparação de estoque deve mostrar retidos × em fluxo.
- **Procurar o problema na ocupação quando ele está na trajetória.** No técnico do Ifes, as vagas se preenchem; a perda ocorre depois do ingresso (§ 5.4).
- **Ranking implícito.** Tabelas ordenadas por crescimento convidam a comparar instituições de perfis, regiões e estágios de expansão diferentes. Os casos foram escolhidos por trajetória, não por posição.
- **Atribuir intenção.** A PNP não registra decisões. Toda leitura de "estratégia" é hipótese.
- **Correlações com n = 41 e janelas curtas.** São instáveis. Nenhuma foi tratada como causal.

**Dados complementares por prioridade:**

1. Coortes de matrícula do Ifes (qAcadêmico) ou microdados PNP de matrícula, com ciclo, datas e situação.
2. Duração e carga horária dos PPCs e histórico de reclassificações (Proen/Prodi).
3. Planilhas oficiais da matriz por exercício (MT por instituição e modalidade, 2023–2027).
4. Classificação oficial de formação de professores por curso.
5. Demanda territorial (Censo Escolar, egressos do ensino médio por microrregião).
6. Professor-equivalente por área e inventário de espaços.
7. Deflator e rateio de gastos por campus.

---

## 9. Hipóteses de produto para o PRUMO (separadas dos resultados)

São hipóteses para validar com gestores, não especificações:

- **H-P1 — Premissas com procedência.** Cada premissa do simulador, como conversão vaga → matrícula, M/I por oferta e crescimento da Rede por modalidade, mostraria o valor do próprio campus, a faixa dos comparáveis e a fonte (arquivo, ano-base, fórmula). *Valida-se se o gestor muda a premissa padrão depois de vê-la.*
- **H-P2 — Comparáveis por trajetória, não por tamanho.** Os comparáveis seriam escolhidos por perfil de oferta e mecanismo de crescimento (ingresso, evasão, retenção, composição), com o critério declarado. Evita o "copie quem cresceu mais".
- **H-P3 — Efeito numerador × denominador.** Toda variação de participação seria explicada como "o que fizemos" e "o que a Rede fez". Isso reduz a leitura de perda relativa como fracasso.
- **H-P4 — Alerta de pulso e de exercício.** Uma oferta que move um indicador institucional em mais de 1 p.p. mostraria o ano-base e o exercício da matriz afetados.
- **H-P5 — Antes e depois por campus.** A contribuição de cada campus para a mudança institucional seria mostrada no formato de T8, como insumo para o pacto de metas.

---

## 10. Próximo experimento mínimo de valor

**Estudo de caso para um gestor do Ifes (Proen e diretores de 3–4 campi):**

> *"A oferta técnica concomitante/subsequente do Ifes manteve as vagas preenchidas, mas perdeu 25% das matrículas e metade dos concluintes em alguns campi. O que acontece com as turmas depois do ingresso em Vitória, Serra, Cariacica e Vila Velha, e o que isso implica para abrir ou reformular essas vagas?"*

O foco é a trajetória das turmas, não a ocupação das vagas, que segue alta (§ 5.4).

- **Insumo já existente.** T8 e T9: série 2017–2025 por campus e oferta (vagas, ingressantes, matrículas, concluintes, evasão anual e M/I), com a Rede e os pares como referência (IFSC, IFRN, IFBA, IFPE, IFMA, IFPI, IFPR e IFMT, com porte e número de campi semelhantes; critério em T6).
- **O que acrescentar, sem módulo novo:**
  1. Pedir à Proen/Prodi a lista de reclassificações concomitante/subsequente e as durações dos PPCs.
  2. Extrair do qAcadêmico a situação das coortes 2019–2023 desses cursos nos 4 campi: evadidos no 1º ano, concluídos no prazo, retidos.
  3. Recalcular, para uma coorte de 40 vagas, as matrículas-ano geradas e a MT pela regra RO-MT ([RMO-066](../dominio/matriz-orcamentaria.md#rmo-066)). Comparar com a mesma vaga em integrado.
- **Entregável.** Memorando de 2 páginas com tabela antes/depois e três hipóteses ordenadas por evidência. Uma pergunta ao gestor: *"Isso muda a decisão sobre as vagas de 2027?"*
- **Critério de sucesso.** O gestor identifica pelo menos uma causa que não conhecia, ou descarta uma explicação que usava.
- **Custo.** Baixo: dados públicos já carregados, mais uma extração institucional.

---

## Resposta objetiva

**A inteligência comparativa longitudinal da PNP merece entrar no PRUMO?** Sim, com escopo delimitado:

- **Como camada de premissas e de contexto para o simulador e para o pacto de metas.** Não como painel nem como ranking.
- **Com séries que respeitem as quebras:** ME só em 2021–2025; matrículas e fluxos em 2017–2025, sem ler 2020–2022 como desempenho.
- **Sempre declarada como proxy acadêmica**, nunca como estimativa da matriz.

Os dados locais bastam para isso. Seriam insuficientes para IEA, RAP da matriz, custos e infraestrutura.

**Qual é a primeira pergunta de alto valor que já conseguimos responder com confiabilidade?** *"Quanto cada vaga, por tipo de oferta e campus, se converte em matrícula ativa ao longo do ciclo, e como essa conversão evoluiu no Ifes em relação à Rede e aos pares?"*

- **Os fatos são de confiabilidade alta.** São contagens oficiais coerentes entre arquivos, por campus e oferta, 2017–2025.
- **A explicação ainda depende de coortes institucionais** (§ 10).
- **Um dashboard descritivo não responde a isso.** Ele mostraria "o Ifes cresceu pouco". A decomposição mostra que o Ifes ampliou o ingresso e perdeu conversão depois dele. Já a Rede cresceu com mais tempo de vínculo por ingressante, que inclui retenção. São problemas diferentes, com alavancas e efeitos na matriz diferentes.

---

### Fontes metodológicas consultadas

- Guia PNP (versão com Portaria Setec/MEC 11/2026), [espelho público](https://pnp-ccv.github.io/guiapnp/assets/files/Guia_PNP.pdf), consultado em 10/11/2026: definições de ME (M × FECH × FEC; Portaria Setec/MEC 146/2021), evasão anual, ingressantes, vagas, eficiência por ciclo e retirada da Taxa de Ocupação. O endereço oficial `pnp.mec.gov.br/guiapnp` (versão web, com fichas técnicas) retornou HTTP 403 e não foi lido diretamente. Recomenda-se preservar uma cópia da versão oficial como evidência, como foi feito com a Portaria 243/2026.
- [Demonstrativo C5 da matriz 2026 (IFMT)](../dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx), aba Indicadores: numerador e denominador da RAP por instituição (T13).
- [Guia de Referência Metodológica da PNP 2018](../dominio/evidencias/2026-11-09/pnp-guia-referencia-metodologica-2018.pdf): definição anterior da ME, com fator de nível de curso e apenas matrículas sem programa associado.
- [Fonte canônica da Matriz Orçamentária, v1.2.2](../dominio/matriz-orcamentaria.md), incluindo N2, N3, C5 e RMO-003, 021, 028–032, 057, 066–070, 072 e 075.
- [Portão de dados da prova de conceito](prumo-poc-portao-dados.md): reconciliação de %CT, %FP, %EJA e professor-equivalente com a matriz 2026.
