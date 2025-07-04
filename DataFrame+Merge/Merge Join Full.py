import pandas as pd

loja1_dataFrame = pd.read_excel("Vendedores_Join_Full_Loja1.xlsx")
loja2_dataFrame = pd.read_excel("Vendedores_Join_Full_Loja2.xlsx")

print("\n Vendedores Loja 1 \n")
print(loja1_dataFrame)
print("\n")

print("\n Vendedores Loja 2 \n")
print(loja2_dataFrame)
print("\n")

#-------------------------------------------------
#Join Full = uni os arquivos completamente (usando o .concat)
vendasLoja1e2_DataFrame = pd.concat([loja1_dataFrame, loja2_dataFrame])
print("\n Vendedores Loja 1 e 2 \n")
print(vendasLoja1e2_DataFrame)
print("\n")

#-------------------------------------------------

#.drop_duplicates - remove os vendedores duplicados pelo Id do Vendedor
semVendedoresDuplicados = vendasLoja1e2_DataFrame.drop_duplicates(subset="Id Vendedor")
print(semVendedoresDuplicados)
print("\n")













