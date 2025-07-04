import pandas as pd

vendas_DataFrame = pd.read_excel("Groupby.xlsx")
print("\n DataFrame Vendas \n")
print(vendas_DataFrame)
print("\n")

#groupby - Agrupa pela coluna de Vendedor e usando o mean para calcular a média das colunas
#.select_dtypes(include="number").columns = faz com que selecione apenas as colunas com valores numéricos para calcular a média
#.round(1) = Mostra apenas 1 casa após a vírgula
mediaVendedor = vendas_DataFrame.groupby("Vendedor")[vendas_DataFrame.select_dtypes(include="number").columns].mean().round(1)
print("\n Agrupando pela coluna de Vendedor e calculando a média de cada coluna \n")
print(mediaVendedor)
print("\n")

#groupby - Agrupa pela coluna de Vendedor e usando o mean para calcular a soma das colunas
#.select_dtypes(include="number").columns = faz com que selecione apenas as colunas com valores numéricos para calcular a soma
somaVendedor = vendas_DataFrame.groupby("Vendedor")[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pela coluna de Vendedor e calculando a soma de cada coluna \n")
print(somaVendedor)
print("\n")

#------------------------------------------------
deixandoValoresEmBranco = vendas_DataFrame.groupby(by=["Vendedor"], dropna=False)[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pela coluna de Vendedor e considera valores em branco \n")
print(deixandoValoresEmBranco)
print("\n")

#------------------------------------------------
removendoValoresEmBranco = vendas_DataFrame.groupby(by=["Vendedor"], dropna=True)[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pela coluna de Vendedor e não considera valores em branco \n")
print(removendoValoresEmBranco)
print("\n")

#------------------------------------------------
agrupaDuasColunas = vendas_DataFrame.groupby(["Vendedor", "Produto"])[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pelas colunas de Vendedor e Produto e faz uma soma dos valores \n")
print(agrupaDuasColunas)
print("\n")

#------------------------------------------------
agrupaFrutasVendedor = vendas_DataFrame.groupby(["Produto", "Vendedor"])[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pelas colunas de Produto e Vendedor e faz uma soma dos valores \n")
print(agrupaFrutasVendedor)
print("\n")

#------------------------------------------------
agrupaDataVendedor = vendas_DataFrame.groupby(["Data Venda", "Vendedor"])[vendas_DataFrame.select_dtypes(include="number").columns].sum()
print("\n Agrupando pelas colunas de Data Venda e Vendedor e faz uma soma dos valores \n")
print(agrupaDataVendedor)
print("\n")



















