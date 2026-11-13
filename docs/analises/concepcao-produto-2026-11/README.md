# PRUMO — Estudo de concepção do produto (12/11/2026)

> **Natureza:** estudo de concepção, proposta para discussão. Não altera a [visão de produto](../../produto/visao-prumo.md), que continua a referência canônica, nem os [princípios do projeto](../../../.specify/memory/constitution.md). O que for aceito daqui entra na visão por edição, como manda a convenção do repositório.
> **Pergunta:** como o PRUMO deveria existir como produto digital utilizável: o que é, como se usa, que telas tem, como se constrói e por onde começa.
> **Base:** todo o repositório até o commit `f98a7b7`. Nenhum material existente fora desta pasta foi alterado.
> **Duas rodadas no mesmo dia.** A primeira definiu identidade, experiência, arquitetura, specs e MVP. A segunda ([síntese](09-segunda-rodada.md)) recuperou capacidade de execução, projeção longitudinal e impacto na matriz, e adotou a **participação na matriz orçamentária como estrela-guia**. As mudanças estão marcadas com "[2ª rodada]" em cada documento.

## Segunda rodada em uma página

- **Estrela-guia:** a participação do Ifes no remanescente da matriz, ≈ 3,32% em 2026. Em Funcionamento + Reitoria (90% do bolo) o Ifes tem 3,56%; em Qualidade, só 1,20%, abaixo de dois degraus que zeram sua parte. O espaço está nos degraus, e degraus só se cruzam com contribuições de vários campi. A estrela-guia é placar, não objetivo único: é relativa à Rede, chega com dois anos de atraso e vem sempre com indicadores de guarda. [Documento 7](07-estrela-guia-e-indicadores.md).
- **Taxa de câmbio:** uma MT presencial vale ≈ R$ 1,3 mil por exercício; o degrau de 50% em técnico vale ≈ R$ 2,06 mi ≈ 1.550 MT. É o que permite comparar alavancas de naturezas diferentes.
- **Capacidade mínima por campus na primeira jornada:** turmas simultâneas, salas por turno, até três ambientes críticos e docentes por área, verificados contra o uso de 2025. Sem horário, sem patrimônio. [Documento 8](08-capacidade-e-projecao.md).
- **Projeção longitudinal:** observado → manter → cenário até 2035, com faixas, para nove indicadores; fases do efeito (começa, intensifica, estabiliza, restrição); capacidade no mesmo tempo.
- **Mesa com trajetória institucional:** combinações comparadas até 2035, cruzamento de degrau e exercício, unidades sem simulação em linha separada.
- **Specs:** continuam sete. A SPEC-001 fica mais profunda; a SPEC-004 vira "Capacidade detalhada" e a SPEC-005, "Matriz completa por exercício".
- **Protótipo v2:** Vitória e Serra calculadas com o motor da POC 0.0.2 sobre dados reais da PNP. O protótipo reproduz os números da POC e responde à pergunta do gestor: em Serra, reorganizar, preencher e reduzir a evasão dá +190 concluintes até 2035, esbarra no laboratório em 2028 e move +0,10 p.p. no técnico do Ifes.

## Síntese executiva (primeira rodada, com ajustes da segunda)

## Síntese executiva

### 1. O que é o PRUMO, afinal?

**A mesa onde a instituição decide sua oferta junto com os campi, e onde confere, quando a próxima PNP chega, se o que foi decidido aconteceu.**

É, antes de tudo, um **sistema de registro das decisões estratégicas de oferta**, algo que hoje não existe: a PNP registra o que aconteceu; ninguém registra o que foi decidido, por quê e com quais premissas. A inteligência sobre a Rede e a simulação de oferta são o que torna essas decisões fundamentadas.

O produto se organiza em torno de um ritmo que as 41 instituições da Matriz CONIF já vivem: **a PNP publica o ano → a instituição define as vagas do ano seguinte → as turmas entram e evoluem → a PNP seguinte mostra o que aconteceu.** O PRUMO transforma esse ciclo, que hoje corre em planilhas e reuniões sem memória, num ciclo de aprendizado. [Documento 1](01-visao-concreta.md).

### 2. Como seria usá-lo?

- **A equipe de planejamento** abre o PRUMO e ele já sabe sobre a instituição: a posição em cada objetivo diante de três réguas (meta legal, limiar da matriz, meta pactuada) e quais campi explicam a mudança dos últimos anos. Nenhum cadastro antes.
- **A diretora de um campus** vê suas ofertas como funis (vagas → ingressantes → matrículas → concluintes) e percebe onde perde estudantes. Monta duas ou três alternativas na bancada, vê o que cada uma exige e entrega ano a ano, com a origem de cada premissa, e encaminha uma como proposta.
- **Na reunião do colegiado**, a mesa de composição é projetada: as propostas dos campi se somam do jeito certo, os conflitos entre objetivos aparecem, a distância que falta fica visível. O colegiado decide; o PRUMO registra o pacto.
- **No ano seguinte**, a nova PNP é carregada e cada compromisso é conferido no horizonte que já pode ser observado. O desvio é explicado pelos mesmos mecanismos da projeção (vagas, ocupação, evasão, retenção, conclusão).

[Documento 2](02-experiencia-e-interfaces.md) e [protótipo navegável](prototipo/prumo-conceito.html).

### 3. Telas e funcionalidades mais importantes

| Tela | Pergunta |
|---|---|
| **Agenda estratégica** | Onde estamos, o que mudou na PNP, o que pede atenção no ciclo? |
| **Objetivo** | Régua tripla, quem explica a mudança (ponte por campus), objetivos em tensão |
| **Ficha do campus** | Contribuição a cada objetivo; portfólio como funis |
| **Bancada de alternativas** | O que cada decisão de vagas exige e entrega, quando, com que premissas |
| **Mesa de composição** | Como as propostas dos campi se somam; conflitos; o que falta; modo reunião |
| **Pacto e acompanhamento** | O que aconteceu; desvio explicado; revisão de premissas |

Em todas: **marcador de natureza** em cada número e a **gaveta "Como calcula"**.

### 4. Arquitetura e stack recomendadas

**Monólito modular em Django com PostgreSQL; motor de cálculo como pacote Python puro, executado no servidor; interface renderizada no servidor com HTMX, com componentes interativos isolados só onde necessário.** Dados públicos e dados de cada instituição em zonas separadas do mesmo banco. Nenhum microsserviço, nenhuma integração e nenhum modelo de linguagem no primeiro produto. [Documento 3](03-arquitetura-e-stack.md).

### 5. Primeiras especificações

| Spec | Entrega |
|---|---|
| **SPEC-001 · Plano de oferta orientado por objetivo** | Jornada integrada: estrela-guia e objetivo → ficha do campus com capacidade → bancada com curvas → proposta → mesa com trajetória |
| **SPEC-002 · Pacto e conferência** | Registro do pacto, horizontes, conferência pela PNP seguinte, desvio explicado |
| SPEC-003 · Leitura da Rede | Comparáveis, precedentes, trajetórias |
| SPEC-004 · Capacidade detalhada [2ª rodada] | Componentes, dia e bloco, equipamentos, custos e investimentos |
| SPEC-005 · Matriz completa por exercício [2ª rodada] | Reprodução exata dos ciclos, variantes de regra, cenários da Rede, regra interna |
| SPEC-006 · Segunda instituição | Isolamento, papéis, login |
| SPEC-007 · Documento da decisão | Nota técnica |

[Documento 4](04-funcionalidades-e-specs.md).

### 6. O que construiríamos primeiro

> **[2ª rodada]** Nova definição: o plano de oferta do próximo ciclo **orientado pela estrela-guia**, com capacidade mínima por campus, curvas até 2035 e trajetória institucional na mesa ([documento 5, § 0](05-mvp-e-evolucao.md#0-nova-definição-do-mvp-2ª-rodada)). O texto abaixo é o da primeira rodada.

**O plano de oferta do próximo ciclo orientado por dois objetivos em tensão** (formação técnica e concluintes técnicos), com a equipe de planejamento do Ifes e quatro a seis unidades, incluindo a de educação a distância. Em três incrementos: *começa sabendo* (leitura dos objetivos) → *bancada* (um campus) → *mesa* (composição e reunião). Meta: **usar o PRUMO no ciclo real de definição de vagas de 2028.** [Documento 5](05-mvp-e-evolucao.md).

### 7. O que o torna diferente

1. **Começa sabendo:** abre cheio, para qualquer das 41 instituições, só com dados públicos.
2. **Decide em vagas, mostra concluintes:** a alavanca é a vaga; o resultado que importa é a trajetória das turmas.
3. **Contribuição diferenciada, somada do jeito certo,** com conflitos entre objetivos visíveis.
4. **Toda decisão vira compromisso conferível,** e o desvio é explicado, não só apontado.
5. **Todo número diz o que é e de onde veio.**

## Direção proposta [revista na 2ª rodada]

> O PRUMO é a mesa de decisão do ciclo anual de oferta, guiada pela participação da instituição na matriz: mostra quanto cada degrau vale e quem pode movê-lo, leva cada campus do funil de suas ofertas a alternativas que cabem na sua capacidade, com curvas até dez anos e efeito nos objetivos e na matriz, compõe as propostas numa trajetória institucional e registra o pactuado para que a próxima PNP o confira.

## Decisões antes de iniciar o novo repositório

Detalhadas no [documento 6, § 6](06-avaliacao-critica.md#6-decisões-estratégicas-antes-do-novo-repositório):

1. **Âncora do produto:** objetivos e ciclo anual de vagas, em vez de módulos.
2. **Objetivos da SPEC-001:** formação técnica **e** concluintes técnicos, porque a alavanca do percentual técnico está concentrada na unidade de EaD.
3. **Validação mínima:** três conversas de 30 minutos sobre como a definição de vagas acontece hoje. Não é reabrir a descoberta.
4. **Patrocinador e operador** no Ifes: quem convoca a pauta e quem opera a mesa.
5. **Unidades do piloto,** incluindo a de educação a distância.
6. **Stack:** Django + HTMX + PostgreSQL, motor como pacote puro.
7. **Natureza do repositório e licença:** privado ou aberto (muda o caminho de adoção pela Rede).
8. **Responsável anual pelos dados.**
9. **Critério de aceite do motor** por tipo de oferta.
10. **Meta de uso:** o ciclo real de vagas de 2028.
11. **[2ª rodada] Papel da participação na matriz:** placar com indicadores de guarda, ou meta institucional formal (esta exige emendar o princípio VI).
12. **[2ª rodada] Planilha da matriz como insumo** opcional da primeira jornada, para os parâmetros por oferta.

## Documentos

| # | Documento | Conteúdo |
|---|---|---|
| 1 | [Visão concreta](01-visao-concreta.md) | Identidade, problema, ciclo anual, usuários, proposta de valor, um ano com o PRUMO, princípios de produto |
| 2 | [Experiência e interfaces](02-experiencia-e-interfaces.md) | Duas concepções comparadas, modelo mental, mapa de navegação, telas, jornadas A–E, IA na experiência |
| 3 | [Arquitetura e stack](03-arquitetura-e-stack.md) | Exigências, recomendação, alternativas, domínio, modelo de dados, ingestão, infraestrutura, IA, testes |
| 4 | [Funcionalidades e specs](04-funcionalidades-e-specs.md) | Módulos que não devem existir, organização funcional, o que se calcula com quê, mapa de specs |
| 5 | [MVP e evolução](05-mvp-e-evolucao.md) | Portas de entrada comparadas, as nove perguntas do primeiro produto, incrementos, calendário, riscos |
| 6 | [Avaliação crítica](06-avaliacao-critica.md) | O que sabemos de fato, descobertas, discordâncias, riscos, SaaS, decisões, recomendação final |
| 7 | [Estrela-guia e indicadores](07-estrela-guia-e-indicadores.md) [2ª rodada] | Participação na matriz, árvore de alavancas, mapa de degraus, taxa de câmbio, decisões → consequências, classificação dos indicadores |
| 8 | [Capacidade e projeção](08-capacidade-e-projecao.md) [2ª rodada] | Modelo mínimo de capacidade, projeção longitudinal, incerteza, resposta da bancada |
| 9 | [Síntese da segunda rodada](09-segunda-rodada.md) | O que estava certo, subdimensionado ou faltando; mudanças; novo MVP; riscos |
| — | [Protótipo conceitual v2](prototipo/prumo-conceito.html) | Seis telas; Vitória e Serra calculadas com dados reais; capacidade e outras unidades ilustrativas |
| — | [Protótipo conceitual v1](prototipo/prumo-conceito-v1.html) | Primeira rodada, preservado |

**Abrir o protótipo:** direto no navegador, ou `python3 -m http.server 8766 --directory docs/analises/concepcao-produto-2026-11/prototipo` e `http://localhost:8766/prumo-conceito.html`.

**Remontar o protótipo v2:** `python3 docs/analises/concepcao-produto-2026-11/prototipo/montar.py`. Junta o template, [`simulacao.js`](prototipo/simulacao.js), o motor `poc/coortes002.js` (sem alteração) e um recorte só com dados públicos de `poc/dados-poc002.json`.

**Sobre os números do protótipo e dos exemplos:** os que vêm dos estudos (portão de dados, estudo da PNP, POC 0.0.2, recomposição) estão indicados; os inventados levam a marca "ilustr.". Valores de protótipos com horizontes diferentes foram reunidos na mesa de composição apenas para mostrar a interação. Nada aqui serve para decisão.
