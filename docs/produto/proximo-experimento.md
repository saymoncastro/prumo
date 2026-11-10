# PRUMO — Próximo experimento: o fio da decisão

> **Situação:** proposta de 10/11/2026, ainda não executada nem aprovada. Único experimento recomendado antes de qualquer nova especificação ou protótipo.
> **Contexto:** [visão de produto](visao-prumo.md), hipóteses H2 a H5; [diagnóstico](diagnostico-2026-11.md), §§ 3 e 4.

## 1. O que precisa ser demonstrado

Em três dias, o projeto produziu um estudo e três protótipos, e nenhum foi visto por um gestor. O que falta saber não é técnico:

> Um gestor, partindo de uma observação histórica que ele mesmo escolheu, chega a uma alternativa de decisão e a algo que levaria a uma negociação com a reitoria ou com outro campus?

Se sim, as três capacidades formam um produto. Se o gestor para na primeira etapa, o PRUMO é um painel. Se pula a primeira, é um simulador.

## 2. Menor evidência de valor

Uma sessão de 45 minutos, com um gestor por vez, conduzida por uma pessoa do projeto, **sem software novo**. O condutor faz o papel do produto: mostra o material que já existe e anota.

**Participantes:** três ou quatro, de papéis diferentes. No mínimo uma direção-geral ou de ensino de campus e uma pessoa de planejamento ou ensino da reitoria. Se possível, um gestor de outro instituto, para testar a independência do Ifes.

**Roteiro:**

| Passo | O que acontece | O que se observa |
|---|---|---|
| **1. Escolher** (5 min) | O gestor recebe quatro movimentos históricos, um por cartão, e escolhe o que mais lhe interessa | Qual escolhe e por quê. Se pergunta por algo que não está nos cartões |
| **2. Entender** (10 min) | Vê a decomposição daquele movimento para sua instituição ou campus e para dois comparáveis | Se a explicação que ele dava muda (H2). Se lê a comparação como ranking (H5) |
| **3. Supor** (5 min) | Diz, com suas palavras, por que acha que aquilo aconteceu e o que o confirmaria | Se formula hipótese ou toma o padrão como causa |
| **4. Simular** (15 min) | Vê uma alternativa de decisão ligada ao movimento, com as premissas e a origem de cada uma | Se altera alguma premissa depois de ver de onde veio (H3). Onde hesita |
| **5. Propor** (10 min) | Responde: "o que você levaria desta conversa para a reitoria, ou para os campi?" e preenche, em papel, uma proposta: contribuição, o que precisa, o que oferece, o que precisa ser verdade | Se consegue preencher (H4). Que campos faltam ou sobram |

**Os quatro cartões** saem do estudo da PNP, sem análise nova:

1. Mais vagas, mesmo número de matrículas: onde as turmas se perdem (estudo § 5.4; tabelas T8 e T9).
2. A composição da oferta e os percentuais legais: o efeito de ofertas a distância em pulso (§ 5.7; T11).
3. Crescer e perder participação: o que foi nosso e o que foi da Rede (§ 5.1; T5).
4. Três formas de crescer: ingresso, tempo de vínculo ou reconfiguração (§ 7, casos de outros institutos).

Oferecer quatro cartões, e não um, é o que testa se o produto independe de um caso específico.

## 3. O que já existe e será reutilizado

| Passo | Artefato |
|---|---|
| 1 e 2 | Tabelas e casos do [estudo da PNP](https://github.com/saymoncastro/prumo/blob/claude/prumo-pnp-exploratory-audit-aff2d0/docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md) (PR #1); tela "Comparar" da POC 0.0.2 |
| 4 | Telas "Simular" da [POC 0.0.2](https://github.com/saymoncastro/prumo/blob/claude/prumo-poc-002/docs/analises/prumo-poc-002.md) (PR #2) para o cartão 1; [protótipo da meta de 50%](../../poc/prumo-poc.html) para o cartão 2. Para os cartões 3 e 4 não há simulação pronta: o condutor apresenta a alternativa em uma página impressa |
| 5 | Campos da proposta da [recomposição](../../poc/prumo-recomposicao.html) (responsável, recursos, contrapartidas, indicador) e "o que precisa ser verdade" da POC 0.0.2, transpostos para uma folha |

**O que precisa ser preparado:** quatro cartões de uma página; a folha de proposta; o roteiro do condutor e a ficha de anotação. Se o gestor for de um campus que não seja Vitória, Serra, Itapina ou Barra de São Francisco, extrair da tabela T8 a linha do campus dele.

A falta de simulação pronta para os cartões 3 e 4 é deliberada. Se os gestores escolherem justamente esses, o próximo protótipo deve começar por eles, e não pelo que já está construído.

## 4. Como ler o resultado

| Resultado | Leitura | Consequência |
|---|---|---|
| A maioria chega ao passo 5 com proposta preenchida | O fio se sustenta | Especificar a próxima construção a partir dos cartões escolhidos e dos campos realmente usados |
| Engajam nos passos 1 a 3 e perdem interesse no 4 | O valor percebido está na inteligência | Repensar o peso da simulação; cuidado redobrado com o risco de painel |
| Vão direto ao passo 4 e tratam os anteriores como introdução | A inteligência serve como origem de premissas, não como exploração | A inteligência entra integrada à simulação, não como espaço próprio |
| Travam no passo 5 | A governança, como desenhada, não corresponde a como negociam | Entrevistar sobre como metas e recursos são de fato pactuados antes de construir qualquer coisa |
| Leem a comparação como ranking ou cobrança | Risco político real | Rever a forma de apresentar comparáveis antes de mostrar a outra instituição |

Em qualquer caso, a sessão responde à pergunta deixada em aberto na visão: que forma a inteligência da Rede deve ter na interface.

## 5. O que este experimento não é

- Não é um protótipo novo nem a unificação dos existentes.
- Não valida cálculos. Os números mostrados continuam com as ressalvas dos estudos.
- Não é pesquisa de mercado. A disposição de outra instituição a contratar fica para depois.
- Não produz decisão institucional. As propostas preenchidas são material de pesquisa.

## 6. Pré-requisitos e decisões

- Integrar os PRs #1 e #2, para que o material esteja num só lugar.
- Indicar os participantes e quem conduz.
- Decidir se a sessão com um gestor de fora do Ifes entra agora ou numa segunda rodada.
