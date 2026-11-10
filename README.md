# PRUMO

**Plataforma de Resultados, Unidades, Metas e Ofertas.** Nome provisório.

O PRUMO ajuda instituições educacionais multicampi a compreender o comportamento da Rede Federal, descobrir oportunidades estratégicas, simular caminhos futuros e coordenar decisões locais para alcançar objetivos institucionais compartilhados. O Ifes é o primeiro contexto de validação.

**Estágio:** concepção. O repositório contém estudos, regras de domínio e provas de conceito. Não há sistema em produção nem especificação aprovada.

## Comece por aqui

| Para saber | Leia |
|---|---|
| O que é o PRUMO e para onde vai | [Visão de produto](docs/produto/visao-prumo.md): referência canônica |
| O que foi construído e o que cada coisa demonstrou | [Diagnóstico de 10/11/2026](docs/produto/diagnostico-2026-11.md) |
| Qual é o próximo passo | [Próximo passo](docs/produto/proximo-passo.md) |

Se dois documentos divergirem sobre o que o produto é, vale a visão de produto. Os demais são evidência e histórico.

## Mapa do repositório

### Visão e decisões de produto

| Documento | Papel |
|---|---|
| [docs/produto/visao-prumo.md](docs/produto/visao-prumo.md) | **Vigente.** Tese, capacidades, domínio, diretrizes de SaaS, limites, hipóteses |
| [docs/produto/proximo-passo.md](docs/produto/proximo-passo.md) | O que vem depois da consolidação |
| [.specify/memory/constitution.md](.specify/memory/constitution.md) | Princípios do projeto para o Spec Kit. Derivam da visão; se divergirem, vale a visão |
| [contexto_projeto_…_v1_1.md](contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md) | Documento fundador (08/11/2026). Origem dos princípios |
| [proposta_nome_prumo.md](proposta_nome_prumo.md) | Proposta de nome. Não oficializada |

### Domínio e regras de negócio

| Documento | Papel |
|---|---|
| [docs/dominio/matriz-orcamentaria.md](docs/dominio/matriz-orcamentaria.md) | Fonte canônica da Matriz Orçamentária da Rede Federal, v1.2.2. Dossiê de auditoria e rastreabilidade, não especificação |
| [docs/dominio/revisao-critica-regras-prumo.md](docs/dominio/revisao-critica-regras-prumo.md) | Revisão independente das regras. Contém as regras estratégicas de produto (RPE-01 a RPE-11) |
| [docs/dominio/auditoria-complementar-matriz-orcamentaria.md](docs/dominio/auditoria-complementar-matriz-orcamentaria.md) | Histórico da v1.1.0 |

### Dados e fontes

| Local | Conteúdo | No Git? |
|---|---|---|
| [docs/dominio/evidencias/](docs/dominio/evidencias/) | Por data: portarias, demonstrativo do IFMT 2026, página da PROAD, guia da PNP, cópias de versões anteriores da fonte canônica, scripts de reprodução e resultados. Cada pasta tem um `manifesto.json` | Sim |
| `indicadores-gestao/` | Exportação dos Indicadores de Gestão da PNP, 2017–2025, todas as instituições (93 MB) | Não. Pedir ao responsável |
| Planilha da matriz do Ifes e livro da matriz (raiz) | Fontes não públicas | Não |
| `tests/auditoria_matriz/*.json` | Casos de referência derivados da planilha | Não |

### Estudos e evidências

| Documento | O que estabeleceu |
|---|---|
| [Revisão estratégica](docs/analises/prumo-revisao-estrategica-oportunidades.md) | Onde está a alavanca de coordenação na matriz; oito oportunidades; riscos de concepção |
| [Portão de dados](docs/analises/prumo-poc-portao-dados.md) | A soma dos campi na PNP reproduz os percentuais legais da matriz de 2026 |
| [Estudo da PNP](docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md) | Série longitudinal da Rede: o que é comparável, o que não é, e quatro achados. |

### Provas de conceito

Páginas HTML estáticas, com dados públicos embutidos. Abrem direto no navegador. Nenhuma foi validada com gestores.

| Protótipo | Pergunta | Página | Documento |
|---|---|---|---|
| Meta de 50% técnico (v2) | Como os campi levam a instituição a uma meta agregada? | [poc/prumo-poc.html](poc/prumo-poc.html) | [Portão de dados](docs/analises/prumo-poc-portao-dados.md), [avaliação](docs/analises/prumo-avaliacao-prototipo-v2.md) |
| Recomposição | Como um campus recompõe sua oferta e o que negocia? | [poc/prumo-recomposicao.html](poc/prumo-recomposicao.html) | [Plano e resultados](docs/analises/prumo-plano-demonstracao-itapina.md) |
| POC 0.0.2 | Ampliar, aproveitar melhor ou reorganizar? | [poc/prumo-poc-002.html](poc/prumo-poc-002.html) | [Documento](docs/analises/prumo-poc-002.md) |

O que cada uma comprovou, e o que aproveitar de cada uma, está no [diagnóstico](docs/produto/diagnostico-2026-11.md#3-comparação-dos-protótipos).

## Reproduzir

```bash
python3 poc/montar.py
```

Remonta as páginas a partir dos templates e dos dados derivados versionados.

```bash
node poc/testar_coortes.cjs
```

Valida o motor de coortes da recomposição contra a série histórica.

```bash
node poc/testar_poc002.cjs
```

Valida o motor e os dados da POC 0.0.2.

Os passos abaixo dependem de arquivos locais não versionados:

| Comando | Precisa de |
|---|---|
| `python3 poc/extrair_dados.py`, `python3 poc/extrair_recomposicao.py` | `indicadores-gestao/` na raiz |
| `python3 poc/extrair_poc002.py <pasta>` | A mesma exportação, em qualquer pasta |
| `docs/dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py` | A mesma exportação |
| Testes em [tests/auditoria_matriz/](tests/auditoria_matriz/README.md) | Planilha da matriz e arquivos JSON de referência |
| `docs/dominio/evidencias/2026-11-09/reproduzir_revisao_critica.py` | Planilha da matriz |

## Convenções

- **Uma visão.** Mudança de concepção se faz editando a visão de produto, não criando outro documento de visão.
- **Análises datadas** ficam em `docs/analises/`. Recebem um aviso no topo quando deixam de refletir a visão vigente; não são reescritas.
- **Evidências** ficam em `docs/dominio/evidencias/<data>/`, com manifesto. Isso inclui scripts de reprodução de estudos.
- **Todo número** em documento ou tela indica se é fato, estimativa, premissa ou hipótese, e de onde veio.
- **Não mover** `poc/`, `tests/` nem `docs/dominio/evidencias/`: os scripts dependem desses caminhos.
- **Só dados públicos** entram no Git.
- **Especificações** seguem o Spec Kit: `.specify/` guarda princípios, modelos e scripts; `.claude/skills/speckit-*` guarda os comandos. Uma jornada por vez.

## Pendências de decisão

Ver [diagnóstico, § 7](docs/produto/diagnostico-2026-11.md#7-problemas-de-organização-do-repositório) e [próximo passo](docs/produto/proximo-passo.md).
