# Auditoria complementar da Matriz Orçamentária da Rede Federal

Consultas em **08/11/2026**; conclusão documental em **09/11/2026**, America/Sao_Paulo. Fonte canônica atualizada para **1.1.0**: [matriz-orcamentaria.md](matriz-orcamentaria.md). A [versão 1.0.0 integral](evidencias/2026-11-08/matriz-orcamentaria-v1.0.0.md) foi preservada; não havia histórico Git no diretório. Esta missão não implementou simulador, não alterou dados/fórmulas das planilhas e não modificou regras de produto.

## Resumo executivo

A auditoria avançou na base normativa e na reconstrução de matrículas, mas **não habilita um simulador orçamentário completo ou uma declaração de conformidade vigente**. A íntegra da republicação da Portaria nº 646/2022, incluindo Anexo, foi recuperada em repositório institucional do Cefet-MG. Também foram examinados um demonstrativo público do IFMT para 2026, seu cadastro público de cursos e um guia metodológico do IFPR. Esses materiais são identificados como fontes diferentes, sem transferir parâmetros ou homologações entre instituições.

Os principais resultados são:

- A cadeia de matrícula total de N2 foi recuperada. Doze amostras reais do Ifes foram reproduzidas sem AC como entrada; cinco contraexemplos foram preservados. Nova oferta pode ser analisada como **cenário condicionado**, sem promessa de reprodução oficial integral.
- N2 confirma faixas contínuas de RAPP e IAML, cinco faixas relativas de IEA, fórmula RIP, transição IDH/renda, atualização AE porIPCA/variação das matrículas e piso de campi novos. A validação é do regime identificado, não da norma posterior.
- A divisão de Qualidade em 25% IEA/25% RAP/50% IAML é corroborada por figuras de A e pela operação C5. Isso resolve a interpretação matemática dessa variante, mas não fornece um dispositivo de N3 ou uma homologação anual.
- O `/4` adicional do preço EAD de B continua divergente: N2 e C5 Funcionamento corroboram 25%, enquanto B monetiza 6,25%. O fechamento nacional não foi reproduzido por falta da base comparável e da memória anual.
- A íntegra da Portaria MEC nº 243/2026 continua inacessível. Data exata de publicação, vigência, dispositivos revogadores, anexos, transições e alterações não foram confirmados. Nenhuma regra foi atribuída a ela por inferência.
- Foi aberta **L-23**, conflito entre tabela/roteiro e primeiro ramo da equação IEA de N2. Não se escolheu uma interpretação oficial silenciosamente.

Entre as **22 lacunas originais**,4 foram resolvidas em alcance delimitado,14 parcialmente esclarecidas e 4 continuam abertas. Com a nova L-23, são **23 registros:4 resolvidos,14 parciais e 5 abertos**. Foram revisadas 32RMO existentes e adicionadas RMO-061–065. As19 referências automatizadas passaram, separando 8 testes operacionais,6 de dispositivos/metodologia identificados e 5 de hipóteses.

Aritmética de B com AC fornecida está **PRONTA**. MT de cenário N2, participações e referências financeiras são **CONDICIONAIS** a versão, entradas e premissas. Cálculo vigente integral, fechamento nacional e distribuição interna/valores efetivos do Ifes permanecem **BLOQUEADOS**.

## Escopo, fontes e procedimento

A versão anterior foi lida integralmente e confrontada por amostragem crítica com fontes e números. Mantiveram-se RMO-001–060, L-01–22, os exemplos V-01–10 e a separação normativa/metodológica/operacional. Correções foram localizadas no catálogo e nos quadros que dependiam delas. A versão anterior integral e os resumos antes/depois permitem recuperar os entendimentos substituídos.

| Fonte | Evidência obtida e uso | Limite |
|---|---|---|
| A — livro 2025 | Texto e figuras já inventariados, consultados nos pontos críticos: MT, qualidade, renda e história | Método/história; não norma automaticamente vigente. |
| B — sexta fase Ifes | Extratos de 23 ciclos,22 campi, fórmulas de ancoragem e monetização independente de 2.322 ciclos | AC, cadastros e totais nacionais importados, sem produtor; apenas Ifes. |
| N1 — Decreto7.313/2010 | Art.4º e distinção escopo/proposta/critério | Não fixa a fórmula detalhada dos componentes. |
| N2 — Portaria646/2022 republicada | [PDF institucional Cefet-MG](https://www.audit.cefetmg.br/wp-content/uploads/sites/169/2022/09/MATRIZ-OR%C3%87-PORT-646-25AGO22-SETEC.pdf?download=1),4 páginas DOU122–125; texto integral e tabelas/equações renderizadas examinados | Não se obteve original integral para diff. Assinatura criptográfica não foi validada; reprodução contém códigos impressos de autenticidade DOU. |
| N3 — Portaria243/2026 | [Link DOU](https://www.in.gov.br/web/dou/-/portaria-mec-n-243-de-10-de-marco-de-2026-692098706), título/objeto e pistas institucionais C1–C3 | Articulado e anexos não recuperados; conformidade atual não declarada. |
| C1 — [IFMT, Orçamento Anual](https://ifmt.edu.br/pro-reitorias/administracao/orcamento/orcamento-anual/) | Vincula demonstrativos, informa dados 2024/1 e 2024/2 para matriz 2026 e substituição de N2 | Página institucional é pista de versão, não dispositivo revogador. |
| C5 — [Matriz 2026/PLOA IFMT](https://docs.google.com/spreadsheets/d/1Y742qTN3Svetk9B2ggAefjKF8-rAjs8heIqJncXYwRE/edit) |11 abas: etapas de ciclo, rendas, AE/RIP, Reitoria e qualidade | Outro demonstrativo; preços/bases diferem de B. Índices institucionais fixos não substituem microdados PNP. |
| C6 — [cadastro público de cursos](https://docs.google.com/spreadsheets/d/1voCoeyf8ByxxhAvDihep-weld6XcpVxzYOAVffxOH5I/edit) | PLOA 2025 tem 16.108 registros com nome/tipo/eixo/peso/CH/agro; cotejo de flag sem usar AC | Não é cadastro homologado de B. Chaves ambíguas/ausentes; aba 2027 contém coerções de números em datas, não adotada. |
| C7 — [Guia IFPR/EduCAPES](https://educapes.capes.gov.br/bitstream/capes/1133623/2/GUIA%20DE%20OR%C3%87AMENTO%20RFEPCT.pdf) | Apoio às cinco situações temporais e aos componentes, especialmente pp.27–44 | Produto educacional, sem autoridade para substituir ato; contém imprecisões editoriais. |

As cópias N2/C5/C6, hashes e limites estão no [manifesto](evidencias/2026-11-08/manifesto.json). Os originais A/B foram preservados com os mesmos SHA-256. Arquivos novos são evidências públicas identificadas, não novas versões silenciosas da planilha fornecida.

A investigação de C5 não pressupôs identidade de fase com o Ifes. C5 usa preço presencial 1220,3527, frente a1220,3988573849524 em B; há diferenças de bases e montantes. C1 informa proposta nacional 2026 deR$ 2.951.996.744,68, distinta deD4 deB, R$ 2.803.219.878,73. São razões para exigir conciliação de versão, não autorização para substituir valores.

## Resultado das divergências

As quatro resoluções são **L-07, L-09, L-18 e L-19**. Encerram questões comprováveis de interpretação/dependência/estrutura; não significam que a planilha foi corrigida, que sua intenção institucional foi homologada ou que as capacidades correlatas ficaram integralmente prontas.

| ID / tema | Estado | Evidência/conclusão | Pendência necessária |
|---|---|---|---|
| L-01 — Íntegra/vigência de N3 | **Não determinada** | N2 foi recuperada integralmente, mas N3 não: DOU403/502; C1–C3 confirmam existência/substituição institucionalmente, sem dispositivos. Publicação exata, anexos, vigência, revogação, transição e alterações continuam sem leitura. | Íntegra oficial de N3 e atos posteriores; não declarar conformidade atual. |
| L-02 — Exercício, edição e parâmetros | **Parcialmente esclarecida** | B comprova período educacional 2024; C1 corrobora 2024/1–2024/2 na matriz 2026. core.xml de B registra modificação 25/02/2026, anterior à data do ato N3, sem provar elaboração/homologação. D4 continua rotulado proposta 2025 e difere da proposta nacional 2026 de C1. | Exportação/edição PNP e memória homologada de fase, exercício, D4/D5 e revisões. |
| L-03 — Capital e folha | **Permanece divergente** | N1 inclui outras despesas correntes e capital; N2 define objetivos, mas não reconcilia cada ação/natureza de B com a descrição restrita de A. Folha não é saída de B; frase de A não serve de classificação normativa. | Mapa de ações/naturezas e escopo por componente no exercício. |
| L-04 — Percentuais e bases de Qualidade | **Parcialmente esclarecida** | A figura 5 e C5 Cálculo Custeio corroboram 25/25/50 de QE, equivalente 2,5/2,5/5% do remanescente. N2 confirma normalizações/pesos internos 7/2/1; não explicita essa divisão monetária. | Homologação anual dos submontantes e confronto com N3; não usar o bloco inteiro por índice. |
| L-05 — Faixas contínuas de qualidade | **Parcialmente esclarecida** | N2 tabelas 1–5 resolve operadores/lacunas de A: IEA usa cinco faixas relativas à média; RAPP/CT/FP/EJA têm limites contínuos. Não há teto 100 para RAP. Nova L-23 impede resolver silenciosamente o primeiro ramo IEA; denominadores zero seguem sem regra oficial. | Homologar primeiro ramo IEA, universos e redistribuição zero; obter N3. |
| L-06 — Divisor adicional EAD | **Permanece divergente** | N2/C5 funcionamento sustentam 25%; B paga 6,25% e pondera denominador com 25%. C5 AE EAD tem/4 em base distinta, sem comprovar origem do/4 adicional de B. T-H05 quantifica efeito condicionado, sem fechar a Rede. | Memória de cálculo/versão e definição comparável das MT nacionais e de AC. |
| L-07 — Comentário por campus e denominador | **Resolvida com evidência** | Grafo e T-O05 comprovam AF/J como contribuição ao total do Ifes. A interpretação segura é explícita; não depende de confirmar intenção do autor. Comentário não foi editado, e política interna segue em L-15. | Nenhum bloqueio para interpretar/reproduzir o indicador; eventual correção visual é outra missão. |
| L-08 — Agro SIM em todos os ciclos | **Parcialmente esclarecida** | B!L altera AR/AS, não o cálculo já fixo de AC nem AE. C6 distingue agro; Agronomia/Agropecuária SIM e Biologia/Administração NÃO reproduzem amostras. Há chaves ambíguas/ausentes, e C6 não é cadastro homologado de B. | Cadastro agro da fase produtora do Ifes; não usar L universal para nova MT. |
| L-09 — AO, dias ativos e bissexto | **Resolvida com evidência** | N2/C5 distinguem FEDA do diagnóstico AO:183/366=0,5 para retidos em 2024; AO usa dia do ano de Q/365 e pode exceder 1. Grafo comprova que AO não produz AC/AE. A anualização 365 de carga tem função diferente. | Nenhum bloqueio semântico para separar principal/auxiliar; intenção do diagnóstico não foi homologada. |
| L-10 — Produção de AC/nova oferta | **Parcialmente esclarecida** | Cadeia integral de N2 recuperada, C5 traz etapas; T-M01 reproduz 12 amostras sem AC como entrada. T-M02 conserva cinco contraexemplos; exploração não FIC:1005 coincidem,55 divergem,207 sem chave unívoca em C6. | Fase produtora Ifes, cadastro da edição e regras de curtos/FIC/carga; N3 para uso atual. |
| L-11 — Renda, zero e limites | **Parcialmente esclarecida** | N2 tabela 6 corrige a última faixa de A para≥3,5, mas sobrepõe exatamente 3,5 à faixa anterior e exclui zero do primeiro intervalo. Roteiro usa proporções entre declarantes. C5 corrobora denominador/VR e normalização; não resolve microdados ambíguos. | Tabela/codificação homologada para zero,3,5 e nenhum declarante; N3 e base do exercício. |
| L-12 — CHM fixa e carga de integrado | **Parcialmente esclarecida** | N2 explica CHM ajustada ao catálogo e os ramos de FECH; C5 mostra CHM integrado específica, p.ex.3000 para catálogo 800, não fórmula universal. B tem 452 diferenças de MIN(S,T),83 U>S; a fórmula literal com U não reproduz todos os casos. | Cadastro CHM homologado, regra de teto/carga geral/oferta e memória por ciclo. |
| L-13 — Retenção, FIC e datas | **Parcialmente esclarecida** | N2 confirma cinco situações e duas metades de retidos; início antes do período não exclui regulares. C5 explicita 1095 dias; B FIC usaR=Q, sem fundamento de exceção localizado em N2. Três anos civis não são sempre 1095 dias. | Elegibilidade por tipo/oferta, calendário de retenção/curtos e ato/memória anual. |
| L-14 — AE completa e RIP | **Parcialmente esclarecida** | N2 p.125 confirma RIP proporcional por QRIP/ofício, IPCA+variação de matrículas, transição IDH e renda; C5 corrobora rateios e segrega modalidades. B não fornece bases/quantidades; /4 e seleção EAD de C5 não foram homologados para o Ifes. | Bases ME/renda/financiamento e RIP por ofício, universos e montantes anuais; N3. |
| L-15 — Reitoria e alocação interna | **Parcialmente esclarecida** | N2 define 10% e mesma base de Funcionamento; C5 operacionaliza proporção institucional×montante Reitoria. Atos internos do Ifes, reservas, complementos e ordem anual de rateio não foram obtidos. AF/J não são regra de transferência. | Ato e memória interna Ifes; base nacional/ajustes da Reitoria. |
| L-16 — Totais nacionais e fechamento | **Não determinada** | C5 contém outros parâmetros nacionais/índices, sem reconciliá-los a D9:D12 de B; C1 informa total nacional 2026 diferente de D4. Não há base nacional de ciclos, mesma edição, exclusões e homologação que permitam fechar a Rede. | Primeiro: definição/composição de D9:D12 e base nacional da mesma fase. Depois pisos, ajustes e resíduos. |
| L-17 — Precisão e resíduos | **Parcialmente esclarecida** | AC fixa tem quatro casas e B não arredonda nas fórmulas monetárias; T-H04 separa exibição de arredondamento. Comparação usa HALF_UP a quatro casas, que reproduz inclusive empate da linha 173; isso não comprova política oficial. | Regra upstream oficial de precisão, arredondamento/centavos e destino de resíduos. |
| L-18 — Filtros, H4 e cabeçalhos | **Resolvida com evidência** | Inspeção e fórmulas confirmam filtros de cabeçalho, CURSOS H4 vazio e critério tipo de curso sob rótulo oferta; total geral e visível têm semânticas diferentes. É diagnóstico delimitado, não erro oculto no fechamento recebido. | Nenhum bloqueio para documentar/reproduzir; arquivo original preservado. |
| L-19 — Custo Evadido e causalidade | **Resolvida com evidência** | T-O08 e exemplo linha 57 mostram AI>0 com Z=0/AE=0; AB não identifica evasão e o auxiliar não altera AC nem a Rede. Conclusão comprovada: não é receita recuperável nem contrafactual validado. | Novos estudos causais dependem de trajetória/contrafactual; não impedem interpretação segura do indicador atual. |
| L-20 — Origem dos indicadores | **Parcialmente esclarecida** | N2 define exclusões e a origem PNP; C5 disponibiliza índices institucionais fixos, sem eventos, coortes, docentes/filtros e metadados necessários para reconstruir a origem. Faixas/normalização não validam o índice de entrada. | Base/metodologia da edição PNP e universos; recálculo da origem ou indicadores anuais homologados. |
| L-21 — Pisos e transições | **Parcialmente esclarecida** | N2 arts.8º/9º documenta piso 700 mil por 5 anos e transição de 3 anos desdeLOA2023; C5 mostra aplicação particular. Isso não completa metodologias 2015–2021 nem autoriza prorrogar proteção após 2025 ou N3. | Autorizações/calendário, fontes históricas se necessárias e ordem de complementação/financiamento anual. |
| L-22 — Precisões editoriais/atualização | **Parcialmente esclarecida** | N2 identifica IPCA e variação de matrículas para AE; preserva-se rejeição das extrapolações de A sobre ganho real, datas e referências. Esses trechos não foram usados como fonte normativa; janelas/taxas anuais continuam ausentes. | Correção editorial e memória de atualização anual quando usada em cálculo. |
| L-23 — IEA: tabela/roteiro versus primeiro ramo da equação N2 | **Permanece divergente** | Nova questão: N2 tabela 1/roteiro exige peso 0,5×IEA abaixo de 0,9 m; a equação de p.124 imprime constante 0,5 nesse ramo. T-M04 demonstra diferença. C5 não comprova decisão oficial para B/N3. | Retificação/orientação oficial, memória anual ou decisão institucional identificada; não escolher ramo silenciosamente. |

## Mudanças nas regras

**32RMO revisadas:**003,004,006,008–027,033,038,040,049,050,055,056,059,060. O intervalo 008–027 inclui 20IDs. As demais 28 regras originais mantêm seus campos; referências gerais, índice e quadros foram atualizados quando necessário. O [registro por campo](evidencias/2026-11-08/alteracoes-rmo.json) identifica o núcleo das revisões; a versão 1.0.0 preservada permite comparação integral, incluindo exemplos e observações.

| RMO | Antes — v1.0.0 | Depois — v1.1.0 / fundamento |
|---|---|---|
|003–004 | N2 sustentada apenas por trechos indexados | Art.2º/3º e Anexo integral confirmados; edição PNP/cadastro anual continuam dependências. |
|006,008–013 | Descrições metodológicas de A | Reclassificadas NORMATIVAS no alcance dos dispositivos de N2:80/10/10,800 h, pesos, bônus e fatores EAD. Isso não confirma regime N3. |
|014 | CHM fixa, sem regra universal | N2 distingue CHM, CHC e ramos de FECH; fórmula literal e mínimo do auxiliar não são intercambiáveis; cadastro continua parcial. |
|015 | Retenção descrita e ICQA0,5; cadeia principal ausente | N2 demonstra FEDA 0,5 **e** QTM0,5, exclusão após três anos; operacionalização 1095 dias de C5/B e exceção FIC não equivalem automaticamente à norma. Reclassificada NORMATIVA no alcance delimitado. |
|016–017 | IEA de origem incompleto; quatro faixas ilustradas | Exclusões N2 identificadas; cinco faixas relativas à média, incluindo peso 1. Primeiro ramo ponderado tem conflito L-23. Ilustração de A preservada como variante. |
|018/020 | Normalização com ambiguidade do montante | N2 confirma rateios; C5 corrobora aplicação a submontantes 25%/25% deQE. Valores anuais/versão atual pendentes. |
|019/021/022 | Faixas descontínuas ou sem operadores em A | Tabelas/equações N2 confirmam intervalos contínuos e normalização separada dos marcos antes de 7/2/1. Reclassificadas NORMATIVAS nesse alcance. |
|023 | ME antes de peso/bônus, demais critérios incompletos | N2 delimita orçamento próprio e declarantes; C5 ajuda a separar modalidades; não usar MT monetizada como base AE. |
|024 | Faixa final/renda zero divergentes | N2 corrige parte da informação, mas também contém sobreposição em 3,5SM; renda zero e ausência de declarantes não resolvidas. |
|025 | Fórmula de A com “Orçamento IEA”, sem fechamento | Erro de A permanece documentado; VR/ID de N2 e normalização corroborada em C5 são novas variantes identificadas, sem substituir silenciosamente o orçamento. |
|026 | Índice de inflação desconhecido | IPCA e variação de matrículas confirmados em N2; janelas/taxas/ato anual ausentes. Reclassificada NORMATIVA nesse alcance. |
|027 | RIP NÃO DETERMINADA | Fórmula QRIP/ΣQRIP×AERIP confirmada, reclassificada NORMATIVA N2. Dados/versão Ifes continuam ausentes. |
|033/038 | Parâmetros e AC fixos como fronteiras | Mantidos; cronologia e fontes externas delimitam a reconstrução parcial e demonstram necessidade de conciliar fase/versão. |
|040 |6,25% observado sem fundamento do segundo divisor | Mantido como OPERACIONAL de B; contraste N2/C5 e impacto isolado documentados, sem alterar a fórmula. |
|049/050 | Auxiliares de calendário e não contabilizados | Grafo e N2 reforçam que não são produtores de AC;365 de AO difere de calendário de FEDA. |
|055 | “Custo Evadido” não comprova receita | Conclusão corroborada por caso real/algoritmo; L-19 encerrada nesse alcance. |
|056 | Transformação de nova oferta não determinada | Cadeia N2 recuperada,12 amostras e contraexemplos; reclassificada METODOLÓGICA quanto à capacidade aplicada/compatibilidade parcial. A regra normativa da cadeia é RMO-061. |
|059 | Reitoria/interno sem algoritmo | N2 e C5 sustentam nacional condicional; política interna Ifes continua não determinada. |
|060 | N3 não recuperada | Novas tentativas registradas; continua NÃO DETERMINADA. Recuperar N2 não encerra N3. |

**Cinco regras novas:** RMO-061 registra cadeia de MT N2;062, submontantes QE de A/C5;063, teste algébrico condicional de fechamento EAD;064, normalização AE corroborada por C5;065, piso/transição de N2. Classificações respectivas: NORMATIVA, METODOLÓGICA, DERIVADA, DERIVADA, NORMATIVA. O catálogo totaliza 65RMO; classificação não é medida de prontidão.

As23 famílias anteriores foram preservadas. F-24–27 acrescentam cadeia MT, submontantes QE, assistência e teste de fechamento EAD, com seu tipo de evidência. **F-X1 de A continua divergente e excluída da contagem.** O acréscimo não equivale a reconstrução integral do upstream de B.

## Auditoria normativa e temporal

A recuperação mais relevante foi a **republicação N2**, DOU180 de 21/09/2022, seção 1, pp.122–125. O aviso final informa original no DOU de 31/08/2022, pp.106–109, com incorreção. A data 25/08 é a do ato. O art.11 diz vigor na publicação; não foi produzida interpretação jurídica adicional sobre efeitos da republicação, pois falta o original integral para comparação literal. A referência parcial FNDE de 30/08 citada anteriormente não serve para datar a publicação original de N2.

| Marco | Evidência efetivamente disponível | Aplicabilidade e limite |
|---|---|---|
| 22/09/2010 — N1 | Decreto art.4º, proposta anual, outras despesas correntes e capital; critérios/Comissão | Marco de escopo; não fixa preço ou cadeia MT detalhada. |
| 25/08/2022 — data do ato N2 | Republicação integral informa a data; aviso final identifica original DOU31/08/2022, pp.106–109 | Data do ato não é publicação. A menção da v1.0.0 ao PDF FNDE de 30/08 não será usada para datar a publicação original. |
| 21/09/2022 — republicação N2 | DOU180, seção 1, pp.122–125; art.11: vigor na publicação; aviso de incorreção no original | Esta versão do texto foi lida integralmente. Sem a íntegra original, não se determinou quais palavras/equações mudaram na republicação, nem se atribuiu efeito temporal adicional. |
| LOA 2023 em diante no regime N2 | Art.9º: período de 3 anos para ajuste dos indicadores de instituições abaixo do referencial anterior; Anexo: transição AE até 2023 | Não prorrogar por inferência após 2025. IDH→renda chega a100% renda em 2024 no regime descrito. |
| Ano educacional 2024 | E3/F3 e datas dos ciclos de B; C1 descreve 2024/1 e 2024/2 para matriz 2026 | Ano-base confirmado no retrato; edição/exportação PNP específica não obtida. PNP2025 é hipótese cronológica plausível, não metadado confirmado de B. |
| Elaboração/proposta 2026 | Título de B; C1 proposta 2026 com dados 2024; C5 demonstrativo 2026 | B tem D4 rotulado proposta 2025; C1/C5 não homologa esse número. Proposta inicial, final e LOA devem ser conciliadas separadamente. |
| 25/02/2026,14:07:07Z — metadado de B | `docProps/core.xml`: modificação registrada, sem campo created | Sugere gravação anterior a N3, mas metadado editável não prova elaboração nem homologação. Não converter defaults de bibliotecas em data documental. |
| 10/03/2026 — data de N3 | Título oficial e C2; C1 a identifica como substituta/revogadora de N2 | Não confirmados texto, publicação exata, vigência, anexos, dispositivos revogados, transições ou exercício de aplicação. |
| 12/03/2026 — C3 | Encaminhamento da publicação no histórico de processo | É data de tramitação, não prova autônoma de data de publicação/vigência. |
| 08/11/2026 — consultas;09/11/2026 — conclusão documental | Fontes examinadas, manifesto, scripts/testes | Não se declara ausência de alterações posteriores por falta de resultado em busca; N3/atos subsequentes continuam dependência. |

| Elemento | Referência anterior A/v1.0.0 | Resultado com N2/C5; posterior N3 | Impacto RMO |
|---|---|---|---|
| Blocos e granularidade | A e trechos de N2 | N2 art.3º/Anexo confirma 80/10/10 após AE e níveis unidade/instituição; N3 não comparável sem íntegra | 004/006 |
| MT/retidos | AC fixo; cadeia incompleta | N211 passos recuperados, duas metades para retidos; equivalência B parcial; N3 desconhecida | 014/015/056/061 |
| Pesos/bonificação | A descrevia critérios | N2 p.123 confirma critérios, piso integrado e stricto 3,75; falta cadastro anual B; não comprovada mudança em N3 | 008–013 |
| EAD | A25%/80%; B6,25%/80% | N2/C5 funcionamento 25%/80%; divisor extra de B sem fundamento; não se atribui a N3 | 013/040/063 |
| IEA | Quatro faixas ilustradas de A | N2 cinco faixas relativas à média; equação do primeiro ramo conflita com tabela/roteiro; N3 desconhecida | 016–018; L-23 |
| RAPP/IAML | Figuras sem intervalos completos | Tabelas contínuas N2; normalização por indicador e pesos 7/2/1 confirmados; origem PNP anual pendente | 019–022 |
| Montantes de qualidade | Texto/figuras divergentes | A figura 5 corroborada por C5:25/25/50 de QE; N2 não discrimina essa divisão monetária | 018/020/062 |
| AE/renda | Figura15 insuficiente; índice inflacionário não conhecido | N2 identifica IPCA+variação, seleção por orçamento próprio, declarantes, ID_RPC; C5 corrobora normalização; limites de renda não todos resolvidos | 023–026/064 |
| RIP | Fórmula não determinada | N2 p.125 dá QRIP/ΣQRIP×AERIP; C5 reproduz; entradas Ifes ausentes | 027 |
| Reitoria | Base referida, algoritmo ausente de B | N2 mesma base de Funcionamento; C5 aplica proporção institucional; atos internos Ifes ausentes | 059 |
| Pisos e ajustes | Descrição histórica insuficiente | N2 arts.5º/7º–10: piso 700 mil/5 anos, transição 3 anos, revisão anual; nenhuma equivalência automática com piso atual | 065 |

A comparação anterior/posterior está limitada ao que foi efetivamente lido. N1 define escopo da proposta; N2 detalha cálculo; A descreve metodologia em 2025; B é uma implementação parcial com parâmetros importados. **Nenhuma alteração específica em bloco, peso, AE, Reitoria ou piso foi atribuída a N3 sem o texto.**

| Tentativa relevante | Resultado | O que permite concluir |
|---|---|---|
| N3 no DOU, URL principal e variante com download | Leitor web indisponível/502; obtenção direta 403 | Não permite ler artigos/anexos. |
| Busca pelo título exato, revogação, alterações e repositórios institucionais | C1/C2 identificam o ato e C3 registra encaminhamento; não foi localizada cópia integral recuperável | Confirma existência/objeto e pista de substituição, não vigência/dispositivos nem ausência de alteração posterior. |
| N2 no DOU/PDF oficial e espelho Cefet-MG | Acesso direto ao DOU falhou; espelho institucional recuperado com download | Permitiu ler a republicação inteira e identificar limites que antes faltavam. |
| Quarta fase IFMT2026 vinculada por C1 | Host proad e alternativa institucional retornaram conexão encerrada | Não é fonte efetivamente lida; C5 foi usado como outra evidência identificada. |
| Calculadora pública 2023 vinculada por C1 | Exportação respondeu 401 | Não acessada nem usada como prova; não houve tentativa de ultrapassar autenticação. |

**N3 — campos exigidos que continuam pendentes:** publicação exata; anexos; entrada em vigor; artigos revogados; transição; aplicabilidade por exercício; critérios/constantes e posteriores alterações. A tramitação de 12/03 não deve ser promovida a data de publicação. N2 arts.5º/10 também admitem análise/ajustes anuais: conhecer a portaria não substitui a deliberação da edição.

**Cronologia de B:** dados 2024 são demonstráveis; exercício 2026 é o título, corroborado por C1 para seu próprio processo. PNP2025 é hipótese compatível com o calendário, não exportação identificada. Modificação25/02/2026 no XML é anterior à data do ato N3, mas não prova elaboração/homologação e não afasta revisão posterior. Rótulo “proposta 2025”, parâmetros diferentes de C1/C5 e ausência de ato final impedem declarar B proposta homologada, distribuição final ou orçamento aprovado. Não se aplicou N3 retroativamente por inferência.

## Reconstrução de matrículas e auditoria crítica

A cadeia recuperada é `curso/oferta → cadastro CHM/PC/agro → ciclo/duração → anualização de carga → dias ativos no período → MECHDA → ponderação → bônus → MT`. Fatores monetários EAD são posteriores. Entradas/saídas, unidades, cinco casos e exceções estão autocontidos na fonte canônica§ 6.6/RMO-061; as amostras estão em V-11.

O ensaio de MT **não usa AC, AA, Z ou AR para obter o resultado**. AC só é confrontada ao final. Agro veio de chaves unívocas nome/tipo/eixo de C6, sem escolher a flag que melhor ajustasse o valor. Não se inferiu cadastro completo a partir da concordância matemática. Y de B foi tratado como QTM no ensaio de compatibilidade, sem considerar a coincidência uma prova de elegibilidade ou de origem da contagem. Mantêm-se CHM e peso como entradas fornecidas; produzir esses campos de uma nova oferta requer cadastro homologado.

T-M01 reproduz 12 casos: Agronomia com bônus/ingresso dentro do ano, Biologia retida, integrado Agropecuária, Tecnologia excluída por retenção, Mecânica com empate de precisão, Administração sem bônus, EAD UAB, dois mestrados profissionais, FIC longo e EAD próprio retido. T-M02 registra cinco falhas de equivalência literal: MOOC/FIC curto, Matemática com U>S, Edificações curto retido e dois Comércio curtos. Não se adotou ajuste ad hoc de FEDA, CHM ou bônus para fazê-los coincidir.

A linha 99 ilustra a primeira divergência de curto: com 20 h e 7 matrículas, FECH=20/800 e FEDA=31/366 dão MT0,0148224, enquanto AC=0,175. O valor recebido corresponde a7×20/800 nesse caso; isso é uma observação algébrica, **não uma regra geral confirmada de FIC**. Para linha 284, usar U literal produz 3,2473 frente a2,9530; substituir por mínimo altera o modelo e depende da memória de carga. A coluna U, por si, não resolve a cadeia.

Na exploração de 1.267 ciclos não FIC:1.005 coincidem,55 divergem,207 não têm chave agro unívoca no cadastro de comparação. São contagens exploratórias; não calculam taxa de legalidade, porque C6 é rotulado PLOA 2025 e a política oficial de precisão não foi obtida. A comparação de quatro casas usa HALF_UP explicitamente, incluindo o empate 1,40625→1,4063 da linha 173.

| Anomalia | Efeito principal demonstrável | Limite de conclusão |
|---|---|---|
| L-08, agro universal | L altera AR/AS e AI em certos ramos; não AC/AE já fixas. Cadastro externo diferencia agro em amostras | Não determina como a flag foi usada antes da produção de AC nem a lista completa correta de B. |
| L-09, AO/365 | Fator pode exceder 1; somente cadeia auxiliar | Não confundir com FEDA principal ou com 365 da anualização de carga. Intenção do diagnóstico não homologada. |
| L-12, CHM | U fixa,452 diferenças deMIN(S,T),83U>S; afeta reconstrução externa e auxiliares | Regra anual de carga de integrado/catálogo/teto ausente. |
| L-13, FIC/retidos | B FIC usaR=Q; outrosR=Q+1095. N2 usa três anos e duas metades de retidos | Exceção FIC e equivalência de calendário não comprovadas; curto não tratado por aproximação oficial. |
| L-19, AI | Positivo mesmo em ciclo excluído, com AEzero; sem vínculo causal AI→AC→orçamento | É diagnóstico de referência, não evasão observada nem ganho recuperável. |

**É possível calcular a MT de um novo curso?** Somente como cálculo condicionado a uma versão e entradas completas. A cadeia histórica N2 é conhecida; a passagem “novo curso/vagas” para QTM, cadastro e regras atuais não é automaticamente determinada. Para homologar o cálculo integral faltam: versão N3/anexos/ajustes anuais; fase produtora/cadastro do Ifes; regra de carga e curtos/FIC/retidos; precisão oficial; QTM elegível por coorte/período e calendário de incorporação. Até isso ocorrer, não há “reprodução oficial para qualquer nova oferta”.

A amostragem crítica também confrontou RMO-001/004/006 com dispositivos, RMO-017/019/021 com tabelas visuais, RMO-024/025 com renda/roteiro, RMO-027 com RIP e RMO-039–043/049/055 com fórmulas/números. Resultado: confirmou aritmética operacional e parte do texto metodológico, corrigiu fonte/classificação/faixas quando havia prova e conservou conflitos financeiros/temporais.

## Testes e evidências reproduzíveis

A [suíte](../../tests/auditoria_matriz/README.md) é pequena, determinística e separada do produto. Os extratos esperados foram lidos das fontes, vinculados por SHA-256 e não produzidos pelo algoritmo testado. Comandos a partir da raiz:

```sh
python3 -m unittest discover -s tests/auditoria_matriz -v
python3 tests/auditoria_matriz/verificar_fontes.py
```

| Tipo | Casos | Cobertura e resultado | Não comprova |
|---|---:|---|---|
| Operacional O01–O08 |8 | Preços, EAD, classificação, monetização,23 amostras,22 campi/total, denominador Ifes, ICQA, AO/bissexto, MOOC/AI; passaram | Produção de AC, conformidade N2/N3, receita. |
| Dispositivo/metodologia identificada M01–M06 |6 |12 coincidências MT, cinco contraexemplos preservados, faixas N2, conflito IEA, duas metades e exemplos de AE/RIP; passaram | Homologação do cadastro 2026, regime N3, curtos/FIC universais. |
| Hipótese H01–H05 |5 | Numerador/denominador, fechamento QE, declarantes/renda, zeros/precisão, resíduo EAD condicionado; passaram | Valores oficiais, taxas prospectivas ou garantia de repasse. |

O verificador adicional lê os arquivos sem salvar: confirma 23 extratos, fórmulas de ancoragem, hashes de evidências, monetização de 2.322 ciclos e totalizações dos 22 campi. A maior diferença entre aritmética decimal independente e valores salvos foi **R$ 0,0000000001507095028861**, efeito numérico muito abaixo de centavo. Esse valor não resolve política oficial de arredondamento/resíduos. O SHA-256 de B foi o mesmo antes/depois.

As49.583 fórmulas declaradas conferidas anteriormente permanecem no histórico da v1.0.0. Esta auditoria não apresenta aquela execução como novo teste: verificou amostras/famílias de risco, inventário e monetização por ciclo por outra rotina, preservando escopo e limites. Resultados finais estão em [resultado-validacao.json](evidencias/2026-11-08/resultado-validacao.json).

O teste do fechamento nacional EAD assume bases comparáveis. Seu resíduo éR$ 15.172.836,940377317; no contrafactual isolado Ifes, remover apenas o segundo/4 elevaria a referência emR$ 1.100.623,1242541133. **Não são diferenças de orçamento efetivamente devido.** Faltam composição dos totais nacionais, pisos, complementos e resíduos para fechar o bloco real.

## Prontidão para implementação e causalidade

| Capacidade | RMO | Dados necessários | Situação | Restrição |
|---|---|---|---|---|
| Reproduzir aritmética da sexta fase B | 033–052 | AC e parâmetros fixos de B, classificações literais | **PRONTA** | Mesmo retrato/mesmas entradas; preservar anomalias. Não certifica produção de AC nem metodologia vigente. |
| Recalcular valores por ciclo com MT fornecida | 037/039–041/043 | MT, categoria e preços versionados | **PRONTA** no modo B | Comportamento EAD6,25% e MOOCzero identificado como operacional. Não chamar de regra atual do MEC. |
| Calcular MT de nova oferta sob N2 | 007–015/056/061 | CHM/PC/agro homologados, datas, QTM elegível, versão, tratamento de curtos/retidos | **CONDICIONAL** | Cadeia recuperada e amostras; não generalizar a curtos/FIC/carga sem validação. Vagas→QTM é hipótese. |
| Reproduzir integralmente AC de B ou calcular MT oficial vigente | 056/060/061 | Fase anterior Ifes, cadastro da edição, N3/alterações | **BLOQUEADA** | Há contraexemplos; N3 inacessível. |
| Simular participação nacional de Funcionamento | 013/053/057/063 | Bases comparáveis por situação do Ifes e demais instituições, cenário de crescimento e versão | **CONDICIONAL** | Numerador e denominador devem variar juntos; base de B não é universo futuro homologado. |
| Simular Assistência Estudantil | 023–027/064 | MECHDA elegível, declarantes/renda, bases da Rede, RIP/ofícios, montantes por modalidade | **CONDICIONAL** para variante N2 sem ambiguidades | Renda0/3,5SM, /4 EAD e dados anuais precisam de decisão. Integral atual com B BLOQUEADA. |
| Simular Reitoria nacional | 004–006/059/065 | Referências de Funcionamento da mesma versão, montante Reitoria, pisos/complementos | **CONDICIONAL** | C5 corrobora proporção institucional; base anual/ajustes precisam de memória. |
| Distribuir internamente o orçamento do Ifes | 043–046/058–059 | Ato interno, reservas, fundos, prioridades e valores aprovados | **BLOQUEADA** | AF/J medem contribuição no retrato; não estabelecem repasse. |
| Simular Qualidade e Eficiência | 016–022/062 | Índices da mesma PNP e universo, média IEA, pesos e submontantes | **CONDICIONAL** | Normalizações documentadas; L-23 exige variante homologada; valores da origem e norma atual não certificados. |
| Projetar cenários plurianuais | 053/056–058/060–061 | Coortes, conversão de vagas, permanência/conclusão/retidos, outros IFs e regras por ano | **CONDICIONAL** como cenário | Não produzir previsão oficial sem séries, hipóteses e defasagens. |
| Estimar referência financeira | 005/039/053/057/062–064 | Participação comparável e montante conhecido ou assumido por componente | **CONDICIONAL** | Informar estágio, exercício e pressupostos; nunca equivaler automaticamente a LOA/receita. |
| Fechar toda a matriz nacional/validar conformidade vigente | 060/063/065 | N3/anexos/alterações, ciclos nacionais, parâmetros finais, pisos, resíduos e atos anuais | **BLOQUEADA** | Não resolvida pela coincidência financeira dos ciclos do Ifes. |

A cadeia estratégica precisa manter separados decisão, vagas, ingresso, estoque ao longo dos ciclos, medidas elegíveis, participação e valor. Conversão de vagas e permanência são hipóteses por coorte; não há taxa oficial implícita. O universo das demais instituições é entrada independente: aumento de MT do Ifes não fixa sua participação se a Rede também cresce. Em qualidade há limiares e exceções institucionais; não basta aumentar o numerador educacional.

Uma participação pode virar referência se o montante do mesmo componente/versão for conhecido ou assumido. Referência não é dotação aprovada, disponibilidade financeira ou repasse interno. Dados educacionais 2024 em uma matriz denominada 2026 indicam defasagem deste processo; não estabelecem prazo eterno de dois anos. Registrar ano da decisão, período de dados, edição PNP, exercício da matriz e estágio financeiro em cada cenário.

C5 lista 41 instituições na aba Indicadores, linhas 8–48, e totaliza na linha 50. Isso não prova que esse seja o universo exato dos totais D9:D12 de B ou do regime futuro. Não se completou o denominador com uma contagem genérica de instituições nem se importou o universo de C5 silenciosamente.

## Recomendações priorizadas e respostas finais

| Prioridade / natureza | Providência diretamente sustentada | O que libera |
|---|---|---|
| P0 — obtenção oficial | Recuperar N3/anexos/alterações com dispositivos, vigência/transição e aplicabilidade; comparar com N2 | Versão vigente de regras, hoje bloqueada. |
| P0 — obtenção e homologação da edição | Obter fase produtora AC/PNP e cadastro CHM/PC/agro do Ifes, memória do/4 EAD, parâmetros D4/D5/D9:D12, bases da Rede e fechamento | Equivalência MT, EAD e referências da fase; não basta reenviar AC pronta. |
| P0 — homologação específica | Resolver primeiro ramo IEA, renda 0/3,5/nenhum declarante, curtos/FIC/retidos e precisão/resíduos com fonte/decisão identificada | Algoritmos sem escolha arbitrária de variante. |
| P0 — dados de componentes | Obter indicadores PNP homologados/metadados, ME/renda/financiamento e ofícios RIP, submontantes finais, pisos/complementos | Qualidade, AE/RIP e Reitoria calculáveis para o exercício real. |
| P0 — política/finanças Ifes | Obter ato de rateio interno, reservas/fundos, autorizações de campi e conciliação proposta→LOA→execução | Alocação interna e referência conciliada ao orçamento efetivo. |
| P1 — implementação já delimitada | Pode começar reprodução da sexta fase, com versão B e avisos de alcance; também cenários parametrizados explicitamente condicionais após seleção de entradas/hipóteses | Trabalho seguro nas capacidades PRONTAS/CONDICIONAIS, sem implementar nesta missão. |
| P1 — dados prospectivos | Fornecer coortes, taxas de ingresso/permanência/conclusão, calendários e cenários da Rede/montantes | Projeções plurianuais defensáveis como cenários, não previsões oficiais. |
| Documental — concluída | Corrigir referências/faixas/alcances, indexar IDs, preservar v1.0.0, registrar fontes/testes/estados | Fonte auditável e navegável. Não há AGENTS.md aplicável no repositório/ancestrais; orientação canônica reforçada em§ 16.1. |

**P1. Outros agentes já podem implementar regras confirmadas com segurança?** Sim, no alcance e versão de cada RMO, com fonte e estado de validação registrados. A reprodução de B com AC fornecida está pronta; regras bloqueadas, normativas posteriores e escolhas ambíguas não devem ser codificadas como confirmadas. A suíte distingue observação, dispositivo/metodologia e hipótese.

**P2. É possível simular criação de novo curso nas matrículas da matriz?** Condicionalmente. A cadeia N2 e casos de referência permitem um cenário com QTM/coortes, calendário e cadastro explícitos. Não é possível obter MT oficial vigente de qualquer curso apenas de vagas/nome/carga: curtos/FIC/carga, edição e N3 continuam pendentes, com contraexemplos reais.

**P3. É possível converter MT em projeção defensável de participação do Ifes?** Sim, como cenário condicionado a mesma medida/versão em numerador e denominador, projeção explícita das demais instituições e tratamento dos componentes. Pode-se aplicar um montante conhecido ou assumido para estimar referência. Não é previsão de LOA nem de receita, e a divergência EAD/base nacional impede certificar fechamento real de B.

**P4. Bloqueios exatos do simulador completo?** N3/anexos/alterações e atos anuais; fase produtora/edição PNP e cadastros homologados; curtos/FIC/carga/retidos e precisão; fundamento do segundo/4 EAD e reconciliação nacional; dados/índices/montantes de qualidade, AE/renda/RIP e Reitoria; decisão sobre L-23 e fronteiras de renda; pisos/complementos/resíduos; política interna e conciliação LOA/execução; dados e hipóteses prospectivos por coorte/Rede. Cada dependência está vinculada a L/RMO na fonte canônica. Concluir esta auditoria não significa que esses bloqueios foram resolvidos.
