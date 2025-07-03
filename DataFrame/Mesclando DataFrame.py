import pandas as pd

vendasJaneiro_DataFrame = pd.read_excel("Vendas_Jan.xlsx")

print("\n DataFrame vendas Janeiro \n")
print(vendasJaneiro_DataFrame)
print("\n")

vendasFevereiro_DataFrame = pd.read_excel("Vendas_Fev.xlsx")

print("\n DataFrame vendas Fevereiro \n")
print(vendasFevereiro_DataFrame)
print("\n")

#---------------------------------------------
#pd.concat = junta listas de DataFrames e os concatena
vendasJaneiro_DataFrame = pd.concat([vendasJaneiro_DataFrame, vendasFevereiro_DataFrame])
print("\n DataFrame Jan e Fev unidos \n")
print(vendasJaneiro_DataFrame)
print("\n")

#---------------------------------------------
vendasMarco_DataFrame = pd.read_excel("Vendas_Mar.xlsx")

print("\n DataFrame vendas Março \n")
print(vendasMarco_DataFrame)
print("\n")

#---------------------------------------------
vendasGeral_DataFrame = pd.concat([vendasJaneiro_DataFrame, vendasFevereiro_DataFrame, vendasMarco_DataFrame])

print("\n DataFrame vendas Jan, Fev e Mar \n")
print(vendasGeral_DataFrame)
print("\n")

#---------------------------------------------

resumindoDataFrameGeral = vendasGeral_DataFrame[["Vendedor", "Data Venda", "Total Vendas"]]
print("\n Imprimindo 3 colunas do DataFrame Geral \n")
print(resumindoDataFrameGeral)
print("\n")

#---------------------------------------------

#keys está criando grupos de acordo com a ordem dos meses
vendasGeralComGrupos = pd.concat([vendasJaneiro_DataFrame, vendasFevereiro_DataFrame, vendasMarco_DataFrame], keys=["Janeiro", "Fevereiro", "Março"])
print("\n DataFrame Geral com Grupos \n")
print(vendasGeralComGrupos)
print("\n")

#---------------------------------------------

#Extraindo mês de fevereiro do DataFrame Geral
extraindoFevereiro = vendasGeralComGrupos.loc["Fevereiro"]
print("\n Extraindo mês de fevereiro do DataFrame Geral \n")
print(extraindoFevereiro)
print("\n")
