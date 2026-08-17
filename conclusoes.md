# Análise de Dados Varejo

## Descrição

Este projeto realiza uma análise exploratória da base de varejo (830.000 registros, iniciada em 01/02/2019), avaliando a qualidade dos dados e identificando padrões de comportamento de compra dos clientes.

## Qualidade dos Dados

 Não foram encontrados valores nulos nas colunas de interesse.
 A coluna DATA foi convertida para o formato datetime sem falhas.

 Problemas pontuais:**

- 4 colunas vazias (Unnamed: 10 a 13) removidas.
  - Valor `#N/D` em 3.650 registros (0,44%), tratado como `NAO_INFORMADO`.
- **Duplicatas:** 184.330 linhas repetidas (78,9% dos pedidos). Representam quantidade de itens, não erro de importação → mantidas na base limpa.

## Perfil dos Clientes

O número médio de filhos por cliente é de 1,15 com mediana e moda iguais a 0. A maioria dos clientes não possui filhos, mas a presença de clientes com até 4 filhos eleva a média, gerando uma distribuição assimétrica à direita.

## Padrões de comportamento de compra

Ao cruzar categoria de produto (PR_CAT) com classe econômica (CL_SEG) e com gênero (CL_GENERO), observou-se que a proporção de compras por categoria é praticamente idêntica entre os grupos: alimentos representam cerca de 52% das compras em todas as classes econômicas e em ambos os gêneros, seguido por higiene (~18-19%) e limpeza (~17-18%), com variações de décimos de ponto percentual entre os grupos. Isso indica que, nesta base, o perfil demográfico do cliente (classe econômica ou gênero) não influencia significativamente o mix de categorias de produtos adquiridos — um resultado que contraria a expectativa inicial de que esses fatores diferenciariam o padrão de compra, mas que é sustentado consistentemente pelos dados.

## Linitações

 A Ausência de colunas de valor monetário (preço, receita, lucro) impossibilita análises de faturamento, ticket médio ou margem.
