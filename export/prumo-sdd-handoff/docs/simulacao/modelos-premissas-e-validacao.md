# Simulação estratégica: modelos, premissas e validação

> **Natureza:** visão da simulação plurianual e registro do que foi efetivamente testado. **Capacidade desejada ≠ modelo testado**: a tabela do § 9 separa as duas coisas.
> **Evidência de origem:** dois motores de coortes do laboratório, preservados com seus testes em [scripts/analises/motores-coortes-poc/](../../scripts/analises/README.md) como **referência de comportamento**, não como base de implementação. Histórico das POCs em [aprendizados e limites](../evidencias/aprendizados-e-limites-das-pocs.md).
> **Relacionados:** [visão](../produto/visao.md) § 6.3 · [PNP](../inteligencia/exploracao-estrategica-pnp.md) § 9 · [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) · [governança](../governanca/metas-contribuicoes-e-aprendizado.md)

## 1. Finalidade e princípios

Representar o portfólio de um campus e projetar, ano a ano, o que cada decisão de oferta **exige** (docentes, ambientes, custos, prazo) e **entrega** (ingressantes, matrículas, concluintes, efeitos nos objetivos institucionais e efeitos orçamentários condicionais).

**[PRINCÍPIO]**

- **A decisão é sobre vagas e ofertas**, não sobre matrículas. Matrícula é consequência de ingresso e trajetória.
- **Três marcos de tempo:** ano da decisão → ano-base em que o efeito aparece nos dados → exercício orçamentário que usa esse ano-base (na matriz de 2026, exercício = ano-base + 2; parâmetro por exercício).
- **Recursos chegam ao limite antes do efeito aparecer.** O pico de turmas simultâneas vem antes da repercussão na matriz.
- **Manter também muda.** A linha de base contém as turmas em curso.
- **Projeção não é previsão.** Onde o modelo erra mais ao reproduzir o passado, o resultado aparece em faixa.
- **Reproduzir o histórico não é validar a previsão.** Capacidade preditiva se mede em anos que ficaram fora do ajuste.
- **Só se detalha o recurso que limita a decisão.**
- **Sem recomendação automática** e sem ordenar cursos por retorno financeiro.
- **Simular o ciclo de vida completo das turmas** e o horizonte de planejamento, não só o próximo semestre.

## 2. Linha de base: o portfólio atual

- A linha de base de um campus é o portfólio observado no último ano-base, projetado sem mudança de vagas, com as turmas já ingressadas seguindo até o fim.
- Ela **não é estática**: ofertas em extinção encerram, ofertas recém-abertas crescem (no laboratório, uma graduação veterinária crescia e uma de ciências agrárias se encerrava sem nenhuma decisão nova).
- Cenários são sempre comparados à linha de base, nunca ao último ano observado.

## 3. Decisões e premissas

**Decisões** (por oferta, a partir de um ano de ingresso): abrir, ampliar, reduzir, suspender, substituir uma forma por outra, encerrar; investir em permanência; mudar turno ou modalidade.

**Premissas separadas** (lição central do estudo da PNP: um índice único de "permanência" mistura mecanismos diferentes):

| Premissa | Definição operacional usada no laboratório | Origem possível |
|---|---|---|
| Ocupação | Ingressantes ÷ vagas | Histórico da oferta; limitada pela procura observada |
| Evasão | Evadidos ÷ matrículas (agregado anual) | Histórico da oferta; média do campus; empréstimo |
| Conclusão no prazo | Fração da turma que conclui na duração nominal | Estimada por ajuste |
| Retenção | Quem não conclui no prazo fica mais um ano e então conclui ou evade | Estimada por ajuste |
| Duração | Nominal ou ajustada por tipo de oferta | Projeto pedagógico; ajuste |
| Tamanho de turma | Vagas ÷ 40 com regra de arredondamento | Premissa institucional |

**Toda premissa tem natureza e origem:** histórico próprio da oferta; **empréstimo** de oferta equivalente (obrigatório para oferta nova, identificado como tal); ou **julgamento** do gestor (valor anterior preservado, evidência anexável). Cada premissa mostra o valor histórico próprio e a faixa dos comparáveis.

**Efeito de programas de permanência:** não há evidência que sustente o tamanho do efeito. Nos protótipos foi **arbitrado** (ex.: evasão −30%, faixa −15% a −45%). Enquanto não houver evidência, aparece como premissa de julgamento e o resultado como condicional, nunca como alternativa equivalente às demais.

## 4. Turmas e coortes

- A unidade de projeção é a **turma (coorte de ingresso)**. Matrícula de um ano = soma das coortes ativas.
- Conservação de coorte (RPE-04): ingressantes = ativos + concluintes + evadidos + transferidos, por ciclo e ano.
- Os dados públicos são **agregados anuais**, não coortes reais. Separar evasão, retenção e duração de forma confiável exige dados por turma do sistema acadêmico.
- Mudança de premissa (ex.: evasão menor) pode valer para todas as coortes ativas ou só para as novas; é escolha de modelo a explicitar.

## 5. Capacidade, custos e efeitos orçamentários

| Elemento | O que se quer | O que o laboratório fez |
|---|---|---|
| **Docentes** | Professor-equivalente por área, no pico de turmas simultâneas | Turmas × aulas semanais ÷ 14 h por professor; integrado 30 h, demais 20 h, PROEJA 25 h, pós 8 h; no integrado, metade técnica e metade núcleo comum. **Sem área de formação.** Conferência: 71,9 professores-equivalentes projetados em Itapina para 2026 contra 74 na PNP 2025; 24,3 contra 29 em Barra de São Francisco (diferença atribuída a FIC) |
| **Salas, laboratórios, turnos** | Ambiente crítico por turno ao longo do ciclo | Um ambiente crítico por campus, com capacidade premissa (laboratório de 40 h/semana; 8 salas diurnas) |
| **Gargalo no ciclo** | Em que ano e recurso a alternativa estrangula | Mostrado: ambiente crítico a 120% em 2029 numa expansão |
| **Custos e investimentos** | Custeio incremental, investimento necessário | Custeio por premissa genérica (R$ 3.234 por estudante adicional, outros custeios ÷ ME do Ifes 2025); investimento zero por padrão |
| **Indicadores institucionais** | Efeito no objetivo e conflitos | Percentuais legais do Ifes pela razão das somas, com os demais campi na linha de base |
| **Efeito orçamentário** | Referência condicional por componente e exercício | Só quando a combinação cruza faixa da QE (F-29), Rede de 2026 constante; Funcionamento só como direção (L-24); distribuição interna "sem valor" (RMO-075) |

**[PRINCÍPIO]** Nunca "contribuição − custo", nunca ranking de rentabilidade, nunca receita do campus. Ver [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) § 9.

## 6. Calibração, validação e incerteza

### 6.1. Regra

Um modelo de projeção só é aceito com **erro medido em anos fora do ajuste**, por tipo de oferta. Erro medido nos anos do ajuste mostra só aderência ao passado. A primeira especificação em rascunho fixou: tipos de oferta com erro fora do ajuste **acima de 5%** aparecem em faixa com largura dada pelo erro medido; o limite é parâmetro.

### 6.2. O que foi medido

**Motor da recomposição** (permanência única por oferta, duração fixa por tipo). Ajuste 2017–2021, previsão 2022–2025 com os ingressos observados (**fora do ajuste**). Reexecutado em 11/11/2026 no pacote:

| Oferta | Erro médio 2022–2025 | Reproduzido em 11/11/2026? |
|---|---|---|
| Técnico em Agropecuária integrado | 2% | Sim (2,0%) |
| Técnico em Zootecnia integrado | 3% | Sim (3,4%) |
| Técnico em Alimentos integrado | 3% | Sim (2,7%) |
| Agronomia (bacharelado) | 8% | **Não**: o código versionado retorna "sem série suficiente" |
| Pedagogia (licenciatura) | 15% | **Não**: idem |
| Ciências Agrárias | 19% | **Não**: idem |
| Zootecnia (bacharelado, implantado em 2020) | 63% | Sim (62,7%) |
| Técnico em Agropecuária subsequente | — (não citado nos documentos) | 31,6% na saída do teste |
| Administração (bacharelado) | — (não citado) | 37,2% |
| Técnico em Administração concomitante | 69% (citado só como "concomitante") | 68,9% |

**Os 8%, 15% e 19% de graduação, citados na visão e nos documentos do laboratório, não são reproduzíveis pelo código versionado**: com a retenção de 1 ano acrescentada à duração, o primeiro ano utilizável cai em 2021–2022 e a série de teste fica curta demais. Os números vêm de uma versão anterior do motor que não foi preservada. **Situação: inconclusivo.** Não usar esses três valores como evidência de capacidade preditiva em graduação.

Escolher a duração pelo melhor ajuste foi testado e abandonado nesse motor: os integrados passavam de 2–3% para 15–18% de erro.

**Motor da POC 0.0.2** (evasão, conclusão no prazo e retenção separadas; duração escolhida entre dois candidatos). Ajuste e medição **nos mesmos anos** (2023–2025): mostra aderência, não previsão.

| Oferta | Erro em matrículas | Erro em concluintes | Teste de 1 ano (ajuste 2023–2024, previsão 2025) |
|---|---|---|---|
| Mecânica concomitante (Vitória) | 7,9% | 9,2% | 1,7% |
| Eletrotécnica concomitante (Vitória) | 2,2% | 8,7% | 0,5% |
| Eletrotécnica integrado (Vitória) | 5,8% | 43,2% | 2,5% |
| Informática concomitante (Serra) | 12,6% | 41,7% | 2,2% |
| Informática para Internet integrado (Serra) | 4,7% | 11,4% | 3,2% |

O teste de um ano existe no código, mas é fraco (a duração foi escolhida com 2023–2025; há um único ponto) e não é citado nos documentos. Há só 2 a 3 pontos por oferta para ajustar conclusão e duração; dois parâmetros ficaram no limite da grade (conclusão 0 e 1).

**Nenhum motor foi testado contra o futuro real.**

### 6.3. Como a incerteza aparece

- **Faixas pelo erro do modelo** (recomposição: banda = máximo entre erro de validação e 2%, ou 5% sem validação, ou 25% sem teste; POC 0.0.2: banda de matrícula = máximo entre erros e 5%, de concluintes = máximo entre erros e 10%, teto de 60%).
- **Faixas pela premissa**: pessimista e otimista multiplicando o efeito (0,5 e 1,5 para permanência; 0,7 e 1,2 para ocupação nova).
- **"O que precisa ser verdade"**: lista das premissas de que o resultado mais depende, cada uma com sua natureza.
- **Não estimado**, explícito, onde não há base.

**Não houve análise de sensibilidade sistemática** (varredura de premissas). Só multiplicadores fixos e bandas de erro.

## 7. Motores investigados e decisões pendentes

| | Motor da recomposição | Motor da POC 0.0.2 |
|---|---|---|
| Mecanismo | Permanência única r por oferta, ajustada entre 0,50 e 1,00 | Evasão, conclusão no prazo e retenção separadas |
| Duração | Fixa por tipo (integrado 3; concomitante/subsequente 2; bacharelado 5 + 1; licenciatura/tecnologia 4 + 1) | Escolhida entre dois candidatos por ajuste |
| Turmas | vagas ÷ 40 arredondado, mínimo 1 | teto(vagas ÷ 40 − 0,05) |
| Evasão | Não entra nas ofertas existentes | Evadidos ÷ matrículas |
| Calibração | 2017–2021, teste 2022–2025 | 2023–2025 |
| Testes | 6 verificações, passam | 16 verificações, passam |

São **incompatíveis** (reescrita, não evolução). **Pendente**: um motor único, com que mecanismos, e qual erro fora do ajuste é aceitável por tipo de oferta. Decidir só depois de saber que pergunta o gestor faz; unificar antes é risco de superengenharia.

**Achado a verificar antes de reuso:** na POC 0.0.2, a própria linha de base "manter" derruba a EJA do Ifes de 1,98% (2025) para cerca de 1,54% em 2032, porque o PROEJA de Vitória cai de cerca de 598 para 421 ME (oferta sem vagas e evasão de 0,43). Pode ser artefato da ancoragem e da evasão alta. Não documentado no laboratório.

## 8. Comparação de cenários

- Alternativas lado a lado com a linha de base, ano a ano e "em regime".
- Sem indicação da melhor. A resposta honesta pode ser condicional (ex.: "B é a mais promissora se for possível reduzir a evasão em cerca de 30% a um custo aceitável").
- Resultado registrado guarda as versões de dados, regras e modelo e não é recalculado em silêncio.

## 9. Capacidades desejadas × testadas

| Capacidade | Situação |
|---|---|
| Linha de base com turmas em curso | **Testada** (ambos os motores) |
| Ampliar, reduzir, suspender, abrir oferta | **Testada** em motor; ilustrada em tela |
| Substituir forma de oferta | Ilustrada (POC 0.0.2) |
| Evasão, retenção e conclusão separadas | Ilustrada; ajuste nos mesmos anos |
| Validação fora do ajuste | **Testada** só para técnicos integrados (2–3%) e uma oferta nova (63%); graduação inconclusiva |
| Oferta nova por empréstimo de parâmetros | Ilustrada |
| Efeito de permanência | **Não sustentado** (arbitrado) |
| Docentes por área | **Não testada** |
| Salas, laboratórios, turnos ao longo do ciclo | Esboçada (um ambiente crítico com capacidade premissa) |
| Custos e investimentos | Esboçada (premissa genérica) |
| Efeito em percentuais legais | **Testada** pela razão das somas, com dados conciliados |
| Efeito orçamentário condicional | Esboçada (só cruzamento de faixa da QE) |
| Matrícula total e Funcionamento em reais | **Não estimada** (L-24) |
| Distribuição interna | **Não estimada** (hipótese) |
| Demanda de oferta nova | **Não estimada** |
| Análise de sensibilidade sistemática | **Não feita** |
| Validação com gestores | **Não feita** |
