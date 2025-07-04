import pandas as pd

#Pivot_Table - Diferente da Pivot aceita agregação da valores repetidos

baseLanchonete_DF = pd.read_excel("Vendas_Lanchonete_Pivot_Table.xlsx")
print("\n Imprimindo dados \n")
print(baseLanchonete_DF)
print("\n")

#index = linhas
#columns = colunas
#values = soma
#aggfunc = tipo de cálculo (sum)
pivotEx1 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")
print("\n Imprimindo Data / Cliente / Preço com Desconto / Soma \n")
print(pivotEx1)
print("\n")

#---------------------------------------------------------------
pivotEx2 = baseLanchonete_DF.pivot_table(index="Cliente", columns="Data Venda", values="Preço com Desconto", aggfunc="sum")
print("\n Imprimindo Cliente / Data Venda / Preço com Desconto / Soma \n")
print(pivotEx2)
print("\n")

#---------------------------------------------------------------
pivotEx3 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values=["Preço Total", "Preço com Desconto"], aggfunc="sum")
print("\n Imprimindo com Cliente / Preço Total e Preço com Desconto \n")
print(pivotEx3)
print("\n")

#---------------------------------------------------------------
pivotEx4 = baseLanchonete_DF.pivot_table(index="Data Venda", columns=["Cliente", "Produto"], values="Preço com Desconto", aggfunc="sum")
print("\n Imprimindo com Cliente, Produto e Preço com Desconto \n")
print(pivotEx4)
print("\n")



















