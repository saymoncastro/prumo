# PRUMO — Revisão estratégica independente e oportunidades

> **Data:** 09/11/2026 · **Natureza:** análise crítica de concepção; não é decisão institucional, especificação aprovada nem compromisso de implementação.
> **Documento irmão:** [Revisão crítica das regras de negócio](../dominio/revisao-critica-regras-prumo.md), que contém a auditoria técnica e as evidências numéricas.
> **Reprodução dos números:** [`reproduzir_revisao_critica.py`](../dominio/evidencias/2026-11-09/reproduzir_revisao_critica.py) e [resultado JSON](../dominio/evidencias/2026-11-09/resultado-revisao-critica.json).

**Convenção de natureza da afirmação**, usada em todo o texto:

| Marca | Significado |
|---|---|
| **[FATO]** | Verificado nas fontes do repositório, com referência. |
| **[REGISTRADO]** | Decisão ou visão já registrada nos documentos do projeto. |
| **[INFERÊNCIA]** | Conclusão técnica derivada de fatos, com premissas explícitas. |
| **[HIPÓTESE]** | Proposição estratégica a validar com gestores ou dados. |
| **[RECOMENDAÇÃO]** | Posição desta revisão. |

> **Atualização de 09/11/2026: Portaria MEC nº 243/2026 obtida** (DOU de 12/03/2026; análise no [§ 0 do Documento B](../dominio/revisao-critica-regras-prumo.md#0-atualização-de-09112026-portaria-mec-nº-2432026-n3-obtida)). Ela **mantém** as faixas de Qualidade, os blocos 80/10/10, EAD 25%/80% e o texto da cadeia de MT, e **fixa a MOOC em 8%** do presencial. As conclusões centrais deste documento ficam **reforçadas**: os degraus de Qualidade valem sob a norma vigente, e a MOOC deixa de ser alavanca orçamentária relevante. Os trechos que citavam a MOOC a 80% ou a Portaria 243 como indisponível foram corrigidos abaixo. As correções de regras foram incorporadas na [fonte canônica v1.2.0](../dominio/matriz-orcamentaria.md).

---

## 1. Resumo executivo

A visão do Prumo (governança distribuída de metas, com a simulação acadêmico-orçamentária como porta de entrada) está **conceitualmente correta**. Mas há um descompasso entre a tese e a forma como o trabalho foi conduzido: o esforço recaiu sobre reproduzir, com rigor quase forense, a parte da matriz que **menos depende de coordenação entre campi**, ou seja, o preço por matrícula no bloco de Funcionamento. A parte que **mais depende** dessa coordenação ficou classificada como "condicional": os indicadores institucionais com degraus do bloco de Qualidade e Eficiência.

Quatro descobertas desta revisão mudam a leitura do problema:

1. **A matrícula total (MT) já está reproduzida, e é simples.** [FATO] Uma regra operacional unificada reproduz **2.322/2.322 ciclos** da planilha do Ifes e **1.086/1.086 ciclos** do demonstrativo do IFMT, a quatro casas decimais. A leitura literal da Portaria 646/2022 acerta 1.300 e 993, respectivamente. Os cinco "contraexemplos" da auditoria anterior e os 1.055 ciclos FIC, que ela não testou, ficam explicados. Em termos de gestão: **MT ≈ estudantes ativos × horas do curso efetivamente transcorridas no ano-base ÷ 800 × peso do curso** (×1,5 para cursos agropecuários), com redutores para retidos. Uma aluno-hora presencial vale cerca de **R$ 1,53 × peso** na referência de Funcionamento 2026. Reproduzir mais essa cadeia tem retorno marginal baixo.

2. **No bloco de Qualidade, o Ifes está abaixo de dois degraus que zeram sua participação.** [FATO, C5 2026] O Ifes tem 44% de matrículas equivalentes em cursos técnicos (degrau em 50%) e 1,86% em PROEJA (degrau em 2,5%). Recebe **R$ 0** nos subcomponentes CT (R$ 77,2 mi na Rede) e EJA (R$ 11,0 mi). A RAP de 18,15 está a **0,15** do degrau que zera o subcomponente RAP: uma perda de cerca de 224 matrículas equivalentes presenciais (0,8%) bastaria. [INFERÊNCIA, mantidos os demais participantes] Alcançar 50% de CT renderia cerca de **+R$ 2,06 mi/ano**; alcançar 60%, **+R$ 4,76 mi/ano**. Isso equivale a 3% a 7,6% de todo o Funcionamento do Ifes (R$ 62,8 mi) e corresponde ao que se obteria com milhares de novas matrículas totais.

3. **Esses degraus são metas institucionais que coincidem com mandatos legais e que só se alcançam com contribuições diferenciadas dos campi.** Os mandatos são 50% em técnicos (Lei 11.892/2008, art. 8º) e EJA. [INFERÊNCIA] O percentual técnico do Ifes é a agregação dos portfólios de 22 campi, cujas participações técnicas estimadas vão de 15% a 85%. Nenhum campus sozinho move o indicador; nenhum precisa fazer o mesmo esforço. Esse é, literalmente, o problema que a tese de governança distribuída descreve, e ele tem valor demonstrável em reais, em conformidade legal e em missão.

4. **O maior risco de concepção é o produto incentivar a otimização local contra o coletivo.** [INFERÊNCIA] Mostrar "contribuição do campus na matriz em R$" estimula volume de matrícula total (FIC curto, MOOC, EAD de baixo custo). Esse volume rende pouco no Funcionamento e pode **diluir** os percentuais institucionais (CT, FP) e a RAP, que são os indicadores de maior alavancagem. Um simulador centrado em Funcionamento por campus pode piorar decisões.

**Recomendação central.** Reposicionar a primeira prova de valor de "simulador de oferta com efeito na Matriz CONIF" para **"pacto de metas institucionais com degraus: como os campi, com contribuições diferentes, levam o Ifes a cruzar limiares legais e orçamentários"**. O motor de coortes e a MT continuam necessários, mas como instrumentos dessa decisão. A Portaria 243/2026 já foi obtida e confirma as faixas. Antes de qualquer código, restam três verificações de baixo custo: (a) conciliar a definição de matrícula equivalente usada nos percentuais legais (o Ifes tem 44% na PNP contra 58% estimados a partir das matrículas equalizadas da planilha); (b) obter a regra interna de distribuição do Ifes; (c) pedir à Setec a memória de cálculo da matriz 2027, porque a Portaria 243 repete um texto de MT e IEA que a prática de 2026 não seguiu.

---

## 2. Contexto efetivamente analisado

| Material | Situação | Uso nesta revisão |
|---|---|---|
| `contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md` | Lido integralmente | Base da visão, princípios e fases [REGISTRADO]. |
| `proposta_nome_prumo.md` | Lido integralmente | Posicionamento, tagline e primeiro caso de uso [REGISTRADO]. |
| `docs/dominio/matriz-orcamentaria.md` v1.1.0 | Metadados, glossário, dicionário, fórmulas, §§ 6–17 e RMO selecionadas lidos; catálogo amostrado | Confronto crítico (Documento B). |
| `docs/dominio/auditoria-complementar-matriz-orcamentaria.md` | Resumo e quadro de lacunas lidos | Ponto de partida, não conclusão. |
| `tests/auditoria_matriz/*`, `resultado-validacao.json`, `manifesto.json` | Lidos | Verificação de consistência relatório × evidências. |
| Planilha B (6ª fase Ifes 2026) | Reprocessada independentemente (2.322 ciclos) | Teste da regra de MT e composição por campus. |
| N2 — Portaria 646/2022, republicação | Texto extraído; p. 124 renderizada e lida visualmente | Cadeia MT, faixas de qualidade, L-23. |
| C5 — demonstrativo IFMT PLOA 2026 | Abas Ciclos, Cálculo Custeio, Custeio, Geral e **Indicadores** reprocessadas | Teste fora da amostra; posição do Ifes nas faixas de qualidade; MOOC. |
| N3 — Portaria MEC 243/2026 | **Obtida via usuário** em 09/11/2026 (impressão web do DOU de 12/03/2026), lida integralmente | Confirma faixas e blocos; MOOC 8%; ver Documento B § 0. |
| Livro A, Decreto 7.313/2010 | Não relidos integralmente; usados via fonte canônica | Sem nova conclusão própria. |
| Dissertação UFES (Matriz IPP), PDI, dados de Ifes Ads/GPS/eLabi/Trajetória, inventários físicos e docentes | **Não disponíveis no repositório** | Ausência registrada; nada inferido sobre seu conteúdo. |

---

## 3. Avaliação crítica da concepção atual

### 3.1. O que está certo e deve ser preservado

- **[REGISTRADO → confirmado como correto]** Separar observado, projetado e decidido; não converter matrícula em receita garantida; versionar regras por exercício; não reduzir a estratégia a orçamento. Os achados desta revisão reforçam cada um desses princípios.
- **[REGISTRADO → confirmado]** A governança distribuída como núcleo. Os achados do bloco de Qualidade dão a ela um **conteúdo quantitativo** que antes faltava.
- **[REGISTRADO → confirmado]** Agregar indicadores pela razão das somas, e não pela média de percentuais (§ 13.3 do contexto). Isso é crítico: %CT, RAP e IEA são razões institucionais.

### 3.2. Erros ou riscos de enquadramento identificados

| Questionamento proposto pela missão | Veredito | Fundamentação |
|---|---|---|
| Confundimos projeção de indicadores com apoio à decisão? | **Parcialmente.** | O contexto lista perguntas decisórias boas (§ 6), mas o trabalho executado (65 RMO, 19 testes) produziu um **calculador de Funcionamento**. Nenhum artefato liga uma decisão concreta a um degrau institucional, a uma meta ou a um compromisso de campus. |
| Priorizamos cálculo antes de entender as decisões? | **Sim.** | A Fase 0 do contexto previa entrevistas e a escolha de uma decisão real. Não há registro de que tenham ocorrido. A auditoria avançou sem saber se o Funcionamento é a parte decisiva. Esta revisão mostra que, para o Ifes em 2026, os degraus de Qualidade podem ter efeito marginal maior que expansões de oferta. |
| Modelamos a instituição como soma de campi? | **Risco real.** | O Funcionamento é aditivo por campus. Qualidade (IEA, RAP, CT, FP, EJA), Reitoria e piso **não são**: são razões institucionais com degraus, e a contribuição de um campus depende do que os outros fazem. Um modelo "soma de campi" erra justamente onde está o valor. |
| Consideramos só o efeito financeiro? | **Na prática, sim.** | Embora o discurso inclua valor público, nenhum indicador educacional (conclusão, evasão, cumprimento legal, EJA) foi modelado. Os degraus de Qualidade mostram que **missão legal e orçamento estão alinhados**, um argumento forte contra a falsa dicotomia "missão × matriz". |
| Simulador sofisticado sem mecanismo de decisão acompanhada? | **Sim, por enquanto.** | Não há modelo de compromisso, meta, responsável ou acompanhamento. É barato introduzi-lo agora: um registro leve de pacto, como na § 12. |

### 3.3. Uma mudança de leitura sobre o Funcionamento

[INFERÊNCIA a partir da regra reproduzida] A MT é, essencialmente, **aluno-hora ponderada no ano civil de referência**. Disso decorrem propriedades úteis para o gestor e ausentes dos documentos:

- **Linearidade em horas.** Ampliar a carga horária efetivamente ofertada, ou ofertar no início do ano em vez do fim, altera a MT do ano-base. Um curso que inicia em agosto contribui com cerca de 5/12 do ano.
- **A evasão afeta os anos seguintes, não o ano corrente.** A MT conta matrículas *ativas no período* por ciclo, sem rateio por dias individuais. A perda aparece no ano-base seguinte e, com a defasagem de dois anos observada em 2026, no exercício orçamentário três anos depois da decisão. [A confirmar: definição PNP de "matrícula ativa no período".]
- **A retenção ainda conta pouco.** O retido após o fim previsto do ciclo vale ¼ por até 3 anos (½ dos dias × ½ do fator); o FIC retido vale zero.
- **O preço é igual para todos.** Logo, a contribuição relativa entre campi no Funcionamento independe do montante. O que muda a posição do Ifes na Rede é o seu volume ponderado *relativo* ao das demais instituições.

Essas propriedades tornam o Funcionamento **explicável em uma frase** e **estimável com planilha simples** a partir de coortes. Não justificam um motor sofisticado.

---

## 4. Problemas institucionais e decisões prioritárias

### 4.1. Problema institucional central (reformulado)

> O Ifes precisa cumprir metas institucionais (legais, educacionais e orçamentárias) que **só existem no agregado**, mas cujas alavancas estão **distribuídas** entre campi com vocações, capacidades e restrições diferentes. Hoje não há um instrumento que mostre a cada campus como sua escolha altera o agregado, nem que permita pactuar contribuições diferentes e acompanhá-las.

A versão anterior ("decidir ofertas com informação insuficiente") é verdadeira, mas é um sintoma. O problema estrutural é de **coordenação**.

### 4.2. Usuários e decisões (priorizados)

| Decisor | Decisão de maior consequência | Hoje decide com... | O que é difícil antecipar |
|---|---|---|---|
| Reitoria / Prodi / Proen | Metas institucionais anuais e plurianuais; priorização de expansão; pactuação com campi | Séries PNP, PDI, negociação política | Qual combinação de contribuições cruza um limiar (CT 50%, RAP 20) e **quando**, dado o atraso de dois anos entre ano-base e exercício |
| Direção-geral de campus | Abrir, ampliar, reconfigurar ou suspender ofertas; alocar docentes e espaços | Conhecimento local, demanda percebida, colegiado | Efeito de sua escolha no agregado institucional; gargalos futuros de coorte; trade-off entre volume (MT) e composição (%CT, RAP) |
| Proen / coordenações | Desenho de PPC, carga horária, turnos, permanência | PPC, normas, histórico | Como evasão e retenção afetam IEA e MT em quais anos |
| Pró-reitoria de Administração / orçamento | Regra de distribuição interna; reservas; complementações | Matriz nacional, regra interna (não obtida) | Se a regra interna reproduz ou neutraliza os incentivos da matriz nacional |
| Gestão de pessoas | Vagas docentes, remoções, códigos de vaga | Banco de professor-equivalente | Efeito de cada contratação ou remoção na RAP institucional, perto do degrau de 18 |

### 4.3. Decisões tomadas hoje com informação insuficiente [HIPÓTESE, a validar em entrevistas]

1. Expansões de FIC, MOOC e EAD sem medir o efeito nos percentuais legais e na RAP.
2. Contratação de docentes sem medir o efeito na RAP, que está a 0,8% do degrau zero.
3. Metas iguais para todos os campi, apesar de vocações muito distintas: participação técnica estimada entre 15% (Viana) e 85% (Montanha).
4. Abertura de ofertas no meio do ano sem considerar a contribuição parcial do ano-base.
5. Ações de permanência avaliadas sem o efeito no IEA. O Ifes está a cerca de 1,7 p.p. de eficiência acadêmica do degrau seguinte (peso 1,5 → 2,0; cerca de +R$ 0,51 mi) e cerca de 2,9 p.p. acima da média da Rede; cair abaixo dela custaria cerca de R$ 0,5 mi.

---

## 5. Oportunidades de alto valor ainda não exploradas

Cada oportunidade abaixo é **não prevista explicitamente** nos documentos atuais, ou prevista sem a fundamentação que a torna prioritária.

### O1 — Gestão de limiares institucionais ("mapa de degraus")

- **Problema:** indicadores institucionais com faixas descontínuas (IEA relativo à média; RAP 18/20/22; CT 50/60%; FP 10/15/20%; EJA 2,5/5/10%) determinam 10% do remanescente nacional (R$ 220,6 mi), e o Ifes está em posição desfavorável em três deles.
- **Decisão melhorada:** quais metas institucionais perseguir, com que prazo e com qual contribuição de cada campus.
- **Beneficiados:** Reitoria, Prodi, Proen e, indiretamente, os estudantes (as metas coincidem com mandatos legais).
- **Por que é valor substancial:** [INFERÊNCIA] +R$ 2,06 a 4,76 mi/ano (CT), +R$ 0,31 a 1,15 mi (EJA), +R$ 0,85 mi (RAP 20), proteção contra −R$ 0,73 mi (RAP < 18). E, sobretudo, conformidade legal.
- **Dados e regras:** indicadores PNP por instituição (já em C5 para 2026); definição de matrícula equivalente para percentuais legais (**ausente**, ver Documento B); faixas de N2/N3.
- **Dependências:** conciliar a definição de %ME. As faixas foram confirmadas, sem alteração, pela Portaria 243/2026.
- **Riscos:** os degraus são relativos à Rede (o valor depende dos demais); N3 pode ter alterado faixas; risco de gaming (ex.: reclassificar cursos).
- **Validação de baixo custo:** reproduzir %CT, %FP, %EJA e RAP do Ifes a partir dos microdados públicos da PNP, por campus; apresentar o mapa de degraus a três gestores e observar se muda alguma decisão em discussão.

### O2 — Pacto de contribuições diferenciadas para uma meta agregada

- **Problema:** metas uniformes são injustas e ineficientes; metas diferenciadas sem instrumento são opacas e pouco legítimas.
- **Decisão:** quanto cada campus contribui para %CT ≥ 50% (ou outra meta), em que horizonte e com quais recursos.
- **Por que é valor:** materializa a tese central do Prumo com um caso real, legalmente fundamentado e economicamente relevante.
- **Dados:** composição do portfólio por campus (B permite uma *proxy*; PNP permite o dado oficial), capacidade docente agregada, coortes previstas.
- **Regras:** agregação por soma de numeradores e denominadores; calendário ano-base → exercício; regras de faixas.
- **Riscos:** conflito político; campi com vocação não técnica podem se sentir penalizados. O pacto deve permitir **compensações** (ex.: um campus contribui com FP ou EJA, outro com CT).
- **Validação:** oficina de 2 horas com 3 a 4 diretores usando planilha, antes de qualquer software.

### O3 — Unidade "aluno-hora ponderada" como linguagem comum

- **Problema:** gestores não entendem a matriz; a fonte canônica tem 236 KB.
- **Decisão:** comparar alternativas de oferta numa unidade compreensível: aluno-hora no ano civil × peso.
- **Valor:** explicabilidade imediata; permite estimativas manuais; desmonta mitos ("especialização vale mais", "FIC não vale nada", "evadido some no mesmo ano").
- **Dados e regras:** a regra operacional de MT reproduzida (Documento B, RO-MT).
- **Risco:** simplificação pode ocultar a dependência relativa da Rede e os degraus. Sempre exibir junto do aviso de relatividade.
- **Validação:** testar a explicação com cinco gestores; medir se conseguem estimar o efeito de uma decisão hipotética.

### O4 — Sentinela de RAP (vagas docentes × matrículas equivalentes)

- **Problema:** a RAP do Ifes (18,15) está a 224 MEq presenciais (0,8%) ou a cerca de 12 professores-equivalentes do degrau que zera R$ 0,73 mi/ano. Também está a cerca de 2.811 MEq ou 140 professores-equivalentes do degrau que dobra o peso.
- **Decisão:** provimento e remoção de docentes; ritmo de expansão; redistribuição de vagas docentes entre campi.
- **Valor:** é uma decisão frequente, distribuída e hoje tomada sem ver o agregado. [HIPÓTESE] Pode ser a decisão com maior frequência × consequência.
- **Dados:** professor-equivalente por campus (PNP), MEq presenciais por campus.
- **Riscos:** incentivo perverso a não contratar ou a superlotar turmas. Exige guarda-corpos de qualidade, como em O8.
- **Validação:** reconstruir a RAP por campus a partir da PNP; verificar com a gestão de pessoas quantas decisões de provimento por ano poderiam mudá-la.

### O5 — Calendário de efeitos (decisão → ano-base → exercício)

- **Problema:** efeitos chegam com dois a três anos de atraso e em exercícios regidos por normas possivelmente diferentes.
- **Decisão:** escolher o momento de início de ofertas (fevereiro × agosto), antecipar compromissos, planejar transições.
- **Valor:** evita frustração ("ampliamos e o orçamento não subiu") e permite planejar a trajetória até um degrau.
- **Dados:** datas de ciclo; regra de defasagem por exercício (2024 → 2026 observado).
- **Validação:** linha do tempo de um caso real passado (ex.: curso aberto em 2022) confrontada com as matrizes 2024 a 2026.

### O6 — Aprendizado previsto × observado com a própria matriz

- **Problema:** não há ciclo de calibração.
- **Valor:** a matriz é publicada anualmente com dados por ciclo. É um **dado observado gratuito** para calibrar premissas de ocupação, evasão e retenção por tipo de curso e campus.
- **Validação:** usar matrizes de anos consecutivos (2025 → 2026) para medir quanto a MT de cada ciclo variou e por quê.

### O7 — Diagnóstico de conformidade entre a planilha do Ifes e a regra nacional

- **Problema:** a planilha B monetiza o EAD externo a 6,25% e o MOOC a zero. O demonstrativo nacional do IFMT para o mesmo exercício usa 25% e 80% (este fora do bolo F, prática anterior à Portaria 243). A Portaria 243 fixa 25% e 8%. Recalculado com as matrículas de B sob a Portaria 243, o Funcionamento do Ifes seria R$ 63,87 a 63,95 mi, contra R$ 62,78 mi em B (+R$ 1,09 a 1,17 mi). Quase todo o efeito vem do EAD externo; a MOOC a 8% vale cerca de R$ 72 mil.
- **Decisão:** se a área de orçamento do Ifes usa B para distribuição interna ou análise, a contribuição de campi com EAD (Viana e outros) está subestimada.
- **Valor:** imediato e de baixo custo; é verificação, não produto.
- **Validação:** perguntar à área responsável qual a origem e o uso de B.

### O8 — Guarda-corpos contra gaming de métricas

- **Problema:** o produto pode ensinar a "ganhar a matriz": MOOC massivo, FIC curto de 20 h, reclassificação de cursos, turmas superlotadas para elevar a RAP.
- **Valor:** protege missão e reputação; é condição de legitimidade do produto.
- **Mecanismo:** cada cenário mostra, ao lado do ganho orçamentário, indicadores de resultado educacional (conclusão, evasão, relação com demanda), e sinaliza quando o ganho vem só de volume de baixa carga.
- **Validação:** revisão por pares de Proen e CPA; checklist de "efeitos colaterais" em cada cenário.

---

## 6. Relações causais e dependências relevantes

### 6.1. Cadeias verificadas, prospectivas e a pesquisar

| Cadeia | Fundamento | Classificação |
|---|---|---|
| Ciclo (datas, CH, peso, QTM) → MT | Reproduzida em 3.408 ciclos (B + C5) | **Verificável e determinística** |
| MT → valor de Funcionamento | Preço comum × MT; fechamento nacional em C5 | **Verificável** (por exercício) |
| Indicadores institucionais → faixas → participação em QE | N2 + C5 2026 (todas as instituições) | **Verificável** para 2026; faixas mantidas pela Portaria 243 |
| Vagas → ingressantes | Sem regra normativa; depende de demanda | **Prospectiva** (taxa de ocupação histórica por curso) |
| Ingressantes → ativos → concluintes/evadidos/retidos | Dados acadêmicos | **Prospectiva** (coortes) |
| Concluintes/evadidos → IEA | C5 mostra IEA = conclusão ÷ (conclusão + evasão) nos ciclos encerrados | **Verificável** na fórmula; dados PNP |
| Portfólio por campus → %CT/%FP/%EJA institucional | Depende da definição de matrícula equivalente da PNP | **A pesquisar** (definição ausente) |
| Docentes e MEq presenciais → RAP | PNP | **Verificável** na fórmula; dados por campus a obter |
| Participação nacional → orçamento do campus | Regra interna do Ifes ausente; IFMT distribui por matriz | **A pesquisar** |
| Oferta → resultados territoriais e egressos | Trajetória, dados externos | **A pesquisar**; janela longa |

### 6.2. Interpretações causais equivocadas que o produto precisa impedir

| Erro | Por que é erro aqui | Proteção |
|---|---|---|
| "Mais matrículas, mais orçamento" | Funcionamento é relativo à Rede; QE pode **cair** se o volume diluir %CT ou RAP | Exibir sempre efeito relativo e efeito nos degraus |
| "Mais vagas, mais ingressantes" | Sem regra; depende de demanda | Ocupação é premissa explícita por cenário |
| "Evasão reduz a matriz do mesmo ano" | Ativo no período conta [a confirmar] | Linha do tempo por ano-base |
| "Melhorar um pouco o indicador gera ganho proporcional" | Faixas são degraus; ganho é zero até o limiar e depois salta | Visualizar distância ao degrau, não "ganho por ponto" |
| "Participação do campus na matriz = orçamento do campus" | Regra interna desconhecida | Separar níveis (nacional, Ifes, campus) |
| "Especialização sempre vale mais que FIC" | Vale por hora e peso; um FIC presencial de 160 h com 30 alunos ≈ R$ 7,3 mil; o peso da especialização depende do cadastro | Comparar em aluno-hora ponderada |
| "MOOC não vale nada" / "MOOC vale muito" | Em B vale zero; em C5 (2026, pré-Portaria 243), 80% fora do bolo; pela Portaria 243, 8% | Tratar como regra versionada por exercício; para 2027+, 8% |
| "Ganhar a média da Rede é suficiente" | IEA é relativo: se a Rede melhora, a faixa muda | Mostrar a posição relativa e sua estabilidade |

### 6.3. Dimensão temporal: granularidade recomendada

[INFERÊNCIA] A regra de MT usa **datas** e a interseção do ciclo com o **ano civil**. O semestre não é a unidade natural. Recomendação:

- **Unidade de cálculo:** ciclo de oferta (coorte de ingresso) × ano civil, com datas de início e fim previstas.
- **Unidade de exibição:** ano de decisão → ano-base → exercício.
- **Infraestrutura e docentes:** turno × semestre letivo (unidade diferente, legitimamente). Não forçar uma unidade única.
- **Estados de coorte:** ingressantes, ativos, concluintes, evadidos, retidos (até 3 anos; FIC zero).

---

## 7. Lacunas de domínio e dados

| Lacuna | Impacto | Como fechar | Custo |
|---|---|---|---|
| ~~Portaria 243/2026~~ obtida; resta saber se a prática de 2026 (MT por fração do ciclo, 0,5×IEA) continuará em 2027, já que o texto da Portaria não a prevê | Precisão das projeções de MT e IEA para 2027+ | Memória de cálculo da matriz 2027 junto à Setec | Baixo |
| Definição de %ME dos percentuais legais e da RAP (PNP) | Bloqueia a oportunidade O1/O2 | Portaria Setec 146/2021 + documentação PNP + microdados; reproduzir os 44% do Ifes | Baixo a médio |
| Regra interna de distribuição do Ifes | Bloqueia qualquer efeito por campus em R$ | Pedido à Proad/Prodi | Baixo |
| Código de campus vazio em B; ausência de chave de curso nacional | Integração e histórico | Usar códigos SISTEC/PNP de unidade e ciclo | Baixo |
| Histórico de ocupação de vagas, evasão e conclusão por curso e campus | Projeção de coortes | PNP (pública) + qAcadêmico agregado | Médio |
| Professor-equivalente por campus e área | O4 e capacidade | PNP + gestão de pessoas | Médio |
| Inventário de salas e laboratórios por turno | Viabilidade física | Cadastro progressivo, **só** para campi do piloto | Médio a alto; adiar |
| Demanda territorial | Valor público | Ifes Ads/GPS: inscritos/vaga por curso | Médio |

**Minimização:** todo o núcleo recomendado funciona com **agregados por ciclo e por campus**. Não há necessidade de dados pessoais na primeira fase.

---

## 8. Riscos estratégicos

1. **Otimização local contra o coletivo** (descrito no § 1). É o risco nº 1.
2. **Divergência entre texto normativo e prática.** A Portaria 243 (vigente) repete fórmulas de MT e IEA que a Setec não seguiu em 2026. Além disso, seu novo art. 7º (manter o referencial anterior + IPCA) pode amortecer ganhos e perdas marginais, se aplicado por instituição. Mitigar com regras versionadas por exercício, variante "texto" × "prática", e confirmação junto à Setec.
3. **Precisão ilusória em reais.** Os ganhos de Qualidade são relativos e mudam com a Rede. Apresentar como faixas e "mantidos os demais".
4. **Legitimidade política do pacto.** Metas diferenciadas podem ser percebidas como imposição. Mitigar com compensações entre indicadores e com o registro de justificativas.
5. **Escopo físico e docente prematuro.** O cadastro de salas e laboratórios por turno é caro e só limita algumas decisões. Fazer sob demanda do piloto.
6. **Gaming e reputação.** Ver O8.
7. **Investimento continuado em reprodução forense.** A MT está resolvida para 2026; o restante (renda, RIP, fechamento nacional) tem baixo valor decisório para campi.
8. **Sustentabilidade de dados.** Sem dono institucional para atualização anual (PNP, matriz, regra interna), o produto envelhece em um ciclo.

---

## 9. Oportunidades que não justificam investimento imediato

| Capacidade | Por que adiar ou eliminar |
|---|---|
| Reproduzir integralmente Assistência Estudantil (renda, RIP, IDH) | Não é alavanca de decisão de oferta dos campi; depende de microdados de renda; montantes próprios. Exibir como valor observado. |
| Fechamento nacional da matriz e reconstrução de todas as instituições | Útil para a Setec, não para o Ifes; a C5 já fornece bases e índices nacionais por exercício. |
| Otimização automática de portfólio (programação matemática) | Sem dados de demanda e custo confiáveis, otimiza premissas. Começar com comparação de 3 a 4 alternativas e com a "distância ao degrau". |
| Grade horária e alocação fina de salas | Já excluído no contexto; manter excluído. Só a verificação de pico de turmas por turno × semestre no piloto. |
| IA generativa no núcleo | Nenhum problema identificado que a exija. Possível uso futuro: explicar cenários em linguagem natural a partir de cálculos determinísticos. |
| Integrações com eLabi, Trajetória e AVA | Valor real só no ciclo de aprendizado (Fase 4). Agora, usar indicadores agregados públicos. |
| Simular PLOA → LOA → execução | Depende de decisões externas; mostrar apenas a referência condicionada. |
| Painéis genéricos de indicadores | Sem decisão associada; a PNP já os fornece. |

---

## 10. Cinco oportunidades de maior potencial

1. **O1 + O2 — Mapa de degraus e pacto de contribuições diferenciadas.** É a única capacidade que, ao mesmo tempo, materializa a tese central (governança distribuída), tem valor financeiro demonstrado (milhões de reais por ano), coincide com mandatos legais e pode ser validada em semanas, com dados públicos.
2. **Motor de coortes simples com saída em aluno-hora ponderada (O3 + O5).** Base para tudo: projeta MT, %ME, concluintes e RAP com a mesma estrutura, e explica o "quando".
3. **Sentinela de RAP (O4).** Decisão frequente, distribuída e com risco iminente identificado (degrau zero a 0,8%).
4. **Registro leve de premissas, propostas e compromissos.** Sem ele, simulação não vira decisão acompanhada. Pode começar como estrutura de dados simples (proposta → parecer → decisão → meta por campus → observado).
5. **Ciclo previsto × observado com matrizes anuais (O6).** Transforma a publicação anual da matriz em mecanismo de calibração e aprendizado institucional.

---

## 11. Avaliação do posicionamento da Matriz Orçamentária

- **Continua um bom ponto de entrada quantitativo?** Sim, mas **pelo bloco errado**. O Funcionamento é aditivo, quase linear e de baixa alavancagem para coordenação. O bloco de Qualidade e Eficiência é onde decisões locais combinadas mudam resultados de forma não linear. Ele deve ser o ponto de entrada da governança.
- **Há capacidades complementares de maior valor com menor esforço?** Sim: mapa de degraus (dados públicos, cálculo simples) e sentinela de RAP.
- **O detalhamento perseguido é proporcional?** Não. A fonte canônica tem 65 RMO, 20 delas sobre comportamentos operacionais de uma planilha (filtros, SUBTOTAL, linhas ocultas, coluna "Custo Evadido"), úteis à auditoria e irrelevantes ao produto. Ao mesmo tempo, faltavam a regra de produção da MT (agora encontrada), a definição de %ME e a economia dos degraus. Recomenda-se **congelar** a auditoria de B e direcionar o esforço às lacunas que bloqueiam decisões.

---

## 12. Recomendações de evolução do produto

1. **[RECOMENDAÇÃO] Reformular o primeiro caso de uso** em `proposta_nome_prumo.md` § 5: de "simulação de ofertas e efeitos na Matriz CONIF" para "pactuação de metas institucionais com degraus, apoiada por simulação de coortes e da matriz".
2. **Introduzir desde já cinco entidades de governança**, mesmo sem fluxo de aprovação: `MetaInstitucional` (indicador, limiar, horizonte), `ContribuicaoCampus` (proposta, justificativa, recursos), `Cenario`, `Premissa` e `Compromisso` (situação, responsável, observado). Elas valem mais que o detalhamento físico.
3. **Separar três motores** com interfaces claras: (a) **coortes** (vagas → ativos → concluintes, por ciclo × ano civil); (b) **regras de matriz versionadas** (MT, faixas, preços, por exercício); (c) **consolidação** (razão das somas, degraus, relatividade à Rede). A matriz é consumidora das coortes, não o contrário.
4. **Tratar a Rede como dado observado por exercício** (C5 traz bases e índices de todas as instituições) e cenários "demais constantes" e "tendência", em vez de reconstruir a Rede.
5. **Adotar o aluno-hora ponderada** como unidade de comunicação, sempre acompanhada do aviso de relatividade.
6. **Guarda-corpos de missão** em toda saída (O8).
7. **Governança de dados mínima:** um responsável anual por PNP, matriz e regra interna; um "pacote do exercício" versionado.
8. **Interromper** novas rodadas de auditoria da planilha B. Concentrar-se em N3, na definição de %ME e na regra interna.

---

## 13. Proposta de primeira demonstração de valor

**"Ifes 50% técnico: quem contribui com quê, e quando chegamos lá?"**

**Pergunta do gestor (Reitoria, Proen e Prodi):** o Ifes está em 44% de matrículas equivalentes em cursos técnicos, abaixo do mínimo legal de 50% e do degrau que hoje lhe dá R$ 0 de R$ 77 mi da Rede. Qual combinação de contribuições dos campi nos leva a 50% (e a 60%), em que ano-base, com que custo docente, e o que acontece com a RAP e o IEA no caminho?

**Dados plausíveis e disponíveis:**

- Indicadores institucionais 2026 de todas as instituições (C5, aba Indicadores). Disponível.
- Composição por campus. Proxy disponível em B; dado oficial nos microdados PNP, a obter e conciliar primeiro.
- Ciclos com datas e carga (B), para projetar a MT de alternativas com a regra reproduzida.
- Professor-equivalente por campus (PNP). A obter.

**Roteiro (executável em planilha antes de software):**

1. **Passo 0 — conciliação.** Reproduzir os 44% do Ifes a partir da PNP. Se não reproduzir, a demonstração para aqui e a lacuna vira prioridade.
2. Mostrar o **mapa de degraus** do Ifes: posição, distância e valor condicional de cada degrau (CT, FP, EJA, RAP, IEA).
3. Mostrar a **composição técnica por campus**. Proxy B: Viana 15%, Serra 38%, Vila Velha 43%, Vitória 54%, campi agrícolas 70–85%.
4. Simular **três pactos alternativos:**
   - (A) **Uniforme:** todos +6 p.p.
   - (B) **Por vocação:** campi com capacidade técnica ociosa ampliam integrados; campi superiores convertem parte de FIC em técnico concomitante ou subsequente.
   - (C) **Combinado:** CT + PROEJA, porque o degrau EJA 2,5% é próximo e soma +R$ 0,31 mi.
5. Para cada pacto: ano-base e exercício do cruzamento; efeito na RAP (risco do degrau 18); docentes adicionais por área; efeito no Funcionamento relativo; indicadores de missão (matrículas técnicas integradas, EJA).
6. **Registrar o pacto escolhido como compromissos por campus** e definir o indicador a acompanhar no ano-base seguinte.

**Critério de sucesso:** os gestores identificam ao menos uma decisão em curso que mudariam, ou uma meta que pactuariam de outra forma, após ver o mapa.

**O que esta demonstração não exige:** inventário físico, Assistência Estudantil, regra interna e integração com sistemas. As faixas usadas são as da Portaria 243/2026, idênticas às de 2026.

---

## 14. Questões que exigem descoberta com gestores

1. Quem é o patrocinador com autoridade sobre metas institucionais pactuadas: Reitoria, Prodi, Proen ou o Colégio de Dirigentes?
2. O Ifes conhece e acompanha sua posição nas faixas de Qualidade? Houve debate sobre os 44% técnicos e os 1,86% de PROEJA?
3. Qual é a regra interna de distribuição de custeio entre campi? Ela reproduz a matriz por campus, como no IFMT, ou usa outro critério?
4. Qual é a origem e o uso da planilha "6ª Fase"? Ela é usada em decisões internas? Os valores de EAD externo (6,25%) e MOOC (zero) foram questionados?
5. Quais decisões de oferta estão em discussão para 2027 e 2028 que poderiam compor o piloto?
6. Como se decidem hoje vagas docentes entre campi? O efeito na RAP é considerado?
7. Os campi aceitariam metas diferenciadas com compensação entre indicadores (CT × FP × EJA)?
8. Há política institucional sobre MOOC e FIC curtos em relação à matriz? Há temor de gaming?
9. Que indicadores de valor público os gestores consideram inegociáveis ao lado do orçamento?
10. Quem manteria anualmente o "pacote do exercício" (PNP, matriz, regras e regra interna)?

---

## 15. Respostas às questões finais obrigatórias

**Q1 — Maior oportunidade não explorada.** A gestão coordenada dos **degraus institucionais do bloco de Qualidade e Eficiência** como metas pactuadas entre campi. O Ifes recebe R$ 0 em CT e EJA e está a 0,8% de perder a RAP. Cruzar CT 50% vale cerca de +R$ 2,06 mi/ano, e a meta coincide com o mandato legal (§§ 1, 5 O1/O2; Documento B § 6, RMO-P04).

**Q2 — Maior risco de concepção.** Construir um simulador de Funcionamento por campus que incentive volume de MT (FIC curto, MOOC, EAD barata) e, com isso, **dilua os indicadores institucionais** de maior alavancagem: otimização local contra o coletivo, embutida no produto (§§ 1, 3.2, 8).

**Q3 — Superestimamos a reprodução integral da matriz?** Sim. A MT está reproduzida para 2026 com uma regra de cinco linhas (Documento B § 5.1). Assistência, RIP e fechamento nacional têm baixo valor decisório para os campi. O que falta para entregar valor não é precisão: é a definição de %ME, a regra interna e a confirmação da prática de cálculo de 2027 sob a Portaria 243, já obtida (§ 11).

**Q4 — As regras extraídas estão adequadas para implementação?** São rastreáveis e honestas sobre limites, mas: (a) a regra central de MT documentada como NORMATIVA (RMO-061) **não** é a regra efetivamente aplicada; (b) a mistura de observações de planilha com regras de negócio dificulta o uso; (c) faltam regras de maior impacto decisório; (d) a densidade e o estilo telegráfico prejudicam a implementação por terceiros (Documento B §§ 2, 5, 14).

**Q5 — Regras ou mecanismos não identificados.** Regra operacional de produção da MT (curtos por fração do ciclo; min(CHC, CHM); limiar de 365 dias; jubilamento FIC), que diverge do texto tanto da Portaria 646 quanto da 243; MOOC a 8% pela Portaria 243 (a 80% fora do bolo F na prática pré-243 de C5); bolo F de B idêntico ao de C5 (o rótulo "2025" é obsoleto); aplicação de 0,5×IEA em 2026 (resolve L-23 operacionalmente); economia dos degraus de Qualidade; IEA = conclusão ÷ (conclusão + evasão); ausência da definição de %ME (Documento B § 6).

**Q6 — Primeira decisão a apoiar.** A pactuação de contribuições dos campi para levar o Ifes a 50% de matrículas equivalentes técnicas (e a proteger a RAP), com a matriz como uma das consequências medidas (§ 13).

**Q7 — Cinco capacidades prioritárias.** (1) Mapa de degraus + pacto diferenciado; (2) motor de coortes em aluno-hora ponderada com calendário de efeitos; (3) sentinela de RAP; (4) registro de premissas e compromissos; (5) ciclo previsto × observado com matrizes anuais (§ 10).

**Q8 — O que simplificar, adiar ou eliminar.** Eliminar a continuação da auditoria forense da planilha B. Adiar Assistência, renda e RIP, o fechamento nacional, o inventário físico detalhado, a otimização automática, a IA no núcleo e as integrações transacionais. Simplificar a fonte canônica numa camada de "regras implementáveis" separada do dossiê de auditoria (§ 9; Documento B § 12).

**Q9 — Como representar contribuições diferenciadas sem reduzir tudo a finanças.** A meta é um **indicador institucional com limiar** (ex.: %CT ≥ 50%), que é simultaneamente legal, educacional e orçamentário. Cada campus contribui com **variações de numerador e denominador** dessa razão, e não com reais. O valor orçamentário aparece como consequência condicional, ao lado de indicadores de missão e de compensações entre metas (CT, FP, EJA, IEA). Assim, o campus com vocação superior contribui via FP ou IEA, e o agrícola via CT, sem metas uniformes (§§ 5 O2, 13).

**Q10 — Caminho de evolução recomendado.**

1. **Semanas 1–4:** obter a definição de %ME com reprodução dos 44%, a regra interna e a memória de cálculo da matriz 2027 (Setec); entrevistar os decisores das questões do § 14.
2. **Semanas 4–8:** demonstração em planilha "Ifes 50% técnico" com 3 a 4 campi.
3. Se validada, construir o mínimo de software: motor de coortes, regras versionadas da matriz 2026, consolidação por razão das somas e registro de compromissos.
4. Só então adicionar a capacidade docente por área e a infraestrutura dos campi do piloto.
5. Fechar o ciclo com a matriz do ano seguinte como dado observado.

---

*Fontes externas consultadas nesta revisão:* tentativa de acesso ao [DOU — Portaria MEC nº 243/2026](https://www.in.gov.br/web/dou/-/portaria-mec-n-243-de-10-de-marco-de-2026-692098706), sem sucesso (conexão encerrada); busca ampliada sem resultado pertinente, entre eles a [lista de portarias 2026 do MGI](https://www.gov.br/gestao/pt-br/acesso-a-informacao/institucional/atos-normativos/2026/2026-portarias), não relacionada ao tema. Demais evidências: arquivos do repositório citados no § 2.
