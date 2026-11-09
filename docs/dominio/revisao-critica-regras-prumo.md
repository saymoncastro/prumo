# Revisão independente das regras de negócio do Prumo

> **Data:** 09/11/2026 · **Objeto:** fonte canônica [`matriz-orcamentaria.md`](matriz-orcamentaria.md) v1.1.0, [relatório complementar](auditoria-complementar-matriz-orcamentaria.md), [suíte de auditoria](../../tests/auditoria_matriz/README.md) e evidências de 08/11/2026.
> **Este documento não altera a fonte canônica.** As propostas do § 10 e a tabela do § 0 foram **incorporadas na fonte canônica v1.2.0** (09/11/2026), em blocos "Revisão 1.2.0", RMO-066–074, F-28–29, V-12–13 e L-24–27. A RMO-P05 virou a lacuna L-25 sem ID de regra, como recomendado.
> **Reprodução:** [`evidencias/2026-11-09/reproduzir_revisao_critica.py`](evidencias/2026-11-09/reproduzir_revisao_critica.py) (somente leitura; não é código de produto) → [`resultado-revisao-critica.json`](evidencias/2026-11-09/resultado-revisao-critica.json).
> **Documento irmão:** [Revisão estratégica](../analises/prumo-revisao-estrategica-oportunidades.md).

## 0. Atualização de 09/11/2026: Portaria MEC nº 243/2026 (N3) obtida

Depois da primeira versão desta revisão, o usuário forneceu a íntegra de N3, em impressão da página do DOU: publicação em **12/03/2026**, DOU nº 48, Seção 1, p. 63. Cópia preservada em [`evidencias/2026-11-09/portaria-243-2026-dou-impressao-web.pdf`](evidencias/2026-11-09/portaria-243-2026-dou-impressao-web.pdf), com SHA-256 e limites no [manifesto](evidencias/2026-11-09/manifesto.json). A página adverte que não substitui a versão certificada. Leitura integral feita; a equação do IEA (imagem) foi conferida visualmente.

**O que N3 confirma, muda ou deixa em aberto:**

| Tema | N3 | Efeito nesta revisão |
|---|---|---|
| Revogação e vigência | Art. 11 revoga N2; art. 12: vigor na publicação (12/03/2026) | L-01 **resolvida** quanto a texto, data e revogação. B e C5 (PLOA 2026) foram elaborados **antes** de N3: seus parâmetros não provam aplicação de N3. N3 rege, no mínimo, a matriz 2027 em diante. |
| Blocos | 80/10/10 após AE, mesma granularidade; art. 4º acrescenta **V – RFP** como indicador | RMO-004/006 confirmadas sob N3. |
| Defasagem | Anexo: "A Matriz de um dado ano é sempre elaborada com dados da PNP do ano anterior" | RMO-P06 passa a ter base **normativa**: matriz N ← PNP N−1 (ano-base N−2, como 2024 → 2026). |
| Cadeia de MT | **Texto idêntico ao de N2**: curto com CHC/800 e FEDA ÷ dias do período; limiar "> 365"; CHM "ajustada de acordo com o CNCT" | A divergência **L-24** (prática RO-MT × texto) **persiste sob N3**. RO-MT continua sendo a melhor evidência da prática, mas só está comprovada para 2026. Pedir à Setec qual forma será aplicada na matriz 2027. |
| EAD externo | 25% | O `/4` de B (6,25%) **não tem respaldo** nem em N2 nem em N3. L-06: anomalia de B confirmada. |
| EAD próprio | 80% | Sem mudança. |
| **MOOC** | **Novo: 8% da matrícula presencial** (CMTM08) | **Corrige o § 5.4:** os 80% de C5 são prática do PLOA 2026, anterior a N3, e não devem ser projetados. Sob N3, a MOOC do Ifes vale cerca de **R$ 72 mil**, e não R$ 722 mil. N3 não diz se a MOOC entra no denominador de F (efeito líquido no Ifes desprezível: ver abaixo). |
| Faixas de Qualidade | Tabelas 1–5 **idênticas** às de N2; pesos CT 7, FP 2, EJA 1 | Toda a análise de degraus (§ 3, RMO-P04) **vale sob N3**. |
| IEA, primeiro ramo | Tabela: peso 0,5; equação (imagem): **constante 0,5**, como em N2 | L-23 **persiste** na norma vigente; C5 segue mostrando a prática 0,5×IEA. |
| Assistência | Tabela 6 reescrita com faixas "0 < RFP ≤ 0,5 … 2,5 < RFP ≤ 3,5 → 0,5; RFP ≥ 3,5 → 0" | L-11: a sobreposição em exatamente 3,5 SM **persiste**; renda zero continua fora de qualquer faixa. |
| Piso de campus novo | R$ 700 mil por 5 anos (art. 8º) | RMO-065 confirmada sob N3. |
| Transição | Art. 9º repete "três anos, a partir da LOA de 2023", prazo já esgotado na LOA 2025 | Texto copiado de N2; **sem proteção de transição explícita para 2027+**. |
| Manutenção do referencial | **Novo art. 7º:** a Setec "envidará esforços" para manter, no mínimo, o referencial do ano anterior atualizado pelo IPCA | Não diz se o piso é da Rede ou de cada instituição. Se for por instituição, amortece ganhos e perdas marginais da matriz. **Questão a esclarecer com a Setec.** |

**Funcionamento do Ifes, com as MT de B, sob os fatores de N3** (bases nacionais e F de B mantidos; [resultado](evidencias/2026-11-09/resultado-revisao-critica.json), chave `funcionamento_ifes_por_regime`):

| Regime | Preço-base | Valor Ifes | Diferença para B |
|---|---:|---:|---:|
| B (EAD 6,25%; MOOC 0) | 1.220,3989 | R$ 62.782.149,76 | — |
| N3, MOOC 8% dentro do denominador | 1.218,8386 | R$ 63.873.167,58 | +R$ 1.091.017,82 |
| N3, MOOC 8% pago fora de F | 1.220,3989 | R$ 63.954.934,31 | +R$ 1.172.784,55 |

**Consequências para o produto:** (1) com MOOC a 8%, a MOOC deixa de ser alavanca orçamentária relevante, e o risco de gaming via MOOC cai muito; o via FIC curto continua (FIC vale 100% por hora). (2) Os degraus de Qualidade continuam sendo a alavanca de maior valor. (3) Os parâmetros 2026 (B e C5) servem como linha de base observada; projeções 2027+ devem usar os fatores de N3.

As seções seguintes foram ajustadas onde N3 altera conclusões; o texto original da primeira versão foi mantido quando continua válido.

---

Siglas de fontes seguem o § 0.1 da fonte canônica: **A** (livro), **B** (planilha 6ª fase Ifes), **N2** (Portaria 646/2022 republicada), **N3** (Portaria 243/2026), **C5** (demonstrativo IFMT PLOA 2026), **C6** (cadastro público).

---

## 1. Escopo e fontes examinadas

| Fonte | Exame nesta revisão |
|---|---|
| Fonte canônica v1.1.0 | §§ 0–4, 6–17 lidos; RMO-038, 041, 056, 061 e outras lidas por amostragem orientada a risco; matriz de rastreabilidade conferida. |
| Relatório complementar | Resumo, fontes e quadro de lacunas lidos; consistência com `resultado-validacao.json` conferida. |
| B | Aba CICLOS (2.322 ciclos) e Parâmetros relidas com `openpyxl`; MT recalculada **sem usar AC como entrada**. |
| N2 | Texto extraído (`pdftotext`); p. 124 renderizada e lida visualmente (faixas e equações de IEA, RAPP, CT, FP, EJA). |
| C5 | Abas **Ciclos** (1.086 ciclos com MT), **Cálculo Custeio**, **Custeio**, **Geral** e **Indicadores** (41 instituições) reprocessadas. |
| N3 | Primeira tentativa em 09/11/2026 sem sucesso; **íntegra obtida em seguida via usuário** (impressão web do DOU de 12/03/2026). Ver § 0. |
| A, N1, C6, C7 | Não reexaminados diretamente; usados pelo que a fonte canônica registra. |

**Consistência relatório × evidências × testes:** [FATO] as contagens do relatório (4/14/4 + L-23; 32 RMO revisadas; RMO-061–065; 19 testes OK; 2.322 ciclos monetizados; 22 campi) coincidem com a fonte canônica e com `resultado-validacao.json`. Não há inflação de resultados. O ponto fraco não é a honestidade do relatório: é que a **hipótese de trabalho para a MT foi a leitura literal de N2**, e as divergências foram tratadas como "contraexemplos a preservar" em vez de sinais da regra real.

---

## 2. Avaliação geral da extração existente

**Pontos fortes (manter):**

- Rastreabilidade exemplar: célula, página, hash, data de consulta.
- Separação rigorosa entre NORMATIVA, METODOLÓGICA, OPERACIONAL, HISTÓRICA, DERIVADA e HIPÓTESE.
- Recusa de inventar regras: N3 nunca foi inferida.
- Distinção correta entre contribuição interna (AF), participação nacional e orçamento efetivo.

**Fragilidades materiais:**

1. **A regra central está classificada contra a evidência.** A cadeia de MT foi registrada como NORMATIVA (RMO-061) na forma literal de N2. A regra efetivamente aplicada na produção da MT de 2026 difere dela em quatro pontos, e essa regra reproduz 100% dos ciclos de duas instituições (§ 5.1).
2. **Mistura de níveis.** Das 65 RMO, cerca de 20 descrevem comportamentos de uma planilha específica: filtros de cabeçalho (RMO-046), SUBTOTAL e visibilidade, coluna "Custo Evadido" (RMO-051/055), fator auxiliar AO (RMO-049), modelos ocultos (RMO-052). São achados de auditoria, não regras de negócio do domínio. Isso infla o catálogo e dificulta a implementação.
3. **Lacunas de alto impacto não catalogadas:** definição de matrícula equivalente dos percentuais legais e da RAP, economia dos degraus de Qualidade, MOOC no regime 2026 e definição operacional de IEA (§ 6).
4. **Conservadorismo assimétrico.** C5 foi tratado como "outro demonstrativo, sem homologação", o que é correto para parâmetros do IFMT. Mas C5 contém **dados nacionais** (bases da Rede, índices de todas as instituições, MT por ciclo produzida pela mesma cadeia nacional), que serviam para resolver L-02, L-06, L-10, L-12, L-13 e L-23. O potencial probatório de C5 ficou subaproveitado.
5. **Legibilidade.** Texto telegráfico com espaços suprimidos ("4 casas", "1095 dias" colados a palavras), frases de ressalva repetidas em quase todas as regras e cerca de 236 KB. Um desenvolvedor precisa ler a regra, a lacuna, a seção 6, a seção 13.1 e o relatório para implementar um passo. É preciso uma camada concisa de "regra implementável" (§ 12).

---

## 3. Regras conferidas independentemente

Amostra orientada a risco (projeções, elegibilidade, denominadores, participação):

| RMO | Tema | Conferência realizada | Resultado |
|---|---|---|---|
| 006 | 80/10/10 após AE | N2 art. 3º; C5 (Reitoria nacional R$ 220.597.802,15 = 10% de (D4 − D5) de B) | **Confirmada**; adicional: Reitoria = QE = R$ 220,6 mi em 2026. |
| 008 / 014 / 061 | Equalização de carga e dias | Recalculado em 2.322 ciclos de B e 1.086 de C5 | **Corrigir:** regra literal reproduz 1.300 (B) / 993 (C5); regra operacional reproduz 2.322 / 1.086. |
| 015 / 035 | Retenção, 3 anos, ICQA | Recalculado; papel de R (DJ) | **Confirmada** com precisão: elegibilidade por DJ; FIC tem DJ = DTC (retido FIC = 0). |
| 011 | Bônus agro | Agro inferido livremente (fator 1 ou 1,5) | **Confirmada:** fator 1,5 surge **somente** em 117 ciclos de 13 cursos agrários (Agronomia, Agropecuária, Agricultura, Agroindústria, Pesca, Aquicultura, Zootecnia, Florestas, Cafeicultura, Ciências Agrárias). L universal de B é irrelevante. |
| 012 | Stricto 3,75 | W de B | Confirmada. |
| 013 / 040 | Fatores EAD | C5 preço EAD = 0,25000 × presencial; FP = 0,8 | **Confirmada a divergência L-06** com evidência mais forte (§ 5.3). |
| 033 / 039 | Bolo e preço | D7 de B × soma de pres + EAD + FP Rede em C5 | **Novo:** F idêntico (diferença de R$ 0,01). |
| 041 | MOOC zero | D11 de B × base MOOC implícita de C5; N3 | **Corrigir:** base nacional idêntica (23.139,69); C5 (2026, pré-N3) paga a 80% fora de F; N3 fixa 8%. |
| 017 / L-23 | Primeiro ramo IEA | p. 124 renderizada; C5 Indicadores col. I/H | Divergência textual confirmada; **C5 aplica 0,5×IEA** (tabela/roteiro). |
| 019 / 021 / 022 | Faixas RAPP, CT, FP, EJA | p. 124; recálculo das somas da Rede em C5 | **Confirmadas**; somas reproduzem C5 (ΣRAPP 1.376,84; ΣCT 18,28; ΣFP 8,064; ΣEJA 0,8606). |
| 016 | Definição IEA | C5 col. E/F/H | **Complementar:** H = E/(E+F) (conclusão/(conclusão+evasão)); Ifes 0,4618/(0,4618+0,4796) = 0,4905. |
| 053 | Participação proporcional | Recalculado para cenários de faixa | Confirmada; precisa ser estendida a degraus (§ 6). |
| 059 | Reitoria | C5 H42 = (Σ valor matriz IFMT incluindo MOOC)/(Σ Rede) × R | **Complementar:** a base de Reitoria **inclui MOOC**. |
| 065 | Piso / transição | C5 Custeio D31–D33 | Confirmada a prática de complementação Setec "no período de transição" ainda citada no PLOA 2026; N3 repete o prazo esgotado (art. 9º) e cria o art. 7º (referencial anterior + IPCA); ver § 0. |

---

## 4. Regras confirmadas

Confirmadas sem ressalvas novas, no alcance já declarado pela fonte canônica: RMO-001, 002, 004, 005, 006, 007, 009, 010, 012, 018, 020, 022, 027, 033 (com o achado de F), 034, 036, 037, 039, 042, 043, 044, 045, 053, 054, 057, 058, 060. As regras históricas (RMO-028–032) não foram reexaminadas e permanecem como estão.

A aritmética de monetização de B (preço × AC) e as totalizações também permanecem corretas. O que muda é a **interpretação** de algumas delas (§ 5).

---

## 5. Inconsistências e divergências

### 5.1. A regra de produção da MT não é a leitura literal de N2 (novo L-24)

**[FATO]** A regra abaixo, denominada aqui **RO-MT (regra operacional de MT, exercício 2026)**, reproduz a quatro casas **2.322/2.322** ciclos de B (bônus agro inferido) e **1.086/1.086** ciclos de C5 (com as flags agro do próprio IFMT, sem inferência). A leitura literal de N2 reproduz 1.300 e 993.

```text
Período P = [DIP, DFP] (ano civil; NP = 366 em 2024)
QTDC = DTC − DIC + 1
Longo  ⇔ QTDC ≥ 365                       (N2 escreve "> 365")
CH     = min(CHC, CHM)  se longo           (N2 escreve CHM)
       = CHM            se curto            (N2 escreve CHC)
Se DTC < DIP (retido):
     se DJ < DIP → MT = 0                   (FIC: DJ = DTC → retido FIC = 0)
     senão DACP = NP/2 e fator_ret = 0,5
Senão DACP = |[DIC, DTC] ∩ P| (dias) e fator_ret = 1
FECHDA = (CH/QTDC × 365/800) × (DACP/NP)   se longo
       = (CH/800) × (DACP/QTDC)             se curto   (N2: DACP/NP)
MT = FECHDA × QTM × PC × (1,5 se agro) × fator_ret, comparado a 4 casas
```

| Diferença em relação a N2 literal | Evidência | Ciclos afetados em B |
|---|---|---|
| (a) Ciclo curto: FEDA = dias ativos ÷ **duração do ciclo**, e não ÷ dias do período | Sem isso, 1.033 FIC curtos e os casos 99, 585/586 e 511 divergem | ~1.047 curtos |
| (b) Ciclo longo: CH = **min(CHC, CHM)** | 81 ciclos longos com CHC < CHM, dos quais 55 têm MT > 0 e tornam o mínimo observável (licenciaturas de 2.800–3.100 h com CHM 3.200; técnicos de 2.992–3.150 h com CHM 3.200); inclui o contraexemplo 284 | 55 observáveis |
| (c) Limiar: QTDC = 365 vai ao ramo longo | 4 especializações de exatamente 365 dias; só é distinguível combinado com (a), porque no ramo curto do texto o resultado coincide | 4 |
| (d) Curto: CH = CHM (U), não CHC | 2 casos com CHM > CHC (linhas 1087, 1965) e 1 com CHC > CHM (1968) | 6 (evidência fraca) |
| (e) Elegibilidade de retidos por DJ (R), com FIC sem tolerância | 77 FIC encerrados antes de 2024 com AC = 0 | 77 |

**Interpretação [INFERÊNCIA]:** (a) e (b) tornam a fórmula equivalente, para ciclos regulares, a **horas do curso transcorridas no ano-base ÷ 800**, exceto pelo fator 365/366 nos longos em ano bissexto. É uma regra coerente: a leitura literal de N2 penalizaria duas vezes os cursos curtos, pois sua carga já é a do ciclo inteiro. Impacto em B: a MT dos ciclos curtos seria 431,0 (literal) em vez de 1.594,5 (aplicada).

**Os cinco contraexemplos de V-11 e T-M02 estão explicados:** 99 e 585/586 por (a); 284 por (b); 511 por (a) aplicado ao retido curto (DACP = 183 sobre QTDC = 337, razão 366/337 = 1,0861). Os "55 divergentes" e os "207 sem chave" da exploração anterior desaparecem quando o agro é inferido pelo fator, e não buscado em C6.

**Classificação proposta:** OPERACIONAL, com confiança **alta** (dois arquivos institucionais independentes, mesma edição nacional) para o exercício 2026. Não é NORMATIVA: N2 diz outra coisa e **N3 reproduz literalmente o texto de N2** (§ 0). A divergência deve ser registrada como **L-24** e levada à Setec ou à Comissão Paritária.

**Limite:** Y de B (= AA de C5) funciona como QTM em 100% dos casos, mas a definição PNP de "matrícula ativa no período" (ativa em algum dia do ano?) não foi lida. Isso importa para o modelo causal de evasão.

### 5.2. Parâmetros de B são os do exercício 2026 (revisão de L-02)

**[FATO]** O Funcionamento de B, `D7 = (D4 − D5) × 0,8 = 1.764.782.417,22`, é **idêntico** à soma dos valores nacionais de presencial + EAD + EAD FP de C5 (R$ 1.764.782.417,21). Logo, o rótulo "Matriz 2025 (proposta)" de `Parâmetros!C4` é obsoleto: D4/D5/D6 produziram o bolo F usado no PLOA 2026. As bases nacionais por situação diferem ligeiramente (presencial 1.371.414,60 em B × 1.371.348,35 implícito em C5), o que é compatível com B ser uma **fase anterior** (6ª) do mesmo exercício. O preço de B (1.220,3989) é provisório; o final é 1.220,3527. A diferença de R$ 2,95 bi registrada em C1 refere-se a outro agregado (proposta total), não ao bolo distribuído pela matriz.

### 5.3. EAD externo: a evidência contra o `/4` é agora fechamento, não analogia (L-06)

**[FATO]** Em C5, os valores da Rede para presencial (preço p), EAD externo (0,25p) e EAD FP (0,8p) somam **exatamente** F. Portanto, o denominador `Σ N_s w_s` com w = (1; 0,25; 0,8) fecha com preços (1; 0,25; 0,8). O `/4` adicional de B (6,25%) **impede** esse fechamento: falta R$ 15,17 mi na Rede, conforme já calculado em T-H05. Conclusão proposta: o `/4` de B é **erro ou artefato de fase**, não regra. Efeito na leitura do Ifes: R$ 1,10 mi de subestimação da contribuição EAD externa.

### 5.4. MOOC: monetizado nacionalmente em 2026, fora do bolo F (corrige RMO-041 e o § 8)

> **Atualizado por N3 (§ 0):** a Portaria 243/2026 fixa a MOOC em **8%** do presencial. Os 80% abaixo descrevem a prática do PLOA 2026, anterior a N3, e não devem ser projetados para 2027+. Sob N3, o valor MOOC do Ifes é de cerca de R$ 72 mil.

**[FATO]** A base nacional MOOC de B (D11 = 23.139,6926) é idêntica à implícita em C5 (R$ 22.590.866,05 ÷ 976,2821 = 23.139,69). C5 paga MOOC a **0,8p**, como acréscimo **fora** de F, e inclui esse valor na base de rateio da Reitoria (H42). B atribui peso 0 no denominador (coerente com "fora de F") **e** preço 0 por ausência de chave. No regime de 2026, isso deixava de lado cerca de R$ 721,6 mil para o Ifes (739,1173 MT × 976,28). A afirmação da fonte canônica de que não se confirmou regra que converta MOOC em valor deve ser revista: há evidência operacional de monetização em 2026 e previsão normativa de 8% em N3. A **origem do recurso** que pagou a MOOC fora de F em 2026, e se sob N3 ela entra no denominador de F, continuam não determinadas.

### 5.5. L-23 tem resolução operacional para 2026

**[FATO]** Em C5 (Indicadores), as 13 instituições abaixo de 0,9 × média têm `IEA ponderado = 0,5 × IEA` (ex.: 0,3037 → 0,152; 0,3332 → 0,167), e não a constante 0,5. A Setec aplicou a **tabela e o roteiro**, não o primeiro ramo da equação da p. 124. Proposta: manter L-23 aberta como **divergência textual de N2**, mas registrar a regra aplicada em 2026 como OPERACIONAL (alta confiança) e usá-la como padrão de cenário.

### 5.6. Média IEA da Rede é inferível

**[INFERÊNCIA]** As fronteiras observadas em C5 restringem a média IEA da Rede de 2026 a **(0,4606; 0,4619]**. A média simples dos 41 índices é 0,4561, o que **não** coincide: a média PNP não é a média simples das instituições (exclusões de N2, ponderação PNP). Logo, a "média da Rede" precisa ser obtida da PNP, não recalculada.

### 5.7. Divergência de definição entre MT e percentuais legais

**[FATO]** A participação técnica estimada a partir das matrículas equalizadas de B (MT ÷ peso ÷ agro) é **57,8%** (61,4% sem FIC). O indicador PNP usado na matriz (C5, Ifes) é **44%**. PROEJA: 1,64% em B × 1,86% na PNP. Licenciaturas: 8,3% × FP 12,06%. Portanto, **%ME dos percentuais legais não é derivável de MT**: há definição própria (matrícula equivalente com fator de esforço de curso? inclusão de EAD/FIC/MOOC no denominador? outra janela?). Isso bloqueia a simulação dos degraus por campus (§ 9).

---

## 6. Regras potencialmente ausentes

| ID provisório | Regra ausente | Por que importa | Evidência disponível |
|---|---|---|---|
| RMO-P01 | **RO-MT** (§ 5.1), regra operacional de produção da MT 2026 | É a regra de projeção de toda nova oferta | B + C5, 3.408 ciclos |
| RMO-P02 | **MOOC:** 8% do presencial a partir de N3 (NORMATIVA); em 2026, prática pré-N3 de 0,8p fora de F, incluída na base da Reitoria (OPERACIONAL) | Política de MOOC/FIC; valor do Ifes | N3 Anexo; C5 Cálculo Custeio; B D11 |
| RMO-P03 | **Definição operacional do IEA:** conclusão ÷ (conclusão + evasão) nos ciclos concluídos; retenção fora | Liga permanência → orçamento | C5 Indicadores E/F/H (41 instituições) |
| RMO-P04 | **Economia dos degraus:** valor marginal de cruzar um limiar = `(w_novo/(Σ − w_atual + w_novo)) × submontante − valor_atual`, mantidos os demais | É a decisão de maior alavancagem identificada | N2 p. 124 + C5 Indicadores |
| RMO-P05 | **Matrícula equivalente para RAP e percentuais legais** (numerador, denominador, fator de esforço, inclusão de EAD, FIC e MOOC) | Sem ela, CT, FP, EJA e RAP por campus não são simuláveis | **Ausente**; Portaria Setec 146/2021 e documentação PNP a extrair |
| RMO-P06 | **Defasagem:** ano-base educacional = exercício − 2 (2024 → 2026), com MT por interseção com ano civil | Calendário de efeitos | B E3:F3; C1; C5 Y:Z |
| RMO-P07 | **Reitoria:** participação = Σ valor matriz da instituição (pres + EAD + MOOC + FP) ÷ Σ Rede × R | Complementa RMO-059 | C5 H42 |
| RMO-P08 | **Referencial 2026 dos subcomponentes de QE:** IEA = RAP = R$ 55.149.450,54; CT = 77.209.230,76; FP = 22.059.780,22; EJA = 11.029.890,11 | Parâmetros por exercício | C5 E46–E58 |
| RMO-P09 | **Indicadores institucionais 2026 por instituição** (IEA, RAP, MEq, professor-equivalente, %CT, %FP, %EJA) como dado observado versionado | Evita reconstruir a Rede | C5 Indicadores |
| RMO-P10 | **Elegibilidade de retidos por DJ** como entrada (não como 1.095 dias calculados); FIC com DJ = DTC | Substitui a ambiguidade "três anos × 1.095 dias" | B R; C5 M; RO-MT |

Regras **não** recomendadas como RMO (são do domínio estratégico; ver § 11): agregação por razão das somas, coortes, metas e pactos.

---

## 7. Questões normativas e temporais

1. **N3 obtida (§ 0).** Publicada em 12/03/2026, depois da elaboração da PLOA 2026 (metadado de B de 25/02/2026). Rege a matriz 2027 em diante. Para 2027+, usar EAD 25%, FP 80%, **MOOC 8%** e as faixas de Qualidade, que não mudaram.
2. **Prática × texto.** N3 **não** formalizou a prática: repete o texto de MT de N2 e a constante 0,5 do IEA. RO-MT e 0,5×IEA seguem como práticas observadas em 2026 sem respaldo textual. A MOOC a 80% de C5 contraria N3. Recomenda-se pedir à Setec, formalmente, a memória de cálculo da matriz 2027 para confirmar qual forma de MT e de IEA será aplicada.
3. **Transição.** O art. 9º de N3 repete o prazo de N2 ("três anos a partir da LOA 2023"), já esgotado. O novo art. 7º compromete esforços para manter o referencial anterior + IPCA, sem dizer se por instituição. A proteção efetiva para 2027+ precisa ser esclarecida.
4. **Defasagem.** Dado 2024 → exercício 2026. Uma decisão de oferta tomada em 2026 para ingresso em 2027 afeta o ano-base 2027 → exercício 2029, sob N3 ou norma posterior (a Comissão Paritária revê parâmetros anualmente, art. 10).
5. **Ano bissexto.** NP = 366 em 2024; ciclos longos carregam o fator 365/366. Em anos não bissextos a fórmula longa e a curta coincidem em "horas transcorridas ÷ 800".

---

## 8. Problemas de granularidade, agregação e interpretação

- **Unidade natural de cálculo:** ciclo (coorte de oferta) × ano civil, com datas em dias. Semestre letivo não é a unidade da matriz.
- **QTM por ciclo, não por pessoa:** sem rateio de dias individuais. Evasão no ano não reduz a MT do ano [a confirmar na definição PNP].
- **Indicadores institucionais (IEA, RAP, %CT, %FP, %EJA) são razões de somas.** A contribuição de um campus é um delta de numerador e de denominador, nunca um percentual próprio a somar. Médias de percentuais de campi são incorretas.
- **Degraus e relatividade:** o valor de QE depende da posição do Ifes **e** das demais instituições; somente "mantidos os demais" ou cenários explícitos.
- **Identidade de campus:** B tem `Código do campus` vazio; nomes de unidade são a chave de fato. Para integrar PNP e sistemas, adotar o código de unidade PNP/SISTEC.
- **Dupla contagem:** MT soma ciclos, não pessoas. Uma pessoa em dois ciclos conta duas vezes (correto para a matriz, incorreto para "estudantes atendidos").
- **Leituras que devem ser proibidas no produto:** AF/J como repasse ao campus; AI ("Custo Evadido") como perda recuperável; MT como pessoas; participação do campus × montante nacional como orçamento do campus.

---

## 9. Lacunas que impedem implementação

| Lacuna | Capacidade bloqueada | Severidade | Caminho |
|---|---|---|---|
| ~~N3 íntegra~~ **resolvida (§ 0)**; restam: forma de MT e de IEA efetivamente aplicada em 2027 (texto × prática), MOOC dentro ou fora de F, alcance do art. 7º | Cálculo 2027+ com confiança operacional | P1 | Memória de cálculo da matriz 2027 junto à Setec; confirmar com a versão certificada do DOU |
| RMO-P05 (%ME e MEq RAP) | Degraus por campus (a capacidade de maior valor) | P0 | Portaria Setec 146/2021 + microdados PNP; teste: reproduzir 44% / 12,06% / 1,86% / 18,15 do Ifes |
| Regra interna do Ifes | Efeito em R$ por campus | P0 para R$ por campus; não bloqueia metas institucionais | Proad/Prodi |
| Taxas de ocupação, evasão e conclusão por curso e campus | Projeção de coortes (vagas → QTM) | P1 | PNP (pública), por ciclo |
| Definição PNP de "matrícula ativa no período" | Modelo causal de evasão × MT | P1 | Glossário PNP |
| Origem do recurso MOOC fora de F | Valor MOOC 2027+ | P2 | Setec |

**Não são mais bloqueios** (resolvidos operacionalmente para 2026 por esta revisão): L-10 (produção de AC), L-12 (CHM), L-13 (FIC e datas), L-23 (ramo aplicado), L-02 (identidade de F).

---

## 10. Propostas concretas de correção das RMO

Preservar os IDs e o histórico (§ 0.2 da fonte canônica). Propostas para a versão 1.2.0:

| RMO / seção | Proposta | Evidência |
|---|---|---|
| **RMO-061** | Manter o texto N2 como variante "N2 literal". Acrescentar a variante **RO-MT 2026** (§ 5.1) como OPERACIONAL, confiança alta, e indicá-la como **padrão de cenário** até N3. Retirar a afirmação de que a equivalência integral com B está bloqueada. | Script; 2.322/2.322 e 1.086/1.086 |
| **RMO-056** | Mudar a situação "nova oferta → MT" de CONDICIONAL por regra para CONDICIONAL **apenas** por QTM projetada e cadastro (CHM, PC, agro, DJ). | Idem |
| **RMO-014 / L-12** | CH = min(CHC, CHM) em ciclos ≥ 365 dias; CHM em curtos. Resolver L-12 operacionalmente. | 55 + 6 ciclos |
| **RMO-015 / RMO-035 / L-13** | Elegibilidade de retidos por DJ; FIC com DJ = DTC; registrar que "1.095 dias" é a forma de cálculo da DJ não FIC. Resolver L-13 operacionalmente. | 77 FIC |
| **RMO-008** | Registrar o limiar efetivo `QTDC ≥ 365` e que, nos curtos, FEDA é relativo à duração do ciclo. | 4 + 1.047 ciclos |
| **RMO-011 / L-08** | Registrar que a inferência pelo fator identifica exatamente 13 cursos agrários em B; propor como cadastro agro de referência do Ifes 2026, a homologar. | 117 ciclos |
| **V-11 / T-M02** | Reescrever: os cinco casos deixam de ser "contraexemplos" e passam a casos de teste **positivos** da RO-MT. Manter T-M02 como teste da **divergência entre N2 literal e prática**. | § 5.1 |
| **RMO-041 / RMO-013 / § 8 (MOOC) / L-16** | Acrescentar: "N3 (2027+): MOOC = 8% do presencial (CMTM08). Em 2026 (C5, pré-N3), MOOC monetizado a 0,8p fora de F, com base nacional igual a D11 de B; o zero de B é artefato da tabela de preços". | § 0; § 5.4 |
| **RMO-060 / L-01** | Resolver: texto, data de publicação (12/03/2026), revogação de N2 e vigência imediata confirmados; registrar as diferenças da tabela do § 0. | § 0 |
| **RMO-003 / RMO-P06** | Promover a defasagem a NORMATIVA: "matriz de um dado ano elaborada com dados da PNP do ano anterior" (N3, Anexo). | § 0 |
| **RMO-024 / L-11** | Atualizar a Tabela 6 para a redação de N3; manter a ambiguidade de 3,5 SM e de renda zero. | § 0 |
| **RMO-065 / L-21** | Registrar o art. 9º de N3 (prazo esgotado) e o novo art. 7º (referencial anterior + IPCA). | § 0 |
| **RMO-040 / L-06** | Elevar a evidência: C5 fecha F com 25%; o `/4` de B impede o fechamento. Classificar o `/4` como **anomalia operacional de B**. | § 5.3 |
| **RMO-033 / L-02** | Registrar a igualdade D7(B) = F(C5); rótulo "2025" obsoleto; B = fase anterior do exercício 2026. | § 5.2 |
| **RMO-017 / L-23** | Registrar que C5 aplica 0,5×IEA; manter a divergência textual aberta. | § 5.5 |
| **RMO-016** | Acrescentar a definição IEA = conclusão ÷ (conclusão + evasão) observada em C5. | § 3 |
| **RMO-059** | Acrescentar a base da Reitoria (inclui MOOC). | C5 H42 |
| **§ 4.1 D23** | "Y funciona como QTM em 100% dos ciclos". | § 5.1 |
| **§ 13.1** | Atualizar a prontidão (§ 13 abaixo). | — |
| **Estrutura** | Separar um apêndice "achados de auditoria da planilha B" (RMO-046, 049–052, 055 e afins) do catálogo de regras de domínio, sem renumerar. | § 2 |

---

## 11. Regras novas recomendadas

### 11.1. Domínio orçamentário (candidatas a RMO-066+)

Com base no § 6: RMO-P01 (RO-MT), P02 (MOOC 2026), P03 (IEA), P04 (degraus), P06 (defasagem), P07 (Reitoria), P08 (submontantes 2026), P09 (indicadores da Rede como dado observado) e P10 (DJ). **RMO-P05 só deve receber ID quando a definição for extraída da fonte**; até lá, registrar como lacuna.

### 11.2. Domínio estratégico do Prumo (série própria, sugerida RPE-xxx, não RMO)

| ID | Regra | Justificativa |
|---|---|---|
| RPE-01 | Indicadores institucionais são agregados como razão de somas de numeradores e denominadores dos campi; nunca como média de percentuais | Contexto § 13.3; evita erro em %CT, RAP e IEA |
| RPE-02 | Toda contribuição de campus é expressa como Δnumerador e Δdenominador do indicador-meta, com ano-base e exercício de efeito | Torna as contribuições comparáveis e agregáveis |
| RPE-03 | Toda meta institucional com limiar exibe a posição atual, a distância ao limiar, o próximo limiar abaixo (risco) e o valor condicional "mantidos os demais" | Degraus não lineares |
| RPE-04 | Conservação de coorte: ingressantes = ativos + concluintes + evadidos + transferidos ao longo do ciclo, por ciclo × ano | Consistência do motor de coortes |
| RPE-05 | Toda saída de cenário declara o estado (observado, projetado, decidido), a versão da regra, o exercício, a premissa de Rede e a premissa de ocupação | Princípio já registrado; torna-o verificável |
| RPE-06 | Cenário que aumenta MT sem aumentar matrícula técnica, conclusão ou atendimento de demanda exibe alerta de "ganho por volume" | Guarda-corpo anti-gaming |
| RPE-07 | Efeito orçamentário por campus só é exibido em R$ com regra interna versionada; caso contrário, apenas em participação e contribuição | Separação nacional × interna |
| RPE-08 | Um pacto registra: meta, contribuições por campus, premissas, responsável, data de revisão e indicador observado | Mínimo de governança |

---

## 12. Impacto das descobertas na arquitetura futura

1. **Motor de MT pequeno e determinístico.** RO-MT cabe em uma função pura por ciclo, com a versão de regra como parâmetro (`N2_literal`, `RO_2026`, futuramente `N3`). Não justifica um motor de regras genérico.
2. **A Rede como dado, não como modelo.** Importar por exercício: bases nacionais por situação, preços, submontantes e indicadores das 41 instituições (há fonte pública em C5). Cenários "demais constantes" e "tendência".
3. **Módulo de faixas** separado: funções de peso por indicador, versionadas, e cálculo de valor marginal de limiar (RMO-P04).
4. **Motor de coortes** como núcleo compartilhado: alimenta MT, %ME (quando RMO-P05 existir), RAP, concluintes e evadidos (IEA) e ocupação física.
5. **Camada de regras implementáveis** separada do dossiê: para cada regra, uma ficha de no máximo 15 linhas (fórmula, entradas, versão, testes), com links para a evidência.
6. **Testes de referência:** substituir T-M01/M02 por uma suíte RO-MT de cobertura total (B + C5), mantendo um teste de que N2 literal **diverge**, que documenta a fronteira texto × prática.

---

## 13. Matriz de prontidão por capacidade (revisada)

| Capacidade | v1.1.0 | Esta revisão | O que falta |
|---|---|---|---|
| Reproduzir monetização de B | PRONTA | PRONTA, com anomalias identificadas (`/4`, MOOC 0) | — |
| Calcular MT de ciclo existente ou nova oferta (regime 2026) | CONDICIONAL | **PRONTA como regra; CONDICIONAL na entrada QTM** | Projeção de ocupação e permanência; cadastro CHM/PC/agro/DJ do curso novo |
| Reproduzir AC de B integralmente | BLOQUEADA | **PRONTA (2026, operacional)** | Homologação Setec; N3 para 2027+ |
| Participação nacional de Funcionamento | CONDICIONAL | CONDICIONAL (bases da Rede 2026 disponíveis em C5) | Premissa de Rede para anos futuros |
| Valor de Qualidade do Ifes e degraus institucionais | CONDICIONAL | **PRONTA para 2026 em nível institucional** (C5 Indicadores) | N3 para 2027+ |
| Degraus de Qualidade por campus (contribuições) | — (não previsto) | **BLOQUEADA** | RMO-P05 (%ME, MEq RAP) e dados PNP por campus |
| Assistência Estudantil | CONDICIONAL | Sem alteração; **baixa prioridade** | — |
| Reitoria nacional | CONDICIONAL | CONDICIONAL (base inclui MOOC) | — |
| Distribuição interna Ifes | BLOQUEADA | BLOQUEADA | Ato interno |
| Fechamento nacional / conformidade vigente | BLOQUEADA | BLOQUEADA (sem valor decisório para o Ifes; **não priorizar**) | Bases nacionais por ciclo; N3 já obtida |
| Fatores de Funcionamento 2027+ (EAD, FP, MOOC) | BLOQUEADA (N3) | **PRONTA (N3):** 25% / 80% / 8% | MOOC dentro ou fora de F |
| Cenários plurianuais | CONDICIONAL | CONDICIONAL; calendário de efeitos definido (RMO-P06) | Séries de coorte; N3 |

---

## 14. Conclusão sobre a confiabilidade da fonte canônica

A fonte canônica v1.1.0 é **confiável quanto ao que afirma**. Não se encontrou afirmação factual falsa sobre B, N2 ou as fontes consultadas, e os limites declarados foram respeitados. É **incompleta e mal calibrada quanto ao que importa para o produto**:

- A regra central de projeção (MT) foi documentada na forma textual que **não** é aplicada. A forma aplicada, agora identificada, reproduz 100% dos ciclos de duas instituições.
- Evidências nacionais disponíveis em C5 resolviam várias lacunas P0/P1 (L-02, L-06, L-10, L-12, L-13, L-23) e não foram exploradas.
- As regras de maior alavancagem decisória (degraus de Qualidade, definição de %ME, MOOC 2026) estavam ausentes, enquanto achados de planilha ocupam parte relevante do catálogo.

**Veredito:** usar a fonte canônica como **dossiê de auditoria e rastreabilidade**, não como especificação. Antes de implementar, (1) incorporar as correções do § 10 e a tabela do § 0 (N3) numa versão 1.2.0 controlada, (2) extrair RMO-P05, (3) obter da Setec a memória de cálculo da matriz 2027 para confirmar se RO-MT e 0,5×IEA continuam sendo aplicados sob N3, cujo texto não os prevê, e (4) produzir a camada concisa de regras implementáveis (§ 12, item 5).
