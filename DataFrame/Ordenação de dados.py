import pandas as pd

baseVendas_DataFrame = pd.read_excel("Ordenação.xlsx")

print("\n Imprimindo dados \n")
print(baseVendas_DataFrame)
print("\n")

#sort_values = ordena a coluna (Pode ordenar valores, datas e textos) // by = indica a coluna a ser ordenada
ordenarVendedor = baseVendas_DataFrame.sort_values(by="Vendedor")

print("\n Ordenando pela coluna de vendedor \n")
print(ordenarVendedor)
print("\n")

#A ordenação em conjunto funciona em ordem hirárquica de acordo com as colunas que forem colocadas no "by"
ordenarVariasColunas = baseVendas_DataFrame.sort_values(by=["Vendedor", "Produto"])
print("\n Ordenando várias colunas \n")
print(ordenarVariasColunas)
print("\n")

#ascending = Ordena do menor para o maior (=True) ou ao contrário (=False)
ordenarZaA = baseVendas_DataFrame.sort_values(by="Vendedor", ascending=False)
print("\n Ordenando coluna Vendedor de Z a A \n")
print(ordenarZaA)
print("\n")
