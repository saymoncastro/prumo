# 6 · Avaliação crítica e recomendação

> **Estudo de concepção de 12/11/2026, revisado na segunda rodada no mesmo dia.** Posição deste estudo sobre a visão vigente, com os pontos de discordância e a recomendação de como iniciar o repositório definitivo.
> **Terceira rodada (13/11):** D11 revista. A participação pode ser meta institucional, sem cota por unidade. A formalização, o horizonte e o valor continuam abertos ([documento 10, § 10](10-terceira-rodada.md#10-decisões-que-esta-rodada-ajusta)).
> **Segunda rodada:** os §§ 3.5 e 3.6 foram revistos (a primeira versão subdimensionou a matriz e a capacidade); o § 3.8 e a decisão D11 são novos. A conclusão original desses parágrafos é citada na própria revisão.
> **Método:** leitura da visão, do diagnóstico, do próximo passo, dos princípios, do documento fundador, das cinco análises, da fonte canônica da matriz (por resumo dirigido) e das capturas e documentos dos protótipos. Nenhum dado foi recalculado.

---

## 1. O que sabemos de fato

### 1.1. Validado ou demonstrado (com evidência reproduzível no repositório)

| Item | Evidência |
|---|---|
| A soma dos campi na PNP reproduz os percentuais legais usados na matriz de 2026 (técnico 0,4403 × 0,44; formação de professores e EJA exatos) | [Portão de dados](../prumo-poc-portao-dados.md) |
| O professor-equivalente da PNP reconcilia com a matriz (±1%); o numerador da RAP não | Portão de dados; estudo da PNP, T13 |
| A regra operacional da matrícula total reproduz 2.322/2.322 ciclos do Ifes e 1.086/1.086 do IFMT; o texto das portarias não | [Revisão crítica](../../dominio/revisao-critica-regras-prumo.md); 32 testes de auditoria |
| Os degraus de Qualidade do Ifes em 2026 (ex.: técnico de 44% para 50% vale cerca de +R$ 2,06 mi/ano, mantidos os demais) | Fonte canônica, V-13; teste T-Q03 |
| Fatos longitudinais da Rede: crescimento por FIC e EaD; matrícula cresce por ingresso e por tempo de vínculo em partes iguais; no técnico concomitante e subsequente do Ifes as vagas se preenchem e matrículas e concluintes caem; uma oferta em pulso move o indicador institucional | [Estudo da PNP](../prumo-pnp-inteligencia-comparativa-exploratoria.md), 14 tabelas |
| Sem a unidade de EaD (Cefor), os campi do Ifes somam cerca de 51% de formação técnica | Portão de dados |
| Um modelo simples de coortes reproduz técnicos integrados com 2–3% de erro fora da amostra; erra 8–19% em graduação e 63% numa oferta recém-implantada | Teste da recomposição |

### 1.2. Decidido conceitualmente (pelo idealizador, sem validação externa)

- Governança distribuída como finalidade; inteligência e simulação como fundamento (visão § 1; princípio I).
- Três réguas por objetivo; razão das somas; decisão em vagas; três marcos de tempo; natureza de todo número; sem recomendação; sem ranking (princípios II a VIII).
- PRUMO pensado como produto reutilizável por outras instituições (visão § 8, direção de 10/11).
- Encerrar a descoberta ampla e não fazer sessões com gestores agora (próximo passo § 1).
- Primeira especificação: jornada integrada estreita, genérica quanto ao objetivo, com o percentual técnico como caso demonstrativo (próximo passo § 3.3).

### 1.3. Hipótese

- Que gestores reconheçam o problema de coordenação como seu e que a reitoria aceite metas diferentes por campus (H1, H6).
- Que a evidência e a procedência das premissas mudem decisões (H2, H3).
- Que comparação por trajetória não seja lida como ranking (H5).
- Que outra instituição tenha interesse e dados compatíveis; que exista quem pague e quem mantenha os dados (H7 a H10).
- Que a distribuição interna do Ifes seja "matriz por campus com piso e teto" (RMO-075, rebaixada a hipótese).
- O efeito de qualquer ação de permanência.
- **Acrescentada por este estudo:** que o ciclo anual de definição de vagas seja um momento real de decisão com participação dos campi.

### 1.4. Explorado e despriorizado

- Reprodução forense da planilha da matriz e o bloco de Funcionamento como porta de entrada.
- Valor de funcionamento em reais por campus.
- Estimar RAP e eficiência acadêmica da matriz pela PNP (não reconciliam).
- "Pacto de degraus" como definição do produto (virou caso de uso).
- Simulação em matrículas de um único ano (v2).
- Programa de permanência com efeito arbitrado como alternativa equivalente às demais.

### 1.5. Ainda a investigar

- Como a definição de vagas acontece de fato no Ifes: quem propõe, quem aprova, quando.
- Se a prática de cálculo de 2026 (matrícula total, 0,5 × IEA) continua em 2027 (memória de cálculo da Setec).
- Definição oficial da matrícula equivalente dos percentuais legais e da RAP (L-25).
- Regra interna de distribuição (piso, teto, Reitoria).
- A causa da queda de concluintes no técnico concomitante e subsequente (exige coortes do sistema acadêmico).
- Qual erro fora da amostra é aceitável por tipo de oferta.
- Interesse de outra instituição.

---

## 2. Principais descobertas deste estudo

1. **Falta ao PRUMO um ritmo, não uma tela.** Todos os documentos descrevem o ciclo "entender → simular → pactuar → acompanhar" como raciocínio. Nenhum o ancora num momento real da vida da instituição. O calendário da PNP e da definição de vagas é esse momento, é comum às 41 instituições e transforma o acompanhamento de promessa em rotina (documento 1, § 1.2).
2. **O produto é um sistema de registro que não existe.** A PNP registra o que aconteceu; ninguém registra o que foi decidido e por quê. Esse é o ativo que cresce com o uso e que dá permanência ao produto entre gestões.
3. **A conferência pode ser demonstrada com dados do passado.** O ciclo inteiro (pactuar, observar, explicar o desvio) pode ser exercitado com uma decisão de 2023 e as edições 2024–2025. Não é preciso esperar dois anos para mostrar o acompanhamento.
4. **O desvio pode ser explicado pelo próprio motor.** Como a projeção é feita por mecanismos separados (vagas, ocupação, evasão, retenção, conclusão), o desvio também pode ser decomposto neles, de forma determinística. Isso diferencia o acompanhamento do PRUMO de qualquer semáforo.
5. **A governança acontece em reunião, e a interface deve servir à reunião.** A primeira versão não precisa de workflow de aprovação; precisa de uma mesa de composição que funcione projetada.
6. **"Começa sabendo" é a vantagem replicável.** A mesma carga pública serve às 41 instituições. É a melhor primeira tela e o melhor argumento para outra instituição, desde que não seja o produto inteiro.

---

## 3. Pontos de discordância e contradições

### 3.1. O caso demonstrativo escolhido enfraquece a tese que deveria demonstrar

O próximo passo usa o percentual técnico como caso demonstrativo da primeira jornada. Os próprios dados mostram que **a alavanca desse indicador está concentrada numa unidade**: sem o Cefor, os campi já somam cerca de 51%. Na POC 0.0.2, nenhuma das 16 combinações de Vitória e Serra passa de +0,41 p.p.; reorientar parte do Cefor move +2,3 p.p. Ou seja, para esse objetivo, o problema real é uma decisão central sobre a oferta a distância, não a coordenação de contribuições de 22 campi.

Isso não invalida o caso: mostrar que "a meta depende de uma decisão de portfólio institucional" é uma descoberta valiosa para a reitoria. Mas usar só ele para demonstrar a governança distribuída corre o risco de concluir, no primeiro uso, que "os campi não fazem diferença".

**Proposta:** usar dois objetivos desde a SPEC-001, o percentual técnico e **concluintes técnicos** (ou outro objetivo de trajetória). No segundo, as alavancas estão realmente distribuídas entre os campi, como o estudo da PNP mostrou. Isso também cumpre de saída o critério "um segundo objetivo cabe sem mudança de estrutura".

### 3.2. Pular a validação com gestores é o maior risco do projeto

A decisão de 10/11 de não fazer sessões com gestores é compreensível: a descoberta já consumiu esforço e era preciso convergir. Mas tudo o que foi validado até aqui é **dado e cálculo**; nada do que é **produto** foi validado. As hipóteses H1 e H6 (o problema de coordenação é reconhecido; a reitoria aceita metas diferenciadas) sustentam a finalidade do produto, e um produto bem construído sobre uma finalidade que os gestores não reconhecem é o pior desfecho possível.

**Proposta:** não reabrir a descoberta. Fazer **três conversas de 30 minutos** antes de fechar a SPEC-001 (pró-reitoria de ensino, planejamento, um diretor de campus), com uma pergunta só: "como a definição de vagas acontece hoje, e o que vocês gostariam de ver antes de decidir?". E colocar o **uso numa reunião real** como critério de aceite do MVP (documento 5, § 2.8).

### 3.3. A inteligência como "espaço de exploração" tende a virar BI

A visão (§ 4.2) e o diagnóstico (§ 4.2, item 1) deixam em aberto a forma da inteligência, inclusive como espaço próprio de exploração. Este estudo propõe fechar a questão: **a leitura sempre parte de um objetivo, de um campus ou de uma oferta**, e o explorador da Rede vem depois (SPEC-003), como lugar de comparáveis e precedentes, não de navegação livre. Essa é a forma mais barata de impedir que a porta de entrada vire o produto.

### 3.4. "Aproveitar melhor" é a alternativa mais atraente e a menos sustentada

Na POC 0.0.2, agir sobre a permanência produz o maior efeito nos dois campi, e o efeito é inteiramente premissa. Um produto de simulação tende a premiar a alternativa com a premissa mais otimista. **Proposta:** o tipo de decisão "agir sobre permanência" existe, mas a alternativa que o usa herda a marca de hipótese, aparece com faixa larga, e a mesa mostra **quanto da composição depende de hipóteses**. É também o argumento mais forte para a primeira integração de dados (coortes do sistema acadêmico), quando ela vier.

### 3.5. O peso da matriz orçamentária na concepção é maior que seu peso na decisão

**[2ª rodada] Revisto.** A primeira versão deste parágrafo concluía que "a matriz é uma das três réguas, e a referência em reais é a SPEC-005, não a primeira". Esta rodada corrige a conclusão, sem mudar o diagnóstico de fundo:

- **Continua valendo:** não retomar a auditoria forense da planilha; não competir com o sistema que Conif e Setec preparam para a matriz oficial; nunca apresentar referência como receita.
- **Muda:** a participação na matriz passa a ser a **estrela-guia** do produto, por orientação do idealizador e porque ela só se move por resultados educacionais ([documento 7, § 1](07-estrela-guia-e-indicadores.md#1-a-estrela-guia)). O mapa de degraus, a MT por parâmetros de oferta e a referência condicional por exercício entram na primeira jornada. O que fica para a SPEC-005 é a reprodução exata e os cenários da Rede.
- **Ressalva mantida:** a estrela-guia é relativa, atrasada, sujeita a mudança de regra e pode ser perseguida pelo caminho errado. Por isso vem com indicadores de guarda e sem otimização automática.

### 3.6. Infraestrutura física: essencial no fundador, sem dados na prática

**[2ª rodada] Revisto.** A primeira versão propunha que, no MVP, o recurso crítico fosse "um campo livre por decisão". Foi um erro de dosagem: um campo livre não é verificável, não é reutilizável entre cenários e não permite comparar a viabilidade de propostas de campi diferentes. A versão corrigida ([documento 8, § 2](08-capacidade-e-projecao.md#2-modelo-mínimo-de-capacidade-por-campus)) é um **modelo mínimo estruturado**: salas por turno, até três ambientes críticos e docentes por área, cadastrados uma vez por campus e verificados contra o uso de 2025. Continua sem inventário patrimonial, sem horário e sem alocação nominal. O nível seguinte (componentes, dia e bloco, custos) fica na SPEC-004.

### 3.7. Contradições menores

| Contradição | Resolução proposta |
|---|---|
| Princípio "uma jornada por vez" × necessidade de carga de dados antes de qualquer jornada | A carga é o incremento I1 da SPEC-001, demonstrável pela leitura dos objetivos |
| "A instituição é parâmetro" × MVP só com o Ifes | Modelo multi-instituição desde o início; nenhum controle de acesso entre instituições no MVP |
| Motor no navegador (protótipos) × reprodutibilidade | Motor no servidor, uma implementação (documento 3, § 2.3) |
| Três motores de coortes divergentes | Um motor novo, especificado pelo comportamento da POC 0.0.2 e testado com os testes da recomposição |

### 3.8. A estrela-guia e os princípios do projeto [2ª rodada]

Adotar a participação na matriz como estrela-guia cria uma tensão com três textos vigentes, que precisa ser resolvida por edição, e não ignorada:

| Texto vigente | O que diz | Como conciliar |
|---|---|---|
| Visão § 1, "O que o PRUMO não é" | Não é calculadora da Matriz CONIF | Continua não sendo: a matriz é o **placar**, não o objeto. O produto calcula decisões acadêmicas e mostra seu efeito no placar |
| Documento fundador § 1 | Não transformar campi em unidades que maximizam receita; valor público acima do orçamento | Indicadores de guarda em toda tela; nenhuma otimização automática; referência nunca como receita do campus |
| Princípio VI | Referência financeira condicional, por componente e exercício | Mantido integralmente: é exatamente como a estrela-guia é exibida |

**Proposta:** acrescentar à visão (§ 1) uma linha de estrela-guia com seus quatro cuidados ([documento 7, § 1.2](07-estrela-guia-e-indicadores.md#12-quatro-cuidados-que-a-estrela-guia-exige)), sem alterar os princípios. Se o idealizador quiser que a participação seja mais que placar (por exemplo, meta institucional formal), isso pede emenda do princípio VI e deve ser decidido explicitamente (D11).

---

## 4. Riscos de produto

| Risco | Sinal de alerta | Proteção no desenho |
|---|---|---|
| **[2ª rodada] Virar calculadora orçamentária** | Pedidos de "quanto o campus ganha"; ordenação de cursos por MT; valores em reais citados como receita | Referência sempre marginal, por exercício e com a Rede declarada; indicadores de guarda ao lado; nenhum ranking por retorno; valor por campus só com regra interna (SPEC-005) |
| **[2ª rodada] Capacidade virar cadastro burocrático** | Campos pedindo inventário de salas, nomes de docentes, horários | Quatro elementos, agregados; cadastro depois do primeiro valor; verificação contra 2025 em vez de cadastro exaustivo |
| **Virar BI sofisticado** | Pedidos de "mais gráficos" e "mais indicadores"; uso só da Agenda | Leitura sempre ancorada; toda tela termina numa ação (guardar evidência, criar alternativa, propor) |
| **Virar sistema burocrático de planejamento** | Formulários de proposta com dez campos; pedidos de alçadas | Proposta gerada da alternativa; pareceres como texto; o PRUMO registra, não conduz |
| **Simulação técnica demais** | Diretor que não passa do quadro de premissas | Abre no quadro comparativo e em texto; premissas um nível abaixo, com valores padrão vindos da evidência |
| **Precisão ilusória** | Números sem faixa citados em ata | Faixa obrigatória onde o erro é relevante; "não estimado" explícito |
| **Incentivo a ganhar métrica** | Alternativas que só sobem matrícula equivalente com FIC curto ou EaD em pulso | Concluintes como segundo objetivo; alerta de oferta em pulso (estudo da PNP, H-P4) |
| **Sensibilidade política da comparação** | Reação de campi à ponte de contribuição | Sem ordenação por desempenho; linguagem de contribuição, não de culpa; teste H5 |
| **Envelhecer em um ciclo** | Ninguém carrega a PNP nova | Papel de curador de dados definido antes do lançamento (H10); carga validada e simples |

---

## 5. O PRUMO é SaaS replicável?

| Camada | Replicabilidade | Por quê |
|---|---|---|
| Dados e leitura | **Alta** | PNP e matriz são as mesmas para as 41 instituições. "Começa sabendo" vale para todas |
| Simulação | **Alta** | Motor calibrado por oferta com dados públicos; premissas são da instituição, mas o modelo é o mesmo |
| Governança | **Média** | Ritos, instâncias, unidades atípicas (como o Cefor) e regra interna variam. O modelo (objetivo, proposta, contribuição, compromisso) é genérico; o rito precisa ser configurável e leve |
| Orçamento | **Média** | Regras nacionais são comuns; a distribuição interna é de cada instituição |

O que depende do Ifes hoje: nomes e exceções fixos no código dos protótipos (já previsto para sair), a unidade de EaD como caso particular e a distribuição interna da PROAD. Nada disso está no núcleo do modelo proposto.

**A dúvida não é técnica, é de mercado.** São 41 compradores públicos, com compra lenta. Três caminhos merecem avaliação antes de investir em infraestrutura de SaaS: (a) adoção via Conif ou Forplan, como ferramenta da Rede; (b) software público ou código aberto, com serviço de implantação e manutenção de dados; (c) acordo de cooperação entre institutos. Cada um muda o modelo de sustentação, não a arquitetura proposta.

**Oportunidades de diferenciação** que nenhuma alternativa atual oferece: o registro de decisões conferido automaticamente pela PNP; a decomposição de desvios; a régua tripla; a composição correta de contribuições; e a manutenção anual dos dados da Rede como serviço, que poupa a cada instituição o trabalho que o estudo da PNP mostrou ser necessário.

**Oportunidades de simplificação:** um motor de coortes, não três; nenhum workflow; nenhuma integração no MVP; nenhum cadastro antes do primeiro valor (o cadastro de capacidade vem depois que o campus já viu seus funis); valor em reais só como referência condicional marginal, sem reprodução da matriz inteira; nenhum modelo de linguagem no MVP.

---

## 6. Decisões estratégicas antes do novo repositório

| # | Decisão | Opções | Recomendação deste estudo |
|---|---|---|---|
| D1 | **Âncora do produto** | Módulos × objetivos e ciclo anual de vagas | Objetivos e ciclo anual, após confirmar o rito (§ 3.2) |
| D2 | **Objetivos da SPEC-001** | Só percentual técnico × técnico + concluintes técnicos × outro par | Técnico + concluintes técnicos (§ 3.1) |
| D3 | **Validação mínima antes de especificar** | Nenhuma × três conversas sobre o rito | Três conversas, sem reabrir a descoberta |
| D4 | **Patrocinador e operador no Ifes** | Prodi, Proen, ambos | Definir quem convoca a pauta e quem opera a mesa; sem isso, não há piloto |
| D5 | **Campi do piloto** | Os quatro com premissas prontas × incluir a unidade de EaD | Incluir a unidade de EaD, que move o principal objetivo |
| D6 | **Stack** | Django + HTMX (recomendado) × FastAPI + React | Django + HTMX + PostgreSQL; motor como pacote puro (documento 3) |
| D7 | **Natureza do repositório e da licença** | Privado × código aberto | Decidir cedo: muda o caminho de adoção pela Rede (§ 5) |
| D8 | **Responsável pelos dados** | Curador no Ifes × equipe do produto | Nomear antes do piloto (H10) |
| D9 | **Critério de aceite do motor** | Erro fora da amostra aceitável por tipo de oferta | Fixar na SPEC-001: proposta inicial ≤ 5% em matrículas de técnicos integrados; faixa obrigatória acima de 10% |
| D10 | **Meta de uso** | Demonstração × uso no ciclo real de vagas de 2028 | Uso no ciclo real |
| D11 | **[2ª rodada, revista na 3ª] Papel da participação na matriz** | Placar × meta institucional formal × meta distribuída por unidade | **Meta institucional, nunca cota por unidade** (orientação do idealizador, 13/11). Abertos: formalização no PDI, com emenda do princípio VI; horizonte e valor (o exemplo de 3,9% no exercício 2030 está fora do alcance mostrado pelo protótipo); quem publica o desafio. Indicadores de guarda continuam |
| D12 | **[2ª rodada] Planilha da matriz como insumo** | Só premissas por oferta × importar a planilha que a instituição recebe | Aceitar importação opcional já na SPEC-001 para parâmetros por oferta; reprodução exata na SPEC-005 |

---

## 7. Recomendação final

### 7.1. Direção do produto

> **Construir o PRUMO como a mesa de decisão do ciclo anual de oferta: começa sabendo sobre a instituição, leva o diretor do funil das suas ofertas a uma proposta fundamentada, compõe as propostas dos campi diante de objetivos com três réguas e registra o que foi pactuado para que a próxima PNP o confira.**

A governança é a finalidade e aparece já no primeiro produto, na mesa de composição usada numa reunião real. A simulação é o instrumento. A leitura da Rede é a primeira tela e a vantagem replicável.

**[2ª rodada]** Formulação revista:

> **O PRUMO é a mesa de decisão do ciclo anual de oferta, guiada pela participação da instituição na matriz: mostra quanto cada degrau vale e quem pode movê-lo, leva cada campus do funil de suas ofertas a alternativas que cabem na sua capacidade, com curvas até dez anos e efeito nos objetivos e na matriz, compõe as propostas numa trajetória institucional e registra o pactuado para que a próxima PNP o confira.**

### 7.2. Como iniciar o repositório definitivo

1. **Antes:** tomar as decisões D1 a D5 e D10; fazer as três conversas; editar a [visão de produto](../../produto/visao-prumo.md) com o que for aceito deste estudo (ciclo anual, dois objetivos, forma da inteligência), e emendar os princípios se necessário. **[13/11]** A visão foi editada com o que é consenso (ver o [README](README.md)). Dois objetivos e forma da inteligência continuam em aberto.
2. **Criar o repositório** com: `prumo_motor/` (pacote puro, com testes), aplicação Django com os módulos do documento 3, `.specify/` com os princípios trazidos deste repositório, e um diretório de dados de referência públicos (percentuais legais 2024, faixas 2026, casos de teste dos motores).
3. **Trazer deste repositório:** princípios, visão, valores de referência e casos de teste; o comportamento dos motores como especificação. **Não trazer:** código dos protótipos, a fonte canônica inteira (fica aqui como dossiê, citada por RMO), dados não públicos.
4. **Especificar a SPEC-001** com `/speckit-specify`, usando o documento 5 como insumo e o § 3.5 do próximo passo para a etapa de esclarecimento.
5. **Construir em três incrementos** (I1 começa sabendo, I2 bancada, I3 mesa), cada um mostrado a um usuário real antes do seguinte.
6. **Manter este repositório** como laboratório de estudos e evidências, como prevê a convenção.
