#while = enquanto

numero = 1
while numero < 11:
    print(numero)
    numero += 1 #numero = numero + 1

#-----------------------------
print("\n")

num = 1
while num <= 1000:
    print("Número:",num)

    #Quando o número chegar a 5 pare
    if num == 5:
        break #parar
    num += 1

#-----------------------------
print("\n")

n = 0
while n < 10:
    n += 1

    #Pula o número 6
    if n == 6:
        continue #comando "continue" faz pular o comando em seguida
    print(n)

#-----------------------------
print("\n")

contador = 0

while contador < 10:
    contador += 1
    print("Número", contador)
else:
    print("Números impressos com sucesso!")
