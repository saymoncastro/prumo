# Manifesto de transferência

> **Documento de controle da migração** do laboratório exploratório `saymoncastro/prumo` para o repositório definitivo do PRUMO.
> **Gerado em:** 11/11/2026, na branch `claude/prumo-knowledge-consolidation-4737ff`, a partir da `main` em `f98a7b7` e da branch `001-jornada-decisao-estrategica` em `0e90151`.
> **Conferência de integridade:** todos os arquivos do pacote têm sha256 em [SHA256SUMS](SHA256SUMS). Na raiz do repositório novo: `shasum -a 256 -c migracao/SHA256SUMS`.
> **Independência:** nenhum arquivo do pacote depende de caminho absoluto do computador de origem. A única dependência externa é a exportação da PNP, descrita em [data/README.md](../data/README.md).

## 1. Documentos novos (escritos nesta consolidação)

Sem checksum aqui: são documentos vivos, que passam a evoluir no repositório novo. Origem de cada um no [inventário](inventario-origem-destino.md).

| Destino | Tipo | Finalidade | Fontes sintetizadas | Atualização prevista |
|---|---|---|---|---|
| `README.md` | Porta de entrada | Navegação e estágio | README, visão, diagnóstico | A cada mudança de estágio |
| `docs/produto/visao.md` | **Canônico** | Visão do produto | Visão de 10/11; documento fundador; proposta de nome | Só por decisão de concepção |
| `docs/produto/jornadas-e-casos-de-uso.md` | Domínio | Jornadas fundamentais | Visão de 10/11 § 6; fundador § 16–17; revisão estratégica; POCs | Ao especificar cada jornada |
| `docs/dominio/glossario-e-modelo-conceitual.md` | Domínio | Vocabulário e relações | Visão de 10/11 § 7; fonte canônica; fundador § 7, § 18 | Ao surgir conceito novo |
| `docs/dominio/matriz-conif-e-indicadores.md` | Domínio | Síntese da matriz | Fonte canônica 1.2.2; revisão crítica; portão de dados | A cada portaria ou exercício novo |
| `docs/inteligencia/exploracao-estrategica-pnp.md` | Domínio | Inteligência longitudinal | Estudo da PNP; portão de dados | A cada edição da PNP |
| `docs/simulacao/modelos-premissas-e-validacao.md` | Domínio | Simulação e validação | Motores, testes e documentos das POCs; estudo da PNP | Ao especificar o motor |
| `docs/governanca/metas-contribuicoes-e-aprendizado.md` | Domínio | Governança distribuída | Visão de 10/11 § 4.4; fundador § 13; revisão estratégica; RPE | Ao especificar pactuação |
| `docs/dados/fontes-qualidade-e-proveniencia.md` | Domínio | Fontes e linhagem | Manifestos de evidência; estudo da PNP; verificação de 11/11 | A cada fonte nova |
| `docs/arquitetura/diretrizes-saas.md` | Princípios | Diretrizes multi-instituição | Visão de 10/11 § 8; princípios v1.0.0 | No plano de cada especificação |
| `docs/evidencias/aprendizados-e-limites-das-pocs.md` | Histórico | O que a exploração ensinou | Diagnóstico; documentos das POCs; avaliação v2 | Estável |
| `docs/decisoes/decisoes-hipoteses-e-pendencias.md` | Controle | Decidido / hipótese / pendente | Próximo passo; visão; rascunho 001; esta auditoria | A cada decisão |
| `docs/sdd/guia-de-inicializacao.md` | Método | Início do SDD | Próximo passo § 3; princípios v1.0.0; rascunho 001 | Depois da primeira especificação |
| `referencias/README.md`, `scripts/analises/README.md`, `data/README.md` | Índices | Uso das referências, scripts e dados | Manifestos de evidência | Ao acrescentar arquivos |
| `.gitignore`, `.editorconfig` | Configuração | Exclusão de dados e segredos; formatação | `.gitignore` do laboratório | Ao escolher a tecnologia |
| `migracao/*` | Controle | Esta migração | — | Congelar depois do primeiro commit |

## 2. Artefatos copiados

**Confiabilidade:** Alta = verificado em 11/11/2026; Média = documentado, não reverificado.

### 2.1. Normas e fontes oficiais

| Destino | Original (commit `f98a7b7`) | Tipo | Confiab. | Dependências | sha256 |
|---|---|---|---|---|---|
| `referencias/normas/portaria-646-republicacao.pdf` | `docs/dominio/evidencias/2026-11-08/portaria-646-republicacao.pdf` | PDF | Alta (checksum = manifesto de 08/11) | — | `cb56fcc25db01375e96ee1b62b37a8a0f774d4eaa105268486daef8b76f7b51c` |
| `referencias/normas/portaria-243-2026-dou-impressao-web.pdf` | `…/2026-11-09/portaria-243-2026-dou-impressao-web.pdf` | PDF | Alta; não certificada | — | `6cb24f83928ecbf60da575d13b1cad7edce9f726306cf619b637ce14623fb02e` |
| `referencias/normas/pnp-guia-referencia-metodologica-2018.pdf` | `…/2026-11-09/pnp-guia-referencia-metodologica-2018.pdf` | PDF | Média (2018) | — | `6f3cd9737ba11637d212c7cc930790a47610c4de626ad82c4855eb7b09dbb491` |
| `referencias/normas/ifmt-matriz-2026.xlsx` | `…/2026-11-08/ifmt-matriz-2026.xlsx` | XLSX | Alta | Lida por `reproduzir_estudo_pnp.py` (T13) | `b341f7a1e8a92bc510abd75058ec4396369d9725654c0d11e2e7e740bb66b9f3` |
| `referencias/normas/proad-orcamento-2026.html` | `…/2026-11-09/proad-orcamento-2026.html` | HTML | Alta | — | `bcb54f357be56841ee90e714b110cbb526235184c739a7e2c9a13aca4d0bd9a9` |
| `referencias/normas/distribuicao-interna-ifes-2026.json` | `…/2026-11-09/distribuicao-interna-ifes-2026.json` | JSON | Alta | — | `b9460099479ab5427d06a99d7ae45616acfb96144f3a2493c6d869e0d4d3b827` |

Todos os checksums conferem com os manifestos de evidência originais. **Resultado esperado:** regras citadas em `docs/` podem ser conferidas nos documentos de origem. **Atualização:** substituir N3 pela versão certificada quando obtida (registrar novo checksum); acrescentar o guia atual da PNP quando obtido.

### 2.2. Fonte canônica, estudos, histórico e SDD

| Destino | Original | Tipo | Confiab. | sha256 |
|---|---|---|---|---|
| `referencias/fonte-canonica-matriz/matriz-orcamentaria-v1.2.2.md` | `docs/dominio/matriz-orcamentaria.md` | Markdown | Alta para 2026 | `11dc92ee5cdcd28b520873497e76a41b6a01c70ff5e02bb52268f15c6c91a74b` |
| `referencias/estudos/estudo-pnp-2026-11-10.md` | `docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md` | Markdown | Alta (reproduzido) | `578c78c875f9f2a43c3c5eff64fd508d566d021d86e98c3b97bf453347936e45` |
| `referencias/estudos/portao-de-dados-2026-11-09.md` | `docs/analises/prumo-poc-portao-dados.md` | Markdown | Alta (conclusão de cima) | `ae0dd81f68b5e8d277130010dd54f2c3ffe7eb9503cefb6dd035e03f8480e933` |
| `referencias/estudos/revisao-estrategica-2026-11-09.md` | `docs/analises/prumo-revisao-estrategica-oportunidades.md` | Markdown | Média | `31026cf7f4d8fe67833489863ec9b9a1c20b8057499f272304c537f111a4600a` |
| `referencias/historico/documento-fundador-v1.1.md` | `contexto_projeto_inteligencia_estrategica_educacional_ifes_v1_1.md` | Markdown | Média | `f1e9836b132821dd8245948df3eca1f7ea270e1bc69c08ecd8d8b8758384218e` |
| `referencias/sdd-laboratorio/constitution-v1.0.0.md` | `.specify/memory/constitution.md` | Markdown | Alta (ratificado) | `04c3ad3b999807236349ff414c68524e7eb05fe9fdf4b73e002a0161fcb98ee4` |
| `referencias/sdd-laboratorio/spec-001-jornada-decisao-estrategica.md` | `specs/001-jornada-decisao-estrategica/spec.md` @ `0e90151` | Markdown | Média (rascunho, PR #5 aberto) | `920efc67e4a7952542791bde0629c7aad2e47e32b1e34cabedb58ab81bef8e90` |

**Dependência:** os links internos desses arquivos apontam para caminhos do laboratório; tradução em [referencias/README.md](../referencias/README.md) § 7. **Atualização:** nenhuma; são registros congelados.

### 2.3. Protótipos

| Destino | Original | Tipo | sha256 |
|---|---|---|---|
| `referencias/prototipos/prumo-poc.html` | `poc/prumo-poc.html` | HTML autocontido | `77a5f44a9ca3bbd3f38af94e0759e8e9453ebe228be3d8cc2daf3a1177a4a64c` |
| `referencias/prototipos/prumo-recomposicao.html` | `poc/prumo-recomposicao.html` | HTML autocontido | `b401d6f4c1da626e98b527f208f27ab201475701a6e5a8d51ae816f645faa59d` |
| `referencias/prototipos/prumo-poc-002.html` | `poc/prumo-poc-002.html` | HTML autocontido | `d82ded735566969e51ecc506223c0e907284e4a97665f69bc356b6e77c84e6a6` |
| `referencias/prototipos/capturas-poc-002/1-comparar.png` | `docs/analises/capturas/poc-002/1-comparar.png` | PNG | `7ceeb2d50f77b30f9cb5bfd4bb637765da0e5794496c8f6385b76193bd219aaf` |
| `referencias/prototipos/capturas-poc-002/2-simular-vitoria.png` | idem | PNG | `01d5f690afad720ffb6c8c8de6ceea04f822634a9a6e4bd50f67d3574d832bc4` |
| `referencias/prototipos/capturas-poc-002/3-simular-serra.png` | idem | PNG | `dcfc94c57cb23cf56ba0b7625561a04d0a30512f2643a0b5449c256a74323c75` |
| `referencias/prototipos/capturas-poc-002/4-compor.png` | idem | PNG | `4ac072f1ee2f928f567836ca04bfe2a276f5a660db27ad7178a3790029ce5e8a` |
| `referencias/prototipos/capturas-poc-002/5-como-calcula.png` | idem | PNG | `e770d9cfb11e1bd8b12152e829c9bb0b5ecdbd4fdc0bd3217a4367e047faff78` |

**Dependência:** folha de estilos do Google Fonts (opcional). **Resultado esperado:** abrir no navegador e navegar; os registros ficam no navegador de quem abre. **Não é código da aplicação.**

### 2.4. Scripts de reprodução

| Destino | Original | Tipo | Dependências | sha256 |
|---|---|---|---|---|
| `scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py` | `docs/dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py` (`8900c81b…`) | Python, **caminhos adaptados** | Python 3; PNP externa; `openpyxl` e `referencias/normas/ifmt-matriz-2026.xlsx` para T13 | `e9c679793b4ca1663752d932d0e38368fc9a32e4dee43223114be6724927e712` |
| `scripts/analises/estudo-pnp/resultado-estudo-pnp.txt` | `…/2026-11-10/resultado-estudo-pnp.txt` | Texto | — | `3eab12c57fba14d69e40de220710d60b90eb8a8e5740109d3efabbe357c14281` |
| `scripts/analises/motores-coortes-poc/recomposicao/coortes.js` | `poc/coortes.js` | JavaScript | — | `4246e7282bacb262e33a19212b9aaaaf9904aa2005446453f8d3041c7f8b25e6` |
| `scripts/analises/motores-coortes-poc/recomposicao/testar_coortes.cjs` | `poc/testar_coortes.cjs` | JavaScript | Node.js | `095e0cf0b717afcb8281b7f6e1a6919effa794ef353f82b7d40ab95b278c1479` |
| `scripts/analises/motores-coortes-poc/recomposicao/dados-recomposicao.json` | `poc/dados-recomposicao.json` | JSON (agregados públicos da PNP) | — | `67ec77579606b4263e63a7354a92595c534ab031ac4b091fad6d3ff721b82024` |
| `scripts/analises/motores-coortes-poc/poc-002/coortes002.js` | `poc/coortes002.js` | JavaScript | — | `8a96751a73ab84e6558afdbe8bea6830e9ca813c631ba986c0e41912aa9ebf95` |
| `scripts/analises/motores-coortes-poc/poc-002/testar_poc002.cjs` | `poc/testar_poc002.cjs` | JavaScript | Node.js | `3fff211f7bfad6ce8b063a438a02d2cfc0cafe6297b23d4102663a63b81d0d82` |
| `scripts/analises/motores-coortes-poc/poc-002/dados-poc002.json` | `poc/dados-poc002.json` | JSON (agregados públicos da PNP) | — | `c3a638c8e416cb55a15d2cdad971aa91d17ca2e6c1860cd092a2d55602ae11d2` |

**Resultado esperado:** `testar_coortes.cjs` → 6 de 6; `testar_poc002.cjs` → 16 de 16; `reproduzir_estudo_pnp.py` → saída idêntica a `resultado-estudo-pnp.txt`. **Verificado no pacote em 11/11/2026.**

**Única alteração de conteúdo do pacote em arquivo copiado** (`reproduzir_estudo_pnp.py`):

```diff
-Relatório: docs/analises/prumo-pnp-inteligencia-comparativa-exploratoria.md
+Relatório: referencias/estudos/estudo-pnp-2026-11-10.md
-    python3 docs/dominio/evidencias/2026-11-10/reproduzir_estudo_pnp.py [caminho/indicadores-gestao]
+    python3 scripts/analises/estudo-pnp/reproduzir_estudo_pnp.py [caminho/indicadores-gestao]
-RAIZ = Path(__file__).resolve().parents[4]
-PNP = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PNP_DIR", RAIZ / "indicadores-gestao"))
+RAIZ = Path(__file__).resolve().parents[3]
+PNP = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PNP_DIR", RAIZ / "data/pnp/indicadores-gestao"))
-    c5 = RAIZ / "docs/dominio/evidencias/2026-11-08/ifmt-matriz-2026.xlsx"
+    c5 = RAIZ / "referencias/normas/ifmt-matriz-2026.xlsx"
```

## 3. Dados externos

| Conjunto | Onde fica | Controle |
|---|---|---|
| Exportação da PNP (18 CSV, 97.030.642 bytes) | Fora do Git: `data/pnp/indicadores-gestao/` | Manifesto e checksums em [data/README.md](../data/README.md); conferidos em 11/11/2026 |

## 4. Permanecem só no laboratório

Consultáveis no repositório `saymoncastro/prumo` (público), commit `f98a7b7`, e na branch `001-jornada-decisao-estrategica`:

- Documentos sintetizados: visão de 10/11, diagnóstico, próximo passo, proposta de nome, revisão crítica, auditoria complementar, avaliação da v2, plano de Itapina, documento da POC 0.0.2.
- Versões 1.0.0 e 1.1.0 da fonte canônica; `alteracoes-rmo.json`; `resultado-validacao.json`; `cadastro-publico.xlsx`.
- Testes de auditoria da matriz (`tests/auditoria_matriz/`), `reproduzir_revisao_critica.py` e resultados: dependem da planilha não pública.
- Templates, extratores, montador e `dados-poc.json` das POCs; v1 da meta de 50% (commit `a3b64df`).
- Spec Kit 1.2.0 instalado (`.specify/`, `.claude/skills/`); lista de qualidade do rascunho 001.

**Nunca transportar:** planilha da matriz do Ifes, livro da matriz, arquivos de teste derivados da planilha, estado local de ferramentas.

## 5. Critérios de aceite da transferência

1. `shasum -a 256 -c migracao/SHA256SUMS` sem falhas.
2. Todos os links relativos de `README.md`, `docs/`, `migracao/`, `data/README.md`, `scripts/analises/README.md` e `referencias/README.md` resolvem (os links internos dos arquivos copiados em `referencias/` são exceção declarada).
3. Os dois testes de motores passam; o estudo da PNP reproduz byte a byte quando a exportação está em `data/pnp/indicadores-gestao/`.
4. Nenhum arquivo de `data/pnp/` aparece em `git status`.
5. A lista de [inicialização](checklist-inicializacao.md) está concluída.
