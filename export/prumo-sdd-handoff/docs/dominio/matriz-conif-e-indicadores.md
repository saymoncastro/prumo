# Matriz CONIF e indicadores institucionais

> **Natureza:** síntese orientada a produto. **A referência normativa e de auditoria é a fonte canônica** [matriz-orcamentaria-v1.2.2.md](../../referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md) (75 regras RMO, 28 lacunas L). Quando uma regra é complexa, este documento cita o identificador e **não** a parafraseia; em caso de divergência, vale a fonte canônica, e a fonte canônica cede às normas que ela cita.
> **Validação:** nenhuma regra foi homologada por especialista de domínio (fonte canônica, § 0 e § 17.3). O que está "reproduzido" foi conferido contra demonstrativos de 2026, não contra o órgão que calcula.
> **Relacionados:** [glossário](glossario-e-modelo-conceitual.md) · [PNP](../inteligencia/exploracao-estrategica-pnp.md) · [fontes](../dados/fontes-qualidade-e-proveniencia.md) · [simulação](../simulacao/modelos-premissas-e-validacao.md)

Siglas de fontes (fonte canônica § 0.1): **N1** Decreto 7.313/2010; **N2** Portaria MEC 646/2022 (revogada); **N3** Portaria MEC 243/2026 (vigente); **A** livro da matriz (2025, cópia não versionada); **B** planilha da matriz do Ifes, 6ª fase (não pública); **C5** demonstrativo da matriz 2026 do IFMT (público); **C8** página de orçamento 2026 da PROAD/Ifes. Detalhe em § 10.

---

## 1. Finalidade e funcionamento geral

A Matriz CONIF (Matriz Orçamentária da Rede Federal) reparte um montante definido externamente entre as 41 instituições da Rede Federal e entre componentes, para "Outras Despesas Correntes e de Capital" (N1 art. 4º; RMO-001). O resultado é uma **referência de participação e de valor**: não é PLOA, LOA, liberação nem receita (RMO-005, RMO-058).

A participação de uma instituição depende do denominador da Rede. Exemplo conceitual da fonte canônica (§ 1, fictício): uma instituição com 20 numa Rede de 100 tem 20%; se passar a 30 e as demais ficarem constantes, terá 30/110 = 27,2727%, e não 30% (RMO-053).

## 2. Componentes

| Bloco | Regra geral | Unidade de cálculo | Referência |
|---|---|---|---|
| Assistência estudantil (AE) | Separada primeiro do orçamento total | Unidade acadêmica | RMO-023 a 027, RMO-064 |
| Funcionamento (F) | 0,8 × (orçamento total − AE) | Unidade acadêmica | RMO-004, RMO-006 |
| Reitoria (R) | 0,1 × (orçamento total − AE) | Instituição | RMO-059 (não determinada), RMO-071 (prática 2026) |
| Qualidade e eficiência (QE) | 0,1 × (orçamento total − AE) | Instituição | RMO-062 |

- **Submontantes de QE** (RMO-062, metodológica: corroborada pelo livro e por C5; nem N2 nem N3 os discriminam): eficiência acadêmica 0,25 QE; relação aluno-professor 0,25 QE; percentuais legais 0,5 QE, divididos em 0,7 / 0,2 / 0,1 entre técnico, formação de professores e EJA.
- **Fora do escopo da fonte canônica ou em aberto:** capital e folha (L-03); componentes históricos (RMO-028 a 032); fechamento nacional (L-16). A AE está documentada, mas classificada como de baixa prioridade decisória (fonte canônica § 13.1).

## 3. Medidas de matrícula e ponderações

**[PRINCÍPIO]** Três medidas **não se substituem** (RMO-007):

| Medida | O que é | Usada em | Derivável das outras? |
|---|---|---|---|
| **Matrícula física** | Vínculos (ciclos) ativos | PNP | — |
| **Matrícula equivalente (ME/Meq)** | Matrícula ponderada por fatores da PNP | Percentuais legais, relação aluno-professor | Não a partir da matrícula total (L-25) |
| **Matrícula total (MT)** | Unidade de matrícula ajustada pela matriz (carga transcorrida, dias, peso, bônus, retenção) | Funcionamento e Reitoria | Não a partir da ME |

No Ifes, ano-base 2024: percentual técnico de **44%** pela ME da PNP contra **57,8%** pela matrícula equalizada da planilha B; formação de professores 12,06% × 8,3%; EJA 1,86% × 1,64% (L-25, prioridade P0, **não determinada**).

**Matrícula total.** A regra que reproduz a prática de 2026 é a **RO-MT** (RMO-066, fórmula F-28, fonte canônica § 6.9). Ela reproduziu 2.322 de 2.322 ciclos da planilha do Ifes e 1.086 de 1.086 do demonstrativo do IFMT. A leitura literal do texto de N2/N3 (cadeia QTDC → CHMD → … → MT, RMO-061 e F-24, § 6.6) reproduz só 1.300 e 993 (L-24). Use as fórmulas da fonte canônica; não as resuma.

**Matrícula equivalente.** A fonte canônica não define o fator de esforço de curso. A definição usada nos estudos vem do Guia de Referência Metodológica da PNP de 2018 (Meq = M × FECH × FEC × fator de nível de curso) e do guia atual (ME = M × FECH × FEC, Portaria Setec/MEC 146/2021). **A fórmula mudou entre os anos-base 2020 e 2021**; a edição exata da mudança não foi confirmada ([PNP](../inteligencia/exploracao-estrategica-pnp.md) § 3). O nome do fator de nível aparece como "FENC" no manifesto de evidências e "FNC" no portão de dados: é o mesmo conceito, grafias diferentes.

**Ponderações** (N2 p. 123, mantidas em N3): referência de 800 horas/ano (RMO-008, RMO-014); pesos de curso 1 / 1,5 / 2 / 2,5 conforme número de laboratórios (RMO-009); piso de 1,5 para o integrado (RMO-010); bônus agropecuário de 50% (RMO-011); stricto sensu com peso final 3,75 (RMO-012); retenção conforme data-limite (RMO-015, RMO-035, RMO-073).

**Tratamento por tipo de oferta** (fonte canônica § 8):

| Oferta | Tratamento | Observação |
|---|---|---|
| EaD próprio / externo | Fatores 0,8 / 0,25 (RMO-013, RMO-067) | A planilha do Ifes aplica 0,0625 ao externo: anomalia (L-06) |
| MOOC | 8% sob N3 (RMO-067) | Em 2026: zero na planilha do Ifes; 0,8 fora de F no IFMT. Entrada no denominador não determinada (L-26) |
| FIC | Retido vale zero | |
| PROEJA | Duas categorias na planilha | Não estender automaticamente o piso do integrado |
| Formação de professores | A planilha calcula contribuição, não atendimento ao percentual legal | A PNP não classifica por curso |

## 4. Indicadores legais e de qualidade

**Metas legais × limiares orçamentários × metas pactuadas** (regra de produto RPE-09). São réguas diferentes e nunca se confundem:

| Indicador | Meta legal (Lei 11.892/2008, art. 8º) | Limiares orçamentários da QE (RMO-021, N2 tabelas 3–5, iguais em N3) |
|---|---|---|
| Técnico (%CT) | 50% | < 0,5 → 0; [0,5; 0,6) → 1; ≥ 0,6 → 2 |
| Formação de professores (%FP) | 20% | < 0,1 → 0; [0,1; 0,15) → 1; [0,15; 0,2) → 2; ≥ 0,2 → 2,5 |
| EJA | 10% | < 0,025 → 0; [0,025; 0,05) → 1; [0,05; 0,1) → 2; ≥ 0,1 → 2,5 |

As metas legais **não** constam da fonte canônica; estão na justificativa de RPE-09 (revisão crítica) e no documento fundador. Só no técnico o limiar coincide com a meta legal. A lei manda aferir os percentuais por aluno-equivalente (art. 8º, § 1º).

**Relação aluno-professor (RAP)** (RMO-019): < 18 → 0; [18; 20) → 1; [20; 22) → 2; ≥ 22 → 2,5.

**Eficiência acadêmica (IEA)** (RMO-016, RMO-017, RMO-068): definição operacional conclusão ÷ (conclusão + evasão), sem qualificação profissional; faixas relativas à média da Rede (fonte canônica, RMO-017). O primeiro ramo tem divergência entre texto e prática (L-23, § 8).

**Normalização e degrau.** Cada indicador × peso é normalizado pela soma da Rede e multiplicado pelo submontante (F-21 a F-23). O efeito de mudar de faixa, **mantidas as demais instituições**, segue RMO-069 / F-29. As faixas são descontínuas.

**Posição do Ifes na matriz 2026** (RMO-072, fonte C5; ano-base 2024): IEA 0,4905 (peso 1,5); RAP 18,148 (peso 1); técnico 0,44 (peso 0); formação de professores 0,1206 (peso 1); EJA 0,0186 (peso 0). Efeitos condicionais de mudar de faixa estão em V-13 da fonte canônica (ex.: técnico → 50%: +R$ 2.055.405; RAP abaixo de 18: −R$ 726.914, margem de 224,39 ME). São **referências condicionais**, não recursos (§ 9).

**Cadeia causal.** Matrículas → MT → Funcionamento; matrículas → indicadores PNP → faixas → QE. Como os percentuais legais e a ME da RAP **não** derivam da MT (L-25), o efeito de faixas por campus está bloqueado na fonte canônica (§ 13.1).

## 5. Regras por exercício e versionamento

**[PRINCÍPIO]** Nenhuma regra de um exercício é verdade permanente. Texto normativo e prática de cálculo são registrados separadamente.

| Ato | Situação |
|---|---|
| N1, Decreto 7.313/2010 | Base legal; art. 4º lido |
| N2, Portaria MEC 646/2022 | Republicada no DOU de 21/09/2022; revogada por N3 |
| N3, Portaria MEC 243, de 10/03/2026 | DOU de 12/03/2026, Seção 1, p. 63; lida de impressão da página web; **versão certificada não conferida** (L-01) |
| Portarias de 2021 (319, 277, 808, 79) | Citadas pelo livro; íntegras não verificadas |
| Portaria Setec/MEC 146/2021 | Definição da ME; não lida diretamente |

**O que N3 muda em relação a N2** (RMO-060): inclui formação de professores no art. 4º, V; cria o art. 7º (referencial do ano anterior + IPCA, RMO-074, alcance não determinado em L-27); explicita a defasagem (RMO-070); fixa MOOC em 8% (RMO-067); reescreve a tabela 6. Mantém blocos, percentuais, a cadeia textual da MT, pesos, faixas e o piso de campus novo.

**Exercícios:**

- **2026** é o caso operacional (ano-base 2024). A planilha do Ifes e o demonstrativo do IFMT foram elaborados **antes** de N3; não provam sua aplicação.
- **2027 em diante:** N3 se aplica, no mínimo, a partir da matriz 2027 (RMO-060). **Não há memória de cálculo de 2027** (L-24, L-26, L-27). Não se sabe se valerá o texto ou a prática de 2026.

**Divergências texto × prática em 2026:**

| Ponto | Lacuna | Situação |
|---|---|---|
| Produção da MT (limiar do ramo longo, carga, fator de dias, retidos) | L-24 (P0) | Divergente: a prática (RO-MT) reproduz os demonstrativos; o texto não. Detalhe em F-28 |
| Primeiro ramo do IEA (constante 0,5 no texto; 0,5 × IEA na tabela, no roteiro e em C5) | L-23 | Divergente; N3 repete |
| MOOC | L-26 | Não determinado |
| EaD externo a 0,0625 na planilha do Ifes | L-06 | Anomalia da planilha |

## 6. Defasagem entre ano-base e exercício

RMO-070 (normativa, N3, Anexo): a matriz de um ano usa dados da PNP do ano anterior, que retrata o ano-base anterior a esse. Na matriz de 2026, **exercício = ano-base + 2**, condicionado à manutenção do calendário da PNP; unidade autorizada depois da PNP entra no exercício seguinte (art. 8º, parágrafo único).

**Tensão registrada:** os §§ 10 e 13.2 da fonte canônica, escritos antes de N3, dizem que não há "regra eterna de dois anos", e o texto não foi harmonizado com RMO-070. O produto deve tratar a defasagem como **parâmetro por exercício**, não como constante.

Consequência para o gestor: uma turma iniciada em agosto conta cerca de 5/12 do ano-base; a evasão aparece no ano-base seguinte; o efeito chega ao exercício cerca de dois anos depois do ano-base.

## 7. Distribuição nacional × distribuição interna

- A matriz distribui **entre instituições**. Como cada instituição reparte entre suas unidades é regra própria.
- Na planilha do Ifes, as colunas por campus são **contribuição** ao total do Ifes, não repasse (RMO-043; L-07).
- **Ifes 2026** (fonte C8, PROAD, publicada em 01/04/2026, atualizada em 05/08/2026): custeio total de R$ 77.513.000,00 (Reitoria 11.705.437,42; Cefor 1.581.820,45; campi 64.225.742,13). Três campi novos receberam R$ 848.891,15 cada. A página descreve o método (piso e teto) sem fórmula nem parâmetros.
- Conciliação PROAD × planilha por universo comparável: −1,75% nos 21 campi consolidados; −0,4% nas 22 unidades comuns; +4,8% em todas as unidades menos a Reitoria.
- **"Matriz por campus com piso e teto" é hipótese forte, não regra reconstruída** (RMO-075, reclassificada para HIPÓTESE na v1.2.2; L-28). Cerca de R$ 4,3 milhões não correspondem aos blocos da matriz. Não se sabe se a QE fica na Reitoria.
- Para o produto: a regra interna é **configuração da instituição**, versionada e com fonte ([diretrizes SaaS](../arquitetura/diretrizes-saas.md) D4). Efeito em reais por campus só com regra interna versionada (RPE-07).

## 8. Divergências metodológicas conhecidas

| # | Divergência | Situação | Referência |
|---|---|---|---|
| 1 | MT: texto de N2/N3 × prática 2026 | Divergente; prática reproduzida | L-24, RMO-066 |
| 2 | Primeiro ramo do IEA | Divergente | L-23 |
| 3 | Percentuais legais e ME da RAP não derivam da MT; %CT do Ifes 44% (PNP) × 57,8% (planilha) | Não determinada | L-25 |
| 4 | **Numerador da RAP**: Ifes 20,11 na PNP (30.574 ÷ 1.520); 17,56 pela definição do guia (26.689 ÷ 1.520); **18,148** na matriz (27.539,39 ÷ 1.517,5). O denominador reconcilia; o numerador não | Irreconciliável sem a documentação do cálculo oficial | Estudo PNP § 5.5, T13; portão de dados |
| 5 | **IEA**: a série pública inclui FIC (Ifes 0,708); a matriz exclui (0,4905) | Não reproduzível pela PNP | RMO-068 |
| 6 | MOOC no denominador de F | Não determinada | L-26 |
| 7 | Alcance do art. 7º de N3 (IPCA) | Não determinada | L-27 |
| 8 | Defasagem "+2" normativa × "não é regra eterna" | Texto não harmonizado | RMO-070; § 6 |
| 9 | Distribuição interna do Ifes | Hipótese | RMO-075, L-28 |

### 8.1. Rótulo de versão da fonte canônica (1.2.0 × 1.2.2)

**Resolvido sem alteração normativa.** O cabeçalho da fonte canônica indicava 1.2.2, enquanto o § 0.3 e o README dos testes de auditoria diziam 1.2.0. O commit `693365b` (10/11/2026) alinhou os dois rótulos em 1.2.2 e acrescentou nota ao título do § 13.1 ("estado ativo da v1.2.0", mantido para não quebrar referências). Nenhuma regra, fórmula ou resultado mudou.

- **O que cada versão acrescentou:** 1.2.0 = revisão crítica e leitura de N3; 1.2.1 = distribuição interna PROAD (RMO-075, L-28); 1.2.2 = conciliação por universo comparável e RMO-075 reclassificada para HIPÓTESE. As versões 1.2.1 e 1.2.2 entraram juntas no commit `24a3036`.
- **Os 32 testes de auditoria foram escritos para a 1.2.0** e não ganharam teste novo na 1.2.1 nem na 1.2.2; o arquivo de resultado chama-se `resultado-testes-1.2.0.txt` por isso. Reexecutados em 11/11/2026: 32 de 32 passam.
- **Rótulos internos ainda desatualizados** (não alterados neste pacote, para não modificar o documento normativo): § 16 itens 2 e 8 ("RMO-001–065", "L-01–23"); § 6.1 ("27 famílias", contra 29 no § 17.1); § 17.2 ("19 testes"); corpo de RMO-060 e RMO-003/004 anteriores à leitura de N3; tabela de lacunas do § 14 partida por linha em branco e com L-28 antes de L-27.
- **Não confundir** com a versão 1.2.0 do Spec Kit usada no laboratório: coincidência de número.

## 9. Limites das projeções em reais

**[PRINCÍPIO]** Referência financeira é condicional e parcial: aparece por componente e por exercício, com as demais instituições constantes, nunca como receita do campus.

- Referência ≠ PLOA ≠ LOA ≠ execução (RMO-005, RMO-058).
- Projetar o denominador da Rede é hipótese (RMO-053, RMO-057).
- O "custo evadido" da planilha não é receita recuperável (RMO-055, L-19).
- Contrafactuais isolados não são crédito devido (fonte canônica § 6.7).
- A fonte canônica define **cinco níveis de saída** (§ 13): direto; relativo à Rede; condicionado a orçamento externo; hipótese; não estimável. Todo valor em reais no produto declara seu nível.
- Valor em reais do Funcionamento por campus está **fora de escopo** e foi descartado como porta de entrada: estimula volume de matrícula de baixo valor que dilui percentuais legais e RAP ([decisões](../decisoes/decisoes-hipoteses-e-pendencias.md)).

## 10. Rastreabilidade das fontes

Inventário completo, com URL, checksum e condição de distribuição, em [fontes, qualidade e proveniência](../dados/fontes-qualidade-e-proveniencia.md) § 2. Arquivos físicos preservados em [referencias/normas/](../../referencias/README.md).

## 11. Regras de produto derivadas da matriz (RPE)

Propostas na revisão crítica de 09/11/2026 (série própria, não normativa). Todas coerentes com os princípios da [visão](../produto/visao.md):

| Regra | Enunciado |
|---|---|
| RPE-01 | Indicadores institucionais agregam-se pela razão das somas, nunca pela média de percentuais |
| RPE-02 | Contribuição de campus = Δnumerador e Δdenominador do indicador-meta, com ano-base e exercício de efeito |
| RPE-03 | Meta com limiar mostra posição atual, distância ao limiar, próximo limiar abaixo (risco) e valor condicional "mantidos os demais" |
| RPE-04 | Conservação de coorte: ingressantes = ativos + concluintes + evadidos + transferidos, por ciclo e ano |
| RPE-05 | Toda saída de cenário declara estado (observado, projetado, decidido), versão da regra, exercício e premissas de Rede e de ocupação |
| RPE-06 | Cenário que aumenta MT sem aumentar matrícula técnica, conclusão ou atendimento de demanda exibe alerta de "ganho por volume" |
| RPE-07 | Efeito orçamentário por campus em reais só com regra interna versionada; sem ela, só participação e contribuição |
| RPE-08 | O pacto registra meta, contribuições por campus, premissas, responsável, data de revisão e indicador observado |
| RPE-09 | Toda meta é tipada (legal/institucional, limiar orçamentário, pactuada), com fonte própria; limiar nunca aparece como cumprimento da meta legal |
| RPE-10 | Toda contribuição registra custo, capacidade consumida e benefícios locais e institucionais; o pacto define a contrapartida |
| RPE-11 | Todo resultado é explicável: aponta dados (fonte, exercício), premissas, regra (versão) e decisões humanas |

## 12. Situação de validação

| Validado | Não validado ou hipótese |
|---|---|
| Leitura de N3 (sem versão certificada) | Homologação por especialista de domínio |
| Reprodução da MT de 2026 na planilha do Ifes e no demonstrativo do IFMT (RO-MT) | Regra de 2027 em diante |
| 32 testes de auditoria passam (dependem de arquivos não públicos) | RMO-057, RMO-075; distribuição interna |
| Conciliação dos percentuais legais e do professor-equivalente PNP × matriz 2026 | Numerador da RAP; IEA; cadastro agropecuário inferido |

**Recomendação herdada:** não retomar a auditoria forense da planilha da matriz. O retorno decisório é baixo; 20 das 65 regras da versão 1.1 tratavam de comportamento da planilha (revisão estratégica § 11).
