listaLetras = ["A", "B", "C", "D", "E"]

#Diferença do FOR para o WHILE: o FOR não precisa colocar (variável + 1) para continuar rodando

#for = para
for posicao in listaLetras:
    print("Letra:", posicao)

print("\n")

for posicaoLetra, letra in enumerate(listaLetras):
    print(posicaoLetra, letra) #Sempre conta da posição 0

print("\n")

for posicaoLetraFrase in "Phyton":
    print(posicaoLetraFrase)

print("\n")

listaCores = ["amarelo", "vermelho", "laranja", "rosa"]

for posicaoCor in listaCores:
    if posicaoCor == "laranja":
        print("Cor laranja encontrada com sucesso!")
        break
