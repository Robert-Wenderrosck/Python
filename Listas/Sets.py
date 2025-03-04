"""
1) add - adiciona itens
2) union - unir sets
3) intersetion - retorna itens existentes em amos os conjuntos
4) symmetric_difference_update - mantém apenas os  itens que não estão presentes em ambos os conjuntos
5) symmetric_difference - retorna apenas os itens que não estão presentes em ambos os conjuntos
"""

#add - adiciona itens
setExemploNumeros = set() #Criou o set
setExemploNumeros.add(1)
setExemploNumeros.add(2)
setExemploNumeros.add(3)
setExemploNumeros.add(4)
setExemploNumeros.add(5)
setExemploNumeros.add("Amanda")

print(setExemploNumeros)
print("\n")

#add - adiciona itens exemplo2 (Esse modo de fazer set imprime os elementos aleatoriamente)
setLetras = {"A", "B", "C"}
print(setLetras)

print("\n")
#---------------------------------------------------------

#union - unir sets

set1 = {"Allan", "Berenice", "Roger"}
set2 = {39, 21, 45}

uniaoSets = set1.union(set2)
print(uniaoSets)

print("\n")
#-----------------------------------------------------------

#intersetion - retorna itens existentes em amos os conjuntos
listaSet1 = {"Python", "C++", "Java"}
listaSet2 = {"VisualG", "Lógica", "Python"}

imprimindoOsDoisParaConferir = listaSet1.union(listaSet2)
print(imprimindoOsDoisParaConferir)

valorQueEstaEmAmbosOsSets = listaSet1.intersection(listaSet2)
print(valorQueEstaEmAmbosOsSets)

print("\n")
#--------------------------------------------------------------

#symmetric_difference_update - mantém apenas os  itens que não estão presentes em ambos os conjuntos

listaSet1.symmetric_difference_update(listaSet2)
print(listaSet1)

print("\n")
#---------------------------------------------------------------

#symmetric_difference - retorna apenas os itens que não estão presentes em ambos os conjuntos

listaS1 = {"Python", "C++", "Java"}
listaS2 = {"VisualG", "Lógica", "Python"}

naoEstaoEmAmbos = listaS1.symmetric_difference(listaS2)

print("\n")
#---------------------------------------------------------------

#Sets não aceitam valores repetidos
setNumero = {1, 2, 3, 4, 5, 6, 6, 7, 8}
print(setNumero)
print(len(setNumero))


