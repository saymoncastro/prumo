# Jornadas e casos de uso

> **Natureza:** jornadas conceituais, não telas, não *backlog* e não especificações. Servem de matéria-prima para especificações futuras, uma de cada vez.
> **Relacionados:** [visão](visao.md) · [governança](../governanca/metas-contribuicoes-e-aprendizado.md) · [simulação](../simulacao/modelos-premissas-e-validacao.md) · [inteligência](../inteligencia/exploracao-estrategica-pnp.md)

Os casos usados como exemplo (meta de 50% de formação técnica, Itapina, Barra de São Francisco, Vitória, Serra) foram explorados no laboratório. São ilustrações, não o limite do produto.

## 1. Jornadas fundamentais

Formato: **ator · contexto · decisão · informações necessárias · resultado esperado · capacidades**. A coluna "Maturidade" diz o quanto a jornada foi exercitada no laboratório ([evidências](../evidencias/aprendizados-e-limites-das-pocs.md)).

### J1. Gestor investiga a trajetória de uma instituição

| | |
|---|---|
| **Ator** | Gestor institucional (planejamento, pró-reitoria) |
| **Contexto** | Um indicador mudou e ninguém sabe explicar por quê (ex.: mais vagas no técnico não viraram mais matrículas) |
| **Decisão** | Que hipótese investigar e que evidência levar adiante |
| **Informações** | Série da instituição, dos campi e da Rede dentro de blocos comparáveis; decomposição da variação (ingresso × tempo de vínculo; numerador × denominador; campi que explicam); comparáveis por perfil e trajetória |
| **Resultado** | Evidência registrada (fato ou padrão), com recorte, fonte e limite; hipótese com o que a confirmaria |
| **Capacidades** | Inteligência → alimenta simulação e governança |
| **Maturidade** | Estudo reproduzível da PNP; sem interface |

### J2. Campus compara alternativas de portfólio

| | |
|---|---|
| **Ator** | Direção-geral e direção de ensino do campus |
| **Contexto** | O campus precisa recompor a oferta: cursos com baixa ocupação, vocação em mudança, metas institucionais |
| **Decisão** | Abrir, ampliar, reduzir, substituir ou encerrar ofertas, a partir de que ano |
| **Informações** | Linha de base com turmas em curso; premissas com histórico próprio e faixa de comparáveis; o que cada alternativa exige e entrega ano a ano |
| **Resultado** | Duas ou três alternativas comparadas lado a lado, sem recomendação automática; a escolhida vira proposta |
| **Capacidades** | Simulação, alimentada por inteligência, destinada à governança |
| **Maturidade** | Ilustrada (protótipo de recomposição); não testada com gestores |

### J3. Gestor simula expansão de vagas

| | |
|---|---|
| **Ator** | Direção de ensino; coordenação de curso |
| **Contexto** | Há demanda percebida para ampliar uma oferta existente |
| **Decisão** | Quantas vagas a mais, em que oferta, a partir de que ingresso |
| **Informações** | Ocupação histórica das vagas; evasão, conclusão e retenção separadas; tempo até o efeito nos dados e no exercício orçamentário; docentes e ambientes adicionais no pico de turmas simultâneas |
| **Resultado** | Ingressantes, matrículas e concluintes por ano, em faixa onde o modelo erra mais; efeito nos objetivos institucionais |
| **Capacidades** | Simulação |
| **Maturidade** | Ilustrada (POC 0.0.2, Vitória e Serra) |

### J4. Campus compara investimento em permanência com ampliação da oferta

| | |
|---|---|
| **Ator** | Direção de ensino; equipe pedagógica |
| **Contexto** | As vagas se preenchem, mas as matrículas caem: a perda está na trajetória |
| **Decisão** | Ampliar vagas, aproveitar melhor as existentes (permanência) ou reorganizar |
| **Informações** | Decomposição da perda; evasão por fase do curso; evidência de efeito de programas de permanência |
| **Resultado** | Comparação honesta, com "não estimado" onde não houver evidência do tamanho do efeito |
| **Capacidades** | Inteligência + simulação |
| **Maturidade** | Ilustrada; **o efeito de permanência foi arbitrado** nos protótipos, sem dado que o sustente. Não deve ser apresentado como alternativa comparável enquanto não houver evidência |

### J5. Gestor avalia viabilidade física e docente

| | |
|---|---|
| **Ator** | Direção do campus; gestão de pessoas; infraestrutura |
| **Contexto** | Uma alternativa parece boa, mas pode não caber |
| **Decisão** | Se a alternativa é viável, em que ano estrangula e o que seria necessário |
| **Informações** | Docentes por área; ambientes críticos por turno; ciclo de vida das turmas (o pico vem antes do efeito); custos e investimentos |
| **Resultado** | Primeiro conflito identificado, com ano e recurso; investimento necessário |
| **Capacidades** | Simulação |
| **Maturidade** | Apenas esboçada (recomposição: docentes, um ambiente crítico, custeio por premissa simples). Fora da primeira fatia |

### J6. Reitoria estabelece um objetivo institucional

| | |
|---|---|
| **Ator** | Reitoria, planejamento, Colégio de Dirigentes |
| **Contexto** | Um indicador institucional precisa mudar (ex.: percentual de formação técnica abaixo da meta legal de 50%) |
| **Decisão** | Qual objetivo, com quais réguas e horizonte |
| **Informações** | Posição atual pela razão das somas; contribuição de cada campus em numerador e denominador; meta legal, limiar orçamentário e meta pactuada separados; conflitos com outros objetivos |
| **Resultado** | Objetivo registrado com réguas e horizonte; ponto de partida para as propostas |
| **Capacidades** | Governança, apoiada por inteligência |
| **Maturidade** | Ilustrada (protótipo da meta de 50%); conciliação de dados comprovada |

### J7. Campi propõem contribuições distintas

| | |
|---|---|
| **Ator** | Direção de cada campus |
| **Contexto** | Há um objetivo institucional e cada campus tem vocação e restrições próprias |
| **Decisão** | Com o que o campus contribui, o que pede e o que oferece em troca |
| **Informações** | Efeito da alternativa escolhida sobre o objetivo e sobre os demais; recursos; o que precisa ser verdade |
| **Resultado** | Proposta registrada: alternativa, contribuição por objetivo, recursos, contrapartidas, premissas, evidências, limites |
| **Capacidades** | Governança, apoiada por simulação |
| **Maturidade** | Ilustrada (recomposição e POC 0.0.2, registro só no navegador) |

### J8. Instituição consolida e compara estratégias

| | |
|---|---|
| **Ator** | Reitoria e planejamento |
| **Contexto** | Propostas diferentes chegaram dos campi |
| **Decisão** | Que combinação de propostas levar à pactuação; com quem negociar o que falta |
| **Informações** | Composição pela razão das somas, ano a ano, diante de cada régua; conflitos entre objetivos; total de recursos pedidos; quanto falta |
| **Resultado** | Composições em estudo comparadas; nenhuma distribuição automática da diferença entre campi |
| **Capacidades** | Governança |
| **Maturidade** | Ilustrada (grade de 16 combinações da POC 0.0.2); é a parte menos demonstrada |

### J9. Gestores acompanham compromissos e resultados

| | |
|---|---|
| **Ator** | Planejamento; direções de campus |
| **Contexto** | Um ou mais ciclos depois da pactuação |
| **Decisão** | Manter, ajustar ou rever premissas, metas e compromissos |
| **Informações** | Compromisso, responsável e indicador; resultado observado na edição seguinte da PNP; horizonte já observável (execução, intermediário, longo prazo) |
| **Resultado** | Premissas revistas; evidência nova; estratégia ajustada |
| **Capacidades** | Governança + inteligência (fecha o ciclo) |
| **Maturidade** | Não exercitada |

### J10. Planejamento e orçamento conferem um cálculo

| | |
|---|---|
| **Ator** | Equipe de planejamento e orçamento |
| **Contexto** | Um número vai ser usado numa negociação |
| **Decisão** | Se o número é confiável |
| **Informações** | Fonte, ano-base, versão da regra, fórmula, premissas, erro do modelo ao reproduzir o passado; efeito acadêmico separado de referência financeira |
| **Resultado** | Número reproduzido ou contestado |
| **Capacidades** | Transversal |
| **Maturidade** | Aba "Como calcula" nos protótipos; fonte canônica da matriz |

## 2. Outros casos que a mesma estrutura deve atender

Não explorados no laboratório. Listados para testar se uma especificação ficou genérica o bastante:

- Priorizar permanência em vez de expansão.
- Redistribuir capacidade docente entre campi ou áreas.
- Avaliar o efeito de ofertas a distância em pulso.
- Acompanhar a participação relativa da instituição na Rede.
- Escolher entre iniciar uma oferta em fevereiro ou agosto (efeito no ano-base e no exercício).
- Avaliar o efeito de contratações e remoções docentes na relação aluno-professor perto de um degrau orçamentário.
- Compensar objetivos entre campi: um contribui com formação de professores ou EJA, outro com formação técnica.
- Substituir uma forma de oferta por outra (ex.: técnico subsequente por integrado).
- Calibrar premissas comparando o previsto com a matriz e a PNP do ano seguinte.

## 3. A primeira jornada recomendada

A combinação de J6 → J1 → J2/J3 → J7 → J8, num escopo estreito, é a **jornada de decisão estratégica institucional** recomendada como primeira especificação. Ver [guia SDD](../sdd/guia-de-inicializacao.md) § 4.
