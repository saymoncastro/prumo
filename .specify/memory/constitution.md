# Princípios do projeto PRUMO

Este documento reúne as regras que toda especificação, plano e tarefa do PRUMO deve respeitar.
Ele não acrescenta concepção: cada princípio deriva da
[visão de produto](../../docs/produto/visao-prumo.md), e a seção de origem está indicada em cada um.
Se este documento e a visão divergirem, vale a visão, e este documento é corrigido.

## Princípios centrais

### I. Uma proposta de valor, três capacidades conectadas

O PRUMO transforma evidências em decisões institucionais melhores, coordenadas e mensuráveis.
Faz isso com três capacidades: inteligência histórica, simulação estratégica e governança distribuída.

- Toda especificação DEVE dizer a quais capacidades serve e como se liga às outras.
- Nenhuma capacidade DEVE ser especificada como produto à parte: nem painel de indicadores,
  nem calculadora de campus, nem sistema de metas.
- A governança distribuída é a finalidade. A solução DEVE ser estruturada a partir dela,
  e não a partir do simulador.
- Não há ordem obrigatória entre as capacidades. O que o gestor leva de uma para outra
  (evidência, premissa, cenário, proposta) DEVE manter contexto e origem.

**Por quê:** cada protótipo anterior promoveu um achado a pergunta organizadora do produto,
e a concepção se fragmentou. **Origem:** visão §§ 1, 4.1 e 5.

### II. Todo número carrega natureza e origem

- Todo número exibido ou armazenado DEVE indicar sua natureza: fato observado, estimado,
  premissa, hipótese, resultado simulado ou não estimado.
- Todo número DEVE indicar fonte, ano-base, versão da regra e fórmula, de modo que um terceiro
  consiga reproduzi-lo.
- O que não pode ser estimado DEVE aparecer como "não estimado". NÃO DEVE ser omitido
  nem aproximado em silêncio.

**Origem:** visão § 7.2, regras 1 e 9; § 8.

### III. Fato, hipótese, projeção e decisão ficam em estruturas separadas

- Série observada, evidência, hipótese, premissa, resultado simulado, proposta, compromisso
  e resultado observado DEVEM ser objetos distintos no modelo.
- A natureza de uma informação NÃO DEVE se perder quando ela passa de uma capacidade a outra.
- Uma proposta NÃO DEVE ser tratada como oferta aprovada. Matrícula projetada NÃO DEVE
  ser tratada como matrícula oficial.

**Origem:** visão § 7.2, regra 2; § 5.

### IV. Regras versionadas por exercício, medidas que não se substituem

- Fórmulas e parâmetros normativos DEVEM ser versionados por exercício orçamentário.
- Texto normativo e prática de cálculo, quando divergem, DEVEM ser registrados separadamente.
- Matrícula física, matrícula equivalente da PNP e matrícula total da matriz DEVEM ser medidas
  distintas. Nenhuma DEVE ser usada no lugar de outra.
- Todo cálculo no tempo DEVE distinguir três marcos: ano da decisão, ano-base em que o efeito
  aparece nos dados e exercício orçamentário que usa esses dados.

**Origem:** visão § 7.2, regras 3 e 4; § 4.3.

### V. Agregação pela razão das somas, série só em bloco comparável

- Indicadores institucionais são razões. DEVEM ser agregados somando numeradores e denominadores.
  Média de percentuais NÃO DEVE ser usada.
- Uma série histórica só DEVE ser apresentada como série dentro de um bloco metodológico
  comparável.
- Quebras conhecidas (mudança de fórmula, pandemia, reclassificação) DEVEM ser metadado da série,
  disponível ao cálculo e à interface.

**Origem:** visão § 7.2, regras 5 e 6.

### VI. Comparação sem ranking, associação sem causa, referência financeira condicional

- O produto NÃO DEVE ordenar instituições, campi ou cursos por desempenho ou retorno.
- Comparáveis DEVEM ser escolhidos por perfil e trajetória, com o critério declarado.
- O produto pode afirmar que algo mudou e que duas coisas andam juntas. NÃO DEVE afirmar causa
  nem atribuir intenção a quem decidiu.
- Referência financeira DEVE aparecer por componente e por exercício, com as demais instituições
  mantidas constantes. NÃO DEVE ser apresentada como receita do campus.

**Origem:** visão § 7.2, regras 7 e 8; § 5, limite epistemológico.

### VII. Simulação honesta

- A decisão simulada DEVE ser sobre vagas e ofertas. Matrícula é consequência de ingresso
  e trajetória.
- A linha de base DEVE conter as decisões já em curso: manter também muda.
- Resultado simulado DEVE ser apresentado como projeção condicionada a premissas. Onde o modelo
  erra mais ao reproduzir o passado, o resultado DEVE aparecer em faixa.
- Um modelo de projeção só DEVE ser aceito com erro medido em anos que ficaram fora do ajuste.
  Erro medido nos mesmos anos do ajuste NÃO DEVE ser apresentado como capacidade preditiva.
- Só DEVE ser detalhado o recurso que limita a decisão. Inventário completo NÃO DEVE ser
  pré-requisito para simular.
- O produto NÃO DEVE recomendar automaticamente uma alternativa.

**Origem:** visão § 4.3.

### VIII. Governança é composição, pactuação, acompanhamento e revisão

- Salvar cenários NÃO DEVE ser tratado como governança.
- Um objetivo institucional DEVE admitir réguas separadas: meta legal, limiar orçamentário
  e meta pactuada.
- O modelo DEVE admitir contribuições diferentes por campus. Dividir a mesma meta percentual
  entre todos NÃO DEVE ser o comportamento padrão.
- A composição institucional DEVE mostrar conflitos entre objetivos.
- O acompanhamento DEVE distinguir três horizontes: execução, resultados intermediários
  e resultados de longo prazo. Um compromisso só DEVE ser avaliado no horizonte que já pôde
  ser observado.
- O PRUMO registra propostas e decisões. NÃO DEVE automatizar a autoridade das instâncias
  que decidem.

**Origem:** visão § 4.4.

### IX. Instituição como parâmetro, dado público separado de dado privado

- Instituição, unidades e exceções DEVEM ser dados ou configuração. NÃO DEVEM estar fixos
  no código.
- Dado público compartilhado e dado de uma instituição DEVEM ficar separados por construção.
  Cenário, premissa, proposta ou compromisso de uma instituição NÃO DEVE ser visível a outra.
- Regra interna de distribuição DEVE ser configuração da instituição, com versão e fonte.
- Unidades DEVEM ter identidade estável própria, independente do nome usado na fonte pública.
- Os papéis institucional e local DEVEM existir no modelo, mesmo sem controle de acesso
  implementado.
- O núcleo DEVE funcionar com dados agregados por oferta e por campus, sem dados pessoais.

**Origem:** visão § 8; § 7.2, regra 10.

### X. Números calculados, não gerados

- Todo número DEVE ser produzido por consulta estruturada, decomposição aritmética, estatística
  descritiva ou modelo explícito, de forma determinística e reproduzível.
- Modelo de linguagem NÃO DEVE produzir números nem fazer parte do núcleo de cálculo.

**Origem:** visão §§ 4.2 e 9.

## Restrições de escopo e de dados

- **Fora de escopo até a visão dizer o contrário:** infraestrutura multi-instituição,
  autenticação e perfis de acesso; fluxo formal de aprovação; integração com sistemas acadêmicos,
  de pessoal ou de patrimônio; inventário completo de salas, laboratórios e docentes; grade horária;
  reprodução integral da matriz; valor em reais do bloco de funcionamento por campus; otimização
  automática de portfólio (visão § 9).
- **Só dados públicos entram no Git.** A exportação da PNP, a planilha da matriz do Ifes, o livro
  da matriz e os arquivos derivados deles ficam fora do repositório.
- **Os protótipos em `poc/` são referência de comportamento e de experiência.** O código deles
  NÃO DEVE ser base da implementação. `poc/`, `tests/` e `docs/dominio/evidencias/` NÃO DEVEM
  ser movidos nem alterados por especificações do produto.
- **Nenhuma tecnologia está definida.** A escolha é feita no plano da primeira especificação
  e DEVE ser a mais simples que respeite os princípios II, III e IX.

## Fluxo de trabalho

- A [visão de produto](../../docs/produto/visao-prumo.md) é a referência de todas
  as especificações. Mudança de concepção se faz editando a visão antes da especificação.
- Especifica-se uma jornada por vez. Nova especificação só começa depois de a anterior
  estar navegável.
- Uma especificação parte da finalidade do produto. NÃO DEVE ser organizada em torno
  de um protótipo anterior nem de uma pergunta específica da série histórica.
- Um caso demonstrativo NÃO DEVE limitar a solução. Quando uma especificação usa um objetivo
  como exemplo, um segundo objetivo DEVE caber sem mudança de estrutura.
- Regras de domínio DEVEM citar a regra correspondente da
  [fonte canônica da matriz](../../docs/dominio/matriz-orcamentaria.md) quando ela existir.
- Cálculos DEVEM ter teste automatizado contra valores de referência documentados.

## Governança

- Estes princípios prevalecem sobre especificações, planos e tarefas. Todo plano DEVE conferir
  a conformidade com cada princípio antes de detalhar a implementação, e justificar por escrito
  qualquer exceção.
- **Emenda:** altera-se primeiro a visão de produto, se a mudança for de concepção; depois este
  documento, em pull request próprio, aprovado pelo idealizador.
- **Versão:** MAJOR quando um princípio é removido ou redefinido; MINOR quando um princípio
  ou seção é acrescentado ou ampliado; PATCH para ajustes de redação.
- A cada emenda, as especificações em andamento DEVEM ser conferidas contra a nova versão.

**Versão**: 1.0.0 | **Ratificado**: 2026-11-11 | **Última emenda**: 2026-11-11
