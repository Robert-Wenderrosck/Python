nome = "Cíntia Alves Moreira"
print(nome)

#Contar caracteres
print("Total de caracteres: " + str(len(nome))) #Comando len para contar o "tamanho" da string, comando str para converter para texto


print(nome[0]) #Retornar só a letra C
print(nome[0:5]) #Retornar as 5 primeiras letras
print(nome[7:12]) #Retorna o primeiro sobrenome
print(nome[7:])

#-------------------------------------------------------

frase = "CUrSo de LóGica De PROgramação PyTHon"

#.upper retorna todas as letras em maiúscula
print(frase.upper())

#.lower retorna todas as letras em minúscula
print(frase.lower())

#-------------------------------------------------------

#.replace muda algo na variável
notaProva = "Tirei nota cinco na prova"

print(notaProva.replace("cinco","dez"))

#-------------------------------------------------------

cpf = "123.456.789-10"

#.split vai criar uma separação conforme um critério selecionado
cpfPartes = cpf.split(".")
print(cpfPartes)
print(cpfPartes[0])
print(cpfPartes[1])

cpfPartes2 = cpfPartes[2].split("-")
print(cpfPartes2[0])
print(cpfPartes2[1])

print("CPF: " + cpfPartes[0] + cpfPartes[1] + cpfPartes2[0] + cpfPartes2[1])

print("\n\n")

#---------------------------- Parte 2 ---------------------------

palavraComEspaco = "              Curso de Phyton           "

print(palavraComEspaco)
#.strip remove os espaços do texto
print(palavraComEspaco.strip())

#-------------------------------------------------------

gostoPorFrutas = "Eu gosto de laranja"
print("laranja" in gostoPorFrutas) #Pergutando se tem a palavra "laranja" no texto da variável
print("maça" in gostoPorFrutas)

resultado = gostoPorFrutas.find("o")

print(resultado)

#-------------------------------------------------------

ganhadorCopa = "Brasil ganhou a copa do mundo"

campeao = "Brasil" not in ganhadorCopa #Perguntando se a palavra NÃO ESTÁ no texto da variável

print(campeao)

#-------------------------------------------------------

aluno = "Rebeca Martins"
nota1 = 9.523
nota2 = 6.2
media = (nota1 + nota2) / 2

#NÃO PODE COLOCAR "+" PARA CONCATENAR VARIÁVEL STRING COM VARIÁVEL INTEIRO (Tem que usar str para converter número em texto)
print("Aluna: " + aluno + " - Média: " + str(media))

print(f"Aluna: {aluno} - Média: {media}") #outra forma de fazer

ajusteTexto = "Aluna: {} - Média: {}"
print(ajusteTexto.format(aluno, media)) #outra forma de fazer

#Ajustar os valores das casas decimais (2 casas)
print(f"Aluna: {aluno} - Média: {media:.2f}")

#Ajustar os valores das casas decimais (2 casas)
ajusteTexto = "Aluna: {} - Média: {:.2f}"
print(ajusteTexto.format(aluno, media))


