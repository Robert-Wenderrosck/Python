import pandas as pd

#Pivot - Está função não suporta agregação de valores repetidos

baseLanchonete_DataFrame = pd.read_excel("Vendas_Lanchonete_Pivot.xlsx")
print("\n Imprimindo dados \n")
print(baseLanchonete_DataFrame)
print("\n")

#index = linhas
#columns = colunas
#values = valores das categorias
pivotExemplo1 = baseLanchonete_DataFrame.pivot(index="Data Venda", columns="Cliente", values="Preço com Desconto")
print("\n Imprimindo clientes / Preço com Desconto \n")
print(pivotExemplo1)
print("\n")

#------------------------------------------------
pivotExemplo2 = baseLanchonete_DataFrame.pivot(index="Cliente", columns="Data Venda", values="Preço com Desconto")
print("\n Imprimindo clientes / Preço com Desconto \n")
print(pivotExemplo2)
print("\n")


















