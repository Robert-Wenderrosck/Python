"""
A diferença das listas para Tuplas é que não podemos editar os elementos da Tupla,
não podemos adicionar elementos, não podemos remover elementos

Só pode criar uma tupla se tiver mais de um item (usa-se espaço ao invés de chaves)
"""

tuplaLetras = ("A", "B", "C", "D")

print(tuplaLetras) #Imprimindo a tupla
print(type(tuplaLetras)) #Imprimindo o tipo da tupla
print(len(tuplaLetras)) #Tamanho da tupla
print(tuplaLetras[0]) #Acessando os itens da tupla
print(tuplaLetras[1])
print(tuplaLetras[-1]) #Acessando o último item da tupla

#----------------------------------------------------

novaTupla = ("E",) #Cria uma nova tupla
print(novaTupla)
print(type(novaTupla))

tuplaLetras += novaTupla #Unindo as tuplas (não consegue adicionar elementos, mas consegue unir tuplas)

print("\n")
print(tuplaLetras)

print("\n")
#-----------------------------------------------------

tuplaNumeros = (1, 2, 3, 4, 5, 6, 7)
print(tuplaNumeros)
listaNumeros = list(tuplaNumeros) #Convertendo tupla em lista
listaNumeros.remove(4) #Removendo o item 4 da lista
tuplaNumeros = tuple(listaNumeros) #Convertendo a lista em tupla

print("\n")
print(tuplaNumeros)
print("\n")

#-------------------------------------------------------

#Imprimindo itens da tupla
tuplaFrutas = ("Bananas", "Abacaxi", "laranja", "Maça")

for item in tuplaFrutas:
    print(item)
