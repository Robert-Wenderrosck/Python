linha = 0

#while = enquanto
while linha < 3:
    coluna = 0
    while coluna < 3:
        print("Linha:", linha, " - Coluna:", coluna)
        coluna += 1 #coluna = coluna + 1
                    #0 + 1 = 1 / 1 + 1 = 2
    linha += 1

#----------------------------------------
print("\n")

numeroInicial = 1
numeroFinal = int(input("Digite um número maior que 1: ")) #"input" pede para o usuário digitar um número e "int" faz o que foi escrito ser convertido em um número

while numeroInicial <= numeroFinal:
    print("Escolhi:", numeroInicial)
    numeroInicial += 1

#----------------------------------------
print("\n")

numero = 1
numeroPar = int(input("Digite um número maior que 1: "))

while numero <= numeroPar:
    if numero % 2 == 0: #Verifica se o número é par
        print(numero, end=" ") #Comando "end=" consegue fazer os valores ficarem na mesma linha
    numero += 1
