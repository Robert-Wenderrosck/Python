listaLetras = ["A", "C", "E", "D", "F", "B"]
print(listaLetras)
listaLetras.sort() #sort / ordenando de A a Z
print(listaLetras)

listaLetras.sort(reverse=True) #sort / ordenando de Z a A
print(listaLetras)

#----------------------------------------------

listaNumeros = [4, 9, 5, 20, 16, 14, 12]
print(listaNumeros)

listaNumeros.sort() #sort / ordenando do 0 ao ...
print(listaNumeros)

listaNumeros.sort(reverse=True) #sort / ordenando do ... ao 0
print(listaNumeros)

#--------------------------------------------------

#Maiuscula e Minuscula
listaMaiMin = ["Sofá", "tv", "carro", "Casa", "Armário"]
listaMaiMin.sort() #sort diferencia as palavras com a primeira letra maiúscula e as todas minúsculas
print(listaMaiMin)

listaMaiMin.sort(key= str.lower) #resolvendo problema do sort
print(listaMaiMin)

