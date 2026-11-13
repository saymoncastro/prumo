# 10 · Terceira rodada: a mesa nos dois sentidos

> **13/11/2026.** Revisão dirigida do protótipo, pedida pelo idealizador depois de relatar uma reunião com 30 a 40 decisões sobre cursos, cada uma analisada isoladamente. A direção estava aprovada. O pedido foi fazer a mesma mesa funcionar nos dois sentidos: da Reitoria para os campi e dos campi e cursos para a Reitoria.
> **Pergunta que o protótipo precisava responder:** *"Se aprovarmos esta combinação de decisões, como muda a trajetória do Ifes nos próximos quatro anos, o que ainda falta para a meta e de que recursos isso depende?"*
> **O que mudou:** o [protótipo v3](prototipo/prumo-conceito.html), um modelo novo de pauta ([`pauta.js`](prototipo/pauta.js)), as operações por curso em [`simulacao.js`](prototipo/simulacao.js) e as [verificações](prototipo/testar_prototipo.cjs). Nos documentos 2, 4, 5, 6 e 7, os trechos revistos têm a marca "[3ª rodada]". A [v2](prototipo/prumo-conceito-v2.html) foi preservada.
> **O que não foi feito:** não há módulo de OKR, fluxo formal de aprovação nem motor orçamentário de produção. Também não foi criada nenhuma especificação nova.

---

## 1. A orientação faz sentido?

Faz sentido, e o estudo segue a orientação sem reabrir a direção. Ela confirma três escolhas que já estavam desenhadas:

- **Governança distribuída.** A Reitoria define prioridades, os campi propõem contribuições diferentes, e o colegiado compõe e pactua (visão, § 1; documento 1).
- **Estrela-guia como placar.** A ressalva do idealizador de que 3,9% "não deve virar a meta de cada campus ou curso" coincide com a qualificação da segunda rodada: a participação é relativa à Rede e chega com dois anos de atraso ([documento 7, § 1.2](07-estrela-guia-e-indicadores.md#12-quatro-cuidados-que-a-estrela-guia-exige)).
- **Evidência, não ranking.** O ganho orçamentário entra como uma evidência ao lado da demanda, da capacidade e da missão da oferta. Isso é o princípio VIII aplicado à alocação de docentes e de obras.

Faltava o que o relato da reunião deixa evidente:

- **A unidade de trabalho da mesa era o campus inteiro.** Por isso não dava para ver uma pausa, uma expansão e uma disputa por código docente como itens separados que interagem.
- **O caminho de cima para baixo não existia.** A Reitoria não tinha onde registrar um desafio, ver a distância até ele e convidar alguém a propor.
- **O curso não tinha lugar.** O coordenador, que é quem consegue mexer na evasão do 1º ano, só aparecia como linha de um funil.

Duas qualificações, ambas demonstradas no protótipo:

1. **O exemplo de 3,4% → 3,9% em quatro anos usa outro ponto de partida.** O último dado observado é ≈ 3,32% (exercício 2026). O protótipo parte dele e mantém a meta de 3,9% como exemplo fictício e editável, para não misturar um número inventado com o observado.
2. **"Quatro anos" na matriz não são quatro anos letivos.** O exercício 2030 lê o ano letivo de 2028. Assim, uma meta para o exercício 2030 recebe só o primeiro ano das decisões do ciclo de oferta 2028. O protótipo mostra isso em todas as telas em que aparece o horizonte.

## 2. O que já existia e foi reaproveitado

| Já existia | Como foi reaproveitado |
|---|---|
| Estrela-guia, mapa de degraus e taxa de câmbio | Viraram a base do desafio: partida, distância, peças que fecham a distância |
| Motor de coortes da POC 0.0.2 e alavancas da bancada | As alavancas viraram uma lista de operações. A pauta e o curso usam a mesma lista. Os resultados da v2 se repetem exatamente (31 casos comparados) |
| Capacidade mínima por campus | Ganhou acréscimos com data (bloco pronto em 2030, código docente em 2028), sem virar inventário |
| Mesa com trajetória institucional | Continua. Agora compõe itens em vez de campus inteiro, e a trajetória da participação entrou como primeira aba |
| Gaveta "Como calcula" | Mostra a cadeia completa de cada item, em quatro passos |
| Linha separada para unidades ilustrativas | Mantida em todas as tabelas e gráficos novos |
| Pacto e conferência (fictícios) | Mantidos como "resultado observado" do ciclo anterior; o pacto novo aparece acima |

## 3. O que mudou no protótipo

| Tela | Mudança |
|---|---|
| **Início** | Linha do desafio sob a estrela-guia. Roteiro da demonstração com os dois caminhos. Pauta resumida por unidade e por situação |
| **Objetivos** | **Desafio da Reitoria:** partida observada, meta, horizonte em exercício (com o ano letivo que ele lê), cenário de referência da Rede e hipótese de formação de professores. Três trajetórias separadas: observado, sem novas decisões e pauta atual. **Partir da meta:** peças que fecham a distância, com valor e primeiro exercício possível. **Hipótese macro:** permanência, ocupação e ampliação aplicadas ao Ifes inteiro por extrapolação declarada, mais a lista de ofertas onde a hipótese tem base nos dados, com o botão "convidar o curso". A árvore de alavancas e a taxa de câmbio continuam abaixo |
| **Campus** | Faixa do desafio, sem cota, com os convites recebidos. Novo card "Cursos": cada oferta com o motivo que a faz aparecer, o convite da Reitoria e a situação da contribuição |
| **Curso** (nova, dentro de Campi) | Visão da coordenação. O objetivo institucional relacionado vem com a frase explícita de que o curso não recebe parte da meta. A situação do curso usa a PNP; a evasão no 1º ano aparece como dado do sistema acadêmico. A contribuição local tem quatro tipos de ação. O compromisso acompanhável é algo que o curso consegue mover (não a participação). Efeito estimado por ano; viabilidade avaliada pelo campus; "levar à mesa" |
| **Bancada** | Sem mudança visível. "Encaminhar" agora cria um item na pauta |
| **Mesa** | **Faixa do desafio:** distância, quanto a pauta fecha e quando os efeitos chegam. **Pauta de decisões:** uma linha por decisão, agrupada por unidade, com filtros, situação, origem, barras de quando o efeito aparece, sinais de conflito e de restrição; o detalhe abre na própria linha. **Os próximos quatro anos:** tabela com sem novas decisões, item selecionado, conjunto (com faixa), ilustrativas à parte e falta para o desafio. **Trajetória:** participação, formação técnica, formação de professores, concluintes e docentes. **O que ainda falta e de que depende.** **Por unidade.** Registrar o pactuado |
| **Pacto** | Novo bloco "O que foi pactuado e o que será acompanhado": indicador, responsável, primeira conferência, efeito projetado na data do pacto, ressalvas e o que aguarda decisão. O compromisso de 2027 continua abaixo como resultado observado |

**Três situações com marcas diferentes em todas as telas:** hipótese simulada (contorno tracejado), proposta do campus (contorno contínuo) e contribuição pactuada (preenchida). O resultado observado (escuro) só aparece no pacto do ciclo anterior.

## 4. O mesmo caso pelos dois caminhos

O caso é a permanência no 1º ano de **Metalurgia concomitante, em Vitória**: evasão anual de 39% e 282 matrículas em 2025.

- **Pela Reitoria:**
  1. Em Objetivos, registrar o desafio e explorar a hipótese macro de permanência.
  2. Em "onde a hipótese tem base", convidar Metalurgia concomitante. Entra na pauta como hipótese simulada, com origem Reitoria.
  3. No campus, o curso aparece com o convite. A coordenação abre o curso, ajusta a ação, o campus confirma a viabilidade e leva à mesa.
  4. O item passa a proposta do campus, com origem "Reitoria → curso".
- **Pelo curso:** Campi → Vitória → Cursos → Metalurgia concomitante → propor → levar à mesa.
- **Onde os dois caminhos se encontram:** o item tem o mesmo identificador e as mesmas operações, e por isso chega à mesma comparação institucional. Uma verificação automática garante isso.

**O que a mesa mostra para esse item** (redução de 25% na evasão, hipótese):

| | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|
| Matrículas | 0 | +15 | +20 | +20 |
| Concluintes | +5 | +11 | +14 | +14 |

- **Na matriz:** ≈ +R$ 19 mil por exercício na parcela simulada a partir de 2033; **nada no exercício 2030**.
- **O que o curso acompanha:** a evasão no 1º ano, não a participação.

## 5. O que o protótipo mostra

Os números abaixo são do estado inicial da demonstração. A capacidade, o código docente, o bloco e as unidades fora de Vitória e Serra são ilustrativos.

1. **A meta de exemplo é grande para o horizonte.**
   - Ir de 3,32% para 3,90% no exercício 2030 pede ≈ +0,58 p.p.: ≈ R$ 12,8 mi ou ≈ 9.700 MT a mais, cerca de 19% da MT do Ifes.
   - Todos os degraus de Qualidade juntos valem ≈ R$ 7,7 mi por exercício.
   - A pauta de demonstração, com 8 itens no conjunto, fecha ≈ 0,5% da distância nas unidades calculadas e ≈ 0,9% com as ilustrativas.
   - Mesmo a hipótese macro mais forte do protótipo (evasão −40%, ocupação até 95% e +20% de vagas onde há procura, extrapoladas para o Ifes inteiro) chega a ≈ 3,41% em 2030 e ≈ 3,68% em 2033.
   - **O que isso significa para o colegiado:** a meta pode ficar como direção, ser recalibrada ou ter o horizonte alongado. Essa escolha é do colegiado; o PRUMO dá a evidência.
2. **Quem mexe no curto prazo é a permanência; quem mexe depois é a oferta.**
   - Com o atraso de dois anos, o exercício 2030 recebe só o primeiro ano das decisões de 2028.
   - **Pausa de Edificações subsequente:** −68 matrículas em 2028 e −133 a partir de 2030; concluintes −10 em 2029 e −23 a partir de 2030; ≈ −R$ 170 mil a partir do exercício 2033. Libera ≈ 5,7 professores-equivalentes, mas numa área diferente da que as expansões pedem.
3. **O código docente em disputa não resolve sozinho nenhum dos dois pedidos.**
   - **Vitória (reorganização de Eletrotécnica):** com o código, a restrição de docentes do núcleo comum passa de 2030 para 2031. O item pede 0,7 → 4,3 professores-equivalentes de 2028 a 2031.
   - **Serra (turma nova de Informática para Internet integrado):** com o código, a restrição de docentes de Informática passa de 2028 para 2029. O item pede 2,1 → 6,4 professores-equivalentes.
   - **O que a mesa mostra:** que um código é um docente, e que decisões de oferta de hoje contratam necessidade de docentes nos anos seguintes. Não escolhe o destino.
4. **O bloco de oficinas não aumenta o atendimento nos quatro anos do plano.**
   - **Sem obra, no turno da procura (noturno):** as oficinas passam de 100% em 2029.
   - **Turma à tarde:** cabe, com ocupação menor (premissa de 70%).
   - **Com o bloco pronto em 2030:** a turma só entra em 2030. Comparado a abrir à tarde, o bloco dá −25, −46 e −23 matrículas de 2028 a 2030, +7 em 2031 e +26 em 2033.
   - **O que isso significa:** o valor do bloco está depois do horizonte e depende de a procura noturna se manter.
5. **Uma pauta de 36 itens continua legível.**
   - Os itens ficam agrupados por unidade, com filtros por unidade, tipo e situação e um filtro "só com conflito ou restrição".
   - Cada linha tem o mesmo desenho, e o detalhe abre sob demanda.
   - Recalcular a mesa inteira leva ≈ 30 ms no navegador.

## 6. Como a mesa evita contar duas vezes

| Risco | Regra no protótipo |
|---|---|
| Mesmo docente em dois campi | O código é um item de recurso com um destino. Soma um docente à capacidade de um único campus; o outro pedido aparece "sem o código" |
| Mesma oferta em dois itens | O segundo item que mexe na mesma oferta aparece como "sobreposto, não somado" e fica fora do conjunto. Exemplo: a proposta combinada da bancada de Serra sobre a turma nova de Informática |
| Somar percentuais locais | Todos os itens de um campus rodam juntos no mesmo motor. O percentual do Ifes é recalculado pela razão das somas, e a linha do Ifes avisa que não é a soma das linhas |
| Misturar calculado com inventado | Unidades ilustrativas e itens de teste ficam em linha separada em todas as tabelas e gráficos |
| Pactuar o que está em disputa | "Registrar o pactuado" deixa de fora itens com disputa, sobreposição ou falta de recurso e diz quais aguardam decisão. Os pactuados levam as ressalvas de capacidade |

## 7. Cadeia de cálculo e natureza dos números

A gaveta "Como calcula" de cada item mostra quatro passos:

1. **Decisão:** as operações em palavras, a variante escolhida e a situação.
2. **Trajetória acadêmica:** as coortes ano a ano, com entrada, progressão, evasão, conclusão e retenção.
3. **Indicadores**, em três grupos:
   - **Entram no cálculo da matriz:** MT por premissa e os percentuais legais pela razão das somas.
   - **Explicam o resultado:** ocupação, evasão, concluintes e retidos.
   - **Avaliam a viabilidade:** salas, laboratório, docentes por área e recursos.
   - IEA e RAP ficam como **não estimados**.
4. **Efeito na matriz:** ΔMT × R$ 1.324 (preço marginal de 2026), mais a mudança de degrau, no exercício dois anos depois.
   - O total de referência é o da Rede em 2026 (R$ 2.205,8 mi), mantido.
   - O cenário da Rede é declarado: no mesmo ritmo que o Ifes, como premissa, ou crescendo 1% ao ano a mais, como ilustração.
   - **O que é o valor em reais:** estimativa da parcela simulada, não previsão do orçamento.

**Um efeito que aparece sem ter sido programado:** a reorientação de parte da EaD do Cefor, que é ilustrativa, mostra ≈ −R$ 134 mil por exercício. Formação de professores continua acima de 20%, mas o valor de Qualidade é proporcional ao percentual dentro da faixa. O objetivo em tensão passa a ter preço visível.

## 8. O que continua ilustrativo ou depende de dados

| Elemento | Situação | O que o tornaria real |
|---|---|---|
| Meta de 3,9% e horizonte | Exemplo fictício, editável | Decisão do colegiado (D11) |
| Capacidade, código docente, bloco | Ilustrativos | Ficha de capacidade do campus; plano de obras; banco de códigos da gestão de pessoas |
| Evasão no 1º ano | Não está na PNP | Sistema acadêmico do campus (classe 3, dado institucional) |
| Efeito das ações de permanência e de ocupação | Hipótese, com faixa de 0,5 a 1,5 vez | Conferência do primeiro pacto; histórico de ações semelhantes |
| Hipótese macro para o Ifes inteiro | Extrapolação de Vitória e Serra (×4,1 pela matrícula equivalente técnica) | Simular todas as unidades com o mesmo motor |
| Valores em reais | Referência marginal, Rede de 2026 constante | Planilha da matriz como insumo (D12) e cenários da Rede (SPEC-005) |
| Itapina, Cefor, 27 itens de teste | Inventados | Propostas reais dessas unidades |
| Motivos acadêmicos e territoriais do código | Texto ilustrativo | Pareceres das unidades |
| Pacto do ciclo 2028 | Registrado só na sessão do navegador | SPEC-002 |

## 9. Efeito nas especificações e no MVP

**Continuam sete especificações.** O que esta rodada pediu cabe nas duas primeiras:

- **SPEC-001** ganha:
  - o desafio institucional, com partida, meta, horizonte e cenário, sem cota por unidade;
  - a pauta como unidade de composição: item, origem, situação, recurso e variantes;
  - o nível do curso, com operações por oferta;
  - recursos compartilhados com destino único;
  - a comparação em quatro anos entre sem novas decisões, item e conjunto.
- **SPEC-001, critério de aceite (6), novo:** a mesa responde à pergunta desta rodada para uma pauta de pelo menos 30 itens, entrando pelo desafio ou por uma proposta de curso.
- **SPEC-002** ganha, por item pactuado, o indicador acompanhado, o responsável e a primeira conferência. Ganha também a regra de que nada em disputa é pactuado.
- **O que fica fora, de propósito:** fluxo de aprovação com alçadas (a mesa registra quem decidiu), cadastro genérico de metas e qualquer meta individual por pessoa.

**Para o MVP**, o efeito é de profundidade, não de escopo. A jornada continua sendo o plano de oferta do ciclo 2028. O que muda é que a mesa compõe decisões, e não só campi, e que a Reitoria pode abrir a conversa com um desafio.

## 10. Decisões que esta rodada ajusta

- **D11, revista: papel da participação na matriz.** A orientação desta rodada a responde em parte.
  - **Fica decidido:** a participação pode ser **meta institucional**, mas não é distribuída como cota.
  - **Continua aberto:**
    1. **Formalização:** se a meta entra formalmente no PDI, o que pede a emenda do princípio VI.
    2. **Calibração:** qual horizonte e qual valor. O exemplo de 3,9% em quatro anos está fora do alcance mostrado pelo protótipo.
    3. **Quem publica o desafio** e em que momento do ciclo de oferta.
- **Nova pergunta para a validação mínima (D3):** a reunião relatada tinha 30 a 40 itens. Quem monta essa pauta hoje, com que antecedência, e quais itens chegam sem dono? A resposta define se a pauta nasce na Reitoria, nos campi ou nos dois.

## 11. Limites

- **Nenhum gestor ou coordenador viu o protótipo.** As hipóteses H1 a H6 continuam sem teste.
- **O motor continua sendo o da POC 0.0.2**, calibrado em 2023–2025. A ação de permanência no 1º ano é representada como redução da evasão anual da oferta, porque o motor não separa a evasão por ano do curso.
- **Só Vitória e Serra são calculadas.** A participação "sem novas decisões" é a partida ajustada pelo cenário da Rede: a dinâmica de manter a oferta nas outras 20 unidades não é projetada.
- **O que fica perdido ao recarregar a página:** o desafio, a pauta e o pacto vivem só na sessão do navegador.
