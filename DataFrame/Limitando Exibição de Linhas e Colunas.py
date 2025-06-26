import pandas as opcoesPandas

#----------------Abrindo o arquivo do Excel----------------------
#Arquivo Excel está na mesma pasta que o arquivo Python (não precisa colocar o caminho)
vendas_dataFrame = opcoesPandas.read_excel("Vendas_Jan.xlsx")
print(vendas_dataFrame)
print("\n")

print("\nIndex exibe apenas informações sobre as linhas do DataFrame\n")
print(vendas_dataFrame.index)
print("\n")

print("\nColumns exibe o nome de todas as colunas do DataFrame\n")
print(vendas_dataFrame.columns)
print("\n")

print("\nHead exibe apenas as 5 primeiras linhas por padrão\n")
print(vendas_dataFrame.head())
print("\n")

print("\nHead exibindo apenas as 10 primeiras linhas\n")
print(vendas_dataFrame.head(10))
print("\n")

print("\nTail exibe apenas as últimas linhas\n")
print(vendas_dataFrame.tail(3))
print("\n")

print("\nImprimindo somente a coluna vendedor\n")
print(vendas_dataFrame["Vendedor"])
print("\n")

print("\nImprimindo mais de uma coluna\n")
print(vendas_dataFrame[["Vendedor", "Total Vendas"]])
print("\n")

print("\nImprimindo somente linhas de 1 a 5\n")
print(vendas_dataFrame.loc[1:5])
print("\n")

#Cria uma variável que busca (.loc) na coluna Vendedor do DataFrame o "Leonardo Almeida"
vendas_LeonardoAlmeida_dataFrame = vendas_dataFrame.loc[vendas_dataFrame["Vendedor"] == "Leonardo Almeida"]
print("\nImprimindo somente vendas do Leonardo Almeida\n")
print(vendas_LeonardoAlmeida_dataFrame)
print("\n")

#Cria uma variável que busca (.loc) na coluna Vendedor do DataFrame o "Leonardo Almeida" e seleciona duas colunas para serem exibidas
vendas_LeonardoAlmeida_dataFrame2 = vendas_dataFrame.loc[vendas_dataFrame["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]
print("\nImprimindo somente vendas do Leonardo Almeida\n")
print(vendas_LeonardoAlmeida_dataFrame2)
print("\n")

print("\nVendedor do Indice 4\n")
print(vendas_dataFrame.loc[4, "Vendedor"])
print("\n")

print("\nMétodo Shape mostra quantas linhas e colunas tem o DataFrame\n")
print(vendas_dataFrame.shape)
print("\n")


transformarLinhasEmColunas = vendas_dataFrame.T
print("\nT = Transpose (Tranforma linhas em colunas e colunas em linhas)\n")
print(transformarLinhasEmColunas)
print("\n")
