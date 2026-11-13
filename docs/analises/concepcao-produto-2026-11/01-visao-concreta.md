# 1 · Visão concreta do PRUMO

> **Estudo de concepção de 12/11/2026, revisado na segunda rodada no mesmo dia.** Proposta para discussão.
> **Segunda rodada:** acrescentado o § 1.3 (estrela-guia). O restante continua válido; capacidade e projeção estão nos documentos [7](07-estrela-guia-e-indicadores.md) e [8](08-capacidade-e-projecao.md). Não altera a [visão de produto](../../produto/visao-prumo.md), que continua a referência canônica. Se as propostas daqui forem aceitas, entram na visão por edição, como manda a convenção do repositório.
> **De onde parte:** o estado do conhecimento (o que foi validado, decidido, explorado e o que segue hipótese) está no [documento 6, § 1](06-avaliacao-critica.md#1-o-que-sabemos-de-fato).

---

## 1. O PRUMO em uma frase

> **O PRUMO é o lugar onde a instituição decide sua oferta junto com os campi, e onde confere, quando os dados oficiais chegam, se o que foi decidido aconteceu.**

Não é um painel que mostra a instituição. É uma **mesa de decisão** que já chega sabendo sobre a instituição.

### 1.1. Identidade principal

Das categorias possíveis (planejamento estratégico, simulação, inteligência para decisão, governança e pactuação), o PRUMO é uma combinação com um centro definido:

| Categoria | Papel no PRUMO |
|---|---|
| Plataforma de governança e pactuação | **O centro.** O objeto que o produto produz e guarda é o *compromisso conferível*: quem se comprometeu com o quê, por quê, com quais premissas |
| Inteligência para tomada de decisão | O que torna o compromisso fundamentado. Sempre ancorada num objetivo ou numa oferta, nunca solta |
| Ambiente de simulação | O instrumento que transforma uma ideia ("abrir mais 40 vagas") em consequências no tempo |
| Planejamento estratégico | O contexto, não o produto. O PRUMO não substitui o PDI, ajuda a cumpri-lo |

O nome mais honesto para a categoria é **sistema de registro das decisões estratégicas de oferta**: um *system of record* que hoje não existe. A PNP registra o que aconteceu. Os sistemas acadêmicos registram a operação. Ninguém registra **o que a instituição decidiu, por que decidiu e o que esperava que acontecesse.**

### 1.2. A ideia organizadora: o ciclo anual da oferta

Todas as 41 instituições da Matriz CONIF vivem o mesmo calendário, imposto de fora:

```
  a PNP publica o ano-base  →  a instituição define as vagas do próximo processo seletivo
          ↑                                              ↓
  a matriz usa aquele ano-base       os campi executam; as turmas entram, evadem, concluem
  dois exercícios depois                                 ↓
          └──────────── a próxima PNP mostra o que aconteceu ───────┘
```

Esse ciclo **já existe** e já produz decisões todos os anos: quantas vagas, em quais cursos, em qual turno, em qual campus. O que falta é que ele seja **pensado em conjunto, registrado e conferido**.

A proposta deste estudo é que o PRUMO se organize em torno desse ritmo, e não em torno de módulos. **[HIPÓTESE]** que o ciclo de definição de vagas seja, no Ifes e nas demais instituições, um momento real de decisão com participação dos campi e aprovação colegiada. É a primeira coisa a confirmar (documento 6, §§ 3.2 e 6).

Consequências práticas:

- **O produto tem uma estação.** Há o momento de ler o ano (PNP nova), o de propor (planejamento de vagas), o de pactuar (colegiado) e o de conferir (PNP seguinte). A interface sabe em que momento a instituição está.
- **Não se cria rito novo.** O PRUMO ocupa um processo que já existe e que hoje corre em planilhas, ofícios e reuniões sem memória.
- **O aprendizado é automático.** Quando a edição seguinte da PNP é carregada, todo compromisso cujo horizonte já pode ser observado é conferido sem que ninguém precise lembrar dele.
- **É replicável.** O calendário e os dados são os mesmos para as 41 instituições.

### 1.3. A estrela-guia [2ª rodada]

> **A participação da instituição na matriz orçamentária é a estrela-guia do PRUMO.**

É o placar que todas as decisões acabam movendo, e é comum às 41 instituições. Para o Ifes, ≈ 3,32% do remanescente de 2026. Ela organiza a Agenda e a Mesa: cada alternativa mostra quanto move a participação, por qual bloco (Funcionamento + Reitoria, que seguem a matrícula total ponderada, ou Qualidade, que segue degraus institucionais) e em qual exercício.

Ela só se move por resultados educacionais: estudantes ativos por mais tempo e presencialmente, concluintes, percentuais legais. Por isso a estrela-guia e a missão apontam na mesma direção na maior parte do caminho, e o PRUMO mostra, ao lado dela, os indicadores de guarda que impedem persegui-la pelo atalho (FIC curto, MOOC, retenção, contenção de docentes). Detalhes, cuidados e mapa de degraus: [documento 7](07-estrela-guia-e-indicadores.md).

---

## 2. O problema que faz um dirigente querer usá-lo

### 2.1. O problema estrutural

As metas de uma instituição multicampi só existem no agregado: percentuais legais, participação na matriz, conclusão, relação aluno-professor. As alavancas estão nos campi, que decidem sua oferta com conhecimento local e quase sem ver o agregado. Isso já está na visão (§ 1) e foi confirmado pelos estudos.

### 2.2. Como o problema aparece na vida do gestor

| Quem | Situação concreta | O que falta hoje |
|---|---|---|
| **Reitor(a)** | No Colégio de Dirigentes, discute-se "precisamos chegar a 50% de técnico". Cada diretor diz que seu campus já faz o possível | Ver quem pode contribuir com quanto, e o que cada contribuição custa |
| **Reitor(a) e pró-reitoria de administração** [2ª rodada] | A participação do instituto na matriz caiu, mesmo com crescimento | Saber o que foi decisão própria e o que foi a Rede; quais degraus estão ao alcance e quanto valem |
| **Pró-reitoria de planejamento ou desenvolvimento institucional** | Precisa propor as metas do PDI por campus | Fundamento para metas diferentes que não pareçam arbitrárias |
| **Pró-reitoria de ensino** | Recebe pedidos de abertura de turmas e de cursos | Saber o que cada pedido faz com os indicadores e com a capacidade, antes de aprovar |
| **Diretor(a)-geral de campus** | Quer abrir uma turma nova ou reformular um curso que perde estudantes | Argumento para levar à reitoria e clareza sobre o que o campus pode oferecer em troca |
| **Todos** | Dois anos depois, o resultado não veio. Ninguém lembra quem decidiu o quê nem com quais premissas. A gestão mudou | Memória da decisão e explicação do desvio |

O gancho de uso não é "ver indicadores". É **chegar à reunião em que a decisão será tomada com uma proposta defensável**, e sair dela com um compromisso registrado.

### 2.3. Por que ele é diferente do que já existe

| Alternativa | O que entrega | Onde o PRUMO é diferente |
|---|---|---|
| PNP e painéis em BI | Indicadores oficiais por instituição e campus | O PRUMO **decompõe** (de onde veio a mudança), liga a observação a uma alternativa e a um compromisso, e **reutiliza a PNP seguinte para conferir** |
| Planilhas de planejamento e de matriz | Cálculo pontual feito por quem domina a regra | Premissas visíveis e com origem, composição correta entre campi (razão das somas), reprodutível por terceiros |
| Sistemas de PDI e de metas | Cadastro de metas e semáforos de acompanhamento | O PRUMO diz **de onde vem a meta e se ela cabe no campus**; o acompanhamento **explica o desvio**, não só o aponta |
| Sistemas acadêmicos | Operação | O PRUMO não opera nada; trabalha com agregados por oferta e por campus |

Três diferenças resumem as demais:

1. **Começa sabendo.** Para qualquer uma das 41 instituições, o PRUMO abre com a posição em cada objetivo, a trajetória e a decomposição por campus, sem que a instituição cadastre nada. O valor aparece antes do primeiro formulário.
2. **Toda decisão vira um compromisso conferível.** A proposta guarda as premissas; a PNP seguinte as testa. O desvio é explicado pelos mesmos mecanismos da projeção (vagas ofertadas, ocupação, evasão, retenção, conclusão).
3. **Todo número diz o que é.** Fato, estimado, premissa, hipótese ou não estimado, com fonte e regra. Em decisão pública, isso é o que torna o número defensável.

---

## 3. Para quem

### 3.1. Usuários e o que fazem no produto

| Papel | Pergunta que traz | O que produz no PRUMO | Frequência **[HIPÓTESE]** |
|---|---|---|---|
| **Equipe de planejamento** (Prodi ou equivalente) | "Onde estamos e o que é possível?" | Leitura do objetivo, mesa de composição, pacto | Intensiva no ciclo; mensal fora dele |
| **Pró-reitoria de ensino** | "Esses pedidos de oferta fazem sentido juntos?" | Pareceres sobre propostas | No ciclo de vagas |
| **Direção-geral e de ensino do campus** | "Qual é o melhor caminho viável para o meu campus?" | Alternativas e proposta do campus | Poucas sessões longas por ano |
| **Reitor(a) e Colégio de Dirigentes** | "O que conseguimos alcançar juntos?" | Decisão; leem, não editam | Nas reuniões de pactuação |
| **Orçamento** | "O cálculo é confiável?" | Conferência de regras e premissas | Pontual |
| **Curador de dados** (função, não cargo) | "Os dados do ano entraram certos?" | Carga anual, correspondência de unidades, regras do exercício | Uma vez por ano |

**Usuário-âncora da primeira versão:** a equipe de planejamento institucional. É quem prepara o material da reunião, quem tem mandato para pedir propostas aos campi e quem sofre com a planilha hoje. A direção de campus é o segundo usuário. O Colégio de Dirigentes é a **plateia**: precisa entender a tela projetada, não operá-la.

### 3.2. Quem paga e por quê

Quem usa todo dia (planejamento, diretor de campus) não é quem contrata. O patrocinador compra **uma estratégia institucional defensável e uma memória que sobrevive à troca de gestão**. O argumento de compra não é "mais indicadores", é "a próxima pactuação de metas será feita com fundamento e conferida automaticamente". O modelo de contratação continua em aberto (documento 6, § 5).

---

## 4. Proposta de valor

**Para a reitoria:** metas diferenciadas por campus com fundamento público, conflitos entre objetivos visíveis antes de decidir e acompanhamento que explica o que aconteceu.

**Para o campus:** um caminho para propor o que o campus pode fazer, com o argumento pronto e com o que precisa em troca, em vez de receber uma meta igual à dos outros.

**Para a instituição:** uma decisão registrada com suas premissas, que pode ser conferida, revista e herdada pela próxima gestão.

**Para os estudantes e o território:** ofertas decididas olhando conclusão, e não só vagas. O estudo da PNP mostrou que no técnico do Ifes as vagas se preenchem e a perda acontece depois do ingresso. Um produto que decide em vagas e mostra concluintes muda a conversa.

---

## 5. Um ano com o PRUMO (narrativa)

> Exemplo ilustrativo. Os números de março e maio vêm dos estudos do repositório (portão de dados, estudo da PNP, POC 0.0.2). Os de junho e do ano seguinte (46,2%, evasão −12%) são inventados para a narrativa.

**Março.** A nova edição da PNP é carregada. Na abertura do PRUMO, a equipe de planejamento vê "O que mudou neste ano-base": o percentual técnico do Ifes subiu de 44,0% para 45,1%; sem a unidade de educação a distância, os campi somam mais de 50%. A formação de professores salta de 12% para 24,8%, e o PRUMO sinaliza **provável reclassificação**, não melhora. Três compromissos do ciclo anterior chegaram ao horizonte de resultados intermediários e são conferidos: dois dentro da faixa, um abaixo.

**Abril.** A pró-reitoria abre a pauta "Plano de oferta 2028" com dois objetivos: aproximar a formação técnica de 50% e recuperar concluintes no técnico concomitante e subsequente. Para cada objetivo, o PRUMO mostra a posição nas três réguas (meta legal, limiar da matriz, meta pactuada) e a contribuição de cada campus para a mudança dos últimos anos.

**Maio.** A diretora de ensino de Serra abre a ficha do campus. Vê que a procura pelo Informática concomitante caiu de 312 para 90 inscritos, enquanto o integrado do mesmo eixo tem 1.765 inscritos para 74 vagas. Monta três alternativas na bancada. A de reorganizar para o integrado entrega quatro vezes mais concluintes por ano em regime, com metade dos docentes adicionais, mas só aparece nos dados em 2031. Ela encaminha essa alternativa como proposta, com o que precisa (2 docentes de núcleo comum) e o que oferece (+20 concluintes técnicos por ano em regime).

**Junho.** Na reunião do Colégio de Dirigentes, a mesa de composição é projetada. Com as propostas de cinco campi, o Ifes chega a 46,2% em 2030. Falta. A mesa mostra que a única alavanca capaz de fechar a distância é a oferta da unidade de educação a distância, e que mexer nela derruba a formação de professores. A discussão muda de "cada campus precisa fazer mais" para "vamos decidir o que fazer com a oferta a distância". O colegiado pactua as propostas dos campi e abre uma pauta própria para a educação a distância.

**Março do ano seguinte.** A PNP nova chega. O compromisso de Vitória (reduzir a evasão no concomitante) é conferido no horizonte intermediário: a evasão caiu 12%, não 30%. O PRUMO reprojeta o cenário trocando cada premissa pelo valor observado e mostra que o desvio vem quase todo da evasão; as vagas foram ofertadas e preenchidas. A premissa é revista, e o pacto também.

Essa narrativa contém as cinco situações pedidas (reitoria, campus, simulação, pactuação, revisão). O passo a passo de cada uma, com telas, está no [documento 2, § 5](02-experiencia-e-interfaces.md#5-jornadas).

---

## 6. Princípios de produto

Complementam, sem substituir, os [princípios do projeto](../../../.specify/memory/constitution.md). Estes são de experiência.

1. **Começa sabendo.** Nenhuma tela inicial vazia. Dados públicos primeiro, cadastro só quando ele destrava uma decisão.
2. **Decide-se em vagas, vê-se em concluintes.** A alavanca é a vaga; o resultado que importa é a trajetória das turmas.
3. **Contribuição, não meta igual.** Toda meta institucional se desdobra em contribuições diferentes, e a soma é feita do jeito certo.
4. **Todo número diz o que é e de onde veio.** Um clique em qualquer número abre como ele foi calculado.
5. **Pronto para a reunião.** As decisões acontecem em colegiado. As telas centrais funcionam projetadas, com a plateia lendo.
6. **Compara, não recomenda.** O PRUMO mostra o que cada alternativa exige e entrega. Quem escolhe é a instância competente.
7. **Fecha o ciclo.** Todo compromisso tem um indicador que a próxima PNP vai conferir.

---

## 7. O que o PRUMO não é

Vale integralmente a lista da [visão, § 1](../../produto/visao-prumo.md#1-o-prumo-em-uma-página). Este estudo acrescenta três:

- **Não é um sistema de workflow de aprovação.** Registra a decisão tomada pela instância competente; não a conduz por alçadas.
- **Não é um explorador de dados genérico.** A inteligência sempre parte de um objetivo, de um campus ou de uma oferta.
- **Não é um sistema de PDI.** Pode receber objetivos do PDI e devolver contribuições pactuadas, mas não gerencia o plano inteiro.
