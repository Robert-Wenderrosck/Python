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

