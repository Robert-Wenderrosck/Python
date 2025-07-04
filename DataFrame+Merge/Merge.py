import pandas as pd

vendasDataFrame = pd.read_excel("Vendas_Merge.xlsx")
print("\n DataFrame Vendas \n")
print(vendasDataFrame)
print("\n")

vendedoresDataFrame = pd.read_excel("Vendedores_Merge.xlsx")
print("\n DataFrame Vendedores \n")
print(vendedoresDataFrame)
print("\n")

produtosDataFrame = pd.read_excel("Produtos_Merge.xlsx")
print("\n DataFrame Produtos \n")
print(produtosDataFrame)
print("\n")

#----------------------------------------------------
#Merge - Trás informações de outros DataFrames para um DataFrame através de um identificador/ coluna em comum
vendasDataFrame = vendasDataFrame.merge(vendedoresDataFrame)
print("\n Merge Vendas x Vendedores \n")
print(vendasDataFrame)
print("\n")

#----------------------------------------------------

vendasDataFrame = vendasDataFrame.merge(produtosDataFrame)
print("\n Merge Vendas x Vendedores x Produtos \n")
print(vendasDataFrame)
print("\n")

#-----------------------------------------------------
#Mostrar todas as colunas de um DataFrame
print(vendasDataFrame.columns)
print("\n")

#-----------------------------------------------------
#Resumir um DataFrame
resumoDataFrame = vendasDataFrame[["Vendedor", "Produto", "Total Vendas"]]
print("\n Resumo DataFrame Merge \n")
print(resumoDataFrame)
print("\n")
