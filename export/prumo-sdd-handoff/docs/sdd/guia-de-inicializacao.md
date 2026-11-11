# Guia de inicialização do desenvolvimento por especificação (SDD)

> **Para quem:** o primeiro agente ou desenvolvedor que trabalhar no repositório definitivo.
> **Pré-requisito:** ter lido a [visão](../produto/visao.md) e as [decisões, hipóteses e pendências](../decisoes/decisoes-hipoteses-e-pendencias.md).
> **Ferramenta:** [Spec Kit](https://github.com/github/spec-kit). No laboratório exploratório foi usada a versão 1.2.0, com integração `claude`, scripts `sh` e numeração sequencial de funcionalidades. Confira as convenções da versão que for instalada; elas mudam entre versões.

## 1. Ordem recomendada

| Etapa | O que fazer | Pronto quando |
|---|---|---|
| **A. Fundação** | Copiar o pacote, conferir a [lista de inicialização](../../migracao/checklist-inicializacao.md), validar links e checksums, primeiro commit | O repositório contém só o pacote e passa na lista |
| **B. Princípios** | Inicializar o Spec Kit e redigir os princípios do projeto (constituição) com `/speckit-constitution` | Princípios de produto **e** de engenharia redigidos e aprovados pelo idealizador |
| **C. Primeira especificação** | `/speckit-specify` → `/speckit-clarify` → `/speckit-checklist` | Uma especificação aprovada, de uma única jornada |
| **D. Plano e tarefas** | `/speckit-plan` → `/speckit-tasks` → `/speckit-analyze` | Tecnologia escolhida no plano, conferência com os princípios, tarefas pequenas e ordenadas |
| **E. Implementação e verificação** | `/speckit-implement`, incrementalmente | Critérios de sucesso conferidos com evidência (testes, valores de referência, demonstração) |

Nova especificação só depois de a anterior estar navegável.

## 2. O que alimenta os princípios do projeto

O laboratório já ratificou uma versão 1.0.0 dos princípios, em 11/11/2026, preservada em [referencias/sdd-laboratorio/constitution-v1.0.0.md](../../referencias/sdd-laboratorio/constitution-v1.0.0.md). Ela é a **entrada principal**, não o resultado: deve ser revista antes de ratificada no repositório novo, porque:

1. **Cita caminhos e seções do laboratório** (`docs/produto/visao-prumo.md`, `poc/`, `tests/`, `docs/dominio/evidencias/`, `docs/dominio/matriz-orcamentaria.md`). No repositório novo esses caminhos são outros ([referencias/README.md](../../referencias/README.md) § 7), e as seções da visão foram renumeradas:

   | Visão de 10/11 (citada nos princípios v1.0.0) | [Visão atual](../produto/visao.md) |
   |---|---|
   | §§ 1, 4.1, 5 | §§ 1, 6.1, 7 |
   | § 4.2 / § 4.3 / § 4.4 | § 6.2 / § 6.3 / § 6.4 |
   | § 7.1 (entidades) | [Glossário](../dominio/glossario-e-modelo-conceitual.md) |
   | § 7.2 (regras de domínio e de dados) | § 13 |
   | § 8 (SaaS) / § 9 (limites) / § 10 (hipóteses) | § 9 / § 10 / § 11 |

2. **Cobre princípios de produto e de domínio, mas quase nada de engenharia.** Faltam testes, integridade de dados, versionamento de regras na implementação, reprodutibilidade matemática, experiência de uso e segurança.

| Fonte no pacote | Fornece |
|---|---|
| [Visão](../produto/visao.md) §§ 1, 6, 7 | Proposta de valor; três capacidades; governança como finalidade; naturezas da informação |
| [Visão](../produto/visao.md) § 13 e [glossário](../dominio/glossario-e-modelo-conceitual.md) | Regras de domínio que valem desde já |
| [Diretrizes SaaS](../arquitetura/diretrizes-saas.md) | Instituição como parâmetro; dado público × privado; versões; rastreabilidade |
| [Simulação](../simulacao/modelos-premissas-e-validacao.md) § 6 | Validação fora do ajuste; faixas; nada de recomendação automática |
| [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) § 5 | Regras versionadas por exercício; texto × prática |
| [Fontes e proveniência](../dados/fontes-qualidade-e-proveniencia.md) | Integridade e linhagem dos dados |

**Princípios de engenharia a acrescentar** (propostos aqui, não decididos):

- Todo cálculo de domínio tem teste automatizado contra valor de referência documentado, com a fonte do valor.
- Testes de cálculo usam dados públicos versionados ou amostras derivadas deles; nunca dados privados.
- Regras e parâmetros normativos vivem como dados versionados, não como constantes no código.
- Resultados são determinísticos: mesma versão de dados, regras e modelo produz o mesmo número.
- A interface nunca exibe número sem natureza e origem disponíveis.
- Nenhum segredo, credencial ou dado pessoal no repositório.
- A tecnologia é a mais simples que respeite os princípios; complexidade exige justificativa escrita no plano.

## 3. Qualidade de uma especificação

Uma boa especificação do PRUMO:

- **Parte da finalidade do produto**, não de um protótipo anterior nem de um achado da série histórica. Cada protótipo do laboratório promoveu um achado a pergunta organizadora do produto, e a concepção se fragmentou três vezes ([evidências](../evidencias/aprendizados-e-limites-das-pocs.md) § 6).
- **Diz a quais capacidades serve** e como se liga às outras.
- **É genérica quanto ao caso.** Se usa um objetivo como exemplo, um segundo objetivo cabe sem mudança de estrutura, e isso é critério de aceite.
- **Cobre uma jornada**, com histórias testáveis em separado.
- **Não escolhe tecnologia.** Isso é do plano.

### 3.1. Requisitos verificáveis

| Evite | Prefira |
|---|---|
| "O sistema deve calcular corretamente o percentual técnico" | "A posição institucional coincide com o valor de referência X (fonte Y, ano-base Z) na precisão publicada" |
| "Exibir a incerteza" | "Tipos de oferta com erro fora do ajuste acima de 5% aparecem em faixa com largura igual ao erro medido; o limite é parâmetro" |
| "Respeitar a matriz" | "Aplica a regra RMO-xxx da versão 1.2.2 da fonte canônica, para o exercício 2026" |
| "Não ranquear" | "Nenhuma tela ordena instituições, campi ou ofertas por desempenho" (verificável por inspeção) |

### 3.2. Rastreabilidade

- Regra de domínio cita a regra correspondente da [fonte canônica da matriz](../../referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md) (RMO-xxx) ou a seção deste pacote.
- Valor de referência cita fonte, ano-base, script ou tabela que o produziu ([fontes e proveniência](../dados/fontes-qualidade-e-proveniencia.md) § 6).
- Decisão de produto cita a entrada correspondente em [decisões](../decisoes/decisoes-hipoteses-e-pendencias.md). Se não existir, registre-a lá primeiro.

### 3.3. Separação de camadas

| Camada | Onde | Contém | Não contém |
|---|---|---|---|
| Domínio e visão | `docs/` | O que o produto é, conceitos, regras, evidências | Telas, tecnologia, tarefas |
| Especificação | `specs/NNN-*/spec.md` | O quê e por quê de uma jornada; requisitos e critérios verificáveis | Como implementar |
| Plano | `specs/NNN-*/plan.md` | Tecnologia, modelo de dados, contratos, conferência com os princípios | Concepção nova de produto |
| Tarefas | `specs/NNN-*/tasks.md` | Passos pequenos e ordenados | Decisões de produto |
| Implementação | `src/` | Código e testes | Regras sem fonte |

Mudança de concepção se faz **editando a visão primeiro**, depois a especificação.

### 3.4. Como evitar especificações abrangentes demais

- Uma especificação por jornada. Se a lista de histórias passar de cinco ou seis, provavelmente são duas jornadas.
- O que fica fora da entrega é escrito como "previsto no modelo, fora desta entrega".
- Nada de *backlog* de dezenas de funcionalidades antes da primeira jornada navegável.

## 4. Primeira fatia vertical

**Recomendação:** a jornada de decisão estratégica institucional, que atravessa as três capacidades num escopo estreito. Ela já foi especificada em rascunho no laboratório, em 11/11/2026, e o rascunho está preservado em [referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md](../../referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md) (pull request aberto, não aprovado).

| Passo | O que o gestor faz | Capacidade |
|---|---|---|
| Objetivo institucional | Vê um objetivo compartilhado, suas réguas e a posição atual | Governança |
| Inteligência e contexto | Examina a trajetória e registra evidências | Inteligência |
| Alternativas locais | Simula decisões de oferta num campus, com origem de cada premissa | Simulação |
| Proposta fundamentada | Registra a alternativa com contribuição, premissas, fontes e limites | Governança |
| Composição institucional | Vê como propostas de campi diferentes se compõem e onde conflitam | Governança |

**Caso demonstrativo:** o percentual de formação técnica (meta legal de 50%), porque é o único objetivo com conciliação de dados comprovada e cálculo aproveitável ([Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) § 4; [PNP](../inteligencia/exploracao-estrategica-pnp.md) § 6). O caso **não** limita a solução: um segundo percentual legal deve caber sem mudança de estrutura.

**Como usar o rascunho:** como entrada de `/speckit-specify`, não como especificação aprovada. Revise-o contra os princípios ratificados no repositório novo, ajuste referências de caminho e confirme com o idealizador as três respostas já registradas na seção "Esclarecimentos" do rascunho.

**Fora da primeira fatia, previsto no modelo:** pactuação formal e acompanhamento nos três horizontes; capacidade docente e física; referência financeira em reais; mais de uma instituição cliente; controle de acesso; integração com sistemas acadêmicos.

## 5. Critérios de aceitação e verificação

- Cada história tem **teste independente**.
- Cálculos conferidos contra **valores de referência documentados**, com fonte. Os valores do portão de dados (percentuais legais do Ifes, ano-base 2024, exercício 2026) são a primeira referência ([PNP](../inteligencia/exploracao-estrategica-pnp.md) § 6).
- Modelo de projeção aceito **só com erro medido em anos fora do ajuste**, por tipo de oferta ([simulação](../simulacao/modelos-premissas-e-validacao.md) § 6).
- Requisitos negativos (sem ranking, sem recomendação, sem causa) verificados por inspeção com lista explícita.
- Quem avalia nesta etapa é o idealizador, sozinho. Escreva antes o que ele espera conseguir fazer ao fim da jornada.

## 6. Decisões que devem ficar abertas até a especificação ou o plano

Lista completa e origem em [decisões](../decisoes/decisoes-hipoteses-e-pendencias.md) § 3. Em resumo: tecnologia; onde vivem os registros; carga da PNP e identidade de campus; motor de coortes único e erro aceitável por tipo de oferta; quanto da separação público × privado se materializa; forma da inteligência fora da primeira fatia; rito de pactuação.

## 7. O que não implementar prematuramente

- Infraestrutura multi-instituição, autenticação, perfis.
- Fluxo formal de aprovação ou rito de pactuação detalhado.
- Explorador genérico de dados ou painel de indicadores.
- Inventário completo de docentes, salas e laboratórios; grade horária.
- Reprodução integral da matriz; valor em reais por campus.
- Otimização automática de portfólio ou recomendação de alternativa.
- Modelo de linguagem no núcleo de cálculo.
- Unificação dos motores de coortes do laboratório antes de saber a pergunta que o gestor faz.
- Qualquer coisa portada do código das POCs sem reespecificação.

## 8. Instrução para o primeiro agente

Texto pronto para entregar ao primeiro agente no repositório novo:

> Você está iniciando o desenvolvimento do PRUMO (Plataforma de Resultados, Unidades, Metas e Ofertas), um produto para instituições educacionais multicampi da Rede Federal. A fase de descoberta terminou; não recomece auditorias nem crie protótipos.
>
> 1. **A visão canônica** está em `docs/produto/visao.md`. Se qualquer outro documento divergir dela, vale a visão.
> 2. **Leia antes de trabalhar**, nesta ordem: `README.md`; `docs/produto/visao.md`; `docs/decisoes/decisoes-hipoteses-e-pendencias.md`; `docs/governanca/metas-contribuicoes-e-aprendizado.md`; `docs/dominio/glossario-e-modelo-conceitual.md`; este guia. Consulte os demais documentos de `docs/` quando a tarefa tocar no tema.
> 3. **Preserve os princípios:** governança distribuída é a finalidade, não um módulo; todo número tem natureza e origem; fato, hipótese, projeção e decisão são objetos separados; regras são versionadas por exercício; agregação pela razão das somas; comparação sem ranking e sem causa; simulação validada fora do ajuste e sem recomendação automática; instituição como parâmetro e dado público separado de privado; números calculados, nunca gerados por modelo de linguagem.
> 4. **Inicie o SDD assim:** inicialize o Spec Kit; redija os princípios do projeto a partir de `referencias/sdd-laboratorio/constitution-v1.0.0.md`, ajustando caminhos e acrescentando princípios de engenharia, e submeta ao idealizador; depois especifique uma única jornada, a de decisão estratégica institucional, usando `referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md` como entrada.
> 5. **Não implemente prematuramente:** infraestrutura multi-instituição, autenticação, fluxo de aprovação, painel genérico, inventário de infraestrutura, valores em reais por campus, recomendação automática, modelo de linguagem no cálculo. Não use o código de `referencias/prototipos/` como base: é referência de comportamento e de experiência. Não gere *backlog* de funcionalidades antes de a primeira jornada estar navegável.
