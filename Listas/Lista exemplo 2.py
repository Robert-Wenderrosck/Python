listaMinMax = [5, 10, 20, 100,  50, 300]

print(min(listaMinMax)) #Imprime o valor mínimo
print(max(listaMinMax)) #Imprime o valor máximo

#--------------------------------------------

#Lista de 0 ate 10
listaNumero1ate10 = [posicao for posicao in range(100)]

print(listaNumero1ate10)


listaNumero1ate100 = [posicao1 for posicao1 in range(100) if posicao1 <=10]

print(listaNumero1ate100)

print("\n\n")
#---------------------------------------------

listaDoisEmDois = list(range(0, 100, 2))
print(listaDoisEmDois)

print("\n\n")
#---------------------------------------------

listaOriginal = ["Carro", "Moto", "Bicicleta", "Lancha"]
listaCopiada = listaOriginal.copy() #copiando a lista

print(listaCopiada)

print("\n\n")
#---------------------------------------------

lista1Letras = ["A", "B", "C"]
lista2Numeros = [1, 2, 3]

#Join unindo listas
listaJoin = lista1Letras + lista2Numeros
print(listaJoin)

print("\n\n")
#-----------------------------------------------

l1 = ["a1", "b1", "c1"]
l2 = [11, 12, 13]

for item in l2:
    l1.append(item)

print(l1)
