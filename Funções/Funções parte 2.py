def funcaoDivisao(numero1, numero2):
    return numero1 / numero2

resultado = funcaoDivisao(10, 2)
print(resultado)

#-----------------------------------------------------
print("\n")

def funcaoMedia(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

media = funcaoMedia(10, 6, 8, 10)

print(media)

#------------------------------------------------------
print("\n")

#Função com argumentos arbitrários, *args
def frutaPreferida(*fruta):
    print("Eu gosto de ", fruta[0])
    print("Eu gosto de ", fruta[1])
    print("Eu gosto de ", fruta[2])
    print("Eu gosto de ", fruta[3])

frutaPreferida("Banana", "Goiaba", "Laranja", "Kiwi")

#----------------------------------------------------------
print("\n")

def unirListas(*listas):
    print(listas)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

unirListas(*lista1, *lista2)

#----------------------------------------------------------
print("\n")

#Se o número de argumentos da palavra-chave for desconhecido adicionamos ** antes do nome do parâmetro
def funcaoKwargs(**parametro):
    print("Eu moro em", parametro["cidade1"])
    print("Eu moro em", parametro["cidade2"])

funcaoKwargs(cidade1 = "SP", cidade2 = "RJ")



