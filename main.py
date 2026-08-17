
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('base_varejo.csv',sep=';')
  
print(df.head())
print(df.shape)
print(df.columns)
df.info()

#Remover colunas totalmente vazias
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
print(df.shape)
print(df.columns)

# Valores nulos
print(df.isnull().sum())
# Duplicidades
print(df.duplicated().sum())

#ajustando a coluna data
print(df["DATA"].head())
print(df["DATA"].dtype)
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(df['DATA'].isna().sum())



# estatísticas principais da coluna npumero de filhos
print("Estatísticas descritivas - Número de filhos")

print(df["CL_FHL"].describe())

print("\nModa:")
print(df["CL_FHL"].mode().tolist())


print("Média:", df["CL_FHL"].mean())
print("Mediana:", df["CL_FHL"].median())
print("Moda:", df["CL_FHL"].mode().tolist())
print("Desvio padrão:", df["CL_FHL"].std())
print("Mínimo:", df["CL_FHL"].min())
print("Máximo:", df["CL_FHL"].max())
print("Contagem:", df["CL_FHL"].count())
print("\nQuartis:")
print(df["CL_FHL"].quantile([0.25, 0.50, 0.75]))




#Categoria mais comprada por classe econômica
print(df.groupby(['CL_SEG', 'PR_CAT']).size())
proporcao = df.groupby(['CL_SEG', 'PR_CAT']).size() / df.groupby('CL_SEG').size()
print(proporcao)
print(df['PR_CAT'].value_counts())


df[df['PR_CAT'] == '#N/D'][['PR_ID', 'PR_NOME', 'PR_CAT']].drop_duplicates()
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'NAO_INFORMADO')
df['PR_NOME'] = df['PR_NOME'].replace('#N/D', 'NAO_INFORMADO')

print((df['PR_CAT'] == '#N/D').sum())
print((df['PR_NOME'] == '#N/D').sum())

df.groupby(['CL_GENERO', 'PR_CAT']).size()
proporcao_genero = df.groupby(['CL_GENERO', 'PR_CAT']).size() / df.groupby('CL_GENERO').size()
print(proporcao_genero)

tamanho_pedidos = df.groupby('CO_ID').size()
print(tamanho_pedidos.mean())
print(tamanho_pedidos.describe())

produtos_distintos = df.groupby('CO_ID')['PR_ID'].nunique()
itens_totais = df.groupby('CO_ID').size()

print("Produtos distintos por pedido:")
print(produtos_distintos.describe())

print("\nItens totais por pedido:")
print(itens_totais.describe())


#  Tratar inconsistência #N/D (recategorizar, não remover)
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'NAO_INFORMADO')
df['PR_NOME'] = df['PR_NOME'].replace('#N/D', 'NAO_INFORMADO')



# Salvar os dados tratados em um novo arquivo CSV
df.to_csv('Base_Varejo_limpa.csv', sep=';', index=False)

print("Exportado com sucesso!")
print(df.shape)
print(df.dtypes)



proporcao = df.groupby(['PR_CAT', 'CL_SEG']).size() / df.groupby('CL_SEG').size()
proporcao = proporcao.unstack()  # transforma em tabela: categorias nas linhas, classes nas colunas

proporcao.plot(kind='bar')
plt.title('Proporção de compras por categoria e classe econômica')
plt.xlabel('Categoria de produto')
plt.ylabel('Proporção dentro da classe')
plt.legend(title='Classe')
plt.tight_layout()
plt.show()

proporcao_genero = df.groupby(['PR_CAT', 'CL_GENERO']).size() / df.groupby('CL_GENERO').size()
proporcao_genero = proporcao_genero.unstack()

proporcao_genero.plot(kind='bar')
plt.title('Proporção de compras por categoria e gênero')
plt.xlabel('Categoria de produto')
plt.ylabel('Proporção dentro do gênero')
plt.legend(title='Gênero')
plt.tight_layout()
plt.show()

tamanho_pedidos = df.groupby('CO_ID').size()

tamanho_pedidos.plot(kind='hist', bins=20)
plt.title('Distribuição do número de itens por pedido')
plt.xlabel('Itens por pedido')
plt.ylabel('Número de pedidos')
plt.show()

