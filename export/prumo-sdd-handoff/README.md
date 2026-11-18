# PRUMO

**Plataforma de Resultados, Unidades, Metas e Ofertas** (nome provisório).

> Transformar evidências em decisões institucionais melhores, coordenadas e mensuráveis.

O PRUMO ajuda instituições educacionais multicampi, inicialmente da Rede Federal de Educação Profissional, Científica e Tecnológica, a compreender a trajetória da Rede, simular caminhos futuros para sua oferta de cursos e coordenar decisões dos campi para alcançar objetivos institucionais compartilhados. O Ifes é o primeiro contexto de validação; o produto é pensado para outras instituições.

## O problema

As metas de uma instituição multicampi (percentuais legais de oferta, participação na matriz orçamentária, eficiência, relação aluno-professor) só existem no agregado. As alavancas que as movem estão nos campi, que têm vocações e restrições diferentes. Os sistemas existentes otimizam a execução de uma estratégia de oferta já escolhida; falta o instrumento que ajude a escolher, comparar e coordenar essa estratégia.

## Três capacidades, uma finalidade

| Capacidade | Pergunta |
|---|---|
| **Inteligência estratégica** | O que podemos aprender com a trajetória da Rede Federal? |
| **Simulação estratégica** | O que pode acontecer se tomarmos decisões diferentes? |
| **Governança distribuída** | Como coordenamos escolhas locais para alcançar resultados institucionais? |

A **governança distribuída é a finalidade**: objetivos institucionais alcançados por contribuições diferentes dos campi, compostas, pactuadas, acompanhadas e revistas. A inteligência e a simulação fundamentam o que se pactua. Não há ordem obrigatória entre elas.

## Estágio

**Início do desenvolvimento por especificação (SDD).** A descoberta terminou num laboratório exploratório (08 a 11/11/2026). Não há sistema, especificação aprovada nem tecnologia escolhida. Este repositório contém só o conhecimento consolidado, evidências selecionadas e scripts de reprodução.

| Já demonstrado | Ainda hipótese |
|---|---|
| A soma dos campi na série pública (PNP) reproduz os percentuais legais da matriz de 2026 | Que gestores reconhecem o problema e usariam o produto (nenhum foi consultado) |
| A série 2017–2025 da Rede permite decompor trajetórias, dentro de blocos comparáveis | Que uma decomposição histórica muda decisões |
| Um motor simples de coortes reproduz técnicos integrados fora do ajuste com erro de 2% a 3% | Capacidade preditiva para graduação, ofertas novas e concomitantes |
| A regra praticada da matrícula total da matriz em 2026 foi reproduzida | A regra de 2027 em diante; a distribuição interna do Ifes |
| Contribuições de campi se decompõem e se compõem de forma exata | Pactuação, acompanhamento e revisão (nunca exercitados) |
| | Demanda comercial e modelo SaaS |

## Como navegar

| Para saber | Leia |
|---|---|
| **O que é o produto** (canônico) | [docs/produto/visao.md](docs/produto/visao.md) |
| O que está decidido, o que é hipótese, o que está pendente | [docs/decisoes/decisoes-hipoteses-e-pendencias.md](docs/decisoes/decisoes-hipoteses-e-pendencias.md) |
| Como começar a especificar | [docs/sdd/guia-de-inicializacao.md](docs/sdd/guia-de-inicializacao.md) |
| Jornadas e casos de uso | [docs/produto/jornadas-e-casos-de-uso.md](docs/produto/jornadas-e-casos-de-uso.md) |
| Vocabulário e modelo conceitual | [docs/dominio/glossario-e-modelo-conceitual.md](docs/dominio/glossario-e-modelo-conceitual.md) |
| Regras da Matriz CONIF e indicadores | [docs/dominio/matriz-conif-e-indicadores.md](docs/dominio/matriz-conif-e-indicadores.md) |
| Inteligência com a série histórica | [docs/inteligencia/exploracao-estrategica-pnp.md](docs/inteligencia/exploracao-estrategica-pnp.md) |
| Simulação: modelos e validação | [docs/simulacao/modelos-premissas-e-validacao.md](docs/simulacao/modelos-premissas-e-validacao.md) |
| Governança: metas, contribuições, pactuação | [docs/governanca/metas-contribuicoes-e-aprendizado.md](docs/governanca/metas-contribuicoes-e-aprendizado.md) |
| Fontes, qualidade e proveniência dos dados | [docs/dados/fontes-qualidade-e-proveniencia.md](docs/dados/fontes-qualidade-e-proveniencia.md) |
| Diretrizes para um produto multi-instituição | [docs/arquitetura/diretrizes-saas.md](docs/arquitetura/diretrizes-saas.md) |
| O que as provas de conceito ensinaram | [docs/evidencias/aprendizados-e-limites-das-pocs.md](docs/evidencias/aprendizados-e-limites-das-pocs.md) |
| Evidências preservadas (normas, estudos, protótipos) | [referencias/README.md](referencias/README.md) |
| Reproduzir resultados | [scripts/analises/README.md](scripts/analises/README.md), [data/README.md](data/README.md) |
| De onde veio cada coisa | [migracao/](migracao/manifesto-transferencia.md) |

**Hierarquia:** `docs/produto/visao.md` prevalece sobre todos os demais documentos. `docs/` é o conhecimento consolidado; `referencias/` é evidência e histórico, não canônico; `specs/` (a criar) conterá as especificações do Spec Kit; `src/` (a criar) conterá o código, conforme a arquitetura aprovada no plano da primeira especificação.

## Estrutura

```text
docs/          conhecimento consolidado (visão, domínio, inteligência, simulação, governança, dados, arquitetura, evidências, decisões, SDD)
referencias/   normas, fonte canônica da matriz, estudos, protótipos e artefatos SDD do laboratório, copiados sem alteração
scripts/       scripts de reprodução analítica (não é código de produção)
data/          dados externos não versionados (só o README é versionado)
migracao/      controle da transferência a partir do repositório exploratório
```

## Convenções

- **Uma visão.** Mudança de concepção se faz editando `docs/produto/visao.md` antes de qualquer especificação.
- **Todo número** indica natureza (fato, estimado, premissa, hipótese, resultado simulado, não estimado) e origem.
- **Só dados públicos no Git.** Dados históricos grandes ficam em `data/`, fora do versionamento.
- **Uma jornada por vez** no Spec Kit; nova especificação só depois da anterior navegável.
- **Protótipos e scripts não são base de implementação.**
