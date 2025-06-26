import pandas as pd

dataFrameDados = pd.read_excel("Deletar_Linhas_Colunas.xlsx")
print(dataFrameDados)
print("\n")
print(type(dataFrameDados))
print("\n")


deletandoLinhasEmBranco = dataFrameDados.dropna()
print("\n-----dropna = deleta linhas que tenham pelo menos 1 valor vazio------\n")
print(dataFrameDados)
print("\n")

del deletandoLinhasEmBranco["Produto"]
print("\n-----del = deletou a coluna Produto------\n")
print(dataFrameDados)
print("\n")

deletarDuasColunas = deletandoLinhasEmBranco.drop(columns=["Data Venda", "Total Vendas"])
print("\n-----drop = usa-se para deletar as colunas específicadas (Data Venda e Total Vendas)------\n")
print(deletarDuasColunas)
print("\n")

#Axis = eixo(1 - Coluna, 0 - Linha)
excluirLinha3 = deletarDuasColunas.drop(2, axis=0)
print("\n-----Excluindo a linha 3------\n")
print(excluirLinha3)
print("\n")

#Axis = eixo(1 - Coluna, 0 - Linha)
excluirMaisLinhas = excluirLinha3.drop([0,1])
print("\n-----Excluindo linhas 0 e 1------\n")
print(excluirMaisLinhas)
print("\n")
