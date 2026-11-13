# Diretrizes de arquitetura para um produto multi-instituição

> **Natureza:** decisões de princípio, não arquitetura técnica. Nenhuma tecnologia, serviço, banco, mecanismo de *tenancy* ou forma de implantação está escolhido. Essas escolhas pertencem ao plano da primeira especificação e devem ser as mais simples que respeitem as diretrizes abaixo.
> **Relacionados:** [visão](../produto/visao.md) § 9 · [glossário e modelo conceitual](../dominio/glossario-e-modelo-conceitual.md) · [fontes e proveniência](../dados/fontes-qualidade-e-proveniencia.md) · [decisões e pendências](../decisoes/decisoes-hipoteses-e-pendencias.md)

## 1. Ponto de partida

O PRUMO passou a ser pensado como produto reutilizável por outras instituições multicampi da Rede Federal em 10/11/2026 (**[DIREÇÃO]** do idealizador). A demanda comercial **não** está validada (hipóteses H7 a H10 da visão).

O objetivo destas diretrizes é **preservar a possibilidade** de atender outra instituição, não construir a infraestrutura para isso. Toda decisão de domínio que só funcione para o Ifes é um defeito; toda infraestrutura construída para clientes que ainda não existem é desperdício.

Os protótipos do laboratório exploratório violam várias destas diretrizes (Ifes, campi e exceções fixos no código; registros no navegador; três motores incompatíveis). Eles **não** são ponto de partida da arquitetura. Ver [aprendizados e limites das POCs](../evidencias/aprendizados-e-limites-das-pocs.md).

## 2. Diretrizes

### D1. Instituição é parâmetro

- Instituição, unidades (campi, polos, reitoria, centros de referência) e exceções são **dados ou configuração**, nunca constantes de código.
- Unidades têm **identidade estável própria**. A fonte pública identifica campus por nome, sem código, e nomes mudam entre edições; o vínculo nome-na-fonte → unidade é um mapeamento versionado.
- Unidades atípicas (ex.: o Cefor do Ifes, polos de educação a distância) são um tipo de unidade, não um caso especial no código.

### D2. Dado público compartilhado separado de dado privado, por construção

| Compartilhado entre todas as instituições | Privado de cada instituição |
|---|---|
| Série pública da Rede Federal (PNP) por edição | Objetivos e metas pactuadas |
| Normas e regras da Matriz CONIF por exercício | Premissas, evidências e hipóteses registradas |
| Demonstrativos públicos | Cenários, alternativas, propostas, composições, compromissos |
| Metas legais e fórmulas nacionais | Regra interna de distribuição orçamentária |
| | Dados acadêmicos por turma, capacidade docente e física, custos |

- Nada privado de uma instituição pode ser visível a outra.
- A separação existe **no modelo** desde a primeira especificação. **Como** ela se materializa (banco único com discriminador, esquemas, bancos separados) é decisão pendente, a tomar quando houver mais de um cliente ou requisito explícito.

### D3. Usuários e papéis no modelo, controle de acesso depois

- Os papéis **institucional** (reitoria, pró-reitorias, planejamento) e **local** (direção de campus, ensino, coordenações) existem no modelo.
- Tudo o que um usuário cria registra **autor e papel**, mesmo sem autenticação.
- Autenticação, perfis e permissões finas ficam fora até uma especificação pedir.

### D4. Regras institucionais parametrizáveis

- Regras nacionais (fórmulas da matriz, metas legais) e regras institucionais (distribuição interna, objetivos pactuados, critérios de comparáveis) usam **o mesmo mecanismo de versão e fonte**.
- Nenhuma regra de um exercício é verdade permanente. Ver [Matriz CONIF e indicadores](../dominio/matriz-conif-e-indicadores.md) § 5.

### D5. Versionamento de fontes, regras e modelos

Três coisas mudam no tempo e precisam de versão própria:

| O que | Exemplo de mudança | Consequência |
|---|---|---|
| **Fonte de dados** | Nova edição da PNP; mudança de fórmula da matrícula equivalente | Toda série observada sabe de qual edição veio |
| **Regra** | Portaria nova; prática de cálculo diferente do texto | Todo cálculo sabe qual versão da regra aplicou |
| **Modelo de projeção** | Novo motor de coortes; recalibração | Todo resultado simulado sabe qual modelo e qual calibração o produziu |

### D6. Rastreabilidade e auditabilidade

- Todo número exibido ou armazenado carrega **natureza** (fato observado, estimado, premissa, hipótese, resultado simulado, não estimado) e **origem** (fonte, ano-base, versão da regra, fórmula).
- O caminho dado bruto → transformação → resultado é reconstituível.
- Registros de governança (proposta, composição, compromisso) são **imutáveis por versão**: revisar cria nova versão e preserva a anterior.

### D7. Reprodutibilidade de cenários

- Um cenário registrado guarda as versões de dados, regras e modelo com que foi calculado. Ao reabrir, mostra os valores originais e avisa se há versão mais recente; não recalcula em silêncio.
- Cálculos são determinísticos. Nenhum número é produzido por modelo de linguagem.

### D8. Agregados bastam

- O núcleo funciona com dados agregados por oferta e por campus, sem dados pessoais.
- Dados por estudante, se um dia entrarem, exigem especificação própria, base legal (LGPD) e isolamento adicional. Ver [fontes e proveniência](../dados/fontes-qualidade-e-proveniencia.md) § 7.

### D9. Integrações futuras como fontes, não como dependências

- Sistemas acadêmicos, de pessoal e de patrimônio são **fontes futuras** de premissas melhores (ex.: evasão por turma, docentes por área), não pré-requisitos.
- A primeira carga de dados é manual, uma vez por edição da PNP. Integração automática só com demanda demonstrada.

### D10. Evolução incremental

- Uma jornada por vez, cada uma navegável antes da próxima.
- Nada de mensageria, microsserviços, filas, *data lake* ou múltiplos bancos sem necessidade demonstrada por especificação.
- A interface não é decidida aqui. A forma da inteligência histórica na interface foi decidida apenas para a primeira fatia (investigação guiada a partir do objetivo; ver [decisões](../decisoes/decisoes-hipoteses-e-pendencias.md)).

## 3. O que fica explicitamente em aberto

| Tema | Por que não decidir agora |
|---|---|
| Linguagem, framework e banco | Pertence ao plano da primeira especificação |
| Mecanismo de isolamento entre clientes | Só há uma instituição com dados próprios |
| Hospedagem e implantação | Sem cliente nem modelo de contratação |
| Autenticação e perfis | Fora da primeira fatia |
| Onde vivem evidências, cenários e propostas | Pendência da primeira especificação (deixam de ficar no navegador) |
| Como a exportação da PNP é carregada | Pendência da primeira especificação |
| Um motor de coortes único e seus mecanismos | Depende das perguntas que o gestor faz; ver [simulação](../simulacao/modelos-premissas-e-validacao.md) § 7 |
