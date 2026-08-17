# Análise Exploratória de Dados — Base de Varejo

## Descrição

Este projeto realiza uma análise exploratória de dados (EDA) sobre uma base de transações de varejo (`Base_Varejo.csv`), contendo 830.000 registros de compras, com informações de cliente, produto e data.

## Estrutura dos dados

| Coluna | Descrição |
| --- | --- |
| `DATA` | Data da compra |
| `CO_ID` | ID do pedido |
| `CL_ID` | ID do cliente |
| `CL_GENERO` | Gênero do cliente |
| `CL_EC` | Estado civil do cliente (código) |
| `CL_FHL` | Número de filhos do cliente |
| `CL_SEG` | Classe econômica do cliente (A, B ou C) |
| `PR_ID` | ID do produto |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

## Etapas realizadas

### 1. Carga e inspeção inicial

- Leitura do CSV com separador `;` (`pd.read_csv(..., sep=';')`)
- Verificação de número de registros, colunas e tipos de dados (`.shape`, `.dtypes`)

### 2. Identificação de problemas

- **Colunas vazias**: 4 colunas sem nome (`Unnamed: 10-13`), 100% nulas em todos os registros — resultado de separadores extras no arquivo original
- **Duplicatas**: 184.330 linhas duplicadas (96.553 cópias extras), afetando 78,9% dos pedidos. Investigação confirmou que toda duplicata ocorre dentro do mesmo pedido e mesmo produto (`CO_ID` + `PR_ID`), indicando ausência de coluna de quantidade — a base representa unidades adicionais via repetição de linha
- **Inconsistência de categoria**: valor `#N/D` em `PR_CAT`/`PR_NOME`, presente em 3.650 registros (0,44%), concentrado em um único produto (`PR_ID = 107`) com cadastro incompleto na fonte original

### 3. Limpeza aplicada

- Remoção das colunas `Unnamed: 10` a `Unnamed: 13`
- Conversão de `DATA` para `datetime` (0 falhas de conversão em 830.000 registros)
- Recategorização de `#N/D` para `NAO_INFORMADO` em `PR_CAT` e `PR_NOME` (preserva o registro da venda em vez de descartá-lo)
- Duplicatas **mantidas** — decisão justificada por representarem quantidade comprada, não erro de importação

### 4. Estatísticas descritivas — número de filhos (`CL_FHL`)

| Métrica | Valor |
| --- | --- |
| Contagem | 830.000 |
| Média | 1,15 |
| Desvio padrão | 1,42 |
| Mínimo | 0 |
| 25% | 0 |
| Mediana (50%) | 0 |
| 75% | 2 |
| Máximo | 4 |
| Moda | 0 |

A distribuição é assimétrica à direita: a maioria dos clientes não tem filhos, mas quem tem eleva a média acima da mediana.

### 5. Agrupamentos

- **Categoria de produto × Classe econômica**: proporção de compras por categoria praticamente idêntica entre classes A, B e C (alimentos 52% em todas)
- **Categoria de produto × Gênero**: mesmo padrão de homogeneidade entre gêneros F e M
- **Tamanho médio de pedido**: 44,9 itens totais / 39,7 produtos distintos por pedido — diferença de 5 itens reflete repetição de quantidade dentro do pedido.

## Gráficos gerados

| Gráfico | Tipo | O que mostra |
| --- | --- | --- |
| Proporção de categoria por classe econômica | Barras agrupadas | Compara visualmente o mix de categorias compradas entre classes A, B e C — reforça a homogeneidade encontrada nos números |
| Proporção de categoria por gênero | Barras agrupadas | Mesma comparação, entre os gêneros F e M — mesmo padrão de homogeneidade |
| Distribuição do número de itens por pedido | Histograma | Mostra a forma da distribuição do tamanho dos pedidos — sem picos ou caudas extremas, consistente com média e mediana próximas (44,9 e 45) |

## Conclusões principais

- A base apresentou boa qualidade estrutural, com problemas pontuais e explicáveis (não sistêmicos)
- O perfil demográfico do cliente (classe econômica, gênero) **não influencia significativamente** o mix de categorias de produtos comprados nesta base — resultado consistente, embora contrário à expectativa inicial
- A base não contém colunas de valor monetário, o que limita análises de receita, lucro ou ticket médio

## Arquivos

- `Base_Varejo.csv` — base original
- `Base_Varejo_limpa.csv` — base após limpeza (mesmo número de linhas: 830.000; 10 colunas)

## Limitações

A ausência de uma coluna explícita de quantidade impede distinguir tecnicamente, linha a linha, duplicata legítima de eventual erro isolado de duplicação. A conclusão de que as duplicatas são legítimas baseia-se no padrão consistente observado (mesmo pedido + mesmo produto), não em confirmação direta pela fonte de dados.
