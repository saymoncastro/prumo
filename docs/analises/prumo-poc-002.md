# POC 0.0.2 do Prumo: decisões de oferta com evidência histórica da PNP

> **Data:** 10/11/2026 · **Natureza:** prova de valor navegável, isolada. Não substitui a POC v2 (`poc/prumo-poc.html`) nem a demonstração de recomposição (`poc/prumo-recomposicao.html`), que continuam geradas sem alteração.
> **Abrir:** `poc/prumo-poc-002.html` no navegador, ou `python3 -m http.server 8765 --directory poc` e `http://localhost:8765/prumo-poc-002.html`.
> **Regerar:** `python3 poc/extrair_poc002.py <caminho>/indicadores-gestao` → `python3 poc/montar.py` → `node poc/testar_poc002.cjs`.
> **Base empírica:** auditoria longitudinal da PNP (`docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md`, PR saymoncastro/prumo#1).

## 1. Pergunta da demonstração

> *"Entre ampliar vagas, melhorar o aproveitamento dos cursos existentes e reorganizar ofertas, qual alternativa parece mais promissora para o meu campus, por quê, e como ela contribuiria para os objetivos institucionais?"*

## 2. Avaliação da POC existente e menor evolução

| O que existia | Reaproveitado | Limitação que impedia decisões realistas |
|---|---|---|
| **POC v2** (Comparar → Simular → Compor, meta de 50% técnico) | Jornada em três etapas, separação entre meta legal, faixa da PNP e limiar da Matriz, contribuição por campus em p.p. (decomposição numerador × denominador), registro de proposta | A decisão era "+n matrículas", com matrícula equivalente média do curso e sem tempo. Não modelava vagas → ingressantes → matrículas → concluintes |
| **Demonstração de recomposição** (Itapina e Barra de São Francisco) | Linguagem visual, marcadores de natureza do número, tempo da Matriz (exercício = ano-base + 2), referência F-29 só quando cruza faixa | Motor de coortes com permanência única *r*: não separa evasão de retenção. Não usa evidência histórica da Rede. Abandonou a jornada em três etapas |
| **Auditoria PNP** | Achado central: no técnico concomitante e subsequente do Ifes, as vagas são preenchidas, mas matrículas e concluintes caem depois do ingresso | — |

**Menor evolução escolhida:**

1. Manter as três etapas e o motor de coortes. Separar no motor os quatro mecanismos que o gestor pode querer mudar: ocupação, evasão, conclusão no prazo e retenção.
2. Tomar a decisão em **vagas**, não em matrículas.
3. Em cada alternativa, mostrar a evidência da PNP específica daquela decisão.

## 3. Por que Vitória e Serra

Os dois campi foram escolhidos pelos dados da auditoria (médias 2017–19 → 2023–25, oferta técnica concomitante e subsequente):

| Campus | Ingressantes/ano | Matrículas | Concluintes/ano | Por que serve à demonstração |
|---|---|---|---|---|
| Vitória | 567 → 629 | 1.492 → 1.257 | 410 → 231 | Maior oferta não integrada do Ifes. Há procura em parte dos cursos. Precedente real de ampliação: Metalurgia concomitante dobrou as vagas em 2023 |
| Serra | 237 → 128 | 832 → 406 | 152 → 53 | A procura pelo concomitante despencou (Informática: 312 → 90 inscritos). O integrado do mesmo eixo tem 1.765 inscritos para 74 vagas |

Os dois campi permitem comparar as três decisões sobre os mesmos cursos:

| Alternativa | Vitória | Serra |
|---|---|---|
| **A · Ampliar vagas** | +36 vagas/ano em Mecânica concomitante | +40 vagas/ano em Informática concomitante |
| **B · Aproveitar melhor** | Mesmas vagas; evasão −30% e ocupação até 95% onde há procura, na oferta não integrada | Igual |
| **C · Reorganizar** | 32 vagas de Eletrotécnica concomitante → Eletrotécnica integrado | 40 vagas de Informática concomitante → Informática para Internet integrado |

Todas começam em 2027. Os ingressos de 2026 já ocorreram e são projetados sem mudança.

## 4. Decisões de UX

- **Comparar mostra trajetória, não ranking.** Ifes × Rede em índice (2017–19 = 100), com a faixa da pandemia sombreada. A tabela dos campi é ordenada por tamanho e declara que não ordena desempenho. Fato e hipótese ficam em caixas separadas na mesma tela.
- **Simular abre com as três alternativas lado a lado**, em relação a manter a oferta. É o quadro que responde à pergunta do gestor. Abaixo vêm a leitura em texto, os gráficos, a evidência da decisão selecionada, as premissas editáveis, "o que precisa ser verdade" e o ano a ano.
- **Evidência ancorada na decisão.** "Ampliar" mostra a série da própria oferta, a procura excedente e o precedente de Metalurgia. "Aproveitar" mostra ocupação e evasão das ofertas não integradas contra os integrados do campus. "Reorganizar" mostra origem e destino lado a lado.
- **Cinco naturezas de número** com marcador visual: fato, estimado, premissa, hipótese e não estimado.
- **Faixas em vez de número único:**
  - premissas pessimista e otimista da alternativa;
  - erro do modelo por oferta;
  - coluna "em regime", para que decisões de prazo longo (integrado de 4 anos) não pareçam inúteis por terminarem fora do horizonte.
- **Compor é o centro.** Ele mostra:
  - escolha de uma alternativa por campus;
  - contribuição de cada campus por objetivo (técnico, formação de professores, EJA, matrículas, concluintes, retidos, docentes) com direção ▲/▼;
  - grade com as 16 combinações;
  - premissas a validar, geradas a partir das escolhas;
  - registro de proposta com situação fixa "para discussão".
- **Sem recomendação automática.** A leitura em texto diz qual alternativa aumenta mais cada medida e o que cada uma exige, e encerra com "o Prumo não escolhe por você".
- **Matriz com três medidas separadas:** matrícula física, matrícula equivalente da PNP e base elegível (MT, não calculada). A MT é sinalizada pela divisão "no prazo × retidos", porque retido vale ¼. A referência em reais de Qualidade (F-29) só aparece se um percentual cruzar faixa. Nas combinações demonstradas, nenhum cruza, e a tela diz isso.

## 5. Premissas quantitativas

| Elemento | Natureza | Valor e origem |
|---|---|---|
| Evasão anual *e* por oferta | fato | Evadidos ÷ matrículas, média 2023–2025 (Taxa de Evasão) |
| Ocupação por oferta | fato | Ingressantes ÷ vagas, média 2023–2025 |
| Matrícula equivalente por matrícula | fato | 2025, por oferta |
| Prazo efetivo *D* | estimado | Melhor ajuste entre dois valores por tipo: integrado 3 ou 4 anos (Vitória: 4); não integrado 2 ou 3; PROEJA 3 ou 4 |
| Conclusão no prazo *c* (o restante fica um ano a mais) | estimado | Ajuste a matrículas e concluintes de 2023–2025 com os ingressos observados |
| Ofertas abertas em 2025 | premissa | *c* emprestado da mediana das ofertas da mesma forma no campus |
| Ocupação das vagas novas (A e destino de C) | premissa | Limitada pela procura excedente de 2025 (inscritos − ingressantes): Vitória Mecânica 100%; Serra Informática 28% |
| Efeito do programa de permanência (B) | premissa | Evasão −30% (faixa −15% a −45%); retenção −0% (editável). **Nenhum dado da PNP sustenta o tamanho do efeito** |
| Turmas e docentes | premissa | 40 vagas por turma; 30 aulas/semana no integrado, 20 no não integrado, 25 no PROEJA; 14 h de aula por professor |
| Demais ofertas e campi | premissa | Constantes como em 2025 |

**Ajuste do modelo** (`node poc/testar_poc002.cjs`; erro médio 2023–2025 nas ofertas das alternativas):

| Oferta | Erro em matrículas | Erro em concluintes |
|---|---:|---:|
| Mecânica concomitante (Vitória) | 7,9% | 9,2% |
| Eletrotécnica concomitante (Vitória) | 2,2% | 8,7% |
| Eletrotécnica integrado (Vitória) | 5,8% | 43,2% |
| Informática concomitante (Serra) | 12,6% | 41,7% |
| Informática para Internet integrado (Serra) | 4,7% | 11,4% |

Concluintes são mais ruidosos e recebem faixa maior.

## 6. O que a demonstração mostra com as premissas iniciais

Valores **estimados** em relação a manter a oferta, com faixa pessimista–otimista entre parênteses.

**Vitória:**

| Alternativa | Matrículas 2032 | Concluintes 2027–32 | Concluintes/ano em regime | Professores-equiv. |
|---|---:|---:|---:|---:|
| A · Ampliar Mecânica | +85 (+59 a +89) | +92 (+64 a +96) | +21 | +2,9 |
| B · Aproveitar melhor | +216 (+141 a +294) | +579 (+307 a +879) | +117 | 0 + programa não estimado |
| C · Eletrotécnica → integrado | +71 | +3 | +11 | +4,3 |

**Serra:**

| Alternativa | Matrículas 2032 | Concluintes 2027–32 | Concluintes/ano em regime | Professores-equiv. |
|---|---:|---:|---:|---:|
| A · Ampliar Informática | +30 | +17 | +5 | +4,3 |
| B · Aproveitar melhor | +46 | +94 (+44 a +151) | +20 | 0 + programa não estimado |
| C · Informática → integrado | +44 | +55 | +20 | +2,1 |

**Ifes, combinação Vitória B + Serra C em 2032:**

| Indicador | Valor |
|---|---|
| Formação técnica | 45,14% (manter: 44,74%; 2025: 45,05%) |
| Contribuição para a formação técnica | Vitória +0,34 p.p.; Serra +0,06 p.p. |
| Formação de professores e EJA | Caem por diluição: −0,18 e −0,01 p.p. |
| Concluintes técnicos 2027–2032 | +634 |
| Combinação de maior efeito na formação técnica | Vitória B + Serra B, com +0,41 p.p. |
| Combinações que levam o Ifes a 50% | Nenhuma das 16 |

**Leituras que um gestor tira sem explicação técnica:**

- **Em Serra, ampliar o concomitante é fraco.** A procura excedente cobre cerca de 11 das 40 vagas, e a turma nova exige docentes mesmo meio vazia. Reorganizar para o integrado entrega quatro vezes mais concluintes por ano com metade dos docentes adicionais.
- **Em Vitória, ampliar Mecânica tem procura, mas repete a conversão atual**, de 0,63 concluinte por ingressante. O precedente de Metalurgia (2023) mostra ingressantes dobrando sem concluintes acompanharem.
- **Aproveitar melhor é a alternativa com mais efeito nos dois campi, e a menos comprovada.** Depende inteiramente de um programa que reduza a evasão, cujo efeito e custo não estão na PNP. A demonstração transforma isso em pergunta explícita: o que precisa ser verdade.
- **Reorganizar para o integrado demora.** Até 2032 quase não aparece em concluintes em Vitória, porque as turmas novas levam 4 a 5 anos. Também troca de público: quem procura o concomitante perde vagas.
- **A meta de 50% não sai de dois campi.** A grade de combinações torna visível por que a meta exige pactuação com outros campi e com o Cefor.

## 7. Critério de sucesso: resultado honesto

A demonstração **responde à pergunta de forma fundamentada no que os dados sustentam**:

- **Ampliar.** Mostra se há procura e quanto ampliar converte em concluintes, com base na série da oferta e num precedente real.
- **Reorganizar.** Mostra procura e evasão do destino como fatos e o prazo de maturação como estimativa.
- **Instituição.** Mostra a contribuição de cada campus e os objetivos em conflito.

Ela **não decide** quando a melhor alternativa depende de um dado que não existe. É o caso de B, cujo valor vem de premissa sobre o efeito de um programa de permanência. Nesse caso, a resposta que a demonstração dá é condicional: *"B é a mais promissora se for possível reduzir a evasão em cerca de 30% a um custo aceitável; senão, em Serra, C; em Vitória, A ou C, com custo docente maior"*.

**O que falta para a resposta deixar de ser condicional** (não implementado, por decisão):

1. Dados por turma do qAcadêmico para Vitória e Serra (2019–2023): onde a evasão ocorre e quanto é retenção, estágio ou atraso. Isso também confirma o prazo efetivo de 4 a 5 anos dos integrados de Vitória.
2. Evidência do efeito e do custo de ações de permanência no próprio Ifes (programas já executados).
3. Docentes por área, salas e laboratórios disponíveis por turno.
4. Validação de 15 minutos com gestores dos dois campi. **Não foi feita**: a avaliação de compreensibilidade acima é do autor, não de usuários.

## 8. Limites

- Agregados anuais, não coortes. Evasão no primeiro ano, retenção e conclusão no prazo são estimadas.
- Inscritos é pouco confiável na PNP. A ocupação de vagas novas é premissa.
- A matrícula equivalente da PNP não é a base elegível da Matriz. Funcionamento, distribuição interna e repasse ao campus não são estimados.
- Professores-equivalentes vêm de premissa simples de aulas por turma, sem área de formação.
- Premissas e propostas ficam no `localStorage` do navegador. Não há backend, autenticação nem persistência compartilhada.

## 9. Diferenças em relação às versões anteriores

| Aspecto | v2 | Recomposição | 0.0.2 |
|---|---|---|---|
| Jornada | Comparar → Simular → Compor | Campus → Pactuação | Comparar → Simular → Compor |
| Decisão | +n matrículas | Vagas, suspensão, oferta nova | Vagas: ampliar, aproveitar (evasão, retenção, ocupação), migrar |
| Tempo | Estático | Coortes até 2029 | Coortes até 2032 e efeito em regime |
| Motor | Matrícula equivalente média | Permanência única *r* | Evasão (fato), conclusão no prazo e retenção (estimadas), ocupação (fato) |
| Evidência histórica | Retrato de um ano | Série do campus | Série do campus, Ifes × Rede e precedente de decisão semelhante |
| Matriz | Referência condicional | F-29 e tempo | F-29 só se cruzar faixa; matrícula física × equivalente × MT |
| Governança | Contribuição em p.p. | Pactuação de dois campi | Contribuição por objetivo, 16 combinações, premissas a validar, proposta "para discussão" |

## 10. Validação feita

- **Testes automatizados:** `node poc/testar_poc002.cjs` passa as 16 verificações:
  - dados iguais aos da auditoria;
  - ajuste das ofertas;
  - ancoragem em 2025;
  - ausência de negativos;
  - conservação matrícula = no prazo + retidos;
  - efeito da ampliação;
  - direção dos efeitos de evasão e retenção;
  - zeragem ao suspender ingressos.

  O teste do motor anterior (`node poc/testar_coortes.cjs`) continua passando.
- **Páginas existentes:** `prumo-poc.html` e `prumo-recomposicao.html` são regeneradas byte a byte iguais.
- **Navegador:**
  - as cinco telas foram percorridas sem erros de console;
  - interações testadas: troca de alternativa, edição e restauração de premissa, escolha de combinação, registro e remoção de proposta;
  - sem rolagem horizontal a 375 px.
- **Capturas:** em `docs/analises/capturas/poc-002/`:
  - [1. Comparar](capturas/poc-002/1-comparar.png)
  - [2. Simular · Vitória](capturas/poc-002/2-simular-vitoria.png)
  - [3. Simular · Serra](capturas/poc-002/3-simular-serra.png)
  - [4. Compor](capturas/poc-002/4-compor.png)
  - [5. Como calcula](capturas/poc-002/5-como-calcula.png)
