dicionario = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42
}

print(dicionario) #Imprimindo
print(len(dicionario)) #Imprimindo a quantidade de linhas
print(type(dicionario)) #Imprimindo o tipo
print("\n")

#Copiando dicionario exemplo 1
dicionario2 = dicionario.copy() #copiando o dicionario
print("Exemplo dicionario2:", dicionario2)

#Copiando dicionario exemplo 2
dicionario3 = dict(dicionario)
print("Exemplo dicionario3:", dicionario3)

#---------------------------------------------------------------
print("\n")

dicionarioPessoas = {
    "Ana": 21,
    "Marcela": 34,
    "Pedro": 42,
    "Pedro": 53  #Em elementos repetidos ele pega o último
}

print(dicionarioPessoas)

#Pegar a idade da Marcela
dados = dicionarioPessoas["Marcela"]
dados2 = dicionarioPessoas.get("Pedro")
print(dados)
print(dados2)

#Pegar somente os nomes (coluna 1)
nomes = dicionarioPessoas.keys()
print(nomes)

#Pegar as idades (coluna 2)
idades = dicionarioPessoas.values()
print(idades)

#-----------------------------------------------------------------------
print("\n\n")

alimentos = {
    "arroz": 35.90,
    "macarrão": 21.90,
    "feijão": 29
}

print(alimentos)

#Alterando o preço do macarrão
alimentos["macarrão"] = 39.
print(alimentos)

#Alterando o preço do feijão
alimentos.update({"feijão": 31})
print(alimentos)

#Adicionando item no dicionário
alimentos["salsicha"] = 35
print(alimentos)

#pop remove o item do dicionário
alimentos.pop("salsicha")
print(alimentos)

#Remove o último item do dicionário
alimentos.popitem()
print(alimentos)

#Removo todos os itens de uma única vez
alimentos.clear()
print(alimentos)

#Adcionando novamente os itens no dicionário
alimentos["arroz"] = 35.90
alimentos["macarrão"] = 21.90
alimentos["feijão"] = 29

print("\n\n")
print(alimentos)

#Deletando o arroz
del alimentos["arroz"]
print(alimentos)

if "macarrão" in alimentos:
    print("Alimento encontrado com sucesso!")
else:
    print("O alimento não foi encontrado na lista")

#------------------------------------------------------------

print("\n\n")

letras = {
    "Letra 1" : "A",
    "Letra 2" : "B",
    "Letra 3" : "C",
    "Letra 4" : "D",
    "Letra 5" : "E",
    "Letra 6" : "F",
}
print(letras)

#Imprimindo os títulos (primeira coluna)
for posicao in letras:
    print(posicao)

#Imprimindo os valores
for i in letras:
    print(letras[i])

print("\n")

#Imprimindo os valores exemplo 2
for contador in letras.values():
    print(contador)

print("\n")

for titulo, valor in letras.items():
    print(titulo, "-", valor)

#-----------------------------------------------------------

exemplo1 = {
    "A" : 1,
    "B" : 2
}

exemplo2 = {
    "C" : 3,
    "D" : 4
}

exemplo3 = {
    "E" : 5,
    "F" : 6
}

unirVariosDicionario = {
    "Dicionário 1:" : exemplo1,
    "Dicionário 2:" : exemplo2,
    "Dicionário 3:" : exemplo3
}

print(unirVariosDicionario)

#-------------------------------------------------
print("\n\n")

escola = {
    "Turma 1" : {
        "Andre:" : 10,
        "Amanda:" : 8
    }
    "Turma 2" : {
        "Cesar:" : 6,
        "Alessandra:" : 7
    }
    "Turma 3" : {
        "Roger:" : 9,
        "Rosiane:" : 10
    }
}

for tur1, tur2 in escola.items():
    print(tur1)
    for tur1, tur2 in tur2.items():
        print("Aluno:", tur1, "- Nota:", tur2)

