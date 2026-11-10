# PRUMO — Próximo passo

> **Situação:** decisão do idealizador em 10/11/2026. Encerra a fase de consolidação conceitual.
> **Contexto:** [visão de produto](visao-prumo.md); [diagnóstico](diagnostico-2026-11.md).

## 1. Decisão

1. **A fase de descoberta conceitual ampla está encerrada.** Não haverá nova auditoria, nova visão nem quarta prova de conceito.
2. **Não haverá sessão de validação com gestores agora.** A avaliação do valor da proposta, nesta etapa, é feita pelo próprio idealizador.
3. **O caminho é:** estabilizar a `main` → iniciar o Spec Kit → especificar a primeira jornada integrada.

**O que essa decisão deixa em aberto.** As hipóteses H1 a H6 da visão dizem respeito à reação de gestores e seguem sem teste. Passam a ser verificadas quando houver produto navegável.

## 2. Estabilizar a `main`

| # | Ação | Situação em 10/11/2026 |
|---|---|---|
| 1 | Conferir o tratamento numérico de `poc/extrair_poc002.py` | **Feito** no [PR #2](https://github.com/saymoncastro/prumo/pull/2). O extrator passou a tratar ponto como separador de milhar, como os outros dois. As colunas lidas da exportação da PNP não contêm ponto, então nada muda: dados e página regenerados são idênticos byte a byte e os 16 testes passam |
| 2 | Alinhar o rótulo de versão da fonte canônica da matriz | **Feito** no PR da consolidação. Cabeçalho, § 0.3 e README dos testes indicam 1.2.2. Nenhuma regra foi alterada |
| 3 | Versionar a consolidação em pull request próprio | **Feito** |
| 4 | Integrar o [PR #1](https://github.com/saymoncastro/prumo/pull/1) (estudo da PNP) | Aguarda autorização. Só acrescenta documentos |
| 5 | Integrar o [PR #2](https://github.com/saymoncastro/prumo/pull/2) (POC 0.0.2) | Aguarda autorização. Depois do #1, porque cita o estudo |
| 6 | Integrar a consolidação | Aguarda autorização. Por último |
| 7 | Trocar, no README e nos documentos de produto, os links para branches por links relativos | Depois da integração. São os links marcados "PR #1" e "PR #2" |

Os três pull requests não alteram os mesmos arquivos. A integração conjunta foi ensaiada numa cópia descartável; o resultado está na descrição do PR da consolidação.

## 3. Entrada no Spec Kit

Nada desta seção foi executado. O Spec Kit não foi inicializado no repositório.

### 3.1. Referência

A [visão de produto](visao-prumo.md) é o documento que orienta todas as especificações. Especificação que divergir dela exige editar a visão primeiro.

### 3.2. Princípios do projeto

O primeiro artefato do Spec Kit é o documento de princípios. Ele deriva de três lugares, sem conteúdo novo:

| Origem | O que fornece |
|---|---|
| Visão § 1 | Proposta de valor; três capacidades conectadas; nenhuma é produto à parte |
| Visão § 7.2 | Dez regras de domínio e de dados: natureza e origem de todo número, estruturas separadas para fato, hipótese, projeção e decisão, regras versionadas por exercício, agregação por razão das somas, série só dentro de bloco comparável, referência financeira condicional, comparação sem ranking, "não estimado" explícito, só agregados |
| Visão §§ 4.3, 4.4, 8 | Decisão em vagas; três marcos de tempo; modelo aceito só com teste em anos fora do ajuste; sem recomendação automática; governança como composição, pactuação, acompanhamento e revisão; instituição como parâmetro; dado público separado de dado privado |

### 3.3. Primeira especificação: jornada de decisão estratégica institucional

A primeira especificação não parte de um protótipo anterior nem de uma pergunta da série histórica. Parte da finalidade do produto e atravessa as três capacidades numa fatia estreita.

| Passo | O que o gestor consegue fazer |
|---|---|
| **Objetivo institucional** | Ver um objetivo compartilhado, com suas réguas e a posição atual da instituição |
| **Inteligência e contexto** | Examinar a trajetória da instituição, de seus campi e da Rede para aquele objetivo, e registrar evidências |
| **Alternativas locais** | Simular decisões de oferta num campus e ver consequências ao longo do tempo, com a origem de cada premissa |
| **Composição institucional** | Ver como propostas de campi diferentes contribuem para o objetivo e onde conflitam com outros |
| **Proposta fundamentada** | Registrar a alternativa com indicadores, premissas, fontes e limites |

**A especificação é genérica quanto ao objetivo.** O percentual de formação técnica serve de caso demonstrativo, porque já tem dados conciliados e cálculo aproveitável. Usar um exemplo para desenvolver não limita a solução a ele: um segundo objetivo (por exemplo, educação de jovens e adultos ou formação de professores) deve caber sem mudança de estrutura, e isso é critério de aceite.

**Fora da primeira especificação:** pactuação formal e acompanhamento nos três horizontes; capacidade docente e física; referência financeira; mais de uma instituição cliente; controle de acesso. Todos ficam previstos no modelo, não na entrega.

### 3.4. O que se reaproveita

| Para | Artefato |
|---|---|
| Objetivo com três réguas; contribuição por campus | Protótipo da meta de 50% técnico |
| Conciliação dos percentuais legais com a matriz | [Portão de dados](../analises/prumo-poc-portao-dados.md) |
| Decomposições e blocos comparáveis da série | Estudo da PNP (PR #1) |
| Simulação em vagas, com evasão, conclusão e retenção separadas | Motor da POC 0.0.2 (PR #2), como referência de comportamento |
| Teste em anos fora do ajuste | Teste do motor da recomposição |
| Marcadores de natureza; "o que precisa ser verdade" | Recomposição e POC 0.0.2 |
| Campos da proposta | Recomposição |
| Faixas e limiares de qualidade | [Fonte canônica](../dominio/matriz-orcamentaria.md), RMO-019 e RMO-021 |

Os protótipos são referência de comportamento e de experiência. O código deles não é base da implementação: tem o Ifes fixo, lógica duplicada e dois motores incompatíveis.

### 3.5. Decisões de produto em aberto

A resolver na etapa de esclarecimento da primeira especificação:

1. **Forma da inteligência na interface:** espaço próprio, investigação guiada por perguntas ou camada integrada à simulação.
2. **Quais campi entram na primeira fatia.** Só há premissas de simulação preparadas para Vitória, Serra, Itapina e Barra de São Francisco.
3. **Motor de coortes.** Um só, com que mecanismos, e qual erro em anos fora do ajuste é aceitável por tipo de oferta.
4. **Onde vivem evidências, cenários e propostas.** Deixam de ficar no navegador.
5. **Carga dos dados públicos:** como a exportação da PNP entra, com identidade estável de campus e metadados de quebra de série.
6. **Quanto da separação entre dado público e dado da instituição** se materializa já na primeira entrega.
7. **Critério de avaliação.** Como o idealizador avalia sozinho, convém escrever antes o que ele espera conseguir fazer ao fim da jornada.

### 3.6. Sequência

1. Integrar os três pull requests (§ 2).
2. Inicializar o Spec Kit na raiz do repositório.
3. Redigir os princípios do projeto a partir do § 3.2.
4. Especificar a jornada do § 3.3, e só ela.
5. Esclarecer as decisões do § 3.5, planejar e dividir em tarefas.

Novas especificações só depois de a primeira jornada estar navegável.
