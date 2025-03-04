listaNome = ["Allan", "Bruna", "Leticia", "Clarice", "Simone", "Carla"]

#Imprimindo os itens de uma lista / MELHOR
for posicao in listaNome:
    print(posicao)

print("\n\n")

#Exemplo impressão com for 2
[print(item) for item in listaNome]

print("\n\n")

contador = 0
while contador < len(listaNome):
    print(listaNome[contador])
    contador = contador + 1

print("\n\n")
#-------------------------------------------
listaNomeC = []

for item in listaNome:
    if "c" in item:
        listaNomeC.append(item) #append adiciona os itens com a letra "c" na variável listaNomeC

print(listaNomeC)

print("\n\n")
#--------------------------------------------

listaMaiuscula = [item.upper() for item in listaNome]
print(listaNome)
print(listaMaiuscula)

listaMinuscula = [item.lower() for item in listaNome]
print(listaMinuscula)



