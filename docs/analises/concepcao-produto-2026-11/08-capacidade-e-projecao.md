# 8 · Capacidade de execução e projeção longitudinal

> **Segunda rodada, 12/11/2026.** Documento novo. Responde aos §§ 2 e 3 do pedido da segunda rodada: como garantir que uma alternativa estrategicamente interessante seja também institucionalmente viável, e como mostrar sua evolução no tempo sem inventar precisão.
> **Protótipo:** [prototipo/prumo-conceito.html](prototipo/prumo-conceito.html), telas *Campi* e *Bancada*. As curvas de Vitória e Serra são calculadas no navegador com o motor da POC 0.0.2 sobre dados reais da PNP; a capacidade é ilustrativa.

---

## 1. O que existia, o que foi omitido e o que foi adiado

| Tema | Onde já aparecia | O que a primeira rodada fez | Veredito desta rodada |
|---|---|---|---|
| Salas e laboratórios por turno, pico de turmas simultâneas | Documento fundador § 8 (essencial); recomposição: "ambiente crítico" com uso por turma e capacidade em h/semana (Itapina: laboratório esgotado em 2029) | Reduziu a "um campo livre por decisão" no MVP; estrutura na SPEC-004 | **Subdimensionado.** Um campo livre não verifica nada nem é reutilizável. A versão mínima estruturada é barata e deve entrar na primeira jornada (§ 2) |
| Docentes por área e carga horária | Fundador § 9 (níveis 1 a 4); recomposição e POC 0.0.2: professores-equivalentes por premissa de aulas por turma | Manteve professores-equivalentes totais | **Subdimensionado.** Docente total não revela gargalo: o gargalo é por área. Nível 2 (área e turno) entra na primeira jornada |
| Curvas de evolução por alternativa | POC 0.0.2: gráficos de matrículas e concluintes 2017–2032 com observado, manter e A/B/C; recomposição: quadro anual até 2029 | Mostrou quadro comparativo e "linha dos três marcos" | **Omitido.** As curvas eram o centro da simulação nos protótipos e a primeira rodada as trocou por uma tabela de resultados finais. Voltam como elemento principal da bancada (§ 3) |
| Alavancas combináveis | POC 0.0.2: três alternativas fixas; recomposição: decisões combináveis | Cinco tipos de decisão como cartões | **Mantido e reforçado.** O protótipo v2 mostra alavancas ligáveis em conjunto |
| Ociosidade e infraestrutura liberada | Fundador § 8.3 | Não tratado | **Faltava.** Entra como sinal na ficha do campus |
| Alocação fina, grade horária, inventário patrimonial | Fundador §§ 8 e 21 (fora do escopo) | Fora | **Adiado por razão legítima.** Continua fora |
| Coortes por turma do sistema acadêmico | Estudo da PNP § 10 | Fora | **Adiado por razão legítima.** Sem acordo de dados; o modelo funciona com agregados |

---

## 2. Modelo mínimo de capacidade por campus

### 2.1. A pergunta que ele responde

> **"Esta alternativa cabe no campus, em que ano deixa de caber, por qual recurso, em qual turno, e o que resolveria?"**

Não responde "qual professor dá qual aula" nem "qual sala recebe qual turma". Essas são perguntas de gestão acadêmica e de horário, que continuam fora do PRUMO.

### 2.2. Os quatro elementos

| Elemento | O que o campus informa | O que o PRUMO calcula | Unidade |
|---|---|---|---|
| **Turmas simultâneas** | Nada (confirma o turno principal de cada oferta) | Turmas ativas por oferta, turno e ano, a partir das coortes: vagas ÷ alunos por turma, para cada ano do ciclo | Turmas |
| **Salas por turno** | Quantas salas comuns estão disponíveis em cada turno | Uso por turno = turmas ÷ salas | Turmas por turno |
| **Ambientes críticos** (até três) | Nome, capacidade semanal por turno, quais ofertas o usam e quantas aulas por turma | Uso por ambiente e turno | Aulas por semana |
| **Docentes por área** | Áreas agregadas (eixos técnicos e núcleo comum) e quantos docentes atuam em cada | Horas-aula demandadas ÷ (docentes × horas de aula por professor) | Professores-equivalentes |

Premissas padrão, editáveis e marcadas: 40 alunos por turma; 30 aulas semanais no integrado (metade técnica, metade núcleo comum), 20 no concomitante e subsequente, 25 no PROEJA; 14 horas de aula por professor. São as mesmas da POC 0.0.2 e da recomposição.

### 2.3. Verificável

Antes de simular, a ficha do campus mostra o **uso calculado em 2025** para cada recurso. O gestor confirma ("sim, usamos 11 salas à noite") ou corrige a premissa até o número bater. É o mesmo princípio do portão de dados aplicado à capacidade: um modelo que não reproduz o presente não projeta o futuro.

A PNP oferece uma conferência externa parcial: o professor-equivalente total do campus. O modelo cobre só as ofertas modeladas (no protótipo, técnicos presenciais), e a ficha mostra a diferença em vez de escondê-la. Em Serra, os técnicos explicam ≈ 39 dos 98 professores-equivalentes; o restante atende graduação e outras ofertas.

### 2.4. Reutilizável

- **Cadastro uma vez por campus**, confirmação uma vez por ano, junto da carga da PNP.
- **Todos os cenários e propostas usam o mesmo cadastro.** A restrição de uma proposta é comparável com a de outra.
- **Versionado como premissa:** a proposta congela a capacidade usada, para que a conferência futura saiba de onde partiu.

**Esforço estimado [HIPÓTESE]:** 20 a 40 minutos por campus, com a direção de ensino. A confirmar no piloto.

### 2.5. O que ele mostra

- **Mapa de calor recurso × ano** mantendo a oferta: verde até 85%, âmbar até 100%, vermelho acima; cinza abaixo de 60% (ociosidade).
- **Primeira restrição** de cada alternativa: ano, recurso e turno.
- **Ociosidade e capacidade liberada**: turnos ou ambientes que esvaziam quando uma oferta é reduzida ou migra (no protótipo, o noturno de Serra quando o concomitante encolhe).
- **Alavancas de resolução** como decisões da própria bancada: mudar o turno das turmas novas, prover docentes de uma área, adequar um ambiente. No protótipo, colocar as turmas novas do integrado de Serra no vespertino resolve o laboratório e deixa só a restrição de núcleo comum.

### 2.6. Escada de detalhamento

| Nível | Conteúdo | Onde |
|---|---|---|
| 1 | Professores-equivalentes totais por premissa | Protótipos anteriores |
| **2** | **Docentes por área, salas por turno, até três ambientes críticos, turmas simultâneas** | **SPEC-001 (primeira jornada)** |
| 3 | Componentes curriculares por área, dia e bloco, equipamentos, custo de adequação e investimento | SPEC-004 |
| 4 | Sensibilidade e alocação com restrições detalhadas | Só se a instituição pedir |

---

## 3. Projeção longitudinal

### 3.1. As três camadas

Toda curva da bancada e da mesa tem três camadas, sempre com o mesmo desenho:

| Camada | Desenho | Natureza |
|---|---|---|
| **Observado** 2017–2025 | Linha preta com pontos | Fato (PNP) |
| **Manter a oferta** 2026–2035 | Linha cinza tracejada | Estimado: as turmas abertas continuam evoluindo, e manter também muda |
| **Cenário** 2026–2035 | Linha verde grossa, com faixa | Estimado: alavancas aplicadas a partir de 2027 |

Opcionalmente, linhas finas com os pontos de partida (ampliar, aproveitar, reorganizar) para comparação.

### 3.2. Indicadores disponíveis na bancada

| Indicador | Histórico | Projeção | Observação |
|---|---|---|---|
| Matrículas | Sim | Sim, com faixa | Inclui retidos |
| Ingressantes | Sim | Sim | Vagas × ocupação |
| Concluintes | Sim | Sim, faixa larga | O mais ruidoso dos indicadores |
| Ocupação de vagas | Sim | Sim | Ingressantes ÷ vagas |
| Evasão anual | Por oferta, não no agregado | Sim | Agregado de ofertas com perfis diferentes não é exibido como série |
| Retidos além do prazo | Não (a PNP não separa por oferta) | Sim | Estimado pelo modelo |
| Matrícula equivalente (PNP) | 2021–2025 | Sim | Bloco comparável só desde 2021 |
| MT estimada | Não | Sim | Por premissa de carga e peso; exata com os ciclos da instituição |
| Professores-equivalentes, salas, ambientes | 2025 (verificação) | Sim | Contra a capacidade informada |

### 3.3. Quando o impacto começa, intensifica, estabiliza e esbarra

A bancada calcula e anota no gráfico, para o indicador selecionado, a diferença entre cenário e manter:

- **Começa:** primeiro ano em que a diferença passa de 5% do seu máximo.
- **Intensifica:** ano de maior variação anual da diferença.
- **Estabiliza:** primeiro ano a partir do qual a diferença fica a menos de 10% do valor final. Se não estabiliza até 2035, diz "ainda crescendo".
- **Restrição:** primeiro ano em que algum recurso passa de 100% da capacidade.

São regras simples, declaradas e determinísticas. Servem para que o gestor leia o ritmo do efeito sem interpretar o gráfico sozinho.

### 3.4. Incerteza sem falsa precisão

A faixa combina três fontes, e a legenda diz quais:

1. **Erro do modelo por oferta**, medido ao reproduzir o passado (POC 0.0.2: 2% a 13% em matrículas; até 43% em concluintes). O critério de aceite do produto exige erro medido **fora da amostra** por tipo de oferta (princípio VII).
2. **Sensibilidade das hipóteses**: efeito de permanência de metade a 1,5 vez o valor central; ocupação das vagas novas de 70% a 120% da premissa.
3. **Quebras metodológicas**: séries de matrícula equivalente só a partir de 2021; pandemia sombreada; ofertas encerradas fora do histórico para que a série seja comparável com a projeção.

**Onde os dados não sustentam a estimativa, não há curva**: IEA e RAP da matriz aparecem como "não estimado", com a direção dada pelos concluintes e pela evasão. Evasão agregada histórica não é desenhada.

### 3.5. Horizonte

Dez anos (2026–2035). É o suficiente para que um integrado de quatro anos aberto em 2027 forme duas turmas e para ver o efeito na matriz até o exercício de 2037. O valor "em regime" da POC 0.0.2 (2042) continua útil como texto, não como curva.

### 3.6. O mesmo horizonte na composição

A mesa institucional só soma unidades projetadas **com o mesmo motor, a mesma edição da PNP e o mesmo horizonte**. Unidades sem simulação (no protótipo, Itapina, Barra de São Francisco e Cefor) aparecem numa **linha separada**, marcada como ilustrativa, e nunca dentro da linha calculada.

---

## 4. A resposta que a bancada precisa dar

O critério de sucesso da segunda rodada é uma pergunta do gestor. A bancada responde com um parágrafo gerado por regra a partir dos números calculados. Exemplo do protótipo, Serra, "Reorganizar + preencher + evasão −20%":

> De 2027 a 2035, **+2 ingressantes e +190 concluintes técnicos** (faixa +116 a +233) em relação a manter a oferta; **+68 matrículas ativas** em 2035. Recursos: até **+2,1 professores-equivalentes**; **restrição em 2028** (laboratórios de informática no matutino e docentes de núcleo comum). Contribuição à formação técnica do Ifes: **+0,10 p.p.** em 2030 e em 2035. Na matriz: ≈ **+99 MT** no ano-base 2030, referência de ≈ **R$ 131 mil** no exercício de 2032. O PRUMO não escolhe por você.

E para Vitória, com a mesma combinação: +343 ingressantes, +648 concluintes (faixa +368 a +932), +4,3 professores-equivalentes, restrição de núcleo comum em 2029, +0,33 p.p. em formação técnica em 2030, ≈ +240 MT e ≈ R$ 317 mil no exercício de 2032.

Os valores de capacidade dependem do cadastro ilustrativo. Os demais vêm do motor sobre dados reais.

Duas leituras para a reitoria saem diretamente desses números:

- **Nenhum campus sozinho move muito a estrela-guia.** A soma de Vitória e Serra, na melhor combinação, fica em torno de +0,4 p.p. em formação técnica. O degrau de 50% exige a composição institucional e a decisão sobre a oferta a distância.
- **A conta de concluintes é a que mais muda entre as alternativas**, e é a que mais depende de hipóteses. A faixa mostra isso.
