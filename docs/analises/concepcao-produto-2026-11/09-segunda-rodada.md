# 9 · Síntese da segunda rodada

> **12/11/2026.** Segunda rodada crítica do estudo de concepção. Foco: capacidade institucional de execução, projeção longitudinal e impacto nos indicadores estratégicos e orçamentários, com a participação na matriz como estrela-guia, por orientação do idealizador.
> **O que mudou nos documentos:** novos [7](07-estrela-guia-e-indicadores.md) e [8](08-capacidade-e-projecao.md); revisões marcadas com "[2ª rodada]" nos documentos [1](01-visao-concreta.md), [2](02-experiencia-e-interfaces.md), [3](03-arquitetura-e-stack.md), [4](04-funcionalidades-e-specs.md), [5](05-mvp-e-evolucao.md) e [6](06-avaliacao-critica.md). Nada foi apagado sem registro: onde a primeira versão errou, a revisão cita o que dizia.
> **Protótipo:** [v2](prototipo/prumo-conceito.html), montado por [`montar.py`](prototipo/montar.py) a partir do template, de [`simulacao.js`](prototipo/simulacao.js), do motor `poc/coortes002.js` (sem alteração) e de um recorte público de `poc/dados-poc002.json`. A [v1](prototipo/prumo-conceito-v1.html) foi preservada.

---

## 1. O que já estava corretamente contemplado

| Elemento | Onde estava | Por que continua |
|---|---|---|
| Ciclo anual de oferta como ritmo do produto | Documento 1 | É o que dá lugar natural à estrela-guia: a matriz chega uma vez por ano, junto da PNP |
| Seis telas (Agenda, Objetivos, Campus, Bancada, Mesa, Pacto) | Documento 2 | Bastaram. Nenhuma tela nova foi necessária, só profundidade |
| Decisão em vagas, consequência em concluintes | Princípio VII; documento 1 | O motor de coortes com mecanismos separados continua sendo a base de tudo |
| Composição pela razão das somas, conflitos entre objetivos | Documentos 2 e 4 | A trajetória institucional usa a mesma regra |
| Natureza de todo número, "não estimado" explícito | Princípios II e VII | Foi o que permitiu trazer a matriz para o MVP sem falsa precisão |
| Stack (Django, motor puro, HTMX com ilhas) | Documento 3 | Comporta capacidade e curvas; a bancada provavelmente vira a ilha interativa |
| Conferência pela PNP seguinte, desvio explicado | SPEC-002 | Ganha a decomposição "o que fizemos × o que a Rede fez" da participação |

## 2. O que estava subdimensionado

| Elemento | Como estava | Problema | Como ficou |
|---|---|---|---|
| **Capacidade** | "Recurso crítico: um campo livre por decisão" no MVP; estrutura na SPEC-004 | Não verificável, não reutilizável, não permite comparar propostas de campi diferentes; desfazia o que a recomposição já mostrava (laboratório esgotado em 2029) | Modelo mínimo estruturado na SPEC-001: turmas simultâneas, salas por turno, até três ambientes críticos, docentes por área, verificação contra 2025 ([documento 8, § 2](08-capacidade-e-projecao.md#2-modelo-mínimo-de-capacidade-por-campus)) |
| **Matriz** | "Uma das três réguas"; reais só na SPEC-005; "fora do MVP: MT, valores em reais" | Deixava de fora justamente o que o patrocinador pergunta, embora os degraus já estejam reproduzidos (V-13) e a regra de MT, validada | Estrela-guia na Agenda; mapa de degraus; MT por parâmetros de oferta; referência condicional por exercício, já na SPEC-001 ([documento 7](07-estrela-guia-e-indicadores.md)) |
| **Docentes** | Professores-equivalentes totais | Total não revela gargalo; gargalo é por área | Docentes por área (núcleo comum e eixos técnicos) |
| **Mesa** | Posição final nas réguas | Não mostra quando a instituição chega lá nem compara caminhos | Trajetória institucional 2021–2035 com até três combinações comparadas |

## 3. O que realmente faltava

1. **A estrela-guia.** O estudo não tinha uma métrica única que organizasse as demais. A participação na matriz cumpre esse papel, é comum às 41 instituições e só se move por resultados educacionais. Faltava também a leitura que ela revela: **o Ifes participa com 3,56% de Funcionamento e Reitoria, mas só com 1,20% de Qualidade**; o espaço está nos degraus institucionais.
2. **A taxa de câmbio entre alavancas.** Sem ela, não há como comparar "reduzir evasão em Vitória" com "decidir a oferta a distância do Cefor". Uma MT presencial vale ≈ R$ 1,3 mil por exercício; o degrau de 50% em técnico vale ≈ 1.550 MT.
3. **As curvas.** A primeira rodada trocou as curvas da POC 0.0.2 por uma tabela de resultados finais e uma linha de marcos. Faltava o principal diferencial que o idealizador apontou: observado → manter → cenário, com faixas e com a capacidade no mesmo tempo.
4. **As fases do efeito** (começa, intensifica, estabiliza, restrição), calculadas por regra declarada.
5. **A classificação dos indicadores** em quatro classes, indicador por indicador ([documento 7, § 6](07-estrela-guia-e-indicadores.md#6-classificação-dos-indicadores)).
6. **A ociosidade**: capacidade liberada quando uma oferta encolhe ou muda de turno.
7. **A verificação da capacidade** contra o presente, equivalente ao portão de dados.
8. **Um dado institucional barato e decisivo**: a planilha da matriz que a instituição já recebe, como fonte dos parâmetros por oferta.

## 4. Mudanças na experiência

| Tela | Antes | Depois |
|---|---|---|
| **Agenda** | Objetivos, pauta, o que mudou | Abre na **estrela-guia por bloco** e no **mapa de degraus** com valor e alavanca |
| **Objetivos** | Régua tripla, ponte, tensão | **Árvore de alavancas** com a classe de cada ligação; **taxa de câmbio** |
| **Ficha do campus** | Funis e sinais | Funis com turno e minissérie; **capacidade com verificação 2025**; **mapa de calor de uso até 2035**; oportunidades e limites, incluindo ociosidade |
| **Bancada** | Cartões de decisão, quadro final, marcos | **Alavancas combináveis**; **resposta em texto** à pergunta do gestor; **curvas** de nove indicadores com faixa e fases; **capacidade no tempo** por recurso; **indicadores e matriz** por ano-base e exercício; mudar turno como alavanca de resolução |
| **Mesa** | Grade e réguas na posição final | **Trajetória institucional** com combinações comparadas; linha separada para unidades não calculadas; cruzamento de degrau e referência condicional; restrição por campus |
| **Pacto** | Sem mudança | — |

No protótipo, a pergunta do critério de sucesso é respondida para Serra e Vitória. Para Serra, com "reorganizar + preencher + reduzir a evasão em 20%": +190 concluintes técnicos de 2027 a 2035 (faixa +116 a +233), +68 matrículas em 2035, +2,1 professores-equivalentes, restrição de laboratório e de núcleo comum em 2028, +0,10 p.p. no técnico do Ifes, ≈ +99 MT e ≈ R$ 131 mil de referência no exercício de 2032. Mudando o turno das turmas novas, a restrição de laboratório desaparece.

## 5. Mapa de funcionalidades e specs

- **Continuam sete especificações.** Nenhuma nova.
- **SPEC-001** ganha capacidade mínima, curvas com faixas, alavancas combináveis, estrela-guia, mapa de degraus, MT por parâmetros e trajetória institucional. O critério de aceite principal passa a ser a pergunta do gestor.
- **SPEC-002** ganha a decomposição da participação observada em "o que fizemos × o que a Rede fez".
- **SPEC-004** passa de "Capacidade que limita" a **"Capacidade detalhada"**: componentes, dia e bloco, equipamentos, custos e investimentos.
- **SPEC-005** passa de "Referência orçamentária condicional" a **"Matriz completa por exercício"**: reprodução exata dos ciclos, variantes de regra, cenários da Rede, regra interna e retorno ao campus.
- A fronteira entre essencial e sofisticação está no [documento 4, § 6](04-funcionalidades-e-specs.md#6-essencial--sofisticação-segunda-rodada).

## 6. Nova definição do MVP

> **O plano de oferta do próximo ciclo orientado pela estrela-guia:** a instituição vê sua participação na matriz e os degraus ao alcance; cada campus constrói alternativas combinando alavancas, vê as curvas até 2035, a capacidade que elas exigem e quando esbarram, e o efeito nos objetivos e na matriz; a reitoria compõe as propostas, compara trajetórias institucionais e registra o pactuado.

Mesmo recorte de usuários (planejamento do Ifes, quatro a seis unidades, incluindo a de educação a distância), mesma meta (ciclo real de vagas de 2028), mesmos três incrementos, com o I2 maior. Detalhe no [documento 5, § 0](05-mvp-e-evolucao.md#0-nova-definição-do-mvp-2ª-rodada).

## 7. Riscos de complexidade e simplificações adotadas

| Risco | Simplificação adotada |
|---|---|
| Capacidade virar sistema de horários ou de patrimônio | Quatro elementos agregados; turno, não dia e bloco; no máximo três ambientes críticos; áreas docentes agregadas; nenhum nome de pessoa ou sala |
| Cadastro antes do valor | A ficha do campus mostra funis e curvas antes de pedir capacidade; sem cadastro, a capacidade aparece como "não estimado" e o resto funciona |
| Capacidade calculada não corresponder à realidade | Verificação contra 2025 antes de simular, com ajuste registrado |
| Curvas transmitirem falsa precisão | Faixa obrigatória; erro fora da amostra como critério de aceite; IEA e RAP projetados nunca desenhados; evasão agregada histórica não desenhada; pandemia e quebra de 2021 marcadas |
| Matriz virar calculadora orçamentária | Estrela-guia como placar; referência marginal, por exercício, Rede declarada; indicadores de guarda; sem ranking por retorno; reprodução completa só na SPEC-005 |
| Explosão de combinações na mesa | Pontos de partida por campus e alavancas combináveis só na bancada; na mesa, uma escolha por unidade e no máximo três combinações comparadas |
| Somar resultados incompatíveis | Mesmo motor, mesma edição e mesmo horizonte para somar; unidades sem simulação em linha separada |
| Motor mais pesado | Continua um motor só, determinístico; a projeção inteira cabe em milissegundos; cache por hash |
| I2 grande demais | Ordem de corte declarada (documento 5, § 3): comparação com pontos de partida, terceiro ambiente crítico, indicadores secundários |

## 8. Onde esta rodada discorda da orientação recebida

O idealizador propôs a participação na matriz como estrela-guia, de modo que "todo o restante vai chegar nessa conclusão". Este estudo aceita a estrela-guia, com uma qualificação: ela é **placar, não objetivo único**. A participação é relativa à Rede, chega com dois anos de atraso, depende de regras que mudam e pode ser perseguida por atalhos que pioram a educação. Na maior parte do caminho, missão e matriz apontam juntas (o técnico integrado é o melhor exemplo). Onde não apontam, o PRUMO mostra os dois lados e não escolhe. A decisão sobre transformar a participação em meta formal fica explícita como D11 ([documento 6, § 6](06-avaliacao-critica.md#6-decisões-estratégicas-antes-do-novo-repositório)).

## 9. Limites desta rodada

- **A capacidade do protótipo é ilustrativa.** Os valores disponíveis foram ajustados para que manter a oferta caiba; servem para mostrar o mecanismo, não o campus real.
- **Itapina, Barra de São Francisco e Cefor são trajetórias inventadas** na mesa, marcadas como tais.
- **O motor do protótipo é o da POC 0.0.2**, calibrado em 2023–2025 com um teste fora da amostra de um ano. Não serve para decisão.
- **MT e reais usam premissas** de carga horária (800 h/ano integrado, 600 h/ano não integrado) e peso 1,5. Com a planilha da matriz, seriam calculados pela regra reproduzida.
- **O valor do degrau de formação de professores (≈ +R$ 1,27 mi)** foi calculado nesta rodada com a mesma fórmula dos demais e depende de confirmar a reclassificação de 2025.
- **Nenhum gestor viu o protótipo.** As hipóteses H1 a H6 da visão continuam sem teste.
