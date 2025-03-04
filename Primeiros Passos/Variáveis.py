nota1 = nota2 = nota3 = nota4 = media = 0 #adicionou variáveis e atribuiu o valor 0
aluno = "Robert Carvalho"

print(aluno)

nota1 = 9
print(nota1)

#Comando input serve para o usuário digitar a informação
aluno = input("Digite o nome do aluno:")
nota1 = input("Digite a nota 1: ") #O comando input vai salvar a nota no formato de texto
nota2 = input("Digite a nota 2: ")
nota3 = input("Digite a nota 3: ")
nota4 = input("Digite a nota 4: ")

#Para somar as notas vai precisar transformar as notas de texto para números (comando float)
media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

print("Aluno: " + aluno)
print("Média:", media)
