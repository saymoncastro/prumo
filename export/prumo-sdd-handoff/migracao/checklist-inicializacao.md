# Lista de inicialização do repositório definitivo

> Siga na ordem. Cada item tem um critério de conclusão verificável. Contexto: [guia SDD](../docs/sdd/guia-de-inicializacao.md) e [manifesto](manifesto-transferencia.md).

## A. Antes de criar o repositório

- [ ] **Decidir a visibilidade** (privado recomendado até decidir P-15): a fonte canônica da matriz contém agregados derivados da planilha não pública do Ifes, já públicos no laboratório. Ver [decisões](../docs/decisoes/decisoes-hipoteses-e-pendencias.md) P-15.
- [ ] **Decidir o destino do PR #5** (especificação 001) no laboratório: deixar aberto como registro, fechar sem integrar ou integrar. O rascunho já está preservado no pacote (P-16).
- [ ] **Nome do repositório.** "prumo" é nome provisório (P-11); não impede começar.

## B. Criar e copiar

- [ ] Criar o repositório vazio (sem README, licença ou `.gitignore` gerados pelo provedor, para não conflitar com o pacote).
- [ ] Copiar **o conteúdo** de `export/prumo-sdd-handoff/` para a raiz, incluindo `.gitignore` e `.editorconfig`, ou descompactar `prumo-sdd-handoff.zip` e mover o conteúdo da pasta para a raiz.
- [ ] Conferir integridade: `shasum -a 256 -c migracao/SHA256SUMS` → todas as linhas `OK`.
- [ ] Colocar a exportação da PNP em `data/pnp/indicadores-gestao/` e conferir os checksums de [data/README.md](../data/README.md).
- [ ] `git status` não lista nada em `data/pnp/`.

## C. Validar

- [ ] `node scripts/analises/motores-coortes-poc/recomposicao/testar_coortes.cjs` → "todas as verificações passaram" (6).
- [ ] `node scripts/analises/motores-coortes-poc/poc-002/testar_poc002.cjs` → "todas as verificações passaram" (16).
- [ ] `python3 scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py data/pnp/indicadores-gestao > /tmp/saida.txt && cmp /tmp/saida.txt scripts/analises/estudo-pnp/resultado-estudo-pnp.txt` → sem diferença (requer `openpyxl`).
- [ ] Links relativos dos documentos resolvem (os links internos de `referencias/` apontam para o laboratório; ver `referencias/README.md` § 7).
- [ ] Busca por segredos e caminhos absolutos sem ocorrências: `grep -rnE '/Users/|/home/|BEGIN (RSA|OPENSSH)|api[_-]?key' --exclude-dir=.git .`

## D. Primeiro commit

- [ ] Conteúdo: **exatamente o pacote** (README, `.gitignore`, `.editorconfig`, `docs/`, `referencias/`, `scripts/`, `data/README.md`, `migracao/`). Sem Spec Kit, sem `specs/`, sem `src/`.
- [ ] Mensagem sugerida: `Fundação: conhecimento consolidado do laboratório exploratório do PRUMO`, citando o commit de origem `f98a7b7` do repositório `saymoncastro/prumo` e esta branch de consolidação.
- [ ] A partir daqui, `migracao/` fica congelada (registro da transferência).

## E. Inicializar o Spec Kit (commit separado)

- [ ] Instalar a versão vigente do Spec Kit e conferir suas convenções (o laboratório usou 1.2.0, integração `claude`, scripts `sh`, numeração sequencial).
- [ ] Inicializar na raiz do repositório (ex.: `specify init --here --ai claude`; confira as opções da versão instalada).
- [ ] Conferir que a inicialização não sobrescreveu `README.md` nem `.gitignore`; mesclar as entradas que ela propuser.
- [ ] Commit: `Spec Kit: inicialização`.

## F. Princípios do projeto (commit e revisão próprios)

- [ ] Rodar `/speckit-constitution` com `referencias/sdd-laboratorio/constitution-v1.0.0.md` como entrada.
- [ ] Ajustar caminhos citados (visão → `docs/produto/visao.md`; fonte canônica → `referencias/fonte-canonica-matriz/…`; `poc/` → `referencias/prototipos/` e `scripts/analises/`).
- [ ] Acrescentar princípios de engenharia ([guia SDD](../docs/sdd/guia-de-inicializacao.md) § 2) e submeter ao idealizador.
- [ ] Registrar a ratificação em [decisões](../docs/decisoes/decisoes-hipoteses-e-pendencias.md) (P-17 → Decidido).

## G. Primeira especificação

- [ ] `/speckit-specify` com a jornada de decisão estratégica institucional, usando `referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md` como entrada.
- [ ] Confirmar com o idealizador D-08, D-09 e D-10 e decidir P-09 (segundo objetivo).
- [ ] `/speckit-clarify` e `/speckit-checklist` antes de qualquer plano.
- [ ] **Não** gerar outras especificações nem *backlog* antes de esta jornada estar navegável.
