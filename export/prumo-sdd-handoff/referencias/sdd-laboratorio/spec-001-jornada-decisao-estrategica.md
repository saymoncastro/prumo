# Especificação: Jornada de decisão estratégica institucional

**Branch da funcionalidade**: `001-jornada-decisao-estrategica`

**Criada em**: 2026-11-11

**Situação**: Rascunho

**Origem**: [próximo passo, § 3.3](../../docs/produto/proximo-passo.md) e [visão de produto](../../docs/produto/visao-prumo.md). Segue os [princípios do projeto](../../.specify/memory/constitution.md), citados abaixo por número (P-I a P-X).

**Resumo**: primeira fatia navegável do PRUMO. Um gestor parte de um objetivo institucional, entende como a instituição chegou à posição atual, simula alternativas de oferta num campus, vê como propostas de campi diferentes se compõem e registra uma proposta fundamentada. A fatia é estreita, mas atravessa as três capacidades do produto: inteligência histórica, simulação estratégica e governança distribuída.

A especificação é **genérica quanto ao objetivo**. O percentual de formação técnica é o caso demonstrativo. Um segundo objetivo deve caber sem mudança de estrutura.

## Cenários de uso e testes *(obrigatório)*

Dois atores: o **gestor institucional** (reitoria, planejamento) e o **gestor de campus** (direção-geral, direção de ensino). Nesta fatia não há controle de acesso: a mesma pessoa pode percorrer a jornada nos dois papéis, e o papel fica registrado em tudo o que ela cria.

Não há ordem obrigatória entre as histórias. O gestor pode entrar por qualquer uma e levar para as outras o que produziu.

### História 1 — Ver o objetivo institucional e a posição atual (Prioridade: P1)

O gestor institucional abre um objetivo compartilhado da instituição. Vê o indicador, suas réguas (meta legal, limiar orçamentário e meta pactuada, quando existirem), a posição atual da instituição e quanto cada campus contribui para o numerador e para o denominador.

**Por que esta prioridade**: o objetivo institucional é o que orienta as outras capacidades (P-I). Sem ele, a inteligência vira painel e a simulação vira calculadora de campus.

**Teste independente**: abrir o objetivo demonstrativo e conferir que a posição institucional e a contribuição de cada campus reproduzem os valores de referência documentados no portão de dados.

**Cenários de aceite**:

1. **Dado** um objetivo com meta legal e limiar orçamentário, **quando** o gestor o abre, **então** vê cada régua separada, com seu valor, sua fonte normativa e o exercício a que se aplica.
2. **Dado** um objetivo sem meta pactuada, **quando** o gestor o abre, **então** essa régua aparece como "não definida", e não como zero nem omitida.
3. **Dado** o objetivo aberto, **quando** o gestor consulta a posição atual, **então** vê o valor institucional calculado pela razão das somas dos campi, com ano-base, fonte e fórmula.
4. **Dado** o objetivo aberto, **quando** o gestor consulta os campi, **então** vê o numerador e o denominador de cada um e o quanto cada campus aproxima ou afasta a instituição das réguas, sem ordenação por desempenho.
5. **Dado** qualquer número da tela, **quando** o gestor pede sua origem, **então** vê natureza, fonte, ano-base, versão da regra e fórmula.

---

### História 2 — Examinar a trajetória e registrar evidências (Prioridade: P2)

A partir do objetivo, o gestor examina como o indicador evoluiu na instituição, em seus campi e na Rede Federal. Decompõe a variação entre dois anos, compara com instituições ou campi de trajetória parecida e registra o que encontrou como evidência, que poderá anexar depois a uma premissa ou a uma proposta.

**Por que esta prioridade**: a inteligência se mede pelo que o gestor leva dela (visão § 4.1). É também a capacidade mais comprovada e a única que funciona só com dados públicos.

**Teste independente**: para o objetivo demonstrativo, obter a trajetória da instituição, de um campus e da Rede, registrar uma evidência e reencontrá-la depois, com recorte, fonte e limite.

**Cenários de aceite**:

1. **Dado** um objetivo, **quando** o gestor pede a trajetória, **então** vê a série da instituição, de cada campus e da Rede, apenas dentro do bloco de anos comparáveis para aquele indicador.
2. **Dado** uma série com quebra conhecida (mudança de fórmula, pandemia, reclassificação), **quando** ela é exibida, **então** a quebra aparece marcada na própria série, e valores de blocos diferentes não são ligados nem comparados.
3. **Dado** dois anos do mesmo bloco, **quando** o gestor pede a decomposição da variação, **então** vê quanto veio do numerador e quanto do denominador, e quais campi explicam a mudança institucional.
4. **Dado** uma instituição ou um campus, **quando** o gestor pede comparáveis, **então** vê casos escolhidos por perfil e trajetória, com o critério declarado e sem ordenação por desempenho.
5. **Dado** um resultado em tela, **quando** o gestor o registra como evidência, **então** ela guarda o recorte, o método, a fonte, o limite de interpretação, o autor e o papel dele.
6. **Dado** uma evidência registrada, **quando** o gestor a classifica, **então** escolhe entre fato observado, padrão ou associação e hipótese; hipótese exige dizer o que a confirmaria.
7. **Dado** qualquer texto gerado pela plataforma sobre uma variação, **quando** exibido, **então** descreve o que mudou e o que andou junto, sem afirmar causa nem intenção.

---

### História 3 — Simular alternativas de oferta num campus (Prioridade: P3)

O gestor de campus monta alternativas de oferta para o seu campus: abrir, ampliar, reduzir ou encerrar vagas numa oferta a partir de um ano. Para cada alternativa, vê ano a ano o que ela entrega (ingressantes, matrículas, concluintes, efeito no objetivo institucional) e de onde vem cada premissa usada.

**Por que esta prioridade**: é o que liga a evidência histórica a uma decisão futura. Depende das histórias 1 e 2 para ter contexto e premissas com origem.

**Teste independente**: num campus com premissas preparadas, montar a linha de base e duas alternativas, e conferir que os resultados ano a ano e o efeito no objetivo são reproduzíveis a partir das premissas exibidas.

**Cenários de aceite**:

1. **Dado** um campus, **quando** o gestor abre a simulação, **então** vê a linha de base: o que acontece se nada mudar, já com o efeito das turmas em curso.
2. **Dado** a linha de base, **quando** o gestor cria uma alternativa, **então** as decisões são expressas em vagas por oferta e por ano de ingresso, e nunca em matrículas.
3. **Dado** uma alternativa, **quando** o gestor consulta os resultados, **então** vê, para cada ano, ingressantes, matrículas e concluintes, e o valor do indicador do objetivo para o campus e para a instituição.
4. **Dado** os resultados de uma alternativa, **quando** exibidos, **então** distinguem o ano da decisão, o ano-base em que o efeito aparece nos dados e o exercício orçamentário que usa esse ano-base.
5. **Dado** uma premissa da simulação, **quando** o gestor a consulta, **então** vê seu valor, sua origem (histórico da própria oferta, empréstimo de oferta equivalente ou julgamento do gestor), o valor histórico correspondente e a faixa dos comparáveis.
6. **Dado** uma premissa, **quando** o gestor a altera, **então** a origem passa a "julgamento do gestor", o valor anterior continua visível e ele pode anexar uma evidência registrada.
7. **Dado** uma oferta nova, sem histórico, **quando** simulada, **então** suas premissas são emprestadas de oferta equivalente e identificadas como empréstimo.
8. **Dado** um tipo de oferta em que o modelo erra mais ao reproduzir anos fora do ajuste, **quando** o resultado é exibido, **então** aparece em faixa, com o erro medido informado.
9. **Dado** duas ou três alternativas, **quando** o gestor as compara, **então** as vê lado a lado com a linha de base, sem que a plataforma indique a melhor.
10. **Dado** uma alternativa, **quando** o gestor pede "o que precisa ser verdade", **então** vê a lista das premissas de que o resultado mais depende.

---

### História 4 — Registrar uma proposta fundamentada (Prioridade: P4)

O gestor de campus escolhe uma alternativa e a registra como proposta do campus: contribuição ao objetivo, indicadores projetados, premissas, evidências anexadas, fontes e limites.

**Por que esta prioridade**: é o objeto que a governança consome. Sem a proposta, a simulação termina em si mesma.

**Teste independente**: registrar uma proposta a partir de uma alternativa, fechar e reabrir a plataforma e reencontrar a proposta íntegra, legível por alguém que não a montou.

**Cenários de aceite**:

1. **Dado** uma alternativa simulada, **quando** o gestor a registra como proposta, **então** a proposta guarda as decisões de oferta, a contribuição ao objetivo em numerador e denominador por ano, as premissas com origem, as evidências anexadas, a versão das regras e dos dados, o autor e o papel dele.
2. **Dado** uma proposta registrada, **quando** exibida, **então** está marcada como proposta, distinta de oferta aprovada e de compromisso pactuado.
3. **Dado** uma proposta registrada, **quando** exibida, **então** lista seus limites: o que não foi estimado, o que foi emprestado e onde o modelo erra mais.
4. **Dado** uma proposta registrada, **quando** os dados públicos ou as regras são atualizados, **então** a proposta continua mostrando os valores com que foi feita e indica que há versão mais recente.
5. **Dado** uma proposta registrada, **quando** o gestor volta em outra sessão ou em outro equipamento, **então** ela está disponível.
6. **Dado** uma proposta registrada, **quando** o gestor a revisa, **então** a versão anterior é preservada.

---

### História 5 — Compor propostas de campi diferentes (Prioridade: P5)

O gestor institucional reúne propostas de campi diferentes e vê o efeito agregado no objetivo, ano a ano, e onde a combinação conflita com outros objetivos institucionais.

**Por que esta prioridade**: é a finalidade do produto (P-VIII) e a parte menos demonstrada até aqui. Fica por último só porque depende de existirem propostas.

**Teste independente**: com propostas de pelo menos dois campi, montar uma composição e conferir que o valor institucional resulta da soma de numeradores e denominadores, e não da média dos percentuais.

**Cenários de aceite**:

1. **Dado** propostas de campi diferentes, **quando** o gestor monta uma composição, **então** escolhe no máximo uma proposta por campus; os campi sem proposta entram com a linha de base.
2. **Dado** uma composição, **quando** exibida, **então** mostra o indicador institucional por ano, calculado pela razão das somas, diante de cada régua do objetivo.
3. **Dado** uma composição, **quando** exibida, **então** mostra a contribuição de cada campus em numerador e denominador, que pode ser diferente de campus para campus.
4. **Dado** uma composição, **quando** ela melhora o objetivo em exame e piora outro objetivo cadastrado, **então** o conflito aparece com o valor do outro objetivo antes e depois.
5. **Dado** uma composição que não alcança uma régua, **quando** exibida, **então** mostra quanto falta, em numerador ou denominador, sem distribuir a diferença automaticamente entre os campi.
6. **Dado** duas composições, **quando** o gestor as compara, **então** as vê lado a lado, sem que a plataforma indique a melhor.
7. **Dado** uma composição, **quando** o gestor a guarda, **então** ela fica registrada como composição em estudo, distinta de pacto.

---

### Casos de borda

- **Campus sem premissas preparadas**: a simulação não é oferecida para ele. Na composição, entra com a linha de base, identificado como "sem simulação".
- **Indicador que não se reconcilia com a fonte oficial**: o objetivo pode ser cadastrado, mas a posição atual aparece como "não estimada", com o motivo.
- **Denominador zero ou campus sem oferta no recorte**: o percentual do campus aparece como "não se aplica"; numerador e denominador continuam entrando na soma institucional.
- **Campus cujo nome mudou na fonte pública entre edições**: a série é contínua, porque a identidade do campus não depende do nome.
- **Unidades atípicas** (reitoria, polos de educação a distância): aparecem identificadas como tais e entram na soma institucional conforme a regra do indicador.
- **Ano do horizonte que ultrapassa o último exercício com regra publicada**: o resultado é exibido com a última regra conhecida, marcada como premissa.
- **Proposta feita com dados ou regras já substituídos**: continua válida como registro, com aviso de versão.
- **Duas propostas do mesmo campus na mesma composição**: não é permitido; o gestor escolhe uma.
- **Alternativa que reduz vagas abaixo de turmas já ingressadas**: as turmas em curso seguem até o fim; o efeito da redução só começa no ingresso seguinte.

## Requisitos *(obrigatório)*

### Requisitos funcionais

**Objetivo institucional**

- **RF-001**: O sistema DEVE representar um objetivo institucional por: indicador (numerador, denominador e regra de cálculo), réguas e horizonte. Nenhum objetivo específico DEVE estar fixo na estrutura.
- **RF-002**: O sistema DEVE admitir até três réguas por objetivo (meta legal, limiar orçamentário, meta pactuada), cada uma com valor, fonte e exercício, e DEVE exibir como "não definida" a régua ausente.
- **RF-003**: O sistema DEVE calcular a posição institucional pela soma dos numeradores dividida pela soma dos denominadores dos campi.
- **RF-004**: O sistema DEVE mostrar a contribuição de cada campus em numerador e denominador, sem ordená-los por desempenho.
- **RF-005**: O sistema DEVE trazer cadastrado o objetivo demonstrativo (percentual de formação técnica) e pelo menos um segundo objetivo de mesma natureza, ambos percorríveis pelas histórias 1, 2 e 5 com a mesma estrutura.

**Natureza e origem**

- **RF-006**: Todo número exibido DEVE informar, a pedido, natureza (fato observado, estimado, premissa, hipótese, resultado simulado ou não estimado), fonte, ano-base, versão da regra e fórmula.
- **RF-007**: O sistema DEVE exibir "não estimado", com o motivo, sempre que um valor não puder ser calculado com os dados disponíveis.
- **RF-008**: O sistema DEVE manter como objetos distintos: série observada, evidência, hipótese, premissa, resultado simulado, alternativa, proposta e composição.

**Inteligência e contexto**

- **RF-009**: O sistema DEVE exibir a trajetória do indicador de um objetivo para a instituição, cada campus e a Rede Federal, restrita a blocos de anos metodologicamente comparáveis.
- **RF-010**: O sistema DEVE registrar as quebras de série como atributo da série e exibi-las junto dela.
- **RF-011**: O sistema DEVE decompor a variação do indicador entre dois anos do mesmo bloco em efeito do numerador e do denominador, e em contribuição por campus.
- **RF-012**: O sistema DEVE oferecer comparáveis por perfil e trajetória, com o critério declarado.
- **RF-013**: O gestor DEVE conseguir registrar um resultado como evidência, com recorte, método, fonte, limite, classificação de natureza, autor e papel.
- **RF-014**: O sistema NÃO DEVE afirmar causa nem atribuir intenção em nenhum texto que produza.
- **RF-015**: A inteligência DEVE ser apresentada como investigação guiada a partir do objetivo, por perguntas fixas: como chegamos aqui, quais campi explicam a mudança e o que aconteceu em comparáveis. Exploração livre de instituições, ofertas e períodos fica fora desta entrega.

**Alternativas locais**

- **RF-016**: O sistema DEVE oferecer simulação para os quatro campi que já têm premissas preparadas: Vitória, Serra, Itapina e Barra de São Francisco. Os demais campi entram no objetivo, na trajetória e na composição com a linha de base. A lista de campi com simulação DEVE ser dado, não estrutura.
- **RF-017**: O sistema DEVE calcular a linha de base de um campus com as turmas em curso e a oferta atual mantida.
- **RF-018**: O gestor DEVE conseguir criar alternativas alterando vagas por oferta e por ano de ingresso, incluindo oferta nova e encerramento.
- **RF-019**: O sistema DEVE projetar, por ano, ingressantes, matrículas e concluintes de cada oferta, com ocupação, evasão, conclusão e retenção como premissas separadas.
- **RF-020**: O sistema DEVE mostrar o efeito de cada alternativa no indicador do objetivo, para o campus e para a instituição, com os demais campi na linha de base.
- **RF-021**: O sistema DEVE distinguir, em cada resultado, ano da decisão, ano-base e exercício orçamentário.
- **RF-022**: Cada premissa DEVE ter valor, origem (histórico próprio, empréstimo ou julgamento), referência histórica e faixa dos comparáveis; a alteração pelo gestor DEVE preservar o valor anterior e admitir evidência anexada.
- **RF-023**: O modelo de projeção DEVE ter seu erro medido em anos fora do ajuste, por tipo de oferta, e esse erro DEVE ser exibido ao gestor.
- **RF-024**: O sistema DEVE exibir em faixa o resultado dos tipos de oferta cujo erro fora do ajuste supera 5%, com a largura da faixa dada pelo erro medido. Até 5%, exibe valor único com o erro informado. O limite DEVE ser parâmetro.
- **RF-025**: O sistema DEVE permitir comparar alternativas lado a lado com a linha de base e listar as premissas de que cada resultado mais depende.
- **RF-026**: O sistema NÃO DEVE recomendar alternativa nem ordenar ofertas por retorno.

**Proposta fundamentada**

- **RF-027**: O gestor DEVE conseguir registrar uma alternativa como proposta do campus, com decisões de oferta, contribuição ao objetivo por ano, premissas, evidências, limites, versão de dados e regras, autor e papel.
- **RF-028**: Propostas, evidências, alternativas e composições DEVEM persistir entre sessões e equipamentos.
- **RF-029**: Uma proposta DEVE conservar os valores com que foi registrada e indicar quando há dados ou regras mais recentes; revisões DEVEM preservar a versão anterior.
- **RF-030**: O sistema DEVE marcar toda proposta como proposta, distinta de oferta aprovada e de compromisso.

**Composição institucional**

- **RF-031**: O gestor DEVE conseguir montar composições com no máximo uma proposta por campus; campi sem proposta entram com a linha de base.
- **RF-032**: O sistema DEVE calcular o indicador institucional da composição, por ano, pela razão das somas, e exibi-lo diante de cada régua.
- **RF-033**: O sistema DEVE mostrar o efeito da composição nos demais objetivos cadastrados e destacar aqueles que pioram.
- **RF-034**: O sistema DEVE mostrar quanto falta para cada régua e NÃO DEVE distribuir a diferença entre os campi automaticamente.
- **RF-035**: O sistema DEVE permitir comparar composições e guardá-las como composição em estudo, distinta de pacto.

**Instituição e dados**

- **RF-036**: A instituição, seus campi, suas unidades atípicas e suas exceções DEVEM ser dados ou configuração. A jornada DEVE funcionar para outra instituição da Rede apenas com troca de dados, no que depende só de dados públicos (histórias 1 e 2).
- **RF-037**: Dados públicos compartilhados (série da Rede, normas, regras por exercício) DEVEM ficar separados dos dados da instituição (objetivos pactuados, premissas, evidências, alternativas, propostas, composições).
- **RF-038**: Cada campus DEVE ter identidade estável, independente do nome usado na fonte pública.
- **RF-039**: Tudo o que o gestor cria DEVE registrar autor e papel (institucional ou local), mesmo sem controle de acesso.
- **RF-040**: O sistema DEVE funcionar só com dados agregados por oferta e por campus, sem dados pessoais.
- **RF-041**: Todo número DEVE ser produzido por cálculo determinístico e reproduzível; nenhum número DEVE ser produzido por modelo de linguagem.

### Entidades principais

- **Instituição**: quem contrata e para quem os objetivos valem. Tem unidades.
- **Unidade (campus)**: quem decide a oferta. Identidade estável; pode ser atípica.
- **Oferta**: curso numa unidade, com tipo, forma, modalidade e turno. É a unidade de decisão.
- **Turma**: coorte de ingresso de uma oferta. É a unidade de projeção no tempo.
- **Série observada**: indicador por recorte e ano-base, com fonte, versão e blocos comparáveis.
- **Regra**: fórmula ou parâmetro normativo, versionado por exercício.
- **Objetivo institucional**: indicador, réguas e horizonte.
- **Evidência**: fato, padrão ou hipótese registrado, com recorte, método, fonte e limite.
- **Premissa**: valor assumido, com natureza e origem.
- **Alternativa (cenário)**: linha de base, decisões de oferta, premissas e versão das regras; produz resultados simulados.
- **Proposta**: alternativa escolhida por uma unidade, com contribuição a um ou mais objetivos.
- **Composição**: conjunto de propostas de unidades diferentes, com o resultado institucional.

Previstas no modelo e fora desta entrega: **Compromisso** (proposta pactuada), **Resultado observado** (série posterior lida contra o compromisso) e **Capacidade** (docentes e ambientes).

## Critérios de sucesso *(obrigatório)*

### Resultados mensuráveis

- **CS-001**: O idealizador percorre a jornada completa, do objetivo à proposta registrada e à composição com pelo menos dois campi, em até 30 minutos e sem ajuda externa.
- **CS-002**: A posição institucional e a contribuição por campus do objetivo demonstrativo coincidem com os valores de referência documentados no portão de dados, na precisão ali publicada.
- **CS-003**: 100% dos números exibidos informam natureza, fonte, ano-base e fórmula.
- **CS-004**: O segundo objetivo é cadastrado e percorrido nas histórias 1, 2 e 5 sem alteração de estrutura, só com dados e configuração.
- **CS-005**: Toda composição exibida tem o indicador institucional igual à razão das somas dos campi, conferível à mão com os valores em tela.
- **CS-006**: Uma segunda instituição da Rede Federal é percorrida nas histórias 1 e 2 só com troca de dados públicos e configuração.
- **CS-007**: Um leitor que não montou a proposta consegue dizer, lendo apenas a proposta registrada, o que muda na oferta, quanto contribui para o objetivo, em que anos, com quais premissas e com quais limites.
- **CS-008**: Todo tipo de oferta simulado tem erro fora do ajuste medido e exibido; nenhum resultado é apresentado sem essa informação.
- **CS-009**: Nenhuma tela ordena instituições, campi ou ofertas por desempenho, e nenhuma indica uma alternativa como a recomendada.
- **CS-010**: Propostas e evidências registradas numa sessão são reencontradas íntegras em outra sessão e em outro equipamento.

## Esclarecimentos

### Sessão de 2026-11-11

- P: Que forma tem a inteligência histórica na interface? → R: Investigação guiada a partir do objetivo (RF-015).
- P: Quais campi têm simulação na primeira fatia? → R: Os quatro com premissas preparadas (RF-016).
- P: A partir de que erro fora do ajuste o resultado aparece em faixa? → R: Acima de 5% (RF-024).

## Premissas

- **Quem avalia**: o idealizador, sozinho. Os critérios CS-001 a CS-010 são o que ele confere. As hipóteses H1 a H6 da visão, sobre a reação de gestores, não são testadas por esta entrega.
- **Sem controle de acesso**: uma pessoa pode atuar nos dois papéis. O papel é registrado, não imposto.
- **Uma instituição com dados próprios**: o Ifes. A separação entre dado público e dado da instituição existe no modelo; operar várias instituições clientes não faz parte desta entrega.
- **Fontes**: exportação pública dos Indicadores de Gestão da PNP (2017–2025) e regras da matriz documentadas na fonte canônica. A atualização dos dados é manual, uma vez por edição da PNP.
- **Segundo objetivo**: outro percentual legal já conciliado no portão de dados (educação de jovens e adultos ou formação de professores).
- **Horizonte de simulação**: o suficiente para cobrir um ciclo completo da oferta mais longa simulada mais a defasagem até o exercício orçamentário.
- **Protótipos anteriores**: são referência de comportamento e de valores esperados. O código deles não é base desta entrega.
- **Fora desta especificação, previsto no modelo**: pactuação formal e acompanhamento nos três horizontes; capacidade docente e física; referência financeira; mais de uma instituição cliente; controle de acesso; integração com sistemas acadêmicos.
