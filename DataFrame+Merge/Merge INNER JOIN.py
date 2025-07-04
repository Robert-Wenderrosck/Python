import pandas as pd

#INNER = Só mantém os registros que existem nos dois DataFrames
loja1_DataFrame = pd.read_excel("Vendas_+INNER_JOIN_Loja1.xlsx")
loja2_DataFrame = pd.read_excel("Vendas_+INNER_JOIN_Loja2.xlsx")

print("\n Vendas Loja 1 \n")
print(loja1_DataFrame)
print("\n")

print("\n Vendas Loja 2 \n")
print(loja2_DataFrame)
print("\n")

#----------------------------------------
#Identificar os vendedores que venderam em ambas as lojas

#Merge = Função para juntar dois DataFrames // on = qual coluna // how = tipo de junção --> Inner
#**Na prática usar apenas merge() sem o argumento 'how=' é a mesma coisa queusar merge(...how='inner)
vendedoresAmbasAsLojas_DataFrame = pd.merge(loja1_DataFrame, loja2_DataFrame, on=["Vendedor"], how="inner")

#_x = Loja 1
#_y = Loja 2
print("\n Vendedores que venderam em ambas as lojas \n")
print(vendedoresAmbasAsLojas_DataFrame)
print("\n")

#Exibir o nome de todas as colunas
print(vendedoresAmbasAsLojas_DataFrame.columns.values.tolist())

#---------------------------------------------
#Resumindo as colunas // suffixes = Renomeia as colunas
vendedoresLojasResumo= pd.merge(loja1_DataFrame, loja2_DataFrame[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes=(" Loja 1", " Loja 2"))
print("\n Vendedores que venderam em ambas as lojas Resumo \n")
print(vendedoresLojasResumo)
print("\n")

#---------------------------------------------
resumo = vendedoresLojasResumo[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]
print(resumo)
print("\n")

