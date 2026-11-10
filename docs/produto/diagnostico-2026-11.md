# PRUMO — Diagnóstico do estado atual (10/11/2026)

> **Atualização de 10/11/2026:** depois deste diagnóstico, o idealizador decidiu não fazer sessões com gestores agora e seguir para a estruturação da solução. Ver [próximo passo](proximo-passo.md). As menções abaixo a "próximo experimento" refletem a recomendação original. As duas pendências técnicas apontadas nos §§ 3 e 4.2 (tratamento numérico do extrator da POC 0.0.2 e rótulo de versão da fonte canônica) foram resolvidas no mesmo dia, sem alterar nenhum resultado.
> **Integração:** os PRs #1 e #2 foram integrados à `main` em 10/11/2026, depois deste diagnóstico. As marcas "(PR #1)" e "(PR #2)" e o § 1.1 descrevem a situação anterior.
> **Natureza:** retrato do repositório e da evolução do projeto em 10/11/2026, feito para fundamentar a [visão de produto](visao-prumo.md). É um registro datado: não será mantido em dia. Nenhum protótipo, motor de cálculo ou dado foi alterado nesta atividade.
> **Método:** leitura do histórico do Git, das três branches, dos dois pull requests abertos, dos documentos de concepção e de análise, e do código dos três protótipos. Os documentos de domínio foram lidos por amostragem dirigida (sumário, versões, lacunas, regras de produto). Os testes dos motores de coortes foram executados; os testes de auditoria da matriz não, porque dependem de arquivos locais não versionados.

Referências a arquivos que só existem em pull request aberto apontam para a branch no GitHub e estão marcadas com **(PR #1)** ou **(PR #2)**.

---

## 1. Inventário

### 1.1. Onde está cada coisa

| Local | Conteúdo | Situação |
|---|---|---|
| `main` (commit `7931c60`, 09/11) | Documentos de concepção, domínio da matriz, três análises, protótipos v2 e recomposição | Integrado |
| Branch `claude/prumo-pnp-exploratory-audit-aff2d0`, [PR #1](https://github.com/saymoncastro/prumo/pull/1) | Estudo da PNP, script de reprodução e saída (3 arquivos, só documentos) | **Aberto, fora da `main`** |
| Branch `claude/prumo-poc-002`, [PR #2](https://github.com/saymoncastro/prumo/pull/2) | POC 0.0.2: página, motor, extrator, testes, documento e capturas (13 arquivos; altera `poc/montar.py`) | **Aberto, fora da `main`** |
| Pasta local `indicadores-gestao/` (93 MB) | Exportação dos Indicadores de Gestão da PNP, 2017–2025, todas as instituições | Não versionada; existe só no diretório principal |
| Raiz local | Planilha da matriz do Ifes (6ª fase) e livro da matriz | Não versionados, por não serem públicos |
| `tests/auditoria_matriz/*.json` locais | Casos de referência derivados da planilha | Não versionados |

Não havia alterações não commitadas em nenhum dos três diretórios de trabalho.

### 1.2. Documentos por função

| Função | Documento | Estado |
|---|---|---|
| **Visão** | [Documento fundador v1.1](../../contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md) (08/11) | Origem dos princípios. Escopo ampliado pela visão de 10/11 |
| | [Proposta de nome](../../proposta_nome_prumo.md) (08/11) | Nome provisório, não oficializado. O § 5 (primeiro caso de uso) está superado |
| | [Revisão estratégica e oportunidades](../analises/prumo-revisao-estrategica-oportunidades.md) (09/11) | Análise válida. A recomendação de reposicionar o produto em torno do "pacto de degraus" foi um episódio, não a visão vigente |
| **Domínio** | [Fonte canônica da matriz](../dominio/matriz-orcamentaria.md) v1.2.2 | Vigente. 75 regras, 28 lacunas |
| | [Revisão crítica das regras](../dominio/revisao-critica-regras-prumo.md) | Vigente. É o documento de domínio mais orientado a produto (regras RPE-01 a RPE-11) |
| | [Auditoria complementar](../dominio/auditoria-complementar-matriz-orcamentaria.md) | Histórico da v1.1.0; superada em parte pela v1.2.0 |
| **Evidências** | `docs/dominio/evidencias/2026-11-08` e `2026-11-09` | Cópias das versões 1.0.0 e 1.1.0 da fonte canônica, portarias, demonstrativo do IFMT, página da PROAD, guia da PNP de 2018, scripts e resultados |
| | `tests/auditoria_matriz/` | 32 testes de auditoria; só rodam com os arquivos locais |
| **Estudos** | [Portão de dados](../analises/prumo-poc-portao-dados.md) (09/11) | Conciliação PNP × matriz 2026. Resultado válido e reaproveitado por tudo que veio depois |
| | [Estudo da PNP](../analises/prumo-pnp-inteligencia-comparativa-exploratoria.md) **(PR #1)** (10/11) | Auditoria longitudinal reproduzível, com 14 tabelas |
| **Protótipos** | [Avaliação da v2](../analises/prumo-avaliacao-prototipo-v2.md), [plano de Itapina](../analises/prumo-plano-demonstracao-itapina.md) (09/11) | Registro do desenho e dos resultados de cada protótipo |
| | [Documento da POC 0.0.2](../analises/prumo-poc-002.md) **(PR #2)** (10/11) | Idem |
| | `poc/` | Templates, motores, extratores, dados derivados e páginas montadas |

---

## 2. Linha do tempo

Todo o trabalho registrado ocorreu em três dias.

| Quando | O que aconteceu | Pergunta que orientava | Fonte |
|---|---|---|---|
| 08/11 | Documento fundador e proposta de nome | Como melhorar as decisões que definem a oferta? | Documento fundador §§ 0.1, 13 |
| 08–09/11 | Auditoria da matriz: fonte canônica v1.0.0 → v1.2.2 | Conseguimos reproduzir a matriz? | Commits `f0d5669`, `24a3036` |
| 09/11 | Revisão estratégica | O esforço está no lugar certo? | Revisão estratégica § 1 |
| 09/11 | Portão de dados; protótipo v1 e, 18 minutos depois, v2 | Como os campi levam o Ifes a 50% de formação técnica? | Commits `a3b64df`, `b010949` |
| 09/11 | Avaliação da v2; plano e demonstração de recomposição | Como um campus recompõe sua oferta e o que negocia com o Ifes? | Commit `7931c60` |
| 10/11 | Estudo da PNP | A série histórica da Rede merece entrar no produto? | PR #1 |
| 10/11 | POC 0.0.2 | Ampliar, aproveitar melhor ou reorganizar? | PR #2 |
| 10/11 | Consolidação | O que é o PRUMO, afinal? | Este documento |

### Respostas às oito perguntas da reconstrução

1. **Hipótese original.** Governança distribuída como núcleo; simulação acadêmico-orçamentária, com foco na Matriz CONIF, como primeiro instrumento. O documento fundador já previa três níveis: descritivo, preditivo e de execução (§ 3).
2. **O que a primeira POC pretendia demonstrar.** A primeira POC do repositório é a da meta de 50% de formação técnica. Pretendia mostrar que um indicador institucional só se move com contribuições diferentes dos campi, depois de conferir que os dados públicos reproduzem o valor oficial (portão de dados).
3. **O que ela demonstrou.** A conciliação: a soma dos campi na PNP reproduz os percentuais legais usados na matriz de 2026 (técnico 0,4403 contra 0,44). Mostrou também que nenhum ajuste marginal alcança a meta e que uma única unidade de educação a distância move vários indicadores ao mesmo tempo. Não demonstrou recomposição de portfólio, tempo nem viabilidade.
4. **O que motivou os estudos seguintes.** A avaliação da v2 concluiu que o protótipo respondia "quanto falta para 50%?", e não "qual combinação de ofertas atende melhor à missão?". Daí a recomposição. O achado de que as vagas do técnico não viravam matrículas motivou o estudo da PNP e, dele, a POC 0.0.2.
5. **Descobertas incorporadas.** Regra operacional da matrícula total; defasagem de dois anos; três réguas separadas (meta legal, limiar orçamentário, meta pactuada); decisão em vagas, não em matrículas; marcação da natureza de cada número; validação do modelo contra o passado.
6. **Onde o escopo divergiu.** Três vezes, sempre pelo mesmo mecanismo: um achado forte virou a pergunta que organiza o produto (§ 4).
7. **O que permanece válido.** Todos os princípios do documento fundador; a conciliação de dados; as regras de domínio; os fatos do estudo da PNP; a estrutura comparar → simular → compor.
8. **Descartado ou não verificado.** Descartado: o bloco de funcionamento como porta de entrada; a MOOC como alavanca orçamentária; estimar a relação aluno-professor da matriz a partir da PNP. Não verificado: qualquer reação de gestores; a regra de distribuição interna; a prática de cálculo de 2027; a causa da queda de matrículas no técnico.

**Observação sobre "a primeira POC".** Se a expressão se refere a um artefato anterior à meta de 50%, ele não está no repositório nem no histórico do Git. A v1 da meta de 50% foi sobrescrita pela v2 e só existe no commit `a3b64df`.

---

## 3. Comparação dos protótipos

Os três são páginas HTML estáticas, com dados públicos embutidos, sem servidor. Registros ficam no navegador.

| | **Meta de 50% técnico (v2)** | **Recomposição** | **POC 0.0.2** (PR #2) |
|---|---|---|---|
| **Pergunta** | Como os campi levam o Ifes a 50% de formação técnica? | Como um campus recompõe a oferta em três anos e o que negocia? | Ampliar, aproveitar melhor ou reorganizar? |
| **Usuário pressuposto** | Reitoria e planejamento | Direção de campus; reitoria na pactuação | Direção de ensino do campus; visão institucional em "Compor" |
| **Unidades** | Todos os campi do Ifes; todas as instituições | Itapina e Barra de São Francisco | Vitória e Serra; Rede como contexto |
| **Etapas** | Onde estamos → Experimentar → Comparar e registrar | Campus → Pactuação → Como calcula | Comparar → Simular → Compor → Como calcula |
| **Decisão** | +n matrículas num curso existente | Vagas, suspensão, permanência, oferta nova | Três alternativas fixas, parâmetros editáveis |
| **Tempo** | Retrato de um ano | Coortes até 2029 | Coortes até 2032 e efeito em regime |
| **Motor** | Matrícula equivalente média do curso | Permanência única por oferta | Evasão, conclusão no prazo e retenção separadas |
| **Recursos** | Não há | Docentes, ambiente crítico, custeio | Só docentes, por premissa simples |
| **Evidência histórica** | Posição entre pares num ano | Série do campus | Série do campus, Ifes × Rede, precedente |
| **Incerteza** | Avisos e lista de limites | Quatro marcadores, faixa por erro histórico | Cinco marcadores, faixas, "o que precisa ser verdade" |
| **Governança** | Contribuição em pontos percentuais; proposta local | Proposta com responsável, recursos, contrapartidas e indicador | Contribuição por objetivo, 16 combinações, premissas a validar |
| **Testes** | Nenhum | 6, passam | 16, passam |

### O que cada um comprovou, ilustrou ou deixou como hipótese

| | Comprovado | Ilustrado | Hipótese |
|---|---|---|---|
| **v2** | Dados públicos por campus reproduzem os percentuais legais oficiais. A contribuição de cada campus se decompõe de forma exata | Que a meta exige decisão de portfólio institucional | Que um gestor leria a tela assim |
| **Recomposição** | Modelo simples de coortes reproduz técnicos integrados com erro de 2% a 3% | Pico de recursos antes do efeito na matriz; "manter também muda"; proposta com contrapartidas | Premissas de docentes, ambiente e custo; demanda da oferta nova; compreensão em 15 minutos |
| **POC 0.0.2** | Os números da tela conferem com o estudo da PNP | Evidência histórica ao lado da decisão; resposta condicional honesta | Efeito de programa de permanência (sem dado que o sustente); prazos efetivos; compreensão pelo gestor |

**Nenhum protótipo foi mostrado a um gestor.** Toda afirmação de que algo é compreensível é avaliação de quem construiu. As entrevistas previstas na fase 0 do documento fundador também não ocorreram.

### Qualidades de experiência a preservar

- Três réguas separadas para o mesmo indicador (v2).
- Contribuição de cada campus decomposta em numerador e denominador (v2).
- "Manter não é ficar parado" como abertura (recomposição).
- Colunas de ano-base e exercício lado a lado (recomposição).
- Marcadores de natureza em cada número (recomposição, 0.0.2).
- Evidência específica da decisão, e não um painel geral (0.0.2).
- "O que precisa ser verdade" e a recusa explícita em recomendar (0.0.2).
- Aba "Como calcula" com o erro do modelo (recomposição, 0.0.2).

### Limitações técnicas

- **Três motores diferentes.** `coortes002.js` é uma reescrita, não uma evolução de `coortes.js`. Divergem em duração (fixa × ajustada), regra de turmas, definição de evasão e período de calibração.
- **Erros altos fora dos técnicos integrados**, exibidos mas sem verificação automática: 63% numa graduação recém-implantada, 69% num concomitante (recomposição); 42% e 43% em concluintes de duas ofertas (0.0.2).
- **Código duplicado** entre os três extratores e os três templates (classificação de ofertas, faixas de qualidade, cálculo do Ifes).
- **O Ifes está fixo no código:** nomes de campi, exceção do Cefor, exemplos, faixas e metas.
- **Extração depende da pasta local.** Dois dos três extratores só rodam no diretório principal. Montar e testar funcionam sem ela, porque os dados derivados estão versionados.
- **A v2 não tem testes** e teve dois erros numéricos corrigidos depois (reduções acima do saldo; quantidades negativas).
- **Ponto a conferir:** o extrator da 0.0.2 trata números de modo diferente dos outros dois (não remove separador de milhar). Os totais conferem com o estudo, mas a diferença não foi investigada.

---

## 4. Divergências e contradições

### 4.1. O padrão de fragmentação

Cada etapa produziu um achado sólido, e cada achado foi promovido a pergunta organizadora do produto:

| Achado | Promovido a | Documento |
|---|---|---|
| O Ifes recebe zero em dois subcomponentes de qualidade | "Pacto de metas com degraus" como primeiro caso de uso | Revisão estratégica §§ 12–13 |
| A v2 não representa recomposição de portfólio | "Recomposição de um campus em quatro anos" | Avaliação da v2 |
| No técnico, as vagas se preenchem e as matrículas caem | "Ampliar, aproveitar ou reorganizar" | POC 0.0.2 § 1 |

Os achados estão corretos. O erro foi de encaminhamento: tratar um caso de uso como a definição do produto. A [visão](visao-prumo.md) resolve isso classificando os três como exemplos (§ 11).

### 4.2. Contradições encontradas e resolução recomendada

| # | Contradição | Resolução recomendada |
|---|---|---|
| 1 | **Papel da inteligência histórica.** O estudo da PNP conclui que ela deve entrar "como camada de premissas e de contexto", "não como painel". A direção de 10/11 pede uma capacidade de exploração por si só | As duas se conciliam se a exploração for organizada por perguntas e decomposições e terminar em evidência que o gestor leva adiante. As restrições do estudo (sem ranking, sem estimativa orçamentária, sem atribuir intenção) continuam valendo. **A forma na interface fica em aberto** |
| 2 | **Produto institucional ou SaaS.** O documento fundador separa o projeto de uma iniciativa de SaaS e deixa a generalização como questão aberta | Registrar SaaS como direção nova, de 10/11, e como hipótese. Não reescrever o documento fundador |
| 3 | **Jornada.** A recomposição abandonou comparar → simular → compor; a 0.0.2 a retomou | Tratar as três etapas como o esqueleto mais testado internamente, ampliado para entender → simular → pactuar → acompanhar. Validar com gestores antes de fixar |
| 4 | **Governança como núcleo × governança como rodapé.** Todos os documentos a declaram núcleo; em todos os protótipos ela é a última aba, com registro local | É a lacuna central. O próximo experimento deve começar pela negociação, não pelo simulador |
| 5 | **Onde mora o estudo da PNP.** O script de reprodução foi colocado em `docs/dominio/evidencias/`, embora seja evidência de análise, não de domínio | Manter onde está: mover quebraria referências. Registrar a convenção no README |
| 6 | **Versão da fonte canônica.** O cabeçalho diz 1.2.2; o § 0.3 e o README dos testes dizem 1.2.0 | Rótulos não atualizados. Corrigir numa próxima edição do documento de domínio; não alterado aqui |
| 7 | **Nomes dos protótipos.** "v1", "v2", "recomposição" e "0.0.2" não formam uma sequência | Usar os nomes pela pergunta que respondem. Não renomear arquivos |
| 8 | **A POC 0.0.2 cita um estudo que não está na sua branch.** O PR #2 parte da `main`, não do PR #1 | Integrar o PR #1 antes do PR #2 |

---

## 5. Limitações metodológicas confirmadas

Todas já documentadas nos estudos. Nenhuma foi reinvestigada.

| Tema | Limitação | Fonte |
|---|---|---|
| **Comparabilidade entre anos** | A série mostra cada ano com a metodologia de sua edição. Não há código estável de campus | Estudo da PNP §§ 2.2, 2.3 |
| **Matrícula equivalente** | Fórmula mudou entre os anos-base 2020 e 2021. Só é série em 2021–2025. Para períodos longos, usar matrículas físicas da oferta regular presencial | Estudo da PNP § 2.4 |
| **Pandemia** | 2020–2022: evasão subnotificada e retenção inflada. Melhoras nesses anos são artefato | Estudo da PNP § 2.4 |
| **Rótulos instáveis** | Programa (MOOC, PROEJA) e forma (concomitante, subsequente) mudam de classificação ao longo da série | Estudo da PNP § 2.4 |
| **PNP × matriz** | Matrícula física, matrícula equivalente e matrícula total são três medidas. A total não se deriva da equivalente | Estudo da PNP § 4; fonte canônica RMO-066 |
| **Relação aluno-professor** | O denominador reconcilia (±1%). O numerador não: 20,11 na PNP, 17,56 pela definição do guia, 18,148 na matriz | Portão de dados; estudo da PNP § 5.5 |
| **Eficiência acadêmica** | O arquivo público inclui FIC; o índice da matriz exclui. Não é reproduzível | Estudo da PNP § 2.4; fonte canônica RMO-068 |
| **Dupla contagem** | Decomposições só valem com grupos mutuamente exclusivos. A matrícula total soma ciclos, não pessoas | Estudo da PNP § 5.1; revisão crítica § 8 |
| **Formação de professores** | A PNP não permite classificar por curso. Salto de 12% para 24,8% entre 2024 e 2025 é provável reclassificação | Portão de dados |
| **Correlação e causa** | Correlações com 41 instituições e janelas curtas. Nenhuma tratada como causal. A PNP não registra decisões | Estudo da PNP § 8 |
| **Defasagem** | Exercício = ano-base + 2 na matriz de 2026. Não tratar como regra permanente | Fonte canônica RMO-070 |
| **Texto × prática** | A prática de cálculo de 2026 diverge do texto das portarias. Não se sabe qual valerá em 2027 | Fonte canônica L-24 |
| **Distribuição interna** | "Matriz por campus com piso e teto" é hipótese forte, não regra reconstruída | Fonte canônica RMO-075 |
| **Indicadores não utilizáveis** | Taxa de ocupação (retirada da PNP), inscritos por vaga (baixa confiabilidade), gastos (nominais, só por instituição) | Estudo da PNP § 2.4 |

---

## 6. Mapa de consolidação das POCs

Nenhuma interface foi unificada. O mapa orienta trabalho futuro.

| Destino | Elemento | Origem |
|---|---|---|
| **Preservar** como está | Conciliação PNP × matriz e seus testes | Portão de dados |
| | Fonte canônica da matriz e evidências | `docs/dominio/` |
| | Estudo da PNP, script e tabelas | PR #1 |
| | Os três protótipos, navegáveis e regeneráveis | `poc/` |
| **Reaproveitar** na próxima construção | Três réguas por objetivo; decomposição numerador × denominador | v2 |
| | Proposta com responsável, recursos, contrapartidas e indicador | Recomposição |
| | Colunas ano-base → exercício; ambiente crítico e pico de recursos | Recomposição |
| | Oferta nova por empréstimo de parâmetros | Recomposição |
| | Marcadores de natureza; evidência junto da decisão; "o que precisa ser verdade"; grade de combinações | POC 0.0.2 |
| | Separação de evasão, conclusão no prazo e retenção | POC 0.0.2 |
| | Decomposições e seleção de comparáveis por trajetória | Estudo da PNP |
| **Reformular** | Inteligência histórica: de etapa "Comparar" e de relatório estático para exploração que gera evidência transportável | v2, 0.0.2, estudo |
| | Motor de coortes: um só, depois de saber quais perguntas o gestor faz | `coortes.js`, `coortes002.js` |
| | Governança: de registro no navegador para objeto central, com acompanhamento | Os três |
| | Instituição como parâmetro, em vez de Ifes fixo no código | Os três |
| | Alternativas: de fixas ou de formulário livre para decisões de oferta combináveis | Recomposição, 0.0.2 |
| **Manter só como evidência histórica** | v1 da meta de 50% | Commit `a3b64df` |
| | Simulação em matrículas de um único ano | v2 |
| | Auditoria complementar da v1.1.0; cópias 1.0.0 e 1.1.0 | `docs/dominio/` |
| | Texto original do portão "não aprovado" | Portão de dados |
| **Descartar conceitualmente** | Um caso de uso como pergunta organizadora do produto | Justificativa no § 4.1 |
| | Funcionamento por campus em reais como porta de entrada | Incentiva volume contra o coletivo (revisão estratégica § 1) |
| | Estimar relação aluno-professor e eficiência da matriz pela PNP | Não reconciliam (§ 5) |
| | Programa de permanência com efeito arbitrado como alternativa comparável às demais | Não há dado que sustente o tamanho do efeito (POC 0.0.2 § 5) |
| | Continuar a auditoria forense da planilha da matriz | Retorno decisório baixo (revisão estratégica § 11) |

---

## 7. Problemas de organização do repositório

| Problema | Tratamento nesta atividade |
|---|---|
| Não havia README | Criado, com mapa de navegação |
| Não havia visão vigente única: quatro documentos descreviam o "primeiro caso de uso" de formas diferentes | Criada a [visão canônica](visao-prumo.md); avisos de situação acrescentados no topo dos documentos anteriores |
| Estudo da PNP e POC 0.0.2 fora da `main` | Não integrados aqui: decisão de quem mantém o repositório. Referenciados por link à branch |
| `docs/analises/` mistura estudos, planos e avaliações de protótipo | Classificados no README. Arquivos não movidos |
| Documentos de visão na raiz | Não movidos |
| `poc/` com três gerações numa pasta plana | Não reorganizada |
| Dependência de dados locais não documentada num só lugar | Documentada no README |

**Por que nada foi movido.** Os scripts localizam a raiz do repositório pela profundidade da própria pasta, os extratores leem o demonstrativo em `docs/dominio/evidencias/2026-11-08/`, o montador exige template, dados e motor na mesma pasta, e os dois pull requests abertos citam os caminhos atuais. Mover arquivos agora quebraria a reprodução dos estudos ou criaria conflitos.

**Reorganização proposta, para depois de integrar os dois PRs** (não executada):

1. Mover os dois documentos da raiz para `docs/produto/historico/`, corrigindo as referências que apontam para eles (cinco nos documentos de análise, além das criadas nesta atividade).
2. Separar `docs/analises/` em `docs/estudos/` (portão de dados, estudo da PNP, revisão estratégica) e `docs/prototipos/` (avaliação da v2, plano de Itapina, POC 0.0.2).
3. Deixar `poc/` e `docs/dominio/evidencias/` como estão.
4. Fazer o extrator da v2 e o da recomposição aceitarem o caminho da pasta de dados por argumento, como o da 0.0.2 já faz.
