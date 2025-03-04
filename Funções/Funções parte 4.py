#Variável no escopo global
nome = "Silvana"

def funcao1():
    print(nome)

def funcao2():
    print(nome)

funcao1()
funcao2()

#---------------------------------------------------
print("\n")

nomeSobrenome = "Steven Jobs"

def funcaoNomeSobrenome():
    print(nomeSobrenome)

def funcaoNomeSobrenome2():
    #Escopo local - Variável local (Quando mudamos o valor da variável dentro da função não estamos mudando o valor, estamos criando uma nova variável)
    nomeSobrenome = "Bill Gates"
    print(nomeSobrenome)

funcaoNomeSobrenome()
funcaoNomeSobrenome2()
print(nomeSobrenome)

#---------------------------------------------------
print("\n")

idade = 32

def funcaoIdade1():
    print(idade)

def funcaoIdade2():
    #Declarando como global, conseguimos alterar a variável dentro das funções. Fazer isso não é recomendado.
    global idade
    idade = 34
    print(idade)

funcaoIdade1()
funcaoIdade2()
print(idade)
