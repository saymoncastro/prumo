# Decisões, hipóteses e pendências

> **Regra de uso:** uma especificação não pode contrariar o que está em **Decidido** sem editar este documento e a [visão](../produto/visao.md) antes. Itens em **Pendente** são escolhas reais a fazer no SDD; não as antecipe. **Recomendações de agentes não são decisões** e estão separadas no § 5.
> **Origem:** cada item cita data e documento de origem no laboratório exploratório. "Idealizador" é o responsável pelo produto. "PR #n" é pull request do repositório exploratório, integrado (ou não) por ele. Na coluna de origem, **"visão de 10/11"** é o documento de visão do laboratório (`docs/produto/visao-prumo.md`), cuja numeração difere da [visão atual](../produto/visao.md).

## 1. Decidido

### 1.1. Decisões explícitas do idealizador

| # | Decisão | Data | Origem |
|---|---|---|---|
| D-01 | Há **uma** visão canônica; mudança de concepção se faz editando-a, não criando outro documento de visão | 10/11/2026 | Visão de produto e README, integrados no PR #3 |
| D-02 | O PRUMO é pensado como **produto reutilizável por outras instituições** (SaaS) **[DIREÇÃO]**. Demanda comercial não validada | 10/11/2026 | Visão de 10/11 § 8 |
| D-03 | **A fase de descoberta conceitual ampla está encerrada.** Sem nova auditoria, nova visão nem quarta prova de conceito | 10/11/2026 | Próximo passo § 1 |
| D-04 | **Sem sessão de validação com gestores agora.** A avaliação desta etapa é feita pelo idealizador; H1–H6 seguem sem teste | 10/11/2026 | Próximo passo § 1 |
| D-05 | O caminho é desenvolvimento por especificação (Spec Kit), começando pela **jornada de decisão estratégica institucional**, genérica quanto ao objetivo, com a meta de 50% técnico como caso demonstrativo; um segundo objetivo deve caber sem mudança de estrutura | 10/11/2026 | Próximo passo § 3.3 |
| D-06 | Uma jornada especificada por vez; nova especificação só depois da anterior navegável | 10/11/2026 | Próximo passo § 3.6; princípios v1.0.0 |
| D-07 | Princípios do projeto **v1.0.0** ratificados (dez princípios) | 11/11/2026 | PR #4; [cópia](../../referencias/sdd-laboratorio/constitution-v1.0.0.md). No repositório novo, servem de entrada para nova ratificação (P-17) |
| D-08 | Na primeira fatia, a inteligência é **investigação guiada a partir do objetivo**, por perguntas fixas; exploração livre fica fora | 11/11/2026 | Especificação 001, Esclarecimentos (PR #5, **aberto**) |
| D-09 | Na primeira fatia, simulação para os **quatro campi com premissas preparadas**: Vitória, Serra, Itapina, Barra de São Francisco; a lista é dado, não estrutura | 11/11/2026 | Idem |
| D-10 | Resultado em **faixa** quando o erro fora do ajuste passa de **5%**; o limite é parâmetro | 11/11/2026 | Idem |
| D-11 | O produto definitivo nasce em **repositório novo**; migra-se conhecimento, não código exploratório | 11/11/2026 | Solicitação desta consolidação |
| D-12 | **Só dados públicos entram no Git**; a exportação da PNP, a planilha da matriz do Ifes, o livro da matriz e derivados ficam fora | 09–10/11/2026 | `.gitignore` e README do laboratório; princípios v1.0.0 |

D-08 a D-10 foram respondidas pelo idealizador, mas estão num rascunho de especificação **não integrado**. Confirme-as ao reespecificar no repositório novo.

### 1.2. Princípios vigentes por incorporação à visão canônica

Formulados no documento fundador (08/11/2026) ou pelos estudos e incorporados à visão integrada pelo idealizador (PR #3, 10/11/2026). Lista completa e justificativas na [visão](../produto/visao.md) e nos princípios v1.0.0.

| # | Princípio | Origem |
|---|---|---|
| V-01 | Governança distribuída é a finalidade; a solução se estrutura a partir dela, não do simulador | Fundador §§ 0.1, 4, 13; visão de 10/11 § 4.1 |
| V-02 | Todo número carrega natureza e origem; "não estimado" explícito | Fundador § 15; visão de 10/11 § 7.2 |
| V-03 | Fato, hipótese, projeção, proposta e decisão em estruturas separadas | Fundador § 15.1; visão de 10/11 § 7.2 |
| V-04 | Regras orçamentárias versionadas por exercício; texto e prática em separado | Fonte canônica; visão de 10/11 § 7.2 |
| V-05 | Matrícula física, equivalente e total não se substituem | Fonte canônica RMO-007; visão de 10/11 § 7.2 |
| V-06 | Agregação pela razão das somas; série só em bloco comparável | RPE-01; estudo PNP; visão de 10/11 § 7.2 |
| V-07 | Comparação sem ranking; associação sem causa; referência financeira condicional | Estudo PNP; fonte canônica § 13; visão de 10/11 § 7.2 |
| V-08 | Decisão em vagas; três marcos de tempo; validação fora do ajuste; sem recomendação automática | Fundador § 7.2; POCs; visão de 10/11 § 4.3 |
| V-09 | Instituição como parâmetro; público separado de privado; agregados bastam | Visão de 10/11 § 8 |
| V-10 | Números calculados de forma determinística; modelo de linguagem não produz números nem integra o núcleo | Fundador § 15.4; visão de 10/11 § 4.2 |
| V-11 | Fora de escopo agora: infraestrutura multi-instituição, autenticação, fluxo de aprovação, integrações, inventário completo, grade horária, reprodução integral da matriz, valor em reais por campus, otimização automática | Visão de 10/11 § 9 |
| V-12 | Descartados: Funcionamento em reais por campus como porta de entrada; MOOC como alavanca orçamentária; estimar RAP e eficiência da matriz pela PNP; permanência com efeito arbitrado como alternativa comparável; auditoria forense da planilha | Diagnóstico de 10/11/2026 § 6, incorporado à visão de 10/11 §§ 9 e 4.3 |
| V-13 | Protótipos são referência de comportamento e experiência; seu código não é base da implementação | Próximo passo § 3.4; princípios v1.0.0 |

## 2. Hipóteses

### 2.1. Hipóteses de produto e de mercado

H1 a H10 da [visão](../produto/visao.md) § 11: reconhecimento do problema pelos gestores; efeito da decomposição histórica; efeito da origem da premissa; cenário que leva a negociação; comparação sem leitura de ranking; reitoria usa propostas diferentes; valor da inteligência para outra instituição; compatibilidade de outra instituição; quem paga; responsável pela atualização anual. **Nenhuma testada.**

Também: papéis de patrocinador, comprador e usuários (visão § 4); escada de adoção com a inteligência como porta de entrada (visão § 9).

### 2.2. Hipóteses de domínio

| # | Hipótese | Origem | O que confirmaria |
|---|---|---|---|
| HD-01 | Distribuição interna do Ifes como "matriz por campus com piso e teto" | RMO-075, L-28 | Regra documentada pela PROAD |
| HD-02 | O ganho de Qualidade da matriz concentra-se na Reitoria (R$ 11,7 milhões em 2026) | Revisão estratégica | Idem |
| HD-03 | Participação técnica dos campi do Ifes entre cerca de 15% e 85% | Revisão estratégica, a partir da planilha não pública | Cálculo com dados públicos por campus |
| HD-04 | O salto de formação de professores do Ifes (12,1% → 24,8%, 2024 → 2025) é reclassificação | Portão de dados | Confirmação com a pró-reitoria |
| HD-05 | Programas de permanência reduzem a evasão em cerca de 30% | POC 0.0.2 (arbitrado) | Evidência de programas executados |
| HD-06 | A queda de matrículas no técnico concomitante/subsequente ocorre por evasão no primeiro ano | Estudo PNP | Dados por turma |
| HD-07 | A queda da EJA na linha de base da POC 0.0.2 (1,98% → 1,54% em 2032) é artefato do motor | Verificação de 11/11/2026 | Revisão do motor e da ancoragem |
| HD-08 | Pacto de metas com degraus como forma de pactuação | Revisão estratégica §§ 12–13; rebaixado a caso de uso em 10/11/2026 | Uso por gestores |

## 3. Pendente

Escolhas reais a fazer durante o SDD. **Não decidir antes da etapa indicada.**

| # | Pendência | Quando decidir | Origem |
|---|---|---|---|
| P-01 | Linguagem, framework, banco de dados, hospedagem | Plano da primeira especificação | Princípios v1.0.0 |
| P-02 | Onde vivem evidências, cenários, propostas e composições (deixam de ficar no navegador) | Plano da primeira especificação | Próximo passo § 3.5 |
| P-03 | Carga da PNP: formato, identidade estável de campus, metadados de quebra de série | Plano da primeira especificação | Idem |
| P-04 | Motor de coortes único: mecanismos e erro fora do ajuste aceitável por tipo de oferta | Plano da primeira especificação | Idem; [simulação](../simulacao/modelos-premissas-e-validacao.md) § 7 |
| P-05 | Quanto da separação entre dado público e dado da instituição se materializa na primeira entrega | Plano da primeira especificação | Idem |
| P-06 | Mecanismo de isolamento entre clientes (*tenancy*) | Quando houver segundo cliente | [Diretrizes SaaS](../arquitetura/diretrizes-saas.md) |
| P-07 | Forma da inteligência na interface além da primeira fatia | Especificação seguinte | Visão § 6.2 |
| P-08 | Rito de proposta, pactuação e aprovação | Depois de observar uma negociação real | Visão § 10 |
| P-09 | Segundo objetivo da primeira fatia: EJA ou formação de professores | Especificação 001 | Rascunho da especificação 001 |
| P-10 | Horizonte de simulação e granularidade temporal (ciclo × ano civil; turno × semestre) | Especificação ou plano | Fundador § 24, q12 |
| P-11 | Nome e marca (PRUMO é provisório; alternativas registradas: PACTO, NORTE) | Antes de qualquer uso público | Proposta de nome, 08/11/2026 |
| P-12 | Patrocinador, mandato institucional e modelo de contratação | Fora do SDD | Fundador § 24, q1; H9 |
| P-13 | Responsável pela atualização anual de dados e regras | Antes de uso continuado | H10 |
| P-14 | Qual regra da matriz vale em 2027 (texto de N3 ou prática de 2026) | Quando houver memória de cálculo de 2027 | L-24, L-26, L-27 |
| P-15 | Visibilidade do repositório novo e divulgação dos agregados derivados da planilha não pública do Ifes | Antes do primeiro push | [Fontes](../dados/fontes-qualidade-e-proveniencia.md) § 7 |
| P-16 | Destino do PR #5 (especificação 001) no repositório exploratório | Na transferência | Este pacote |
| P-17 | Ratificação dos princípios no repositório novo, com princípios de engenharia | Etapa B do [guia SDD](../sdd/guia-de-inicializacao.md) | Este pacote |
| P-18 | Questões abertas do documento fundador ainda sem resposta: autonomia do campus × colegiados; metas do PDI; equidade territorial sem pesos arbitrários; inventário de salas; carga docente por área; uso legal de dados longitudinais; EaD e formação aberta; cenários parcialmente viáveis; integrações; equipe de validação; como medir o valor do projeto | Quando uma especificação tocar no tema | Fundador § 24 |

## 4. Conclusões metodológicas não reconciliadas

Registradas como estão; **nenhum número foi corrigido** para ajustar a narrativa.

| # | Ponto | Situação | Onde |
|---|---|---|---|
| U-01 | Erros fora do ajuste de 8%, 15% e 19% em graduação (motor da recomposição), citados na visão do laboratório, **não são reproduzíveis** pelo código versionado | Inconclusivo; não usar como evidência | [Simulação](../simulacao/modelos-premissas-e-validacao.md) § 6.2 |
| U-02 | Portão de dados (09/11, 37 instituições) × estudo T13 (10/11, 41): faixas de razão do numerador da RAP e do professor-equivalente diferentes | Não reconciliado | [PNP](../inteligencia/exploracao-estrategica-pnp.md) § 6 |
| U-03 | Percentual técnico do Ifes: 44% (PNP) × 57,8% (planilha da matriz) | L-25, não determinada | [Matriz](../dominio/matriz-conif-e-indicadores.md) § 3 |
| U-04 | Numerador da RAP: 20,11 / 17,56 / 18,148 | Irreconciliável sem documentação oficial | Matriz § 8 |
| U-05 | Defasagem "exercício = ano-base + 2" (RMO-070, normativa) × "não é regra eterna" (fonte canônica §§ 10 e 13.2) | Texto não harmonizado; tratar como parâmetro | Matriz § 6 |
| U-06 | Rótulos internos desatualizados na fonte canônica 1.2.2 (§§ 6.1, 13.1, 14, 16, 17.2; RMO-003/004/060) | Registrado; documento normativo não alterado | Matriz § 8.1 |
| U-07 | "19 CSV" e "64 instituições por ano" no estudo da PNP; são 18 CSV e a cobertura varia | Corrigido aqui; estudo não alterado | [Fontes](../dados/fontes-qualidade-e-proveniencia.md) § 3 |
| U-08 | O portão de dados contém dois vereditos opostos (vale o de cima) | Registrado | PNP § 6 |
| U-09 | Fator de nível de curso grafado "FENC" e "FNC" | Mesmo conceito | Matriz § 3 |
| U-10 | Edição exata da PNP em que a fórmula da matrícula equivalente mudou | Não confirmada | PNP § 3 |
| U-11 | Teste fora do ajuste do motor da POC 0.0.2 (1 ano) existe no código, mas não nos documentos; é fraco | Registrado | Simulação § 6.2 |

## 5. Recomendações de agentes ainda não aprovadas

Propostas feitas durante a exploração ou nesta consolidação. **Não são decisões.**

| Recomendação | Origem |
|---|---|
| Princípios de engenharia a acrescentar aos princípios do projeto | [Guia SDD](../sdd/guia-de-inicializacao.md) § 2 (este pacote) |
| Estudo de caso do técnico concomitante/subsequente com dados por turma do sistema acadêmico | Estudo PNP § 10 |
| Entrevistas com gestores (fase 0 do documento fundador) e oficina de 2 h com 3 a 4 diretores | Fundador § 22; revisão estratégica O2 |
| "O próximo experimento deve começar pela negociação, não pelo simulador" | Diagnóstico de 10/11/2026 § 4.2 |
| Preservar o guia atual da PNP como evidência | Estudo PNP |
| Separar os testes de auditoria que dependem só do demonstrativo público (C5) dos que dependem da planilha não pública | Verificação de 11/11/2026 |
| Conferir a versão certificada da Portaria 243/2026 | Manifesto de evidências de 09/11/2026 |
| Verificar a Portaria MEC 357/2026 (metas de oferta técnica por campus), citada no documento fundador | Este pacote |
| Usar a matriz anual como dado de calibração (previsto × observado) | Revisão estratégica O6 |
| Guardas contra manipulação de métricas (MOOC massivo, FIC curto, reclassificação, turmas superlotadas) | Revisão estratégica O8 |
