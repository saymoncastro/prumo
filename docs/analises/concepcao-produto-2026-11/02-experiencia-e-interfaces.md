# 2 · Experiência e interfaces

> **Estudo de concepção de 12/11/2026, revisado na segunda rodada no mesmo dia.** Proposta para discussão, não telas aprovadas.
> **Protótipo navegável v2:** [prototipo/prumo-conceito.html](prototipo/prumo-conceito.html). Curvas de Vitória e Serra calculadas com o motor da POC 0.0.2 sobre dados reais da PNP; capacidade e unidades marcadas como ilustrativas. A primeira versão está preservada em [prototipo/prumo-conceito-v1.html](prototipo/prumo-conceito-v1.html).
> **Segunda rodada:** novo § 8 com o enriquecimento da Agenda, da Ficha do campus, da Bancada e da Mesa. As descrições do § 4 continuam válidas onde o § 8 não as substitui.

---

## 1. Duas concepções comparadas

### Concepção A · Convencional, organizada por módulos

Menu lateral com **Indicadores** (painéis por tema), **Cursos e ofertas** (cadastro), **Cenários** (formulário de parâmetros e tabela de resultados), **Metas** (cadastro de metas institucionais e de metas por campus), **Acompanhamento** (semáforos por meta) e **Relatórios**.

### Concepção B · Orientada a decisões

O produto se organiza em torno de **objetivos** e da **pauta de decisão** do ciclo. Não há "módulo de cenários": há uma **bancada de alternativas** dentro da ficha de cada campus. Não há "módulo de metas": cada objetivo tem uma **mesa de composição** onde as contribuições dos campi se somam. Os objetos que o gestor produz (evidência, alternativa, proposta, compromisso) circulam entre as telas e carregam sua origem.

### Comparação

| Critério | A · Convencional | B · Orientada a decisões |
|---|---|---|
| Familiaridade para o gestor | Alta: parece com o que já usa | Média: exige entender "objetivo → contribuição" |
| Tempo até o primeiro valor | Longo: painéis genéricos ou cadastro antes de simular | Curto: abre na posição do objetivo, já com dados públicos |
| Risco de virar BI | **Alto.** "Indicadores" é um módulo que se basta | Baixo: a leitura sempre termina numa alternativa ou numa evidência guardada |
| Risco de virar burocracia | **Alto.** "Metas por campus" vira formulário e semáforo | Médio: a proposta é um objeto curto, gerado da alternativa |
| Ligação entre capacidades | Fraca: o usuário cruza menus e perde contexto | Forte: a contribuição do campus aparece no objetivo e o objetivo aparece no campus |
| Uso em reunião colegiada | Ruim: telas de cadastro não se projetam | Bom: a mesa de composição é feita para ser projetada |
| Facilidade de especificar e construir | Alta | Média: exige motor de composição desde cedo |
| Fidelidade à tese (governança como finalidade) | Baixa: governança é mais um módulo | Alta: governança é o centro da navegação |

### Recomendação: B como estrutura, A onde ela é honesta

A estrutura de navegação e as telas centrais seguem a concepção B. Mas há coisas que a concepção A faz bem e que não devem ser reinventadas:

- **listas, tabelas ordenáveis, busca e exportação** para tudo o que é registro (propostas, compromissos, ofertas, evidências);
- **páginas estáveis com endereço próprio** para cada objetivo, campus, oferta e compromisso, para que possam ser citadas em ofício ou ata;
- **impressão e exportação em PDF** de uma proposta ou de um pacto, porque a decisão pública vive em documento.

O que se descarta da concepção A: painéis temáticos sem decisão associada, cadastros como porta de entrada, semáforos sem explicação, menus por tipo de dado.

---

## 2. Modelo mental: três lugares, quatro objetos, um ritmo

O gestor precisa guardar pouca coisa na cabeça para navegar:

**Três lugares**

| Lugar | Pergunta | Quem mais usa |
|---|---|---|
| **Objetivos** | "Onde a instituição está em relação ao que quer, e quem contribui?" | Reitoria, planejamento |
| **Campi** | "O que o meu campus oferece, o que está acontecendo com as turmas e que alternativas tenho?" | Direção de campus |
| **Rede** | "O que aconteceu em instituições e campi parecidos?" | Planejamento, quando precisa de comparação ou precedente |

**Quatro objetos que o gestor carrega**

| Objeto | Nasce em | Vai para |
|---|---|---|
| **Evidência** | Qualquer leitura (botão "guardar como evidência") | Premissa de alternativa, justificativa de proposta |
| **Alternativa** | Bancada do campus | Comparação com outras alternativas; proposta |
| **Proposta** | Alternativa escolhida pelo campus | Mesa de composição do objetivo |
| **Compromisso** | Proposta pactuada | Acompanhamento; conferência pela próxima PNP |

**Um ritmo:** o ciclo anual (ler o ano → propor → pactuar → conferir). A tela inicial mostra em que momento do ciclo a instituição está e o que está pendente.

---

## 3. Mapa de navegação

```
Início · Agenda estratégica
 ├─ O que mudou na última PNP
 ├─ Pauta do ciclo (ex.: Plano de oferta 2028) ──────────────┐
 └─ Compromissos a conferir                                   │
                                                              ▼
Objetivos ─────────────── Objetivo (ex.: formação técnica)
                           ├─ Posição e réguas
                           ├─ Quem explica a mudança (ponte por campus)
                           ├─ Mesa de composição ◄──── propostas dos campi
                           └─ Pacto e acompanhamento
                                                              ▲
Campi ─────────────────── Ficha do campus                     │
                           ├─ Contribuição a cada objetivo    │
                           ├─ Portfólio de ofertas (funis)    │
                           │    └─ Oferta (série, evidência)  │
                           └─ Bancada de alternativas ── proposta
                                                              
Rede ──────────────────── Trajetórias, comparáveis, precedentes

Em qualquer tela: gaveta "Como calcula" (clique num número) · bandeja de evidências
```

Seis telas centrais carregam o produto. As demais são listas e detalhes.

---

## 4. Telas centrais

### 4.1. Agenda estratégica (início)

**Propósito:** dizer em dez segundos onde a instituição está e o que precisa de atenção.

**Mostra:**
- uma faixa por objetivo ativo: valor atual, régua tripla compacta (meta legal, limiar da matriz, meta pactuada), tendência de três anos e "quem mais mexeu" (o campus com maior contribuição à variação);
- **O que mudou na última PNP:** até cinco mudanças relevantes, já decompostas e classificadas (melhora, piora, provável reclassificação, oferta em pulso). Nada de lista de cem indicadores;
- a **pauta do ciclo**: etapa atual, campi que já propuseram, data da reunião de pactuação;
- **compromissos a conferir**: os que chegaram a um horizonte observável na última carga.

**Não mostra:** gráficos de todos os indicadores, rankings, semáforos sem explicação.

### 4.2. Objetivo

**Propósito:** responder "onde estamos, como chegamos aqui e quem pode contribuir".

**Mostra:**
- **Régua tripla.** Uma régua horizontal com a posição atual, a meta legal, os limiares da matriz e a meta pactuada, cada marca com sua natureza. No técnico, limiar e meta legal coincidem (50%); em EJA, o primeiro limiar (2,5%) é um quarto da meta legal (10%). A régua torna isso óbvio sem texto.
- **Ponte de contribuição.** Gráfico em cascata da variação do indicador entre dois anos-base, decomposta por campus (efeito no numerador menos efeito no denominador). Responde "quem explica a mudança" sem ranking.
- **Trajetória** dentro do bloco metodológico comparável, com quebras de série marcadas no próprio eixo (fórmula de 2021, pandemia 2020–2022).
- **Comparáveis:** três a cinco instituições escolhidas por perfil e trajetória, com o critério declarado.
- **Objetivos em tensão:** os outros objetivos que se movem quando este se move (técnico × formação de professores × EJA).
- Acesso à **mesa de composição** e ao **pacto vigente**.

**Interações:** trocar o par de anos da ponte; abrir um campus da ponte; guardar qualquer leitura como evidência.

### 4.3. Ficha do campus

**Propósito:** dar ao diretor uma visão do próprio portfólio que ele não tem hoje.

**Mostra:**
- **Contribuição do campus a cada objetivo institucional** (em pontos percentuais, com sinal). Não é nota: é quanto o campus move o agregado.
- **Portfólio como funis.** Cada oferta numa linha: vagas → ingressantes → matrículas → concluintes, com mini-série 2017–2025. A forma do funil diz onde está o problema (a vaga não preenche, ou preenche e o estudante não conclui). É a tradução visual do achado central do estudo da PNP.
- **Sinais:** procura excedente, ofertas em queda de conversão, ofertas recém-abertas com pouca série, prováveis reclassificações.
- Acesso à **bancada de alternativas**.

### 4.4. Bancada de alternativas (simulação)

**Propósito:** transformar uma ideia de oferta em consequências no tempo e compará-la com outras.

**Composição da tela:**
1. **Decisões como cartões.** Cada alternativa é um conjunto curto de decisões em linguagem de gestor: "+36 vagas em Mecânica concomitante a partir de 2027"; "Eletrotécnica: 32 vagas do concomitante passam ao integrado". Há cinco tipos de decisão: ampliar ou reduzir vagas, abrir oferta, suspender ingresso (as turmas em curso concluem), migrar vagas entre ofertas, e agir sobre permanência. A linha de base "manter" é sempre a primeira coluna, porque manter também muda.
2. **Quadro comparativo.** Alternativas lado a lado contra "manter": matrículas, concluintes no horizonte e em regime, contribuição para cada objetivo, docentes e ambiente crítico. Valores com faixa.
3. **Linha dos três marcos.** Uma linha do tempo com ano da decisão, ano-base em que o efeito aparece e exercício da matriz que o usa, mostrando também **quando o recurso aperta** (pico de turmas simultâneas) antes de o efeito aparecer.
4. **Premissas com procedência.** Cada premissa mostra o valor do próprio campus, a faixa de ofertas comparáveis e a fonte. Oferta nova usa parâmetros emprestados, rotulados como empréstimo. Premissa sem base (ex.: efeito de um programa de permanência) aparece como **hipótese**, com faixa larga, e a alternativa inteira herda essa marca.
5. **O que precisa ser verdade.** Lista gerada das premissas e dos recursos: "haver procura para mais 36 vagas", "2 docentes da área técnica", "um programa capaz de reduzir a evasão em 30%".
6. **Precedente.** Quando houver, a série de uma decisão parecida já tomada (ex.: Metalurgia dobrou as vagas em 2023), como fato e sem inferência causal.

**Divulgação progressiva:** a tela abre no quadro comparativo e na leitura em texto. Premissas, ano a ano e "como calcula" ficam um nível abaixo. O diretor não precisa ver um parâmetro para obter um resultado; precisa poder vê-lo quando duvidar.

**Ação final:** "Encaminhar como proposta", que gera a proposta com contribuição, recursos pedidos, contrapartidas e premissas a validar.

### 4.5. Mesa de composição (governança)

**Propósito:** ver como propostas diferentes dos campi se somam para o objetivo, e negociar.

**Mostra:**
- **Grade campi × objetivos.** Uma linha por campus, com a alternativa escolhida (seletor: manter, A, B, C) e a contribuição a cada objetivo. A última linha é a instituição, calculada pela razão das somas. Uma coluna de recursos pedidos.
- **Distância às réguas.** Para cada objetivo, a régua tripla com a posição projetada da composição atual.
- **Conflitos.** Quando uma escolha melhora um objetivo e piora outro, a célula mostra os dois sinais e o par de objetivos aparece em destaque.
- **O que falta e onde pode estar.** Distância restante e quais unidades ainda não propuseram ou têm alternativas não usadas que fecham parte dela. Não é recomendação: é a lista das alavancas restantes com seu efeito.
- **Retorno ao campus.** Quando a regra interna de distribuição estiver configurada, quanto do efeito institucional volta a cada campus. Sem a regra, "não estimado".

**Modo reunião:** fonte maior, sem menus, uma régua por objetivo, alternância rápida entre composições ("e se Serra ficar em manter?"). Pensado para ser projetado no Colégio de Dirigentes e operado pela equipe de planejamento.

**Ação final:** "Registrar pacto": transforma as propostas escolhidas em compromissos, com responsável, indicador e marcos por horizonte. Registra a instância que decidiu e a data. O PRUMO não aprova nada; registra o que foi aprovado.

### 4.6. Pacto e acompanhamento

**Propósito:** conferir o que aconteceu e explicar os desvios.

**Mostra:**
- **Compromissos por horizonte:** execução (as vagas foram ofertadas?), resultados intermediários (ingresso e ocupação vieram?), longo prazo (matrículas, concluintes, efeito na matriz). Cada compromisso é avaliado só no horizonte que já pôde ser observado; os outros aparecem como "ainda não observável", com a data em que serão.
- **Desvio explicado.** Para cada compromisso fora da faixa, uma cascata que vai do projetado ao observado passando pelos mesmos mecanismos da projeção: vagas efetivamente ofertadas, ocupação, evasão, retenção, conclusão, e "resto" (o que o modelo não explica). É calculada reprojetando o cenário com cada premissa trocada pelo valor observado, uma de cada vez, em ordem fixa e declarada. Determinístico e auditável.
- **Revisão:** a partir do desvio, revisar a premissa (e propagar para os cenários que a usam), revisar a meta pactuada ou registrar uma justificativa.

### 4.7. Elementos transversais

| Elemento | O que é |
|---|---|
| **Marcador de natureza** | Etiqueta em todo número: fato, estimado, premissa, hipótese, não estimado. Cores e formas consistentes, legíveis em impressão em preto e branco |
| **Gaveta "Como calcula"** | Clique em qualquer número abre: fonte e edição, ano-base, regra e versão, fórmula com os valores, premissas usadas, erro do modelo quando houver. É a resposta à pergunta "o cálculo é confiável?" |
| **Bandeja de evidências** | Tudo o que o gestor guardou na sessão, pronto para anexar a uma premissa ou proposta |
| **Faixa de incerteza** | Onde o modelo erra mais ao reproduzir o passado, o número vem em faixa. Nunca um número sozinho onde o erro é grande |
| **Linguagem** | "Concluintes por ano em regime", não "fluxo estacionário". "Manter também muda", não "linha de base dinâmica". Glossário acessível pelo próprio termo |

---

## 5. Jornadas

Cada jornada lista passos, telas, dados e valor produzido. Telas referem-se ao § 4. Os valores de Vitória (+36 vagas, +2,9 professores-equivalentes, precedente de Metalurgia) vêm da POC 0.0.2; o laboratório lotado e a evasão −12% são ilustrativos.

### Cenário A · Reitoria: entender a situação e definir prioridades

| Passo | O que o gestor faz | Tela | Dados |
|---|---|---|---|
| 1 | Abre o PRUMO e lê "o que mudou" no ano-base | Agenda | PNP (fato) |
| 2 | Abre o objetivo "formação técnica", vê a régua tripla e a tendência | Objetivo | PNP; faixas da Portaria 243/2026; meta pactuada, se houver |
| 3 | Lê a ponte: a variação de 2021 a 2025 veio de quais campi; percebe o peso da unidade de EaD | Objetivo | PNP por campus |
| 4 | Compara com três institutos de trajetória parecida | Objetivo → Rede | PNP de todas as instituições |
| 5 | Vê os objetivos em tensão (formação de professores sobe com a mesma oferta) | Objetivo | PNP |
| 6 | Guarda duas evidências e abre a pauta do ciclo com dois objetivos e uma meta pactuada provisória | Agenda | Escolha do gestor |

**Valor:** prioridades com fundamento, e a descoberta de que a alavanca principal pode estar numa única unidade, não na soma dos campi.

### Cenário B · Direção de campus: entender a contribuição e avaliar a oferta

| Passo | O que o gestor faz | Tela | Dados |
|---|---|---|---|
| 1 | Abre a ficha do campus; vê a contribuição a cada objetivo | Campus | PNP |
| 2 | Lê os funis; nota que o concomitante perdeu concluintes com as vagas preenchidas | Campus | PNP por oferta, 2017–2025 |
| 3 | Abre a oferta; vê a série e a procura excedente; guarda como evidência | Oferta | PNP (inscritos com aviso de baixa confiabilidade) |
| 4 | Vê o que a pauta pede do campus (objetivos do ciclo) | Campus | Pauta aberta pela reitoria |
| 5 | Passa para a bancada (Cenário C) | Bancada | — |

**Valor:** o diretor entende seu portfólio pelo que acontece com as turmas, não só pelo número de vagas, e sabe qual é sua posição nos objetivos.

### Cenário C · Simulação de expansão

| Passo | O que o gestor faz | Tela | Dados |
|---|---|---|---|
| 1 | Cria alternativa "Ampliar": +36 vagas em Mecânica concomitante a partir de 2027 | Bancada | Decisão do gestor |
| 2 | Cria "Reorganizar": 32 vagas do concomitante passam ao integrado | Bancada | Idem |
| 3 | Vê o quadro comparativo contra "manter", com faixas | Bancada | Motor de coortes calibrado na PNP |
| 4 | Vê na linha dos marcos que o pico de turmas é em 2029 e o efeito na matriz só em 2031 | Bancada | Regra de defasagem do exercício |
| 5 | Vê o recurso crítico: "Ampliar" exige +2,9 professores-equivalentes; o laboratório de usinagem passa de 100% no turno matutino em 2029 | Bancada | **Cadastro mínimo de capacidade do campus** (docentes por área, salas por turno, ambientes críticos), feito uma vez e verificado contra 2025 [2ª rodada; a primeira versão previa informar só para esta decisão] |
| 6 | Abre a premissa de ocupação; vê que a procura excedente cobre as vagas; mantém 100% | Bancada | PNP (inscritos − ingressantes) |
| 7 | Lê "o que precisa ser verdade" e encaminha "Reorganizar" como proposta | Bancada | — |

**Valor:** o diretor descobre o gargalo e o momento em que ele aparece antes de pedir a turma, e chega à reitoria com o argumento pronto.

**Onde não há dado:** docentes por área e ambientes por turno não estão na PNP. A bancada pede **só o recurso que limita esta decisão**, com a pergunta "que recurso pode faltar?". Se o gestor não informar, o resultado aparece como "não estimado" naquela linha, e o resto da simulação continua funcionando.

### Cenário D · Pactuação institucional

| Passo | O que acontece | Tela | Dados |
|---|---|---|---|
| 1 | A reitoria abre a pauta com objetivo, meta pactuada provisória e prazo para propostas | Agenda → Objetivo | Decisão da reitoria |
| 2 | Cada campus envia uma proposta (cenários B e C) | Bancada | Propostas |
| 3 | A equipe de planejamento monta composições na mesa; identifica conflitos e distância restante | Mesa | Propostas + PNP |
| 4 | Pró-reitorias anotam pareceres nas propostas (texto, não fluxo) | Proposta | — |
| 5 | Na reunião do colegiado, a mesa é projetada em modo reunião; testam-se variações ao vivo | Mesa (modo reunião) | — |
| 6 | O colegiado decide; a equipe registra o pacto com responsáveis e indicadores | Mesa → Pacto | Ata (referência) |

**Valor:** metas diferenciadas negociadas com o efeito conjunto à vista, e um registro que todos podem citar.

**Sobre diferenciação e incentivos:** a mesa mostra, por campus, a contribuição, o custo (recursos pedidos) e, se configurada a regra interna, o retorno. Uma contribuição grande com custo grande é tão visível quanto uma pequena e barata. Compensações entre objetivos (um campus contribui em técnico, outro em EJA) ficam explícitas na grade.

### Cenário E · Acompanhamento e revisão

| Passo | O que acontece | Tela | Dados |
|---|---|---|---|
| 1 | A nova PNP é carregada; a Agenda lista compromissos que chegaram a um horizonte observável | Agenda | PNP nova |
| 2 | O gestor abre um compromisso fora da faixa | Pacto | Compromisso + PNP |
| 3 | Vê o desvio explicado: vagas ofertadas conforme o pactuado; ocupação ok; evasão caiu 12% e não 30% | Pacto | Reprojeção com valores observados |
| 4 | Revisa a premissa de efeito do programa de permanência; o PRUMO mostra os outros cenários que usam a mesma premissa | Pacto | Cenários vigentes |
| 5 | Ajusta a meta do horizonte de longo prazo e registra a justificativa | Pacto | — |

**Valor:** a instituição aprende com a própria decisão. A revisão vira técnica ("a premissa de evasão estava otimista"), não política ("o campus não cumpriu").

---

## 6. Inteligência artificial na experiência

Há poucos lugares onde um modelo de linguagem agrega valor real à experiência, e nenhum deles está no núcleo. Detalhes e regras no [documento 3, § 8](03-arquitetura-e-stack.md#8-inteligência-artificial).

| Uso | Valor | Quando |
|---|---|---|
| Redigir a **nota técnica** de uma proposta ou pacto a partir dos resultados calculados, com cada número vinculado ao cálculo | Alto: é trabalho real do planejamento e hoje toma dias | Depois do MVP |
| Explicar em linguagem simples o conteúdo da gaveta "Como calcula" | Médio | Depois, se a gaveta não bastar |
| Perguntas em linguagem natural sobre os dados | Baixo e arriscado | Não planejar |
| Sugerir alternativas ou escolher a melhor | Contraria o princípio de não recomendar | Não fazer |

---

## 7. O que se evita deliberadamente

- **Tela inicial de painéis.** Substituída por "o que mudou" e pela pauta.
- **Assistentes de muitos passos** para criar cenários. A alternativa nasce de um cartão de decisão com valores padrão vindos da evidência.
- **Cadastro antes de valor.** Infraestrutura e docentes só aparecem quando uma decisão precisa deles.
- **Ranking de campi ou de cursos.** Tabelas ordenam por tamanho ou nome, e dizem isso.
- **Saldo "contribuição menos custo"** e qualquer "retorno financeiro" de curso.
- **Semáforo sem explicação.** Todo desvio vem decomposto.

---

## 8. Segunda rodada: telas enriquecidas

Nenhuma tela nova. Quatro telas ganham profundidade. Todas aparecem no [protótipo v2](prototipo/prumo-conceito.html).

### 8.1. Agenda: a estrela-guia na abertura

- **Faixa da estrela-guia:** participação na matriz (≈ 3,32% em 2026) por bloco: Funcionamento 3,56%, Reitoria ≈ 3,5%, Qualidade 1,20% da fatia da Rede. Um clique abre a composição do número.
- **Alavancas da estrela-guia:** o mapa de degraus com valor por exercício, alavanca e natureza ([documento 7, § 3](07-estrela-guia-e-indicadores.md#3-mapa-de-degraus-do-ifes-exercício-2026)).
- **O que mudou** passa a dizer quando uma mudança da PNP pode cruzar um degrau (formação de professores em 2025).

### 8.2. Objetivos: da estrela-guia às decisões

- **Árvore de alavancas:** participação → blocos → indicadores → decisões, com a classe de cada ligação (calculável, projetável, dado institucional, não estimável).
- **Taxa de câmbio:** quanto vale uma MT, um estudante de integrado, um retido, um degrau. É a ferramenta para comparar alavancas de naturezas diferentes.
- Régua tripla e objetivos em tensão continuam.

### 8.3. Ficha do campus: portfólio, capacidade e gargalos

| Bloco | O que mostra | Dados |
|---|---|---|
| **Indicadores do campus** | Matrículas, concluintes (antes e depois), efeito do campus no percentual técnico do Ifes, restrição prevista mantendo a oferta | PNP; modelo |
| **Portfólio como funis** | Por oferta: vagas, ingressantes, matrículas, concluintes, evasão e ocupação, turno principal, uso de ambiente crítico, minissérie 2017–2025 | PNP |
| **Capacidade** | Por recurso (salas por turno, ambiente crítico, docentes por área): disponível, uso calculado em 2025 para verificar, pico mantendo a oferta | Cadastro mínimo do campus + modelo |
| **Uso ao longo dos anos** | Mapa de calor recurso × ano até 2035 mantendo a oferta: lotação, folga, ociosidade | Modelo |
| **Oportunidades e limites** | Procura excedente, perda depois do ingresso, procura abaixo das vagas, ociosidade projetada | PNP + modelo |

### 8.4. Bancada: simulação longitudinal com capacidade

| Área | Conteúdo |
|---|---|
| **Pontos de partida** | Manter, Ampliar, Aproveitar melhor, Reorganizar, Combinada. São exemplos, não recomendações |
| **Alavancas combináveis** | Ampliar vagas (oferta, quantidade, ocupação das novas); Reorganizar (de, para, quantidade, turno das turmas novas); Preencher melhor (ocupação-alvo onde há procura); Reduzir evasão (hipótese, com faixa) |
| **Resposta em texto** | Um parágrafo gerado por regra que responde à pergunta do gestor: estudantes a mais atendidos e formados, recursos, primeira restrição, contribuição aos objetivos, efeito na matriz e exercício |
| **Curvas** | Nove indicadores selecionáveis; observado → manter → cenário até 2035; faixa; pandemia sombreada; marcas de começa, estabiliza e restrição; comparação opcional com os pontos de partida |
| **Capacidade no tempo** | Um pequeno gráfico por recurso: manter, cenário e linha de capacidade; pico destacado |
| **Indicadores e matriz** | Diferença em relação a manter por ano-base: ingressantes, matrículas, concluintes, ocupação, retidos, ME, percentuais do Ifes, MT, referência de Funcionamento + Reitoria com o exercício, professores-equivalentes; IEA e RAP como "não estimado" |
| **O que precisa ser verdade** | Gerado das alavancas e da restrição |

**Interação-chave demonstrada no protótipo:** em Serra, a combinação "reorganizar + preencher + reduzir evasão" esbarra em 2028 no laboratório de informática do matutino. Ao mudar o turno das turmas novas do integrado para o vespertino, a restrição do laboratório desaparece e sobra a de núcleo comum, que vira um pedido de recurso explícito na proposta.

### 8.5. Mesa: trajetória institucional

- **Gráfico da trajetória do Ifes** 2021–2035 (bloco comparável da matrícula equivalente) para formação técnica, formação de professores, concluintes e docentes adicionais: observado, manter, composição atual e até três combinações guardadas.
- **Linhas separadas** para unidades calculadas e para unidades sem simulação (ilustrativas), nunca somadas em silêncio.
- **Cruzamento de degrau:** ano-base em que a composição cruza 50% (se cruzar), o exercício correspondente e a referência condicional de Qualidade.
- **Tabela por unidade:** contribuição em 2030 e 2035, concluintes 2027–2035, pico de docentes, MT, primeira restrição de capacidade, natureza (calculado ou ilustrativo).
- **Conflito de objetivos:** a formação de professores projetada e sua posição em relação ao degrau de 20%.
