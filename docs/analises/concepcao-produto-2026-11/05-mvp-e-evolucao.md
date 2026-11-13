# 5 · Primeiro produto utilizável e evolução

> **Estudo de concepção de 12/11/2026, revisado na segunda rodada no mesmo dia.** Proposta de recorte. As datas são orientação, não compromisso.
> **Mudanças da segunda rodada (marcadas com [2ª rodada]):** a estrela-guia (participação na matriz) organiza o MVP; capacidade mínima por campus e projeção longitudinal entram na primeira jornada; MT por parâmetros de oferta e referência condicional deixam de estar fora do MVP. Nova definição do MVP no § 0. Justificativas no [documento 9](09-segunda-rodada.md).

---

## 0. Nova definição do MVP [2ª rodada]

> **O primeiro produto do PRUMO é o plano de oferta do próximo ciclo orientado pela estrela-guia: a instituição vê sua participação na matriz e os degraus ao alcance; cada campus constrói alternativas combinando alavancas, vê as curvas até 2035, a capacidade que elas exigem e quando esbarram, e o efeito nos objetivos e na matriz; a reitoria compõe as propostas, compara trajetórias institucionais e registra o pactuado.**

Continua com uma instituição (Ifes), quatro a seis unidades, sem integrações e sem modelo de linguagem. O que cresceu foi a profundidade da bancada e da ficha do campus, não o número de módulos. O que foi deliberadamente deixado de fora está no § 2.7 e no [documento 4, § 6](04-funcionalidades-e-specs.md#6-essencial--sofisticação-segunda-rodada).

O critério de sucesso da segunda rodada passa a ser o critério central de aceite do MVP: um diretor de campus consegue responder, para o próprio campus, *"se reorganizarmos a oferta, preenchermos melhor as vagas e reduzirmos a evasão, quantos estudantes a mais atenderemos e formaremos nos próximos anos, que indicadores podem melhorar, de quais recursos precisaremos e como isso contribui para os objetivos institucionais?"*. O [protótipo v2](prototipo/prumo-conceito.html) mostra essa resposta para Vitória e Serra.

---

## 1. Qual porta de entrada?

Cinco candidatas, avaliadas pelos mesmos critérios.

| Porta | Valor sem dado da instituição | Exercita a governança | Risco de virar o produto inteiro | Ancoragem num rito existente | Custo |
|---|---|---|---|---|---|
| **a. Simulador de oferta do campus** | Médio | Fraco: decisão isolada | Alto: "calculadora de campus" | Médio | Médio |
| **b. Leitura da Rede (inteligência)** | **Alto**: abre pronta para qualquer instituição | Nenhum | **Muito alto**: vira painel | Fraco | Baixo |
| **c. Pacto de degraus (50% técnico)** | Alto | Alto no discurso | Médio | Fraco: não há rito anual de "pacto de degraus" | Médio |
| **d. Plano de oferta orientado por objetivo** | Alto | **Alto**: composição de propostas reais | Baixo: atravessa as três capacidades | **Forte**: o ciclo anual de vagas | Médio-alto |
| **e. Conferência retroativa** | Alto | Médio | Baixo | Médio | Baixo, mas depende de d |

**Recomendação: (d), com (b) como primeira tela e (e) como demonstração do ciclo.**

- **O simulador não é a melhor porta sozinho.** Ele entrega valor ao diretor, mas não produz nada que a reitoria use, e repete o padrão de fragmentação dos protótipos (diagnóstico, § 4.1). Como parte de (d), ele é indispensável.
- **A leitura da Rede é a melhor primeira tela e o pior produto.** É o que o PRUMO mostra no primeiro minuto, para qualquer instituição. Mas, se for entregue sozinha, a pergunta seguinte é "e daí?".
- **O pacto de degraus confunde a régua com o objetivo.** O limiar da matriz é uma das três réguas de um objetivo, e o caso do técnico tem um problema próprio (documento 6, § 3.1).
- **O plano de oferta orientado por objetivo** usa a decisão que a instituição já toma todo ano, atravessa leitura, simulação e composição, e termina num objeto que a reitoria usa na reunião.

---

## 2. As nove perguntas

### 2.1. Qual é o primeiro problema concreto?

> **"Como preparar a definição de vagas do próximo ano de modo que as escolhas dos campi se somem para os objetivos da instituição, com fundamento e com o efeito conjunto visível antes de decidir?"**

Com dois objetivos em tensão, para forçar a composição a mostrar conflitos:

1. **Formação técnica** (percentual legal; meta legal e limiar da matriz em 50%). Conciliado com a matriz de 2026.
2. **Concluintes técnicos por ano** (contagem; agrega por soma). Ataca o achado central do estudo da PNP: no técnico do Ifes as vagas se preenchem e os concluintes caem.

**[2ª rodada]** Os dois objetivos ficam subordinados à estrela-guia: o primeiro é um degrau da Qualidade (≈ R$ 2,06 mi), o segundo move a MT (90% do bolo) e o IEA. A Agenda mostra a participação por bloco e o mapa de degraus completo ([documento 7](07-estrela-guia-e-indicadores.md)), mesmo para indicadores que o MVP não projeta (IEA e RAP aparecem como posição observada e margem).

O primeiro tem réguas externas. O segundo tem alavancas realmente distribuídas entre os campi. Juntos, mostram que a mesma decisão pode melhorar um e não o outro.

### 2.2. Quem usa a primeira versão?

- **Operador:** equipe de planejamento institucional do Ifes (duas a três pessoas).
- **Usuários locais:** direção de ensino de **quatro a seis campi** escolhidos por terem casos diferentes. Sugestão: Vitória e Serra (dados e alternativas da POC 0.0.2), Itapina e Barra de São Francisco (recomposição), e a unidade de educação a distância (é ela que move o percentual técnico).
- **Plateia:** Colégio de Dirigentes ou a câmara que trata das vagas, numa reunião real.

### 2.3. Quais dados?

| Dado | Origem | Situação |
|---|---|---|
| Indicadores de Gestão da PNP 2017–2025, todas as instituições | Exportação pública | Já obtida (fora do Git); carga a construir |
| Percentuais legais da matriz 2026, faixas de Qualidade | Demonstrativo do IFMT; Portaria 243/2026 | No repositório |
| Correspondência de unidades do Ifes entre edições | Curadoria | A fazer; pequena |
| Duração padrão por tipo de oferta | Norma e PPC | Premissa por tipo, ajustável |
| Decisões de oferta e premissas | Gestores | Informadas na bancada |
| Docentes por área, salas por turno, até três ambientes críticos | Direção de ensino do campus | **[2ª rodada]** Cadastro mínimo, 20 a 40 minutos por campus, verificado contra o uso de 2025 ([documento 8, § 2](08-capacidade-e-projecao.md#2-modelo-mínimo-de-capacidade-por-campus)) |
| Parâmetros de matriz por oferta (carga horária anual, peso, agropecuário) | Padrão pela norma ou importados da planilha da matriz da instituição | **[2ª rodada]** Premissa marcada; exata com a planilha |
| Dados da matriz 2026 da Rede (faixas, somas, submontantes) | Demonstrativo público C5 e Portaria 243/2026 | No repositório |
| Meta pactuada provisória | Reitoria | Informada na pauta |

Nada de integração com sistemas internos.

### 2.4. Qual é a experiência completa?

1. **Planejamento abre o PRUMO** e vê a Agenda com os dois objetivos, já preenchidos com dados públicos.
2. **Abre cada objetivo:** posição nas réguas, tendência, ponte por campus, objetivos em tensão. Guarda duas evidências.
3. **Abre a pauta** "Plano de oferta 2028", com os dois objetivos, meta pactuada provisória e prazo. Convida os campi do piloto.
4. **Cada diretor abre a ficha do campus:** contribuição atual, funis das ofertas, sinais. **[2ª rodada]** Confere a capacidade calculada para 2025 (salas por turno, ambiente crítico, docentes por área) e vê o mapa de uso até 2035 mantendo a oferta.
5. **Na bancada, combina alavancas** (reorganizar, preencher, reduzir evasão, ampliar, mudar turno), **vê as curvas** observado → manter → cenário até 2035, as fases do efeito, a primeira restrição de capacidade e o efeito nos objetivos e na matriz; ajusta premissas olhando a procedência, lê "o que precisa ser verdade" e **encaminha uma proposta**.
6. **Planejamento abre a mesa:** escolhe uma alternativa por campus, **compara trajetórias institucionais** de diferentes combinações até 2035, vê quando (e se) a composição cruza um degrau, os conflitos, os recursos pedidos, as restrições de cada campus e as alavancas restantes.
7. **Na reunião, a mesa é projetada** em modo reunião. Testam-se variações.
8. **A decisão é registrada** como pacto (na versão mínima: proposta marcada como pactuada, com data e instância).

### 2.5. Quais telas e interações?

| Tela | Essencial no MVP | Pode ser simplificado |
|---|---|---|
| Agenda | **[2ª rodada]** Estrela-guia por bloco, mapa de degraus, objetivos e pauta | "O que mudou" e compromissos a conferir ficam para a SPEC-002 |
| Objetivo | Régua tripla, ponte, trajetória, objetivos em tensão | Comparáveis: três instituições fixas por critério declarado |
| Ficha do campus | Contribuição, funis, **[2ª rodada]** capacidade com verificação 2025 e mapa de uso até 2035, sinais de oportunidade e limite | Sinais automáticos: procura excedente, perda depois do ingresso, procura abaixo das vagas, ociosidade |
| Bancada | **[2ª rodada]** Alavancas combináveis, curvas com faixas para nove indicadores, fases do efeito, capacidade no tempo, quadro de indicadores e matriz por ano-base e exercício, resposta em texto, premissas com procedência, "o que precisa ser verdade", encaminhar | Comparação com no máximo três pontos de partida |
| Mesa | Grade com razão das somas, **[2ª rodada]** trajetória institucional 2021–2035 com até três combinações comparadas, cruzamento de degrau e referência condicional, restrição por campus, conflitos, recursos, modo reunião | Alavancas restantes: lista simples |
| Proposta | Registro imutável com versão do cenário | Pareceres: um campo de texto |
| Gaveta "Como calcula" | Em todos os números | — |

### 2.6. Quais cálculos e regras são indispensáveis?

1. **Séries e blocos metodológicos:** percentuais legais, matrículas, ingressantes, concluintes, evasão anual por oferta e campus, respeitando a quebra de 2021 e a pandemia.
2. **Composição pela razão das somas** e **ponte por campus** (variação do numerador menos efeito no denominador), com a soma dos campi igual à variação da instituição.
3. **Motor de coortes** com ocupação, evasão, conclusão no prazo e retenção separadas, linha de base "manter", oferta nova por empréstimo e **erro medido fora da amostra** por tipo de oferta, exibido como faixa.
4. **Contribuição de uma alternativa aos objetivos:** variação de matrícula equivalente técnica e total (para o percentual) e de concluintes.
5. **Calendário dos três marcos** com a defasagem do exercício (RMO-070).
6. **Professores-equivalentes por premissa simples** (aulas por turma, horas por professor), como nos protótipos, marcado como premissa.
7. **[2ª rodada] Capacidade:** turmas simultâneas por oferta, turno e ano; uso de salas, ambientes críticos e docentes por área; primeira restrição; ociosidade.
8. **[2ª rodada] Matriz:** MT por parâmetros de oferta (RMO-066); referência marginal de Funcionamento + Reitoria; faixas e valor de degrau de Qualidade (F-29, Rede 2026 constante); exercício = ano-base + 2.
9. **[2ª rodada] Fases do efeito:** começa, intensifica, estabiliza, restrição, por regra declarada.

**Fora do MVP:** reprodução exata da MT dos ciclos existentes, cenários de crescimento da Rede, regra interna e retorno ao campus (SPEC-005); IEA e RAP da matriz projetados (não estimáveis); capacidade nível 3 e custos (SPEC-004).

### 2.7. O que pode ser adiado?

Pacto formal com horizontes e conferência (SPEC-002, logo em seguida); explorador da Rede e precedentes automáticos (SPEC-003); **[2ª rodada]** capacidade nível 3, custos e investimentos (SPEC-004); reprodução exata da MT, cenários da Rede e regra interna (SPEC-005); segunda instituição, login institucional e isolamento por linha (SPEC-006); nota técnica (SPEC-007); integrações; IA.

### 2.8. Como demonstrar o valor?

Pelo uso numa decisão real, não por demonstração ao idealizador.

| Teste | Critério de sucesso | Hipótese da visão |
|---|---|---|
| Sessão de 30 minutos com cada diretor do piloto, usando a bancada no próprio campus | O diretor altera ao menos uma premissa depois de ver a procedência e encaminha uma proposta que levaria à reitoria | H3, H4 |
| Leitura do objetivo com a equipe de planejamento | A equipe identifica um fato que muda a explicação que dava para a variação (ex.: o peso da unidade de EaD) | H2 |
| Uso da mesa numa reunião real de definição de vagas | A reunião discute contribuições diferentes por campus em vez de meta igual; ao menos uma decisão é tomada ou adiada por causa do que a mesa mostrou | H1, H6 |
| Comparação sem leitura de ranking | Nenhum participante interpreta a ponte ou os funis como classificação de campi | H5 |

Registrar: onde o gestor hesitou, que premissas mudou, que perguntas a ferramenta não respondeu. Esse registro orienta a ordem das SPEC-003 a 005.

### 2.9. Como o primeiro recorte evolui para a visão completa?

```
MVP (SPEC-001)                → um ciclo: ler, propor, compor, decidir
  + SPEC-002 Pacto e conferência → o ciclo fecha: o que se decidiu é conferido
  + SPEC-003 Leitura da Rede     → premissas e argumentos melhores
  + SPEC-004 Capacidade          → decisões que cabem
  + SPEC-005 Orçamento           → efeito condicional e incentivos explícitos
  + SPEC-006 Segunda instituição → produto da Rede
  + SPEC-007 Documento           → a decisão circula no processo administrativo
```

A governança distribuída não espera: o MVP já termina na mesa de composição com propostas reais. O que fica para depois é a **sofisticação do rito** (horizontes, conferência, pareceres estruturados), não o **conceito** de contribuição e composição. É o que o documento fundador pede (§ 0.1).

---

## 3. Incrementos dentro da SPEC-001

Para que cada etapa produza algo demonstrável:

| Incremento | Entrega | Demonstrável para |
|---|---|---|
| **I1 · Começa sabendo** | Carga da PNP, **estrela-guia e mapa de degraus**, objetivos com régua tripla, ponte por campus, trajetória, "como calcula" | Planejamento: "onde estamos, quanto vale cada degrau e quem explica" |
| **I2 · Campus e bancada** | Funis, **cadastro e verificação de capacidade**, motor de coortes com teste fora da amostra, **curvas com faixas**, alavancas combináveis, efeito na matriz, proposta | Um diretor de campus, respondendo à pergunta do critério de sucesso |
| **I3 · Mesa** | Propostas de vários campi compostas, **trajetória institucional e comparação de combinações**, cruzamento de degrau, conflitos, modo reunião, registro | Reunião de vagas |

**[2ª rodada]** I2 ficou maior. Se for preciso cortar, a ordem é: primeiro a comparação com pontos de partida, depois o terceiro ambiente crítico, depois indicadores secundários das curvas (retidos, ME). Curvas de matrículas, ingressantes e concluintes, capacidade de salas e docentes por área e o efeito na matriz não se cortam.

Se I1 não convencer a equipe de planejamento de que a leitura muda alguma explicação, vale parar e revisar antes de construir I2.

---

## 4. Calendário de referência

**[HIPÓTESE]** A definição de vagas para o processo seletivo de 2028 acontece entre o primeiro e o segundo semestre de 2027. A confirmar com a pró-reitoria de ensino.

| Período | Atividade |
|---|---|
| Nov–dez 2026 | Decisões estratégicas (documento 6, § 6); três conversas de confirmação do rito; novo repositório e SPEC-001 especificada |
| Jan–mar 2027 | I1 e I2; teste da bancada com dois diretores |
| Abr–mai 2027 | I3; carga da edição da PNP com ano-base 2026, se publicada |
| Ciclo de vagas 2028 | Uso real no piloto |
| 2º semestre 2027 | SPEC-002 com conferência retroativa |

O alvo que importa é **usar o PRUMO no ciclo real de vagas de 2028**. Perder esse ciclo empurra a primeira validação real em um ano.

---

## 5. Riscos do recorte

> **[2ª rodada]** Os riscos de complexidade introduzidos por esta rodada e as simplificações adotadas estão no [documento 9, § 7](09-segunda-rodada.md#7-riscos-de-complexidade-e-simplificações-adotadas).

| Risco | Mitigação |
|---|---|
| O rito anual de vagas não é um momento de decisão conjunta no Ifes (é só consolidação de pedidos) | Confirmar antes de especificar. Se for o caso, o PRUMO pode **criar** a conversa, mas a adoção fica mais difícil; ajustar o patrocinador |
| O motor de coortes erra muito em ofertas não integradas e em concluintes | Faixas pelo erro fora da amostra; contribuição em concluintes com faixa larga; nunca um número só |
| A alternativa "agir sobre permanência" domina sem evidência | Marcada como hipótese; faixa larga; "o que precisa ser verdade" em destaque; a mesa mostra quantas contribuições dependem de hipótese |
| Diretores não têm tempo | A bancada abre com alternativas sugeridas pela forma do funil (não recomendadas: exemplos), preenchidas com a evidência do campus |
| Percepção de ranking | Ordenação por nome ou porte; nenhuma cor de "pior"; teste explícito (H5) |
| Expectativa de valor em reais | Dizer na primeira tela o que o MVP não calcula e por quê |
