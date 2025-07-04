import pandas as pd

#LEFT = Mantém todas as linhas do DataFrame da esquerda (primeiro da junção), mesmo que não tenham correspondência no da direita
vendas_DataFrame = pd.read_excel("Vendas_LEFT_JOIN.xlsx")
vendedores_DataFrame = pd.read_excel("Vendedores_LEFT_JOIN.xlsx")

print("\n DataFrame Vendas \n")
print(vendas_DataFrame)
print("\n")

print("\n DataFrame Vendedores \n")
print(vendedores_DataFrame)
print("\n")

#--------------------------------------------------

#left = Trazer os dados pela esquerda ID do Vendedor (=~PROCV do excel)
verificandoVendas_DataFrame = pd.merge(vendas_DataFrame, vendedores_DataFrame, on="Id Vendedor", how="left", suffixes=(" Vendas", " Checagem"))
print("\n DataFrame junção dois DataFrames com LEFT \n")
print(verificandoVendas_DataFrame)
print("\n")

#--------------------------------------------------

#dropna = Deleta linhas que tem pelo menos 1 valor vazio (Remover as linhas que tem o  "NaN" na coluna de Checagem)
tratamentoDados_DataFrame = pd.merge(vendas_DataFrame, vendedores_DataFrame, on="Id Vendedor", how="left", suffixes=(" Vendas", " Checagem"))
print("\n Remover as linhas que tem o 'NaN' na coluna de Checagem \n")
print(tratamentoDados_DataFrame)
print("\n")

#--------------------------------------------------
#Remover coluna repetida do nome do vendedor
del tratamentoDados_DataFrame["Vendedor Checagem"]
print("\n Removendo a coluna 'Vendedor Checagem' \n")
print(tratamentoDados_DataFrame)
print("\n")













