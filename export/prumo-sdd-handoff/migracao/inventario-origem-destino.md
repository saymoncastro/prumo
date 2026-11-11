# Inventário origem → destino

> **Escopo:** todo o material relevante do repositório exploratório `saymoncastro/prumo` (público), em todas as branches, worktrees e arquivos locais não versionados, auditado em 11/11/2026.
> **Referência:** `main` no commit `f98a7b7` (merge do PR #4), salvo indicação. Nenhum merge, exclusão de branch ou alteração de arquivo original foi feito.
> **Arquivos copiados** estão detalhados, com checksum e dependências, no [manifesto de transferência](manifesto-transferencia.md).

## 1. Estado do Git auditado

| Branch | Commit | Situação | Conteúdo fora da `main`? |
|---|---|---|---|
| `main` | `f98a7b7` | Base | — |
| `claude/prumo-pnp-exploratory-audit-aff2d0` | `19273c0` | Integrada (PR #1) | Não |
| `claude/prumo-poc-002` | `c80d2b5` | Integrada (PR #2) | Não |
| `claude/prumo-product-strategy-a30a61` | `0b32f95` | Integrada (PR #3) | Não |
| `claude/prumo-spec-kit` | `f98a7b7` local; `0b6bd44` remoto | Integrada (PR #4) | Não |
| `001-jornada-decisao-estrategica` | `0e90151` | **PR #5 aberto** | **Sim**: `specs/001-…/spec.md`, `checklists/requirements.md`, ajustes em README e próximo passo |
| `claude/prumo-knowledge-consolidation-4737ff` | `f98a7b7` + este pacote | Branch desta consolidação | Só `export/` |

Worktrees: o diretório principal e três worktrees em `.claude/worktrees/`. Nenhum com alteração versionada pendente; só arquivos ignorados (`.claude/launch.json`, `.specify/feature.json`, `.DS_Store`). Nenhuma entrada no *stash*. A versão 1 do protótipo da meta de 50% só existe no commit `a3b64df`.

## 2. Classificação

| Classe | Significado |
|---|---|
| **MIGRAR** | Copiado para o pacote, sem alteração ou com adaptação mínima declarada |
| **SINTETIZAR** | Conteúdo consolidado num documento novo de `docs/`; original não copiado |
| **MANTER COMO EVIDÊNCIA** | Copiado sem alteração para `referencias/`, como evidência não canônica |
| **ARQUIVAR NO ORIGINAL** | Permanece só no repositório exploratório; consultável lá |
| **NÃO TRANSPORTAR** | Não deve ir para o repositório novo (não público, gerado, ferramenta, local) |

Confiabilidade: **Alta** = verificado ou reproduzido em 11/11/2026; **Média** = documentado com fonte, não reverificado; **Baixa** = hipótese, superado ou com inconsistência conhecida.

## 3. Inventário

### 3.1. Concepção e produto

| Caminho original | Finalidade | Confiab. | Relação com a visão | Classe | Destino |
|---|---|---|---|---|---|
| `docs/produto/visao-prumo.md` | Visão canônica de 10/11/2026 | Alta | É a visão | SINTETIZAR | `docs/produto/visao.md` |
| `contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md` | Documento fundador v1.1 (08/11) | Média | Origem dos princípios; escopo superado | MANTER COMO EVIDÊNCIA + SINTETIZAR | `referencias/historico/documento-fundador-v1.1.md`; origem em `visao.md` § 2 |
| `proposta_nome_prumo.md` | Proposta de nome (08/11) | Baixa (§ 5 superado) | Nome provisório | SINTETIZAR | `visao.md` § 1; `decisoes` P-11 |
| `docs/produto/diagnostico-2026-11.md` | Retrato do repositório em 10/11 | Média (datado) | Fundamentou a visão | SINTETIZAR | `docs/evidencias/`, `docs/decisoes/` |
| `docs/produto/proximo-passo.md` | Decisões de 10/11 e entrada no Spec Kit | Alta | Decisões D-03 a D-06 | SINTETIZAR | `docs/decisoes/`, `docs/sdd/` |
| `README.md` | Navegação do laboratório | Alta | — | SINTETIZAR | `README.md` novo |
| `.gitignore` | Exclusão de fontes não públicas | Alta | — | SINTETIZAR | `.gitignore` novo |

### 3.2. Domínio da Matriz CONIF

| Caminho original | Finalidade | Confiab. | Classe | Destino |
|---|---|---|---|---|
| `docs/dominio/matriz-orcamentaria.md` (v1.2.2) | Fonte canônica: 75 RMO, 28 lacunas | Alta para 2026; não homologada | MIGRAR + SINTETIZAR | `referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md`; `docs/dominio/matriz-conif-e-indicadores.md` |
| `docs/dominio/revisao-critica-regras-prumo.md` | Revisão independente; regras RPE-01 a 11 | Média | SINTETIZAR | RPE em `matriz-conif-e-indicadores.md` § 11 |
| `docs/dominio/auditoria-complementar-matriz-orcamentaria.md` | Histórico da v1.1.0 | Baixa (superada em parte) | ARQUIVAR NO ORIGINAL | — |
| `evidencias/2026-11-08/portaria-646-republicacao.pdf` | Norma N2 | Alta | MIGRAR | `referencias/normas/` |
| `evidencias/2026-11-08/ifmt-matriz-2026.xlsx` | Demonstrativo C5 | Alta | MIGRAR | `referencias/normas/` |
| `evidencias/2026-11-08/cadastro-publico.xlsx` | Cadastro C6, auxiliar | Média | ARQUIVAR NO ORIGINAL | URL na fonte canônica |
| `evidencias/2026-11-08/manifesto.json`, `2026-11-09/manifesto.json` | Proveniência das evidências | Alta | SINTETIZAR | `referencias/README.md` |
| `evidencias/2026-11-08/matriz-orcamentaria-v1.0.0.md`, `2026-11-09/matriz-orcamentaria-v1.1.0.md` | Versões anteriores da fonte canônica | Baixa (superadas) | ARQUIVAR NO ORIGINAL | — |
| `evidencias/2026-11-08/alteracoes-rmo.json`, `resultado-validacao.json` | Diferenças 1.0→1.1; validação de hashes | Média | ARQUIVAR NO ORIGINAL | — |
| `evidencias/2026-11-09/portaria-243-2026-dou-impressao-web.pdf` | Norma N3 | Alta (não certificada) | MIGRAR | `referencias/normas/` |
| `evidencias/2026-11-09/pnp-guia-referencia-metodologica-2018.pdf` | Guia C9 | Média (pode estar desatualizado) | MIGRAR | `referencias/normas/` |
| `evidencias/2026-11-09/proad-orcamento-2026.html`, `distribuicao-interna-ifes-2026.json` | Fonte C8 | Alta | MIGRAR | `referencias/normas/` |
| `evidencias/2026-11-09/reproduzir_revisao_critica.py`, `resultado-revisao-critica.json` | Reprodução da revisão crítica | Alta (reproduz), depende de B | ARQUIVAR NO ORIGINAL | Citado em `docs/dados/` § 6 |
| `evidencias/2026-11-09/resultado-testes-1.2.0.txt` | Saída dos 32 testes | Alta | ARQUIVAR NO ORIGINAL | Resultado citado em `matriz-conif-e-indicadores.md` § 8.1 |
| `tests/auditoria_matriz/` (README e 4 scripts, 32 testes) | Prova executável da RO-MT e das faixas | Alta; depende de B | ARQUIVAR NO ORIGINAL | Citado em `docs/dados/` § 6 |

### 3.3. Estudos e análises

| Caminho original | Finalidade | Confiab. | Classe | Destino |
|---|---|---|---|---|
| `docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md` | Estudo da PNP, 14 tabelas | Alta (reproduzido); inconsistências de registro anotadas | MANTER COMO EVIDÊNCIA + SINTETIZAR | `referencias/estudos/estudo-pnp-2026-11-10.md`; `docs/inteligencia/` |
| `docs/dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py` | Reprodução do estudo | Alta | MIGRAR (caminhos adaptados) | `scripts/analises/estudo-pnp/` |
| `docs/dominio/evidencias/2026-11-10/resultado-estudo-pnp.txt` | Saída de referência | Alta | MIGRAR | `scripts/analises/estudo-pnp/` |
| `docs/analises/prumo-poc-portao-dados.md` | Conciliação PNP × matriz 2026 | Alta (conclusão de cima); registro original superado | MANTER COMO EVIDÊNCIA + SINTETIZAR | `referencias/estudos/portao-de-dados-2026-11-09.md`; `docs/inteligencia/` § 6 |
| `docs/analises/prumo-revisao-estrategica-oportunidades.md` | Revisão estratégica, oportunidades, riscos | Média (recomendações; §§ 12–13 rebaixados) | MANTER COMO EVIDÊNCIA + SINTETIZAR | `referencias/estudos/revisao-estrategica-2026-11-09.md`; `docs/governanca/`, `docs/evidencias/` |
| `docs/analises/prumo-avaliacao-prototipo-v2.md` | Avaliação do protótipo da meta de 50% | Média | SINTETIZAR | `docs/evidencias/` § 3.1 |
| `docs/analises/prumo-plano-demonstracao-itapina.md` | Plano e resultados da recomposição | Média; 3 números não reproduzíveis | SINTETIZAR | `docs/evidencias/` § 3.2; `docs/simulacao/` § 6 |
| `docs/analises/prumo-poc-002.md` | Documento da POC 0.0.2 | Alta (números reproduzidos) | SINTETIZAR | `docs/evidencias/` § 3.3; `docs/simulacao/` |
| `docs/analises/capturas/poc-002/*.png` (5) | Capturas da POC 0.0.2 | Alta | MANTER COMO EVIDÊNCIA | `referencias/prototipos/capturas-poc-002/` |

### 3.4. Provas de conceito (`poc/`)

| Caminho original | Finalidade | Classe | Destino |
|---|---|---|---|
| `poc/prumo-poc.html`, `prumo-recomposicao.html`, `prumo-poc-002.html` | Páginas montadas, autocontidas | MANTER COMO EVIDÊNCIA | `referencias/prototipos/` |
| `poc/coortes.js`, `testar_coortes.cjs`, `dados-recomposicao.json` | Motor da recomposição e único teste fora do ajuste de vários anos | MIGRAR (sem alteração) | `scripts/analises/motores-coortes-poc/recomposicao/` |
| `poc/coortes002.js`, `testar_poc002.cjs`, `dados-poc002.json` | Motor da POC 0.0.2 e 16 verificações | MIGRAR (sem alteração) | `scripts/analises/motores-coortes-poc/poc-002/` |
| `poc/*.template.html` (3) | Fonte das páginas | ARQUIVAR NO ORIGINAL | As páginas montadas contêm o mesmo código |
| `poc/extrair_dados.py`, `extrair_recomposicao.py`, `extrair_poc002.py` | Extratores PNP → JSON | ARQUIVAR NO ORIGINAL | Reproduzem byte a byte, mas são código exploratório com o Ifes fixo |
| `poc/montar.py` | Montador das páginas | ARQUIVAR NO ORIGINAL | — |
| `poc/dados-poc.json` | Dados do protótipo da meta de 50% | ARQUIVAR NO ORIGINAL | Embutido em `prumo-poc.html` |
| Commit `a3b64df` (v1 da meta de 50%) | Primeira POC, sobrescrita | ARQUIVAR NO ORIGINAL | — |

### 3.5. Spec Kit e agentes

| Caminho original | Finalidade | Classe | Destino |
|---|---|---|---|
| `.specify/memory/constitution.md` (v1.0.0) | Princípios ratificados no laboratório | MANTER COMO EVIDÊNCIA | `referencias/sdd-laboratorio/constitution-v1.0.0.md` (entrada para nova ratificação) |
| `specs/001-jornada-decisao-estrategica/spec.md` (branch `001-…`, `0e90151`) | Rascunho da primeira especificação | MANTER COMO EVIDÊNCIA | `referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md` |
| `specs/001-…/checklists/requirements.md` | Lista de qualidade do rascunho | ARQUIVAR NO ORIGINAL | Será regenerada |
| `.specify/` (scripts, modelos, integrações, fluxos) | Ferramenta Spec Kit 1.2.0 | NÃO TRANSPORTAR | Reinstalar com a versão vigente |
| `.claude/skills/speckit-*` | Comandos do Spec Kit para o agente | NÃO TRANSPORTAR | Gerados pela inicialização |

### 3.6. Dados e arquivos locais

| Caminho original | Finalidade | Classe | Destino |
|---|---|---|---|
| `indicadores-gestao/` (só no diretório principal, 18 CSV, 97 MB) | Exportação da PNP | NÃO TRANSPORTAR para o Git; **externo** | `data/pnp/indicadores-gestao/` (ignorado); manifesto com checksums em `data/README.md` |
| `6ª Fase - Participação matrículas totais 2026 IFES - cópia.xlsx` | Planilha da matriz do Ifes (B) | NÃO TRANSPORTAR | Não pública |
| `LIVRO-MATRIZ-NOVA-CONFIGURACAO.pdf` | Livro da matriz (A) | NÃO TRANSPORTAR | Obter pelo ISBN 978-65-89380-47-4 |
| `tests/auditoria_matriz/referencias.json`, `ro_mt_casos.json` | Casos derivados de B | NÃO TRANSPORTAR | Não públicos |
| `.claude/launch.json`, `.specify/feature.json`, `.DS_Store`, `.claude/worktrees/` | Estado local | NÃO TRANSPORTAR | — |
| Links para artefatos privados em claude.ai (no portão de dados) | Versões publicadas dos protótipos | NÃO TRANSPORTAR | Inacessíveis a terceiros; as páginas estão em `referencias/prototipos/` |

## 4. Verificações feitas durante o inventário

| Verificação | Resultado |
|---|---|
| Caminhos absolutos (`/Users/`, `/home/`) em arquivos versionados | Nenhum (só no ponteiro `.git` do worktree) |
| Segredos, senhas, chaves, *tokens* | Nenhum; um *token* CSRF de sessão na página salva da PROAD, sem valor |
| E-mails | Nenhum nos arquivos; só nos metadados dos commits |
| Dados pessoais | Nenhum; um autor de dissertação pública citado no documento fundador; nomes de campi e cursos |
| Dados derivados de fonte não pública | Agregados da planilha do Ifes na fonte canônica, na revisão crítica e nos testes, já públicos no laboratório (P-15) |
| Estudo da PNP | Reproduzido byte a byte, no laboratório e já no pacote |
| Testes dos motores | 6/6 e 16/16 passam, no laboratório e já no pacote |
| Extratores e montador das POCs | Reproduzem dados e páginas byte a byte (cópia descartável) |
| Testes de auditoria da matriz | 32/32 passam no diretório principal (com arquivos não públicos) |
| Checksums da PNP | Conferem com o manifesto de `data/README.md` |
