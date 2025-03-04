lista1 = ["A", "B", "C"]
lista2 = ["D", "E", "F"]

lista1.extend(lista2) #Com extend unimos duas listas

print(lista1)

#------------------- Removendo os elementos --------------------------

lista1.remove("E") #Removendo a letra da lista
print(lista1)

lista1.pop(2) #Removendo com o pop o segundo elemento da lista (lembrando que começa do 0)
print(lista1)

lista1.pop() #Removendo o último elemento da lista
print(lista1)

del lista1[0] #Removendo o primeiro elemento da lista
print(lista1)

lista1.clear() #Removendo todos os itens da lista
print(lista1)

#------------------- Adicionando os elementos --------------------------
print("\n")

lista1.append("Maça") #Adicionando itens na lista
print(lista1)

lista1.insert(1, "Goiaba") #Adicionando item na segunda posição
print(lista1)

lista1.insert(1, "Laranja") #Adicionando item na segunda posição
print(lista1)

#Localizar item na lista
if "Laranja" in lista1:
    print("Sim, a Laranja existe na lista")
else:
    print("Não encontramos a fruta")

lista1[2] = "Banana" #Substituindo uma variável da lista

print(lista1)

lista1[1:3] = ["A", "b"]

print(lista1)


