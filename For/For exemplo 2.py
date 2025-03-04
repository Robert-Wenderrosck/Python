listaNomes = ["Bia", "Raquel", "Allan", "Mafalda"]

for posicao in listaNomes:
    if posicao == "Allan":
        continue #Comando para pular o nome "Allan" e continuar para os outros elementos da lista
    print(posicao)

#----------------------------------
print("\n")

for i in range(11): #Range consegue contar de 0 até o 10
    print(i)

print("\n")

#range(start, stop e step)
#range(start = 1, stop = 10, step = 1) / step = contagem de 1 em 1...

#contar de 1 até 10
for posicao in range(1, 11, 2):
    print("Número:",posicao)

print("\n")

#contar do 20 até 10
for i in range(20, 9, -1):
    print("Posição:",i)