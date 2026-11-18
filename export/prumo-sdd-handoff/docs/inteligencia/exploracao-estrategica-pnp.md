# Exploração estratégica da Rede Federal com a PNP

> **Natureza:** consolida o que se sabe sobre usar a série pública da Plataforma Nilo Peçanha (PNP) como inteligência longitudinal e comparativa. Os achados são **fatos sobre a série** e **associações**; não são regras universais nem explicações causais.
> **Evidência de origem:** [estudo exploratório da PNP, 10/11/2026](../../referencias/estudos/estudo-pnp-2026-11-10.md) (14 tabelas, T1 a T14), reproduzível por [scripts/analises/estudo-pnp/](../../scripts/analises/README.md); [portão de dados, 09/11/2026](../../referencias/estudos/portao-de-dados-2026-11-09.md).
> **Relacionados:** [visão](../produto/visao.md) § 6.2 · [fontes e proveniência](../dados/fontes-qualidade-e-proveniencia.md) · [Matriz CONIF](../dominio/matriz-conif-e-indicadores.md) · [simulação](../simulacao/modelos-premissas-e-validacao.md)

## 1. A oportunidade

A PNP publica, por instituição, unidade e curso, os indicadores de gestão da Rede Federal desde o ano-base 2017. Ninguém precisa de dado privado para ler a trajetória de qualquer instituição. O valor do PRUMO não está em exibir esses indicadores (a PNP já faz isso), mas em:

- ler **trajetórias** em vez de retratos;
- **decompor** variações para separar o que a instituição fez do que a Rede fez;
- escolher **comparáveis por trajetória**, com critério declarado;
- converter o que se encontrou em **evidência** que alimenta premissas de simulação e propostas de governança.

**Conclusão do estudo:** a série deve entrar no produto como **camada de premissas e de contexto** para o simulador e para o pacto de metas, **não como painel nem como ranking**. A [visão](../produto/visao.md) concilia isso com uma capacidade de exploração própria, desde que organizada por perguntas e decomposições e terminando em evidência (decisão de 10/11/2026; forma na interface definida só para a primeira fatia).

## 2. Fonte, granularidade e variáveis

- **Natureza:** indicadores agregados já calculados (exportação "Indicadores de Gestão"). **Não há microdados**, coorte individual nem ciclo de matrícula. Cada ano aparece com a metodologia da sua edição; a série não foi recalculada para trás.
- **"Ano" = ano-base**, não edição da PNP (verificado contra a matriz de 2026).
- **Universo:** 64 instituições por ano (63 em 2025). A **Rede41** (38 institutos federais, 2 Cefets e Colégio Pedro II) é o universo da Matriz CONIF; exclui as 23 escolas técnicas vinculadas. Unidades: de 642 (2017) a 661 (2025).
- **Granularidade:** varia por arquivo (curso × unidade; unidade; instituição). Cobertura comprovada arquivo a arquivo em [fontes](../dados/fontes-qualidade-e-proveniencia.md) § 3: **nem todos os arquivos cobrem 2017–2025 nem todas as instituições.**
- **Ligação entre arquivos:** direta no nível unidade × ano; no nível de curso, só por nome + tipo + oferta + modalidade. Não há chave de curso nem de unidade.

| Pergunta de gestão | Variáveis | Situação |
|---|---|---|
| Crescimento | Matrículas, matrícula equivalente | Confirmado |
| Ingresso × tempo de vínculo | Ingressantes, matrículas | Confirmado |
| Portfólio | Tipo, forma, modalidade, eixo | Confirmado, com rótulos instáveis |
| Percentuais legais | Matrícula equivalente por classe | Confirmado (2021–2025) |
| Retenção | Situação de matrícula | Parcial (inclui FIC e EaD) |
| Absorção | Ingressantes/vaga sim; inscritos/vaga não | Parcial |
| Permanência e êxito | Evasão, eficiência acadêmica | Parcial |
| Capacidade docente | Professor-equivalente | Parcial (sem área) |
| Infraestrutura, demanda territorial, custo por campus, intenção de gestão | — | **Ausente** |

## 3. Comparabilidade e quebras metodológicas

**[PRINCÍPIO]** Série só é série dentro de um bloco metodológico comparável; a quebra é metadado da série.

| Quebra | O que acontece | Consequência |
|---|---|---|
| **Fórmula da matrícula equivalente (2020 → 2021)** | A razão ME/matrícula cai (técnico presencial 1,209 → 1,079; tecnologia presencial 1,166 → 1,046; bacharelado presencial 1,131 → 1,088). Na EaD, licenciatura, especialização e tecnologia sobem para cerca de 1,0; técnico EaD e bacharelado EaD já estavam perto disso em 2019 | ME só forma série em **2021–2025**. Para séries longas, usar matrículas físicas. A edição exata da mudança não foi confirmada |
| **Pandemia (2020–2022)** | Evasão anual regular presencial 18,5% (2017) → 9,7% (2020) → 9,1% (2021) → 16,0% (2022); retidos em curso 21,0% (2017) → 46,6% (2021) → 24,9% (2025); vagas −20% em 2020 | Melhoras nesses anos são artefato. Comparar médias trienais A (2017–2019) e B (2023–2025) |
| **Rótulos instáveis** | FIC EaD salta de 90,8 mil para 642,3 mil matrículas em 2020 como "Sem Programa Associado"; MOOC só aparece como programa a partir de 2021; PROEJA, Bolsa Formação e PARTIUIF como programa só em 2025; E-TEC some de 2019 a 2022 | Concomitante e subsequente devem ser analisados juntos; classificações por programa não formam série |
| **Sem código estável de unidade** | Nome mais recente; renomeações e incorporações invisíveis (ex.: Presidente Kennedy, Ifes, a partir de 2022) | O produto precisa de identidade própria de unidade |
| **Formação de professores** | A PNP não permite classificar por curso. No Ifes, %FP oscila: 21,5% (2021), 14,4% (2022), 25,1% (2023), 12,1% (2024), 24,8% (2025) | Série volátil, coerente com ofertas em pulso e reclassificação; confirmar com a instituição |

**Indicadores não utilizáveis:** taxa de ocupação (retirada da PNP para reanálise; 144 linhas acima de 100%); inscritos por vaga (baixa confiabilidade); gastos (nominais, só por instituição, sem deflator). Eficiência acadêmica da PNP inclui FIC e não reproduz a da matriz.

## 4. Tipos de investigação e decomposições

| Investigação | Como | Cuidado |
|---|---|---|
| **Decomposição por grupo de oferta** | Quatro grupos mutuamente exclusivos (regular ou FIC × presencial ou EaD); a soma fecha com o total | Só com grupos exclusivos; a matrícula total soma ciclos, não pessoas |
| **Participação: numerador × denominador** | Δparticipação = (x₂ − x₁)/X₂ (efeito numerador) + (x₁/X₂ − x₁/X₁) (efeito denominador) | Separa "o que fizemos" de "o que a Rede fez". Perder participação não significa piorar |
| **Ingresso × tempo de vínculo** | M/I = matrículas ÷ ingressantes do mesmo ano; decomposição da variância de Δlog matrículas | M/I **não é permanência**: mistura progressão regular, menos evasão e retenção. Sem coorte, não se separa |
| **Contribuição dos campi** | Quanto de cada variação institucional vem de cada campus | Concentração varia muito entre instituições |
| **Reconfiguração de portfólio** | Variação de técnico × graduação por instituição | Distinguir reconfiguração de crescimento simultâneo |
| **Mudanças atípicas e ofertas em pulso** | Altas acima de 20% seguidas de queda acima de 15% por componente, campus ou curso | Nenhum pulso aparece no agregado institucional de 2021–2025; eles ficam no componente ou no campus |

## 5. Comparáveis

- **Por trajetória, não por tamanho**: perfil de oferta e mecanismo de crescimento (ingresso, evasão, retenção, composição), com o critério declarado.
- Pares do Ifes por porte e número de campi, usados no estudo: IFSC, IFRN, IFBA, IFPE, IFMA, IFPI, IFPR, IFMT. É um critério, não o critério.
- Um par só serve de referência de crescimento saudável se o crescimento não vier de retenção.
- **Nunca ranking.** Tabelas ordenadas por crescimento convidam a comparar perfis diferentes.

## 6. Conciliação PNP × matriz (portão de dados)

Teste de 09/11/2026: a soma dos campi do Ifes na PNP, ano-base 2024, reproduz os indicadores usados na matriz de 2026?

| Indicador | PNP (soma dos campi) | Matriz 2026 (C5) | Situação |
|---|---|---|---|
| Percentual técnico | 0,4403 | 0,44 | Reconcilia |
| Formação de professores | 0,1206 | 0,1206 | Reconcilia |
| EJA | 0,0186 | 0,0186 | Reconcilia |
| Professor-equivalente | 1.520 | 1.517,5 | Reconcilia |
| Numerador da RAP | 30.574 | 27.539,39 | **Não reconcilia** (RAP 20,11 × 18,148) |
| Eficiência acadêmica | 0,708 (inclui FIC) | 0,4905 | Não comparável |

São os **valores de referência** da primeira especificação. Ano-base 2025 (provável base da matriz 2027): técnico 0,4505; formação de professores 0,2480; EJA 0,0198.

Achados do portão: sem o Cefor (unidade de educação a distância), os campi do Ifes somam 50,95% de técnico em 2024; o Cefor tem 14,7% da ME do Ifes. Chegar a 50% exigiria converter cerca de 2.240 ME ou criar cerca de 4.480 ME técnicas.

**Divergências não reconciliadas entre o portão e o estudo** (escritos em dias diferentes, com pareamentos diferentes):

| Ponto | Portão (09/11, 37 instituições pareadas) | Estudo T13 (10/11, 41 pareadas) |
|---|---|---|
| Percentuais legais | 31 de 37 coincidem; demais por pareamento de nomes | Não reavaliado |
| Professor-equivalente | 32 de 37 a ±1% | Mediana 1,002 (1,000–1,005); todas a ±0,5% |
| Numerador da RAP, razão PNP ÷ matriz | 1,00 a 1,56 | 1,001 a 2,567 ("Matrículas RAP") |

O documento do portão também preserva, abaixo da conclusão, o registro original anterior aos dados, com o veredito oposto ("portão não aprovado"), e uma explicação já superada (fator de nível de curso como causa da distância). **Vale o veredito de cima** ("aprovado", com os dados de 2024); o texto original é histórico.

## 7. Achados empíricos

Fatos e associações da série 2017–2025. Números exatos e tabelas no [estudo](../../referencias/estudos/estudo-pnp-2026-11-10.md).

1. **O crescimento recente da Rede veio quase todo de FIC e EaD.** De 2021 a 2025, a ME da Rede41 cresceu 12,0% (+122 mil): regular EaD 55,1% do crescimento, FIC presencial 23,0%, FIC EaD 16,7%, regular presencial 5,3%. O Ifes perdeu 0,15 p.p. de participação (+0,12 de efeito numerador, −0,26 de efeito denominador).
2. **Matrícula cresce por duas vias de peso igual.** Entre as médias 2017–2019 e 2023–2025, matrículas regulares presenciais +10,4% com ingressantes −2,3%; M/I de 3,17 para 3,59. A variância de Δlog matrículas se divide 0,50 / 0,50 entre ingressantes e M/I. Correlação com Δ evasão ≈ 0; com professor-equivalente 0,43 (associação; docentes podem seguir ou preceder a matrícula).
3. **No Ifes, o gargalo do técnico está depois do ingresso.** Regular presencial: vagas +9,7%, ingressantes +4,6%, matrículas +0,7%. Técnico concomitante/subsequente: matrículas −25% (5.881 → 4.409) com ingressantes −6%. A queda de ocupação está na graduação (1,03 → 0,92).
4. **A Rede se afastou da meta de 50% técnico.** %CT da Rede: 61,5% (2017), 51,2% (2021), 47,8% (2025); instituições com %CT ≥ 50%: 35 (2017), 25 (2021), 24 (2025). No bloco comparável 2021–2025, queda de 3,4 p.p., com três componentes: metodológico (2021), FIC e pós EaD no denominador, reconfiguração real.
5. **Uma oferta em pulso move o indicador institucional.** Em 2023, especializações EaD de um campus tiraram 6,3 p.p. do %CT do Ifes (36,8%); com o Cefor, cerca de 10 p.p. Sem o Cefor, o Ifes tem 51,0% em 2024 e 50,8% em 2025; com ele, 44,0% e 45,1%.

**Primeira pergunta de alto valor** identificada: quanto cada vaga, por tipo de oferta e campus, se converte em matrícula ativa ao longo do ciclo, e como essa conversão evoluiu na instituição em relação à Rede e aos pares. Os fatos têm confiabilidade alta; a explicação depende de dados por coorte, que a PNP não tem.

## 8. Correlação não é causa

**[PRINCÍPIO]** A PNP não registra decisões. Toda leitura de "estratégia" de uma instituição é hipótese.

- Correlações com n = 41 e janelas curtas; nenhuma tratada como causal.
- Cada caso separa **fato observado**, **associação plausível**, **explicações alternativas** e **o que confirmaria**.
- Crescer por retenção é resultado acadêmico indesejável, não estratégia a imitar.
- O produto pode dizer "isto mudou" e "isto andou junto"; nunca "foi por isso".

## 9. Das descobertas à simulação e à governança

| Descoberta | Vira | Onde |
|---|---|---|
| Conversão vaga → matrícula difere por oferta e campus | Quatro premissas separadas (ocupação, evasão, retenção, conclusão), cada uma com valor do campus, faixa dos comparáveis e fonte. M/I único não serve | [Simulação](../simulacao/modelos-premissas-e-validacao.md) § 3 |
| Denominador da Rede cresce por FIC e EaD | Premissa de crescimento da Rede por modalidade e tipo, com intervalo | Simulação; referência financeira |
| Pulsos movem indicadores institucionais | Alerta quando uma oferta não técnica acima de um limiar afeta %CT ou %FP (ex.: mais de 1 p.p.), com o exercício afetado | Simulação e composição |
| Trajetórias diferentes com resultados parecidos | Comparáveis por trajetória decomposta | Inteligência |
| Contribuição de cada campus à variação institucional | Insumo do objetivo institucional e das propostas | [Governança](../governanca/metas-contribuicoes-e-aprendizado.md) |

## 10. O que a inteligência não faz

- Não ordena instituições, campi ou cursos por desempenho.
- Não atribui intenção.
- Não estima dotação em reais nem distribuição interna (a PNP não alcança).
- Não usa modelo de linguagem para produzir números.
- Não substitui dados por coorte: onde a pergunta exige coorte, diz "não estimável com a PNP".

## 11. Dados complementares que destravariam perguntas

Em ordem de prioridade (estudo § 8): dados por coorte ou turma do sistema acadêmico; projetos pedagógicos e reclassificações; planilhas oficiais da matriz 2023–2027; classificação de formação de professores; Censo Escolar; professor-equivalente por área e inventário de espaços; deflator e rateio de gastos.

## 12. Inconsistências de registro no estudo original

Encontradas na verificação de 11/11/2026; o estudo original **não foi alterado**:

- O estudo e o script dizem "19 CSV"; são **18 CSV** (o 19º arquivo da pasta é um arquivo de sistema `.DS_Store`).
- O estudo generaliza "64 instituições por ano"; a cobertura varia por arquivo e ano ([fontes](../dados/fontes-qualidade-e-proveniencia.md) § 3).
- O script ainda rotula M/I como "anos de permanência por ingressante" (T6), termo abandonado na revisão do estudo.
- O estudo lista **cinco** achados no § 1; a expressão "quatro achados" usada em outros documentos refere-se aos quatro *insights* priorizados (I-1 a I-4, § 6).
