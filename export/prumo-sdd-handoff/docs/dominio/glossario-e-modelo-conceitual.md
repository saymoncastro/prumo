# Glossário e modelo conceitual

> **Natureza:** vocabulário e relações conceituais. **Não** é esquema de banco, modelo de classes nem contrato de API; isso nasce no plano de cada especificação.
> **Relacionados:** [visão](../produto/visao.md) · [Matriz CONIF e indicadores](matriz-conif-e-indicadores.md) · [governança](../governanca/metas-contribuicoes-e-aprendizado.md) · [simulação](../simulacao/modelos-premissas-e-validacao.md)

Coluna **Origem**: **Oficial** = termo de norma, da Plataforma Nilo Peçanha (PNP) ou da Matriz CONIF, com definição externa que o PRUMO não altera; **PRUMO** = conceito próprio do produto.

## 1. Estrutura institucional

| Termo | Origem | Definição | Observação |
|---|---|---|---|
| **Rede Federal** | Oficial | Rede Federal de Educação Profissional, Científica e Tecnológica (Lei 11.892/2008) | Universo da Matriz CONIF: 41 instituições (38 institutos federais, 2 Cefets e o Colégio Pedro II) |
| **Instituição** | Oficial | Autarquia da Rede Federal (ex.: Ifes) | No PRUMO, é parâmetro e potencial cliente, nunca constante |
| **Unidade** | Oficial (PNP: "unidade de ensino") | Campus, campus avançado, polo, centro de referência ou reitoria | O PRUMO atribui identidade estável própria; a PNP identifica por nome, sem código |
| **Unidade atípica** | PRUMO | Unidade cujo comportamento foge ao de um campus regular (ex.: o Cefor do Ifes, que concentra educação a distância; polos; reitoria) | Tipo de unidade, não exceção no código |
| **Oferta** | PRUMO, sobre conceito oficial de curso | Curso numa unidade, com tipo, forma, modalidade e turno | **Unidade de decisão** do produto |
| **Tipo de curso** | Oficial (PNP) | Técnico, graduação (tecnologia, bacharelado, licenciatura), pós-graduação, qualificação profissional (FIC) etc. | |
| **Forma** | Oficial (PNP) | Para o técnico: integrado, concomitante, subsequente | Rótulos instáveis ao longo da série ([PNP](../inteligencia/exploracao-estrategica-pnp.md) § 3) |
| **Modalidade** | Oficial | Presencial ou a distância | |
| **Tipologia / programa** | Oficial (PNP) | Classificações como PROEJA, MOOC, formação de professores | Mudam de classificação entre edições |
| **Turno** | Oficial | Matutino, vespertino, noturno, integral | Relevante para capacidade física |
| **Turma (coorte de ingresso)** | PRUMO, sobre conceito oficial de ciclo de matrícula | Grupo que ingressa numa oferta num mesmo período | **Unidade de projeção no tempo** |
| **Ciclo de matrícula** | Oficial (PNP) | Registro de um ingresso numa oferta, do início ao término previsto | A matrícula total da matriz soma ciclos, não pessoas |

## 2. Medidas e indicadores

| Termo | Origem | Definição | Observação |
|---|---|---|---|
| **Matrícula (física)** | Oficial (PNP) | Contagem de vínculos ativos no ano-base | |
| **Matrícula equivalente (Meq)** | Oficial (PNP) | Matrícula ponderada por fatores de carga horária, esforço e nível do curso | Fórmula mudou entre os anos-base 2020 e 2021. Definição: [Matriz CONIF](matriz-conif-e-indicadores.md) § 3 |
| **Matrícula total** | Oficial (Matriz CONIF) | Medida usada na distribuição orçamentária | Não se deriva da matrícula equivalente da PNP |
| **Indicador** | Oficial ou PRUMO | Medida com numerador, denominador e regra de cálculo | Indicadores institucionais são razões; agregam-se pela razão das somas |
| **Percentual legal** | Oficial (Lei 11.892/2008) | Participação mínima de ofertas em técnico, formação de professores e EJA | Detalhe em [Matriz CONIF](matriz-conif-e-indicadores.md) § 4 |
| **Relação aluno-professor (RAP)** | Oficial | Matrículas por docente, conforme definição da fonte | Três valores diferentes para o mesmo conceito; não reconcilia ([Matriz CONIF](matriz-conif-e-indicadores.md) § 8) |
| **Eficiência acadêmica** | Oficial | Concluintes em relação a quem saiu do ciclo, conforme definição da fonte | A série pública inclui FIC; o índice da matriz exclui |
| **Taxa de evasão, retenção, conclusão** | Oficial (PNP) e PRUMO | Situação dos ciclos ao fim do período | No simulador, são premissas separadas |
| **Ocupação** | Oficial (PNP) e PRUMO | Ingressantes em relação às vagas | A PNP retirou o indicador; no simulador é premissa |
| **Ano-base** | Oficial | Ano a que os dados se referem | |
| **Exercício orçamentário** | Oficial | Ano em que o orçamento é executado | Na matriz de 2026, o exercício usou dados de dois anos antes; não é regra permanente |

## 3. Orçamento

| Termo | Origem | Definição |
|---|---|---|
| **Matriz CONIF** (Matriz Orçamentária) | Oficial | Modelo de distribuição dos recursos de custeio entre as instituições da Rede Federal, definido em portaria por exercício. Detalhe em [Matriz CONIF e indicadores](matriz-conif-e-indicadores.md) |
| **Componente / bloco** | Oficial | Parcela da matriz com regra própria (ex.: funcionamento, qualidade, assistência estudantil) |
| **Distribuição interna** | Oficial (por instituição) | Como cada instituição reparte entre suas unidades o que recebeu. No Ifes, regra não reconstruída |
| **Referência financeira** | PRUMO | Efeito condicional e parcial de uma decisão sobre um componente da matriz, num exercício, com as demais instituições constantes. Nunca é receita do campus |

## 4. Análise, planejamento e governança

| Termo | Origem | Definição |
|---|---|---|
| **Série observada** | PRUMO | Indicador por recorte e ano-base, com edição da fonte e blocos comparáveis |
| **Bloco comparável** | PRUMO | Intervalo de anos em que a metodologia de um indicador é estável. Quebras são metadado da série |
| **Fonte e versão** | PRUMO | Origem de um dado e edição de que veio |
| **Regra** | PRUMO, sobre normas oficiais | Fórmula ou parâmetro normativo, versionado por exercício, com texto e prática registrados em separado |
| **Evidência** | PRUMO | Fato observado ou padrão registrado pelo gestor, com recorte, método, fonte e limite de interpretação |
| **Hipótese** | PRUMO | Explicação possível ligada a evidências, com o que a confirmaria |
| **Premissa** | PRUMO | Valor assumido num cenário, com natureza e origem: histórico próprio, empréstimo de oferta equivalente ou julgamento |
| **Linha de base** | PRUMO | O que acontece se nada mudar, já com as turmas em curso. "Manter também muda" |
| **Cenário / alternativa** | PRUMO | Linha de base + decisões de oferta + premissas + versões de regras, dados e modelo → resultados simulados |
| **Resultado simulado** | PRUMO | Consequência condicionada às premissas, com faixa quando o modelo erra mais |
| **Capacidade** | PRUMO | Docentes por área e ambientes (salas, laboratórios) por turno; detalhada só onde limita a decisão |
| **Recurso orçamentário** | PRUMO | Custo, investimento ou recurso pedido associado a uma alternativa |
| **Objetivo institucional** | PRUMO | Indicador + réguas + horizonte, compartilhado pela instituição |
| **Régua** | PRUMO | Valor de referência de um objetivo. Até três, separadas: **meta legal**, **limiar orçamentário**, **meta pactuada** |
| **Meta** | Oficial ou PRUMO | Valor a alcançar. A meta legal é oficial; a pactuada é da instituição |
| **Contribuição** | PRUMO | Efeito de uma unidade sobre um objetivo, em numerador e denominador |
| **Proposta** | PRUMO | Alternativa escolhida por uma unidade, com contribuição por objetivo, recursos, contrapartidas, premissas e limites. Não é oferta aprovada |
| **Composição** | PRUMO | Conjunto de no máximo uma proposta por unidade, com o resultado institucional pela razão das somas. Em estudo, não é pacto |
| **Compromisso pactuado** | PRUMO | Proposta aprovada pela instância competente, com responsável, indicador e horizonte de acompanhamento |
| **Resultado observado** | PRUMO | Série dos anos seguintes lida contra o compromisso; volta a ser fato e fecha o ciclo |
| **Horizonte de acompanhamento** | PRUMO | Execução (ano da decisão), resultados intermediários (1 a 2 anos), longo prazo (ciclo completo e efeito na matriz) |

## 5. Naturezas da informação

Cada informação tem uma natureza, e a natureza nunca se perde quando passa de uma capacidade a outra.

| Natureza | Definição | Onde nasce |
|---|---|---|
| **Fato observado** | Contagem ou razão diretamente demonstrável pelos dados | Inteligência |
| **Padrão ou associação** | Relação empírica entre casos ou períodos; nunca causa | Inteligência |
| **Hipótese** | Explicação possível, com o que a confirmaria | Inteligência, registrada pelo gestor |
| **Premissa** | Valor assumido, com origem declarada | Simulação |
| **Resultado simulado (projeção)** | Consequência condicionada às premissas | Simulação |
| **Proposta** | Alternativa encaminhada por uma unidade | Governança |
| **Decisão ou compromisso** | Alternativa pactuada, com responsável | Governança |
| **Resultado observado** | Série posterior ao compromisso | Governança + Inteligência |
| **Não estimado** | Valor que não pode ser calculado com os dados disponíveis; aparece como tal, com o motivo | Qualquer uma |

## 6. Relações conceituais

```text
Instituição 1─* Unidade 1─* Oferta 1─* Turma
Instituição 1─* Objetivo institucional ─ Indicador (numerador, denominador, regra)
Objetivo ─ até 3 Réguas (legal, orçamentária, pactuada)
Série observada ─ Fonte/versão ─ blocos comparáveis
Evidência ─ recorte de Série observada;  Hipótese *─* Evidência
Cenário ─ pertence a 1 Unidade; altera Ofertas a partir de um ano; usa Premissas, versões de Regras, dados e modelo
Premissa ─ origem: histórico próprio | empréstimo | julgamento ; pode citar Evidência
Proposta ─ escolhe 1 Cenário; declara Contribuição a 1..* Objetivos; pede Recursos; oferece contrapartidas
Composição ─ no máximo 1 Proposta por Unidade; Unidades sem proposta entram com a linha de base
Compromisso ─ Proposta pactuada; responsável; indicador; horizonte
Resultado observado ─ Série observada posterior, lida contra o Compromisso → nova Evidência
```

Regras transversais:

- A composição institucional soma numeradores e denominadores; nunca faz média de percentuais.
- Matrícula física, matrícula equivalente e matrícula total são medidas distintas; nenhuma substitui outra.
- Série observada, evidência, hipótese, premissa, resultado simulado, proposta, compromisso e resultado observado são objetos distintos.
- Dados comuns a todas as instituições e dados de cada instituição ficam separados ([diretrizes SaaS](../arquitetura/diretrizes-saas.md) D2).
