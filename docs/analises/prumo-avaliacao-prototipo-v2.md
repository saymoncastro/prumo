# Avaliação do protótipo Prumo v2 diante da visão do projeto

Data: 09/11/2026. Natureza: parecer de produto baseado no código e nos documentos locais; não é homologação de regras, decisão institucional ou implementação de uma nova versão.

## Parecer

O protótipo demonstra uma parte útil do problema: a composição das ofertas altera os indicadores institucionais e exige coordenação entre unidades. Ainda não demonstra a capacidade central proposta para o Prumo: comparar recomposições viáveis do portfólio educacional e pactuar contribuições diferentes dos campi, considerando consequências acadêmicas, financeiras, territoriais e temporais.

A distância apontada pelo usuário procede. Não se resolve acrescentando cartões ou mais indicadores ao mesmo formulário. É necessário mudar a decisão que organiza a experiência: de “quanto falta para 50% técnico?” para “qual combinação de ofertas atende melhor à missão e às metas, dentro dos recursos disponíveis, e como cada campus participa?”. Os 50% podem continuar como um caso de uso e uma restrição da comparação.

Há uma explicação documentada para a redução: o portão da prova de conceito acordou um recorte de percentuais legais, RAP, poucos campi e um exercício. Portanto, o protótipo não falhou em entregar tudo que esse recorte excluía. O problema é usar esse resultado como teste suficiente da tese mais ampla. A versão 2 corrige erros e melhora a comunicação, mas mantém o mesmo recorte decisório.

## Evidências e consequências

| Achado | Evidência local | Consequência |
|---|---|---|
| Recomposição do portfólio não está representada como operação | `poc/prumo-poc.template.html`, `renderEditor`, oferece ampliar técnico existente, reduzir oferta e ajustar docentes; `opcoesCurso` limita ampliação a técnicos já existentes | Não se pode propor novo curso, ampliar uma oferta não técnica, mudar turno/modalidade, substituir uma oferta com transição ou suspender novos ingressos preservando turmas existentes. Combinar redução e ampliação é uma aproximação aritmética de substituição. |
| Estoque de matrículas funciona como variável de decisão imediata | `simular` calcula `dme = q * x.me / x.matriculas` e altera o retrato do ano-base | Não distingue vagas, ingressantes, turmas e estudantes em curso. Reduzir ingressos futuros não equivale a retirar estudantes atuais do estoque. |
| Particularidades dos cursos foram comprimidas na média histórica | A extração guarda nome, tipo, oferta, presencialidade, matrículas equivalentes e alguns volumes; a simulação utiliza a razão equivalente/estudante | A média incorpora a composição histórica, mas não explica nem recalcula duração, calendário, pesos, financiamento e comportamento de novas coortes. Não permite avaliar uma oferta ainda inexistente. |
| Referência financeira é parcial | `reais` recalcula apenas CT e EJA no bloco de Qualidade; exclui Funcionamento, FP, RAP, IEA, custos e alocação interna | R$ 0 nos exemplos significa variação nula nesses dois subcomponentes, sob aquelas premissas. Não significa impacto financeiro total nulo. |
| Viabilidade não participa da comparação | Não há capacidade por área docente/turno, infraestrutura compatível, demanda ou custos no modelo de cenário | A alternativa com melhor percentual pode não caber no campus, não captar estudantes ou exigir recursos indisponíveis. |
| Horizonte não é projetado | Seleção entre retratos de 2024 e 2025, sem progressão de coortes | Não se mostram a convivência de turmas antigas e novas, o pico de recursos ou o momento da repercussão orçamentária. |
| Governança aparece como registro local | `proposta` e `localStorage` guardam nome, autor, justificativa e resultados | É um começo útil, mas não explicita recursos solicitados, contrapartidas, compromissos por campus, responsáveis e acompanhamento. O JSON salvo resume decisões em frases, sem guardar sozinho os insumos e versões necessários à reprodução integral. |

Referências de visão: documento fundador, §§ 0.1, 6–12; revisão estratégica, §§ 12–13. Referências quantitativas: fonte canônica, RMO-007–015, RMO-053, RMO-066–070 e § 13.1. Os documentos contêm atualizações sucessivas; este parecer usa o código da v2 e os quadros ativos, sem promover trechos históricos a estado atual.

## O que significa avaliar financeiramente cada curso

O curso é uma unidade importante do portfólio, mas o objeto de cálculo precisa distinguir curso, oferta em campus/turno/modalidade e coorte de ingresso. Duas ofertas com o mesmo nome podem ter condições e efeitos distintos.

É necessário separar quatro dimensões:

1. **Contribuição acadêmico-orçamentária:** medidas elegíveis por finalidade, carga de referência, duração, calendário, pesos aplicáveis, eventual bonificação, modalidade, fonte de financiamento e elegibilidade. Matrícula equivalente da PNP e MT da matriz não são medidas intercambiáveis.
2. **Efeito institucional:** mudança de participação relativa e dos indicadores de Qualidade, considerando a composição do Ifes e as premissas da Rede. Ganhos compartilhados por cruzamento de faixa não pertencem automaticamente a um único curso ou campus.
3. **Esforço financeiro e operacional:** investimento inicial, custeio incremental, pessoal necessário, técnicos, consumíveis, manutenção e recursos compartilhados. Separar custo atribuído ao curso de despesa adicional efetivamente causada pela decisão.
4. **Valor público e viabilidade:** demanda territorial, acesso, permanência, conclusão, formação de professores, EJA e demais compromissos institucionais; disponibilidade de docentes por área, ambientes e turnos.

“Retorno financeiro” deve ter seu significado explícito: contribuição à referência da matriz, efeito no orçamento institucional, possível alocação ao campus e custo da alternativa são resultados diferentes. Um curso de maior ponderação pode também exigir mais recursos. Não há evidência suficiente para ordenar cursos por uma rentabilidade única.

O protótipo deve mostrar valores observados, resultados condicionados a hipóteses e dimensões ainda não estimáveis. A regra interna de distribuição continua hipótese em aspectos relevantes do levantamento; não se deve atribuir ao campus um repasse automático derivado da contribuição à matriz.

## Próxima prova de valor recomendada

Preservar a conciliação dos dados, a distinção entre réguas, a decomposição institucional e os avisos de incerteza. Usar esses componentes em um recorte pequeno que contenha a cadeia decisória completa.

**Pergunta:** como um campus pode recompor sua oferta em um horizonte de quatro anos, e qual contribuição essa escolha permite negociar com o Ifes?

Selecionar um campus real, um conjunto pequeno de ofertas e três alternativas:

- **Manutenção:** manter o portfólio e projetar as coortes e recursos comprometidos.
- **Expansão:** ampliar uma oferta existente, com hipótese explícita de ocupação e permanência.
- **Recomposição:** suspender ou reduzir novos ingressos em uma oferta, concluir as turmas já abertas e iniciar outra oferta de forma gradual, condicionada às autorizações cabíveis.

Para cada alternativa, apresentar o portfólio antes/depois e, por período: vagas, ingressantes, estudantes ativos e concluintes; demanda docente por área; ambiente/turno crítico; investimento e custeio incremental; indicadores institucionais afetados; referência financeira parcial identificada por componente e exercício; premissas e dados pendentes. Detalhar apenas os recursos que limitam essas decisões, sem exigir um inventário institucional completo.

Depois, consolidar a proposta com pelo menos outro campus e registrar a contribuição negociada, os recursos solicitados, as contrapartidas propostas, o responsável e o indicador de acompanhamento. Fluxos sofisticados de aprovação podem esperar; a relação entre escolha local, recursos e compromisso institucional precisa aparecer já na demonstração.

Onde faltarem dados reais, aceitar premissas editáveis e sinalizadas para demonstrar o comportamento do produto. Esses resultados não validam uma decisão real. Separar a validação da experiência decisória da homologação dos cálculos.

**Critérios de aceite:** o gestor consegue identificar o que muda no portfólio; por que os cursos produzem efeitos diferentes; quando a mudança exige mais recursos e quando pode repercutir na matriz; o que o campus precisa para executá-la; e o que oferece em contrapartida ao objetivo institucional. A comparação admite alternativas que melhorem dimensões diferentes, sem impor uma recomendação automática baseada no percentual técnico.

## Problemas numéricos confirmados na versão atual

Além das limitações de produto, duas verificações executando a função `simular` original com `dados-poc.json`, no ano-base 2024, confirmaram:

- **Reduções repetidas não respeitam o saldo acumulado.** Três decisões de redução integral do mesmo curso não técnico do Cefor, cada uma de 3.499 matrículas, são aceitas. O estoque equivalente projetado da unidade passa de 5.532,0945 para −4.964,9055. O aviso emitido trata apenas da incerteza em formação de professores. Cada redução é limitada contra o retrato original, não contra o saldo após decisões anteriores.
- **Ampliação aceita quantidade negativa.** Na oferta técnica do Cefor, informar uma ampliação de menos duas vezes o estoque produz contribuição técnica da unidade de −222, ante 222 originais, sem aviso.

São reproduções do cálculo, não testes de navegação. Não houve alteração do protótipo nesta avaliação. Antes de usar seus resultados em uma demonstração decisória, validar sinais, limites acumulados, denominadores e consistência dos intervalos. Corrigir esses erros não resolve, por si só, o desvio de concepção descrito neste parecer.

## Fontes locais examinadas

- [Contexto fundador](../../contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md).
- [Revisão estratégica e oportunidades](prumo-revisao-estrategica-oportunidades.md).
- [Portão de dados e histórico da v2](prumo-poc-portao-dados.md).
- [Fonte canônica das regras da matriz](../dominio/matriz-orcamentaria.md), especialmente o quadro ativo de prontidão e as regras acima.
- [Revisão crítica das regras](../dominio/revisao-critica-regras-prumo.md).
- [Template do protótipo](../../poc/prumo-poc.template.html), [extração](../../poc/extrair_dados.py) e base `poc/dados-poc.json`.

## Complemento: ajustes à recomendação (09/11/2026)

A recomendação acima foi aceita, com quatro ajustes. O plano resultante está em [Plano da demonstração em Itapina](prumo-plano-demonstracao-itapina.md).

1. **Separar dados reais de premissas.** A exportação da PNP traz, por oferta e por campus, a série 2017–2025 de vagas, inscritos, ingressantes, matrículas e concluintes, além de turno, eixo e evasão. Turmas e procura devem vir desses dados. Custos e docentes só existem por instituição, e não há dado de laboratórios: entram como premissas editáveis e sinalizadas, limitadas aos recursos que restringem a decisão.
2. **Validar a projeção contra o passado (§ 15.5 do documento fundador).** Um modelo simples de coortes, calibrado com 2017–2021 e testado em 2022–2025 nas ofertas de Itapina, errou 2% a 3% nos técnicos integrados, 8% a 19% em graduação e conclusão de turmas, e 63% numa oferta recém-implantada. Os resultados devem aparecer em faixa quando o erro da classe de oferta for relevante.
3. **Avaliar oferta nova com parâmetros de oferta equivalente.** A relação entre matrícula equivalente e matrícula e a evasão podem ser tomadas do mesmo curso em outro campus do Ifes ou da Rede, identificadas como empréstimo, não como fator oficial.
4. **Mostrar quando cada efeito chega.** A matriz usa dados de cerca de dois anos antes do exercício: decisões com ingresso em 2027 aparecem por volta do exercício de 2029, e o pico de recursos vem antes. A distribuição interna continua sem regra validada (RMO-075) e não deve aparecer como receita do campus.
