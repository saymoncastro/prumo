# Governança distribuída: metas, contribuições e aprendizado

> **Natureza:** o núcleo conceitual do PRUMO. A inteligência e a simulação existem para fundamentar o que se descreve aqui.
> **Maturidade:** é a capacidade **menos demonstrada**. Nos protótipos, limitou-se a registrar uma proposta no navegador. Tudo o que vai além disso é concepção, não evidência.
> **Relacionados:** [visão](../produto/visao.md) § 6.4 · [glossário](../dominio/glossario-e-modelo-conceitual.md) · [jornadas](../produto/jornadas-e-casos-de-uso.md) J6–J9 · [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) § 11 (RPE)

## 1. Por que a governança é a finalidade

As metas de uma instituição multicampi só existem no agregado; as alavancas estão nos campi. Sem um instrumento de coordenação:

- a inteligência vira painel;
- a simulação vira calculadora de campus, que otimiza localmente e pode prejudicar o coletivo (o risco nº 1 apontado na revisão estratégica);
- as metas são distribuídas de forma uniforme.

A cadeia que deve ficar visível, desde o documento fundador: **objetivo institucional → alternativas locais → projeção → efeitos nos indicadores e no orçamento → consolidação → compromisso → acompanhamento → revisão.**

**Governança não é salvar cenários.** É composição, pactuação, acompanhamento e revisão. A formalização dos ritos pode ser progressiva; **o conceito de contribuição e sua composição, não**.

## 2. Objetivos institucionais e metas agregadas

Um **objetivo institucional** é um indicador (numerador, denominador, regra de cálculo), suas réguas e um horizonte.

| Régua | Natureza | Exemplo (percentual técnico) |
|---|---|---|
| **Meta legal** | Norma; fonte própria | 50% (Lei 11.892/2008, art. 8º) |
| **Limiar orçamentário** | Faixa da matriz do exercício | 50% e 60% (QE, RMO-021) |
| **Meta pactuada** | Decisão da instituição | Definida pelas instâncias competentes; pode não existir ("não definida", nunca zero) |

As réguas não se confundem (RPE-09). Só no técnico o limiar coincide com a meta legal; em formação de professores (meta 20%) e EJA (meta 10%), cruzar o primeiro limiar não cumpre a lei.

**Posição atual** pela razão das somas dos campi, com ano-base e fonte. No Ifes, ano-base 2024: técnico 0,4403 na PNP (0,44 na matriz 2026), abaixo da meta legal e do limiar.

**A heterogeneidade é a regra.** A participação técnica **estimada** dos 22 campi do Ifes vai de cerca de 15% a 85% (inferência a partir da planilha interna da matriz, não pública; revisão estratégica § 1). Uma unidade de educação a distância (Cefor) tem 14,7% da ME do Ifes; sem ela, os campi somam 50,95% de técnico em 2024. **Nenhum campus sozinho move o indicador e nenhum precisa fazer o mesmo esforço.**

## 3. Diagnósticos locais

Antes de propor, cada campus vê:

- sua contribuição atual ao objetivo, em numerador e denominador;
- sua trajetória e a de campi com perfil parecido ([PNP](../inteligencia/exploracao-estrategica-pnp.md) §§ 4–5);
- o que limita suas alternativas (docentes, ambientes, demanda, missão local);
- as evidências registradas que fundamentam suas premissas.

## 4. Contribuições diferenciadas

Uma **contribuição** é o efeito de uma unidade sobre um objetivo, expresso em **Δnumerador e Δdenominador**, com ano-base e exercício de efeito (RPE-02). Exemplos do documento fundador, sobre uma mesma meta:

- campus A amplia uma oferta de alta demanda e melhora a ocupação;
- campus B investe em permanência;
- campus C reconfigura turnos e substitui uma oferta.

**[PRINCÍPIO]** O modelo não pressupõe distribuição uniforme. Dividir a mesma meta percentual entre todos não é o comportamento padrão. Compensações são legítimas: um campus pode contribuir com formação de professores ou EJA enquanto outro contribui com técnico.

**Contribuição de um campus a um percentual institucional** (decomposição exata usada no protótipo da meta de 50%):

```text
contribuição_campus (p.p.) = (Δnumerador_campus − p_atual × Δdenominador_campus) ÷ denominador_institucional_novo
```

A soma das contribuições é igual à variação do percentual institucional.

## 5. Composição matemática

**[PRINCÍPIO]** Indicadores institucionais são razões e agregam-se **pela razão das somas**, nunca pela média de percentuais (RPE-01).

| Grandeza | Como compõe |
|---|---|
| Matrículas, ingressantes, concluintes | Somam |
| Percentuais legais, RAP, eficiência | Somam-se numeradores e denominadores; depois divide-se |
| Evasão | Recalculada por numerador e denominador |
| Matrícula equivalente | Segue sua regra de ponderação |
| Ocupação de infraestrutura | Por horas-capacidade ou vagas de horário, no mesmo turno |
| Efeito orçamentário | **Não é soma de "receitas projetadas"** |

Na matriz, o **Funcionamento** é aproximadamente aditivo entre campi; **Qualidade, Reitoria e pisos não são** (faixas descontínuas, normalização pela Rede). Um modelo que só soma campi "erra justamente onde está o valor" (revisão estratégica § 3.2).

**Composição** = no máximo uma proposta por campus; campi sem proposta entram com a linha de base. Mostra o indicador por ano diante de cada régua e **quanto falta**, sem distribuir a diferença automaticamente.

## 6. Conflitos entre metas

- Volume de matrícula em FIC curto, MOOC ou EaD pode **diluir** percentuais legais e a relação aluno-professor.
- Contratar docentes afeta a relação aluno-professor; no Ifes 2026, a RAP estava a 0,15 do degrau que zera o subcomponente.
- Uma oferta que eleva um percentual legal pode baixar outro (na POC 0.0.2, uma combinação que elevava o técnico reduzia formação de professores em 0,18 p.p. e EJA em 0,01 p.p. em relação a manter).
- **Degraus são consequência, não objetivo** (parecer externo registrado na revisão estratégica): um curso superior com demanda e êxito não deve ser descartado para proteger o percentual técnico, assim como contratações docentes não devem ser contidas para proteger a RAP.

A composição mostra todo conflito com o valor do outro objetivo antes e depois.

## 7. Comparação de alternativas

- Alternativas locais e composições institucionais lado a lado, sem indicação da melhor.
- Grade de combinações (a POC 0.0.2 mostrou 16 combinações de dois campi; **nenhuma** alcançava 50% de técnico).
- Comparações explicitam recursos pedidos, contrapartidas e premissas a validar.

## 8. Negociação e pactuação

**Proposta** (de um campus): alternativa escolhida; contribuição por objetivo e por ano; recursos solicitados; contrapartidas oferecidas; premissas e "o que precisa ser verdade"; evidências; limites; autor e papel. **Uma proposta não é oferta aprovada.**

**Compromisso pactuado**: proposta aprovada pela instância competente, com responsável, indicador de acompanhamento, marcos e data de revisão (RPE-08).

**Incentivos fazem parte do desenho.** Quando o ganho é institucional e o custo é local, o pacto precisa dizer como o benefício retorna a quem contribuiu (RPE-10). **[HIPÓTESE]** No Ifes, o ganho de Qualidade parece concentrar-se na Reitoria (R$ 11,7 milhões na distribuição interna de 2026), mas a regra interna não foi reconstruída (RMO-075, L-28).

**Ciclo de gestão** (documento fundador § 13.4): diagnóstico → objetivos → propostas locais → simulação e negociação → aprovação → execução → acompanhamento → revisão periódica.

### 8.1. Exemplo explorado: "pacto de metas com degraus" (hipótese, não visão vigente)

A revisão estratégica de 09/11/2026 propôs reorganizar o produto em torno de um pacto de metas com degraus orçamentários. Foi **rebaixado a caso de uso** em 10/11/2026. Permanece útil como exemplo de pactuação:

- reproduzir os 44% de técnico do Ifes pela PNP (feito: portão de dados);
- mapa de degraus (técnico, formação de professores, EJA, RAP, eficiência);
- três pactos comparados: **(A) uniforme**, todos os campi +6 p.p.; **(B) por vocação**; **(C) técnico + PROEJA**;
- para cada pacto: ano-base e exercício, RAP, docentes, referência relativa e indicadores de missão;
- critério de sucesso proposto: o gestor muda ao menos uma decisão ou meta.

Nada disso foi executado com gestores.

## 9. Responsabilidades

| Quem | Papel |
|---|---|
| Reitoria e planejamento | Diretrizes, objetivos, consolidação |
| Pró-reitorias e diretorias sistêmicas | Avaliação técnica |
| Direção dos campi | Propostas e compromissos |
| Coordenações | Hipóteses pedagógicas |
| Orçamento, pessoal e infraestrutura | Validação de recursos |
| Colegiados e conselhos | Deliberação |
| TI e dados | Sustentação; **não** substitui competências decisórias |

**[PRINCÍPIO]** O PRUMO registra propostas e decisões; quem decide são as instâncias competentes. Não automatiza a autoridade administrativa.

## 10. Acompanhamento: três horizontes

| Horizonte | Pergunta | Quando se observa |
|---|---|---|
| **Execução** | A decisão foi implementada? As vagas foram ofertadas? | No ano da decisão |
| **Resultados intermediários** | Inscrições, ingressos e ocupação vieram como previsto? | Um a dois anos |
| **Longo prazo** | Matrículas, permanência, conclusão e repercussão orçamentária seguiram a projeção? | Do ciclo completo das turmas em diante; o efeito na matriz, cerca de dois anos depois do ano-base |

Cada compromisso é avaliado **só no horizonte que já pôde ser observado**. Uma estratégia não fracassou porque seu efeito ainda não teve tempo de aparecer.

## 11. Revisão e aprendizado

O ciclo fecha quando o **resultado observado** (edição seguinte da PNP; matriz do exercício seguinte) é lido contra o compromisso:

- vira **evidência nova** para a inteligência;
- **recalibra premissas** do simulador (previsto × observado; a matriz anual é dado de calibração "gratuito", oportunidade O6 da revisão estratégica);
- motiva **revisão de metas** e de compromissos.

Sem essa comparação, as três capacidades formam uma linha, não um ciclo.

## 12. O que a governança não é

- Não é salvar cenários.
- Não é dividir a mesma meta entre todos.
- Não é fluxo de aprovação automatizado.
- Não é sistema genérico de metas, OKRs ou tarefas.
- Não é ranking de campi.

## 13. Estado da evidência

| Elemento | Situação |
|---|---|
| Contribuição por campus em numerador e denominador | Demonstrada com dados conciliados (protótipo da meta de 50%) |
| Três réguas separadas | Ilustrada |
| Proposta com responsável, recursos, contrapartidas e indicador | Ilustrada (registro no navegador) |
| Composição pela razão das somas e grade de combinações | Ilustrada |
| Conflitos entre objetivos | Ilustrado (percentuais legais) |
| Pactuação, acompanhamento, revisão | **Não exercitados** |
| Reação de gestores e da reitoria a metas diferenciadas | **Hipóteses H1, H4, H6** |
| Regra de retorno do benefício ao campus | **Hipótese** |
| Rito de aprovação | **Pendente**; não desenhar antes de ver uma negociação real |
