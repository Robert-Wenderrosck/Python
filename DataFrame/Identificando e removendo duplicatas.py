import pandas as pd

baseVendas_DataFrame = pd.read_excel("Base_Vendas.xlsx")

print("\n Imprimindo os dados \n")
print(baseVendas_DataFrame)
print("\n")

#nunique = resumo dos itens, conta quantos valores únicos tem
resumoValoresUnicos = baseVendas_DataFrame.nunique()
print("\n Resumo valores únicos com a função nunique \n")
print(resumoValoresUnicos)
print("\n")

#subset = Identifica a coluna que se quer verificar a duplicidade
#keep = Controla como considerar o valor da duplicidade (First -> Considera o primeiro valor como falso, Last -> Considera o último valor como falso, False -> Considera todos como duplicados)
confereDuplicidades = baseVendas_DataFrame.duplicated(subset="Vendedor", keep="first")
print("\n Resumo valores únicos com a função duplicated \n")
print(confereDuplicidades)
print("\n")

baseVendas_DataFrame["Confere Duplicidade"] = baseVendas_DataFrame.duplicated(subset="Vendedor", keep="first")
print("\n Adicionando nova coluna (Informação Duplicada) \n")
print(baseVendas_DataFrame)
print("\n")

#drop_duplicates = removendo valores duplicados
removerDuplicidade = baseVendas_DataFrame.drop_duplicates(subset="Vendedor", keep="first")
print("\n Após remover as duplicidades \n")
print(removerDuplicidade)
print("\n")
