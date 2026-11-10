# Prova de conceito do Prumo — portão de dados (formação técnica e RAP)

> **Situação em 10/11/2026.** Registro preservado como evidência. A conciliação de dados continua válida. A meta de 50% de formação técnica é um caso de uso entre outros. Ver a [visão de produto](../produto/visao-prumo.md).

## Atualização (09/11/2026): portão aprovado para percentuais legais; protótipo construído

O usuário forneceu a exportação dos **Indicadores de Gestão da PNP** (pasta local `indicadores-gestao/`, 93 MB, todas as instituições, anos-base 2017–2025; não versionada). Com ela:

| Teste | Resultado |
|---|---|
| Soma dos campi do Ifes, ano-base 2024 × valores da matriz 2026 | **Aprovado.** Técnico 0,4403 × 0,44; formação de professores 0,1206 × 0,1206; EJA 0,0186 × 0,0186. Na Rede, 31 de 37 instituições pareadas coincidem; as demais diferenças são de pareamento de nomes. |
| Professor-equivalente (denominador da RAP) | **Aprovado.** Ifes 1.520 × 1.517,5; 32 de 37 instituições a ±1%. |
| Numerador da RAP | **Não reconciliado.** Ifes 30.574 (PNP) × 27.539,39 (matriz); a razão varia de 1,00 a 1,56 entre instituições. Diferença de definição não identificada. RAP da PNP 20,11 × RAP da matriz 18,148. |
| Unidades | A matrícula equivalente de `PercentuaisLegais.csv` é 100 × a soma por curso de `DadosGerais.csv`, campus a campus, o que permite simular no nível do curso. |
| Eficiência acadêmica | O arquivo por campus inclui FIC (IEA do Ifes 0,708 × 0,4905 na matriz, que exclui FIC). Usada só na comparação, com o valor da matriz. |
| Convenção de ano | "Ano" no arquivo = ano-base. O ano-base 2025 (provável base da matriz 2027) também está disponível: técnico 45,05%, formação de professores 24,8%, EJA 1,98%. |

**Achado principal:**
- **Sem o Cefor, os campi do Ifes somam 50,95% de formação técnica em 2024.** O Cefor tem 14,7% da matrícula equivalente do Ifes, quase toda em especializações e FIC a distância, e leva o indicador institucional a 44%.
- **A mesma oferta sustenta a formação de professores.** Em 2025, o Cefor contabiliza 4.463 matrículas equivalentes nessa categoria, e o Ifes passa de 12% para 24,8%, acima da meta legal de 20%.
- **Chegar a 50% técnico exige converter ~2.240 matrículas equivalentes** não técnicas em técnicas, ou criar ~4.480 técnicas novas (2024).
- **Nos exemplos simulados com dados de 2024**, a expansão em quatro campi (240 estudantes) move o indicador +0,4 p.p.; reorientar parte da oferta EAD do Cefor move +2,3 p.p., com queda na formação de professores. Nenhum exemplo atinge 50%: a meta envolve uma decisão de portfólio institucional, não ajustes marginais.

**Protótipo:** [Prumo 50% Técnico](https://claude.ai/artifact/Ai7wKRGm3XP38DgJeM2WYQ), artifact privado; fonte em `poc/`:
- `extrair_dados.py` gera `dados-poc.json`, só com dados públicos da PNP e da matriz;
- `montar.py` gera `prumo-poc.html` a partir do template.

Etapas: comparar (Ifes × pares por porte, com meta legal, limiar da matriz e faixa PNP), simular (até 3 alternativas, decisões por curso e campus) e compor (contribuição de cada campus em p.p., proposta salva com premissas). Valores em reais são opcionais, só para 2024, no regime da matriz 2026 e com os demais constantes.

**Premissas declaradas na simulação:**
- A matrícula equivalente por estudante é a do próprio curso no ano escolhido.
- A participação da oferta não técnica na formação de professores é proporcional ao campus.
- A variação do numerador da RAP segue a razão atual do campus.
- A RAP da matriz é ajustada em proporção à RAP da PNP.

### Versão 2 do protótipo (após avaliação externa, 09/11/2026)

| Achado da avaliação | Correção |
|---|---|
| A interface usava a RAP da PNP (20,11) para indicar a faixa da matriz, cuja RAP é 18,148 | As duas RAPs aparecem separadas. A RAP da PNP é comparada só com a referência 20 do PNE; a da matriz aparece como fato observado (faixa 1, a 0,15 do limiar 18) e **não é estimada** nos cenários. A referência em reais exclui a RAP. |
| Formação de professores estimada pela proporção do campus | Removida a proporção. Decisões em cursos não técnicos mostram um **intervalo** (o curso conta ou não conta), com alerta. Verificação: a PNP não permite classificar por curso. A formação de professores inclui licenciaturas, parte das especializações e FICs, e há inconsistências (Piúma 2024: 208 ME em licenciatura e formação de professores zero). |
| Matrícula equivalente de novas vagas pela média do curso | Mantida, declarada como estimativa exploratória junto ao resultado e nos limites. |
| Três formulários simultâneos | Um cenário aberto por vez. Os demais aparecem como cartões-resumo (resultado e distância à meta). Decisões descritas em uma frase, editáveis sob demanda. Dois exemplos, com até três cenários. |
| Distância à meta pouco explícita | Frase de veredito ("Ainda faltam X p.p. para 50%. Esta combinação não alcança a meta.") e régua com a marca de 50%. |
| Narrativa "o Cefor reduz o percentual técnico" | Reescrita: "a composição das unidades afeta várias metas ao mesmo tempo". O Cefor responde por 25% da formação de professores do Ifes em 2024; a tabela por unidade mostra técnico e formação de professores lado a lado. |
| Salto da formação de professores (12,1% → 24,8%) | Sinalizado na etapa 1 como **provável mudança de classificação** (Cefor 1.132 → 4.463 ME com especializações em queda de 4.462 para 2.788; Vitória, Vila Velha e Cariacica também sobem). Confirmar com a Prodi antes de interpretar. |

Conferido no navegador: as três etapas sem erro de console. Resultados de exemplo (2024): expansão em dois campi +0,23 p.p. (faltam 5,7); reorientação parcial do Cefor +2,28 p.p. (faltam 3,7), com formação de professores entre 8,3% e 12,5%.

O texto abaixo é o registro original, anterior à obtenção dos dados.

---

> **Data:** 09/11/2026 · **Situação original:** portão **não aprovado**; prova de conceito suspensa até obter os dados indicados no § 4.
> **Escopo acordado:** caso de uso "aproximar o Ifes da meta de 50% de formação técnica"; indicadores simulados: percentual técnico (MeqCT) e RAP; 3 ou 4 campi; até 3 alternativas; um exercício de referência; benchmarking como porta de entrada.
> **Portão técnico:** reconstruir numeradores e denominadores oficiais **por campus** e agregá-los ao valor publicado para o Ifes (MeqCT 44%; RAP 18,148 = 27.539,39 MEq presenciais ÷ 1.517,5 professores-equivalentes, PNP usada na matriz 2026). Se não reconciliar, não compensar a diferença com fórmulas inventadas.

## 1. Resultado

| Item | Resultado |
|---|---|
| Acesso aos microdados da PNP (matrículas e servidores) | **Bloqueado.** Os arquivos ficam em `dadosabertos.mec.gov.br`, e o painel em `pnp.mec.gov.br` e `plataformanilopecanha.mec.gov.br`. Todos exigem verificação anti-robô (Cloudflare), que não deve ser contornada por automação. O catálogo do dados.gov.br lista microdados até a PNP 2024 (ano-base 2023); a edição 2025 (ano-base 2024), usada na matriz 2026, não aparece no catálogo. |
| Definição oficial dos indicadores | **Parcial.** Obtido o Guia de Referência Metodológica da PNP de 2018 ([cópia](../dominio/evidencias/2026-11-09/pnp-guia-referencia-metodologica-2018.pdf)), de edição antiga. |
| MeqCT do Ifes (44%) | **Não reconciliado.** Aplicando a definição do guia aos 2.322 ciclos da planilha, a participação técnica fica em ~60% (MeqCT ≈ 0,59–0,64 conforme a carga usada), longe de 44%. O fator de esforço de curso (FEC) não está na planilha, e a definição atual pode diferir. |
| Numerador da RAP (27.539,39) | **Próximo, não reconciliado.** A mesma definição, restrita a matrículas presenciais sem financiamento externo, dá 27.452 com a carga do ciclo (−0,3%) ou 25.629 com a carga de catálogo. Sem o FEC e a definição vigente, a proximidade pode ser coincidência. |
| Denominador da RAP (professor-equivalente) por campus | **Sem dados.** Depende dos microdados de servidores, bloqueados. |

## 2. O que o guia da PNP esclarece

As definições abaixo vêm do guia de 2018 e precisam ser confirmadas na edição vigente:

- **Matrícula equivalente:** `Meq = M × FECH × FEC × FNC`, contando só matrículas "Sem Programa Associado", ou seja, **sem financiamento externo**. M = matrículas ativas em ao menos um dia do ano.
- **FECH (fator de equiparação de carga horária):** FIC = CH ÷ 800; demais cursos = CH de referência ÷ (duração em anos, arredondada para múltiplo de 0,5, × 800). É diferente da equalização da matriz, que usa dias ativos.
- **FNC (fator de nível de curso):** técnico e FIC = 1; licenciatura, tecnologia e bacharelado = 20/18; especialização = 20/12; mestrado e doutorado = 20/8. Esse é o fator 20/18 citado no parecer. Ele **aumenta o peso das matrículas superiores no denominador** e explica parte da distância entre a participação técnica bruta e o MeqCT.
- **FEC (fator de esforço de curso):** dado do SISTEC, ausente da planilha.
- **MeqCT = Meq em cursos técnicos ÷ Meq total.** A agregação mínima é a **unidade (campus)**, então a decomposição por campus existe na fonte oficial.
- **Faixa da PNP para MeqCT:** meta 50%, faixa "adequada" de 45% a 55%, polaridade "quanto mais próximo do centro da meta, melhor". A PNP não trata 70% como melhor que 55%, enquanto a matriz dá peso 2 a partir de 60%. Essa diferença precisa aparecer no benchmarking (RPE-09).

## 3. Consequência para a prova de conceito

- Sem os dados oficiais por campus, a etapa "contribuições dos campi" exigiria números estimados a partir da planilha da matriz, que não reconciliam com a PNP. Isso violaria o portão. **Não construí o protótipo.**
- O **benchmarking entre instituições** não depende do portão. Os indicadores das 41 instituições para 2026 já estão no demonstrativo do IFMT (C5). Ele pode ser mostrado isoladamente, mas, sozinho, seria o "dashboard" que a concepção quer evitar.

## 4. O que destrava o portão (qualquer uma das opções)

| Opção | Ação | Quem | Esforço |
|---|---|---|---|
| A — Microdados oficiais | Baixar no navegador, passando a verificação, os microdados de **matrículas** e de **servidores** da PNP edição 2025 (ano-base 2024), além do Guia de Referência Metodológica vigente. Salvar em `dados-pnp/` na raiz do projeto, pasta que ficará no `.gitignore`. | Usuário | Baixo, se os arquivos existirem; arquivos grandes |
| B — Extração institucional | Pedir ao pesquisador institucional ou à Prodi do Ifes, por campus: Meq em cursos técnicos, Meq total, Meq presencial e professores-equivalentes, da PNP 2025. Com esses quatro números por campus, o portão se resolve somando e comparando com 44% e 18,148. | Usuário, Prodi | Baixo |
| C — Painel PNP | Exportar do painel da PNP, filtrado por unidade do Ifes, os indicadores MeqCT e RAP com numerador e denominador. | Usuário | Baixo a médio |

A opção B é a mais rápida e a menos sujeita a erro de reconstrução. A opção A permite simular no nível de curso.

## 5. O que será feito quando o portão passar

1. Somar os numeradores e denominadores por campus e conferir os valores do Ifes (44%; 18,148). Tolerância: diferença de arredondamento.
2. Escolher 3 ou 4 campi com perfis diferentes.
3. Construir o protótipo navegável (uma página):
   - **Comparar:** posição do Ifes entre as 41 instituições, com a meta legal, o limiar da matriz e a faixa da PNP.
   - **Simular:** até 3 alternativas, com premissas explícitas de alunos, carga horária, nível e docentes. Exemplos: ampliar turma técnica, converter FIC em técnico, contratar docentes.
   - **Compor:** contribuições por campus, efeito agregado em MeqCT e RAP, e salvamento do cenário com premissas e limitações. O valor em reais é opcional.
4. Teste de 15 minutos com gestores, usando os critérios de sucesso já acordados.

## Fontes consultadas

- [dados.gov.br — PNP Microdados Matrículas (PNP 2024, ano-base 2023)](https://dados.gov.br/dados/conjuntos-dados/plataforma-nilo-pecanha-pnp--microdados-matriculas)
- [dados.gov.br — Plataforma Nilo Peçanha (recursos 2017–2021)](https://dados.gov.br/dados/conjuntos-dados/mec-plataforma-nilo-pecanha-pnp)
- [Guia de Referência Metodológica da PNP, cópia Cefet-MG](https://www.audit.cefetmg.br/wp-content/uploads/sites/169/2022/07/GuiaPNP.pdf)
