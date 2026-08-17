# Miniprojeto_Elza_Analise_de_Dados_T4

Análise Exploratória de Dados — Base de Varejo
Descrição
Este projeto realiza uma análise exploratória de dados (EDA) sobre uma base de transações de varejo (Base_Varejo.csv), contendo 830.000 registros de compras, com informações de cliente, produto e data.

Estrutura dos dados
Coluna
Descrição
DATA
Data da compra
CO_ID
ID do pedido
CL_ID
ID do cliente
CL_GENERO
Gênero do cliente
CL_EC
Estado civil do cliente (código)
CL_FHL
Número de filhos do cliente
CL_SEG
Classe econômica do cliente (A, B ou C)
PR_ID
ID do produto
PR_CAT
Categoria do produto
PR_NOME
Nome do produto
Etapas realizadas
1. Carga e inspeção inicial
Leitura do CSV com separador ; (pd.read_csv(..., sep=';'))
Verificação de número de registros, colunas e tipos de dados (.shape, .dtypes)
2. Identificação de problemas
Colunas vazias: 4 colunas sem nome (Unnamed: 10-13), 100% nulas em todos os registros — resultado de separadores extras no arquivo original
Duplicatas: 184.330 linhas duplicadas (96.553 cópias extras), afetando 78,9% dos pedidos. Investigação confirmou que toda duplicata ocorre dentro do mesmo pedido e mesmo produto (CO_ID + PR_ID), indicando ausência de coluna de quantidade — a base representa unidades adicionais via repetição de linha
Inconsistência de categoria: valor #N/D em PR_CAT/PR_NOME, presente em 3.650 registros (0,44%), concentrado em um único produto (PR_ID = 107) com cadastro incompleto na fonte original

3. Limpeza aplicada
Remoção das colunas Unnamed: 10 a Unnamed: 13
Conversão de DATA para datetime (0 falhas de conversão em 830.000 registros)
Recategorização de #N/D para NAO_INFORMADO em PR_CAT e PR_NOME (preserva o registro da venda em vez de descartá-lo)
Duplicatas mantidas — decisão justificada por representarem quantidade comprada, não erro de importação
