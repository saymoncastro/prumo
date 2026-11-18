# Referências preservadas

> **Estes arquivos não são documentação canônica.** São evidências e registros históricos, copiados **sem alteração** do repositório exploratório (checksums abaixo) para que o projeto possa ser verificado sem acesso a ele. O conhecimento consolidado está em [docs/](../docs/produto/visao.md); se uma referência divergir de `docs/`, vale `docs/`, e a divergência deve estar registrada em [decisões](../docs/decisoes/decisoes-hipoteses-e-pendencias.md) § 4.
> **Links internos dos arquivos copiados** apontam para caminhos do repositório exploratório (ex.: `docs/analises/...`, `poc/...`) e **não funcionam aqui**. Isso é esperado; o § 7 traduz os caminhos.

## 1. Normas e documentos oficiais (`normas/`)

| Arquivo | ID | Origem | Versão / data | Finalidade | sha256 | Bytes |
|---|---|---|---|---|---|---|
| `portaria-646-republicacao.pdf` | N2 | Republicação no DOU nº 180 de 21/09/2022, Seção 1, pp. 122–125, via repositório do Cefet-MG: `https://www.audit.cefetmg.br/wp-content/uploads/sites/169/2022/09/MATRIZ-OR%C3%87-PORT-646-25AGO22-SETEC.pdf` | Revogada pela Portaria 243/2026 | Regime da matriz até 2025; texto das fórmulas | `cb56fcc25db01375e96ee1b62b37a8a0f774d4eaa105268486daef8b76f7b51c` | 3.255.634 |
| `portaria-243-2026-dou-impressao-web.pdf` | N3 | Impressão da página do DOU: `https://www.in.gov.br/web/dou/-/portaria-mec-n-243-de-10-de-marco-de-2026-692098706` (DOU de 12/03/2026, Ed. 48, Seção 1, p. 63) | Vigente; **não é a versão certificada** | Regime vigente da matriz | `6cb24f83928ecbf60da575d13b1cad7edce9f726306cf619b637ce14623fb02e` | 729.400 |
| `pnp-guia-referencia-metodologica-2018.pdf` | C9 | Guia de Referência Metodológica da PNP (MEC/Setec), via Cefet-MG: `https://www.audit.cefetmg.br/wp-content/uploads/sites/169/2022/07/GuiaPNP.pdf` | 2018, 98 p.; pode estar desatualizado | Definições de matrícula equivalente | `6f3cd9737ba11637d212c7cc930790a47610c4de626ad82c4855eb7b09dbb491` | 3.541.603 |
| `ifmt-matriz-2026.xlsx` | C5 | Demonstrativo público da matriz 2026 (PLOA) do IFMT: `https://docs.google.com/spreadsheets/d/1Y742qTN3Svetk9B2ggAefjKF8-rAjs8heIqJncXYwRE/export?format=xlsx` | Consulta de 08/11/2026 | Indicadores da Rede; reprodução da MT; numerador da RAP; usado pelo estudo da PNP (T13) | `b341f7a1e8a92bc510abd75058ec4396369d9725654c0d11e2e7e740bb66b9f3` | 366.321 |
| `proad-orcamento-2026.html` | C8 | Página "Orçamento 2026" da PROAD/Ifes: `https://proad.ifes.edu.br/orcamento-2026` | Publicada em 01/04/2026, atualizada em 05/08/2026; baixada em 09/11/2026 | Distribuição interna do Ifes | `bcb54f357be56841ee90e714b110cbb526235184c739a7e2c9a13aca4d0bd9a9` | 61.708 |
| `distribuicao-interna-ifes-2026.json` | C8 | Extrato da página acima | 09/11/2026 | Idem, legível por máquina | `b9460099479ab5427d06a99d7ae45616acfb96144f3a2493c6d869e0d4d3b827` | 2.364 |

**Por que cópia física:** as URLs são espelhos de terceiros ou exportações de planilhas que podem mudar ou sumir; os checksums permitem conferir que a regra foi lida do mesmo documento. Todas são publicações públicas. A página da PROAD contém um *token* CSRF de sessão do sistema de publicação, sem valor fora daquela sessão.

**Não copiados** (obter pela URL ou pelo registro): Decreto 7.313/2010; Lei 11.892/2008; Portaria Setec/MEC 146/2021; cadastro público de cursos do IFMT (C6); guia de orçamento da RFEPCT (C7, 16 MB, EduCAPES); livro da matriz (A, ISBN 978-65-89380-47-4). URLs na fonte canônica, § 0.1. **Não públicos, nunca copiar:** planilha da matriz do Ifes (B) e os arquivos de teste derivados dela.

## 2. Fonte canônica da matriz (`fonte-canonica-matriz/`)

| Arquivo | Origem | sha256 |
|---|---|---|
| `matriz-orcamentaria-v1.2.2.md` | `docs/dominio/matriz-orcamentaria.md`, commit `f98a7b7` | `11dc92ee5cdcd28b520873497e76a41b6a01c70ff5e02bb52268f15c6c91a74b` |

Dossiê de auditoria e rastreabilidade com 75 regras (RMO-001 a RMO-075) e 28 lacunas (L-01 a L-28). **É a referência normativa** citada por [Matriz CONIF e indicadores](../docs/dominio/matriz-conif-e-indicadores.md). Contém agregados derivados da planilha não pública do Ifes, já publicados no repositório exploratório ([fontes](../docs/dados/fontes-qualidade-e-proveniencia.md) § 7). Rótulos internos desatualizados: ver Matriz CONIF § 8.1.

## 3. Estudos (`estudos/`)

| Arquivo | Origem | Data | sha256 |
|---|---|---|---|
| `estudo-pnp-2026-11-10.md` | `docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md` | 10/11/2026 | `578c78c875f9f2a43c3c5eff64fd508d566d021d86e98c3b97bf453347936e45` |
| `portao-de-dados-2026-11-09.md` | `docs/analises/prumo-poc-portao-dados.md` | 09/11/2026 | `ae0dd81f68b5e8d277130010dd54f2c3ffe7eb9503cefb6dd035e03f8480e933` |
| `revisao-estrategica-2026-11-09.md` | `docs/analises/prumo-revisao-estrategica-oportunidades.md` | 09/11/2026 | `31026cf7f4d8fe67833489863ec9b9a1c20b8057499f272304c537f111a4600a` |

Preservados porque contêm as tabelas e os números que fundamentam valores de referência citados em `docs/`. Cada um tem, no topo, um aviso de situação de 10/11/2026. O portão de dados contém, abaixo da conclusão, o registro original com veredito oposto: vale a conclusão de cima.

## 4. Registro histórico (`historico/`)

| Arquivo | Origem | sha256 |
|---|---|---|
| `documento-fundador-v1.1.md` | `contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md` (08/11/2026) | `f1e9836b132821dd8245948df3eca1f7ea270e1bc69c08ecd8d8b8758384218e` |

Origem dos princípios e das questões abertas. **Substituído em escopo** pela [visão](../docs/produto/visao.md); não é documento de visão concorrente. Não há versão 1.0 no histórico do Git.

## 5. SDD no laboratório (`sdd-laboratorio/`)

| Arquivo | Origem | Situação | sha256 |
|---|---|---|---|
| `constitution-v1.0.0.md` | `.specify/memory/constitution.md` | Ratificado em 11/11/2026 (PR #4) | `04c3ad3b999807236349ff414c68524e7eb05fe9fdf4b73e002a0161fcb98ee4` |
| `spec-001-jornada-decisao-estrategica.md` | `specs/001-jornada-decisao-estrategica/spec.md`, branch `001-jornada-decisao-estrategica`, commit `0e90151` | **Rascunho**, PR #5 aberto | `920efc67e4a7952542791bde0629c7aad2e47e32b1e34cabedb58ab81bef8e90` |

**Entradas** para `/speckit-constitution` e `/speckit-specify` no repositório novo, não artefatos prontos. Ver [guia SDD](../docs/sdd/guia-de-inicializacao.md) §§ 2 e 4.

## 6. Protótipos (`prototipos/`)

Páginas HTML estáticas e autocontidas (dados e motor embutidos). Abrem direto no navegador; a única dependência externa é a folha de estilos do Google Fonts, com fontes de reserva. Registros ficam no `localStorage` do navegador.

| Arquivo | Protótipo | sha256 |
|---|---|---|
| `prumo-poc.html` | Meta de 50% de formação técnica (v2) | `77a5f44a9ca3bbd3f38af94e0759e8e9453ebe228be3d8cc2daf3a1177a4a64c` |
| `prumo-recomposicao.html` | Recomposição (Itapina e Barra de São Francisco) | `b401d6f4c1da626e98b527f208f27ab201475701a6e5a8d51ae816f645faa59d` |
| `prumo-poc-002.html` | POC 0.0.2 (Vitória e Serra) | `d82ded735566969e51ecc506223c0e907284e4a97665f69bc356b6e77c84e6a6` |
| `capturas-poc-002/1-comparar.png` … `5-como-calcula.png` | Capturas das cinco etapas da POC 0.0.2 | ver [manifesto](../migracao/manifesto-transferencia.md) |

**Referência de comportamento e experiência, não de código.** O que reaproveitar e o que não deve orientar a arquitetura de cada um: [aprendizados e limites das POCs](../docs/evidencias/aprendizados-e-limites-das-pocs.md) § 3.

## 7. Tradução de caminhos do repositório exploratório

| Caminho citado nos arquivos copiados | Neste repositório |
|---|---|
| `docs/produto/visao-prumo.md` | `docs/produto/visao.md` |
| `docs/dominio/matriz-orcamentaria.md` | `referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md` |
| `docs/dominio/revisao-critica-regras-prumo.md` | Sintetizado em `docs/dominio/matriz-conif-e-indicadores.md` (RPE) |
| `docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md` | `referencias/estudos/estudo-pnp-2026-11-10.md` |
| `docs/analises/prumo-poc-portao-dados.md` | `referencias/estudos/portao-de-dados-2026-11-09.md` |
| `docs/analises/prumo-revisao-estrategica-oportunidades.md` | `referencias/estudos/revisao-estrategica-2026-11-09.md` |
| `docs/analises/prumo-poc-002.md`, `prumo-avaliacao-prototipo-v2.md`, `prumo-plano-demonstracao-itapina.md` | Sintetizados em `docs/evidencias/aprendizados-e-limites-das-pocs.md` |
| `docs/produto/diagnostico-2026-11.md`, `docs/produto/proximo-passo.md` | Sintetizados em `docs/decisoes/` e `docs/evidencias/` |
| `contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md` | `referencias/historico/documento-fundador-v1.1.md` |
| `docs/dominio/evidencias/2026-11-08/`, `2026-11-09/` (normas) | `referencias/normas/` |
| `docs/dominio/evidencias/2026-11-10/` | `scripts/analises/estudo-pnp/` |
| `poc/coortes*.js`, `poc/testar_*.cjs`, `poc/dados-recomposicao.json`, `poc/dados-poc002.json` | `scripts/analises/motores-coortes-poc/` |
| `poc/*.html` | `referencias/prototipos/` |
| `indicadores-gestao/` | Externo; `data/pnp/indicadores-gestao/` (ignorado pelo Git) |
| `tests/auditoria_matriz/`, demais arquivos de `poc/`, `docs/dominio/auditoria-complementar-…`, cópias 1.0.0 e 1.1.0 da fonte canônica | Permanecem só no repositório exploratório |
