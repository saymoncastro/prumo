# Aprendizados e limites das provas de conceito e estudos

> **Natureza:** história experimental do laboratório (08 a 11/11/2026), registrada para não ser repetida. **Nenhuma prova de conceito representa a arquitetura do produto**, e nenhuma foi mostrada a um gestor: toda afirmação de compreensibilidade é avaliação de quem construiu.
> **Artefatos preservados:** páginas estáticas em [referencias/prototipos/](../../referencias/README.md); motores e testes em [scripts/analises/motores-coortes-poc/](../../scripts/analises/README.md); estudos em [referencias/estudos/](../../referencias/README.md). O restante ficou no repositório exploratório ([inventário](../../migracao/inventario-origem-destino.md)).
> **Relacionados:** [simulação](../simulacao/modelos-premissas-e-validacao.md) · [PNP](../inteligencia/exploracao-estrategica-pnp.md) · [decisões](../decisoes/decisoes-hipoteses-e-pendencias.md)

## 1. Linha do tempo

| Data | Trabalho | Pergunta |
|---|---|---|
| 08/11 | Documento fundador v1.1; proposta de nome | Como melhorar as decisões que definem a oferta? |
| 08–09/11 | Auditoria da matriz: fonte canônica 1.0.0 → 1.2.2 | Conseguimos reproduzir a matriz? |
| 09/11 | Revisão estratégica | O esforço está no lugar certo? |
| 09/11 | Portão de dados; protótipo da meta de 50% (v1 e, 18 minutos depois, v2) | Como os campi levam o Ifes a 50% de técnico? |
| 09/11 | Avaliação da v2; demonstração de recomposição | Como um campus recompõe a oferta e o que negocia? |
| 10/11 | Estudo da PNP | A série histórica merece entrar no produto? |
| 10/11 | POC 0.0.2 | Ampliar, aproveitar melhor ou reorganizar? |
| 10/11 | Consolidação: visão canônica e diagnóstico | O que é o PRUMO, afinal? |
| 11/11 | Spec Kit: princípios v1.0.0 e rascunho da especificação 001 | Primeira jornada integrada |

## 2. Estudos

### 2.1. Auditoria da Matriz CONIF (fonte canônica 1.0.0 → 1.2.2)

| | |
|---|---|
| **Objetivo** | Reproduzir as regras da matriz e documentá-las com rastreabilidade |
| **Artefatos** | [Fonte canônica 1.2.2](../../referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md); revisão crítica e auditoria complementar (laboratório); 32 testes em `tests/auditoria_matriz/` (laboratório) |
| **Dados** | Planilha do Ifes (não pública), demonstrativo do IFMT 2026, portarias 646/2022 e 243/2026, página da PROAD |
| **Comprovou** | A regra operacional da matrícula total (RO-MT) reproduz 2.322/2.322 ciclos do Ifes e 1.086/1.086 do IFMT; o texto das portarias, só 1.300 e 993. Defasagem de dois anos em 2026. Três réguas separadas. 32 testes passam (reexecutados em 11/11/2026) |
| **Limitações** | Depende de arquivos não públicos; nenhuma regra homologada por especialista; nada sobre 2027 |
| **Decisões que fundamentou** | Regras versionadas por exercício; texto × prática registrados em separado; três medidas de matrícula; referência financeira condicional |
| **Lição** | Retorno decisório baixo da auditoria forense da planilha (20 das 65 regras da versão 1.1 tratavam da planilha). Congelar |

### 2.2. Revisão estratégica (09/11/2026)

| | |
|---|---|
| **Objetivo** | Avaliar se o esforço estava no lugar certo |
| **Artefato** | [revisao-estrategica-2026-11-09.md](../../referencias/estudos/revisao-estrategica-2026-11-09.md) |
| **Estabeleceu** | A alavanca de coordenação está no bloco de Qualidade e Eficiência (indicadores com degraus), não no Funcionamento (aditivo e de baixa alavancagem). O Ifes recebia R$ 0 nos subcomponentes de técnico (44% contra degrau de 50%) e EJA (1,86% contra 2,5%) em 2026. Oito oportunidades (mapa de degraus; pacto de contribuições; aluno-hora ponderada; sentinela de RAP; calendário de efeitos; previsto × observado; conformidade da planilha; guardas contra manipulação de métricas). Oito riscos de concepção |
| **Limitação** | Valores em reais são inferências "mantidos os demais"; o reposicionamento do produto em torno do "pacto de degraus" foi rebaixado a caso de uso |

### 2.3. Portão de dados (09/11/2026)

| | |
|---|---|
| **Objetivo** | Conferir se os dados públicos reproduzem os valores oficiais antes de construir protótipo |
| **Artefato** | [portao-de-dados-2026-11-09.md](../../referencias/estudos/portao-de-dados-2026-11-09.md) |
| **Comprovou** | A soma dos campi na PNP (ano-base 2024) reproduz os percentuais legais e o professor-equivalente da matriz 2026. O numerador da RAP e a eficiência acadêmica não reconciliam ([PNP](../inteligencia/exploracao-estrategica-pnp.md) § 6) |
| **Limitação** | O mesmo arquivo preserva o registro original com veredito oposto; vale a conclusão de cima. Contém link para um artefato privado que não funciona para terceiros |
| **Reaproveitamento** | **Valores de referência** da primeira especificação |

### 2.4. Estudo da PNP (10/11/2026)

| | |
|---|---|
| **Objetivo** | Saber se a série histórica da Rede merece entrar no produto e como |
| **Artefatos** | [estudo-pnp-2026-11-10.md](../../referencias/estudos/estudo-pnp-2026-11-10.md); script e resultado em [scripts/analises/estudo-pnp/](../../scripts/analises/README.md) |
| **Comprovou** | 14 tabelas reproduzíveis; reproduzidas **byte a byte** em 11/11/2026, já na estrutura do pacote. Quebras metodológicas; cinco achados; quatro *insights* priorizados |
| **Limitações** | Agregados, sem coorte; correlações com n = 41; nenhuma afirmação causal |
| **Decisões que fundamentou** | Inteligência como camada de premissas e contexto, não painel; decisão em vagas com quatro premissas separadas; série só em bloco comparável |

## 3. Protótipos

Os três são páginas HTML estáticas, autocontidas (dados e motor embutidos; única dependência externa: fontes tipográficas do Google Fonts, com reserva local), registros em `localStorage`, sem servidor.

### 3.1. Meta de 50% de formação técnica (v1 e v2)

| | |
|---|---|
| **Pergunta** | Como os campi levam o Ifes a 50% de formação técnica? |
| **Usuário pressuposto** | Reitoria e planejamento |
| **Artefato** | [referencias/prototipos/prumo-poc.html](../../referencias/prototipos/prumo-poc.html) (v2). A v1 só existe no commit `a3b64df` do laboratório |
| **Dados** | PNP anos-base 2024 e 2025; demonstrativo C5 |
| **Mecânica** | Retrato de um ano; decisão em "+n matrículas" num curso existente; contribuição por campus decomposta |
| **Comprovou** | Dados públicos por campus reproduzem os percentuais legais oficiais; a contribuição de cada campus se decompõe de forma exata |
| **Ilustrou** | Nenhum ajuste marginal alcança a meta (dois campi: +0,23 p.p.; reorientar o Cefor: +2,28 p.p.); uma unidade de EaD move vários indicadores ao mesmo tempo |
| **Limitações** | Decisão em matrículas, não em vagas; sem tempo, sem coortes, sem recursos; sem testes; dois erros numéricos corrigidos depois (reduções acima do saldo; quantidades negativas) |
| **Reaproveitar** | Três réguas separadas; frase de veredito ("ainda faltam X p.p."); contribuição em p.p. por campus; alerta de mudança de classificação |
| **Não deve orientar** | Simulação em matrículas de um único ano; Ifes e Cefor fixos no código |

### 3.2. Recomposição de oferta (Itapina e Barra de São Francisco)

| | |
|---|---|
| **Pergunta** | Como um campus recompõe sua oferta entre 2027 e 2029, o que cada alternativa exige e entrega, e o que negocia com a instituição? |
| **Usuário pressuposto** | Direção de campus; reitoria na pactuação |
| **Artefatos** | [referencias/prototipos/prumo-recomposicao.html](../../referencias/prototipos/prumo-recomposicao.html); motor e teste em `scripts/analises/motores-coortes-poc/recomposicao/` |
| **Dados** | PNP 2017–2025; parâmetros emprestados de outros campi para oferta nova; C5 |
| **Comprovou** | Motor simples de coortes reproduz técnicos integrados fora do ajuste com erro de 2% a 3% |
| **Ilustrou** | Pico de recursos antes do efeito na matriz (ambiente crítico a 120% em 2029 numa expansão); "manter também muda"; colunas ano-base → exercício; proposta com responsável, contrapartidas, recursos e indicador; nenhuma combinação cruza limiar |
| **Limitações** | Erros altos fora dos integrados (63% em oferta recém-implantada; 68,9% num concomitante); **8%, 15% e 19% de graduação não reproduzíveis pelo código versionado** ([simulação](../simulacao/modelos-premissas-e-validacao.md) § 6.2); docentes, ambiente e custo por premissa genérica; demanda da oferta nova não estimada |
| **Reaproveitar** | Marcadores [FATO], [PREMISSA], [EMPRÉSTIMO], [NÃO ESTIMADO]; oferta nova por empréstimo; campos da proposta; aba "Como calcula" com o erro do modelo |
| **Não deve orientar** | Abas por campus fixas; ambientes e expressões de curso fixos no código |

### 3.3. POC 0.0.2 (Vitória e Serra)

| | |
|---|---|
| **Pergunta** | Ampliar vagas, aproveitar melhor os cursos existentes ou reorganizar ofertas? |
| **Usuário pressuposto** | Direção de ensino do campus; visão institucional em "Compor" |
| **Artefatos** | [referencias/prototipos/prumo-poc-002.html](../../referencias/prototipos/prumo-poc-002.html); capturas em `referencias/prototipos/capturas-poc-002/`; motor e teste em `scripts/analises/motores-coortes-poc/poc-002/` |
| **Dados** | PNP 2017–2025; trajetórias Ifes × Rede41; C5 |
| **Comprovou** | Os números da tela conferem com o estudo da PNP (16 verificações passam) |
| **Ilustrou** | Evidência histórica junto da decisão (precedente); três alternativas lado a lado com faixas e coluna "em regime"; "o que precisa ser verdade"; resposta condicional honesta; contribuição por objetivo e grade de 16 combinações; "o PRUMO não escolhe por você" |
| **Limitações** | Ajuste e erro nos mesmos anos (2023–2025); erros de 42% e 43% em concluintes de duas ofertas; efeito do programa de permanência arbitrado; docentes sem área; linha de base derruba a EJA do Ifes de 1,98% para cerca de 1,54% em 2032 (a verificar) |
| **Reaproveitar** | Marcadores fato / estimado / premissa / hipótese / não estimado; trajetória em índice com a pandemia sombreada; tabela de campi sem ordenação; separação de evasão, conclusão e retenção (como comportamento); compor como centro |
| **Não deve orientar** | Alternativas fixas; campi e cursos fixos no código |

## 4. Testes reproduzíveis

| Teste | Comando (no repositório novo) | Precisa de dados externos? | Resultado em 11/11/2026 |
|---|---|---|---|
| Motor da recomposição | `node scripts/analises/motores-coortes-poc/recomposicao/testar_coortes.cjs` | Não | 6 de 6 passam |
| Motor da POC 0.0.2 | `node scripts/analises/motores-coortes-poc/poc-002/testar_poc002.cjs` | Não | 16 de 16 passam |
| Estudo da PNP | `python3 scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py <pasta PNP>` | Sim (PNP) | Saída idêntica byte a byte |
| Auditoria da matriz (32 testes) | Só no laboratório | Sim (planilha não pública) | 32 de 32 passam |

Os extratores e o montador das POCs reproduziram dados e páginas byte a byte em cópia descartável (11/11/2026); ficaram no laboratório.

## 5. Limitações técnicas transversais

- **Três motores incompatíveis** (a 0.0.2 é reescrita, não evolução): duração, regra de turmas, definição de evasão e calibração divergem.
- **Código duplicado** entre extratores e templates (classificação de ofertas, faixas de qualidade, cálculo da instituição).
- **Ifes fixo no código:** nomes de campi, exceção do Cefor, exemplos, faixas, metas, coordenadas de células do demonstrativo.
- **Persistência no navegador** e dados embutidos no HTML.
- **Classificação de formação de professores por nome de curso.**

## 6. O padrão de fragmentação

Cada etapa produziu um achado sólido, e cada achado foi promovido a pergunta organizadora do produto:

| Achado | Promovido a |
|---|---|
| O Ifes recebe zero em dois subcomponentes de qualidade | "Pacto de metas com degraus" como primeiro caso de uso |
| A v2 não representa recomposição de portfólio | "Recomposição de um campus" |
| No técnico, as vagas se preenchem e as matrículas caem | "Ampliar, aproveitar ou reorganizar" |

Os achados estão corretos. O erro foi tratar um caso de uso como definição do produto. **Uma especificação parte da finalidade do produto, não de um protótipo nem de um achado** ([guia SDD](../sdd/guia-de-inicializacao.md) § 3).

## 7. O que foi descartado

| Descartado | Por quê |
|---|---|
| Funcionamento por campus em reais como porta de entrada | Incentiva volume de baixo valor contra o coletivo; estimável com planilha simples |
| MOOC como alavanca orçamentária | A Portaria 243/2026 fixou em 8%; vale cerca de R$ 72 mil para o Ifes |
| Estimar RAP e eficiência da matriz pela PNP | Não reconciliam |
| Programa de permanência com efeito arbitrado como alternativa comparável | Sem dado que sustente o tamanho do efeito |
| Continuar a auditoria forense da planilha | Retorno decisório baixo |
| Um caso de uso como pergunta organizadora | § 6 |
