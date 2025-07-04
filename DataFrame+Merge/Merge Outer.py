import pandas as pd

#OUTER = Mantém todos os registros dos dois DataFrames, mesmo que não tenham correspondência entre si (quando não tem correspodência = 'NaN', quando tem mostra os dois )
vendasLoja1_dataFrame = pd.read_excel("Outer_Vendas_Loja1.xlsx")
vendasLoja2_dataFrame = pd.read_excel("Outer_Vendas_Loja2.xlsx")

print("\n DataFrame Vendas Loja 1 \n")
print(vendasLoja1_dataFrame)
print("\n")

print("\n DataFrame Vendas Loja 2 \n")
print(vendasLoja2_dataFrame)
print("\n")

verificandoVendas_dataFrame = pd.merge(vendasLoja1_dataFrame, vendasLoja2_dataFrame, on=["Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))
print("\n Juntando dados com o 'Outer' e verificando os vendedores que venderam em ambas as lojas \n")
print(verificandoVendas_dataFrame)
print("\n")

#---------------------------------------------
#Removendo as linhas que tem "NaN" (valor vazio)
tratandoDados_DataFrame = verificandoVendas_dataFrame.dropna()
print("\n Removendo linhas com o 'NaN' (valor vazio) \n")
print(tratandoDados_DataFrame)
print("\n")

#---------------------------------------------
#Removendo a coluna "Vendedor Loja 2"
del tratandoDados_DataFrame["Vendedor Loja 2"]
print("\n Removendo a coluna 'Vendedor Loja 2'  \n")
print(tratandoDados_DataFrame)
print("\n")














