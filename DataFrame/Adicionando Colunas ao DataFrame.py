import pandas as opcoesPandas

notasAlunos_DataFrame = opcoesPandas.DataFrame({
    "Nome" : ["Ana", "Pedro", "João"],
    "Nota 1" : [9, 7, 10],
    "Nota 2" : [6, 9, 8],
    "Nota 3" : [7, 5, 10],
    "Nota 4" : [10, 10, 6]
})

print("\n------------- DataFrame Dicionário Notas Alunos -----------\n")
print(notasAlunos_DataFrame)
print("\n")

#-------------------------------------------
notasAlunos_DataFrame["Média"] = (notasAlunos_DataFrame["Nota 1"] + notasAlunos_DataFrame["Nota 2"] + notasAlunos_DataFrame["Nota 3"] + notasAlunos_DataFrame["Nota 4"]) / 4
print("\n--------------DataFrame com uma nova coluna (média)---------\n")
print(notasAlunos_DataFrame)
print("\n")

#--------------------------------------------

notasAlunos_DataFrame["Faltas"] = 5
print("\n--------------DataFrame com uma nova coluna (faltas com valor padrão)---------\n")
print(notasAlunos_DataFrame)
print("\n")

#--------------------------------------------

notasAlunos_DataFrame["Faltas"] = (8, 9, 15)
print("\n--------------DataFrame substituindo valores na coluna de faltas---------\n")
print(notasAlunos_DataFrame)
print("\n")

#--------------------------------------------

notasAlunos_DataFrame["Faltas"] = (8, 9, 15)
print("\n--------------DataFrame substituindo valores na coluna de faltas---------\n")
print(notasAlunos_DataFrame)
print("\n")

#--------------------------------------------

#loc = localizar (índice 1, coluna "Nota 2" --> Pedro/Nota 2
notasAlunos_DataFrame.loc[1, "Nota 2"] = 12
print("\n--------------DataFrame alterando o valor da Nota 2 do Pedro---------\n")
print(notasAlunos_DataFrame)
print("\n")

#--------------------------------------------
notasAlunos_DataFrame["Média"] = (notasAlunos_DataFrame["Nota 1"] + notasAlunos_DataFrame["Nota 2"] + notasAlunos_DataFrame["Nota 3"] + notasAlunos_DataFrame["Nota 4"]) / 4
print("\n--------------DataFrame recalculando a média---------\n")
print(notasAlunos_DataFrame)
print("\n")


