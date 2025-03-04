#A função print é uma função que recebe o parametro que digitamos e imprime o resultado na tela
print("Exemplo 1 de função")


print("\n")

#Uma função
def minhaPrimeiraFuncao():
    print("Essa é a minha primeira função criada com Python")

minhaPrimeiraFuncao()

#-----------------------------------------------
print("\n")

def funcaoTexto(nome):
    print(nome, "Santos")

funcaoTexto("Ana")
funcaoTexto("Roger")
funcaoTexto("Marcos")

#-------------------------------------------------
print("\n")

def funcaoSaudacao(saudacao, nome):
    print(saudacao, nome)

funcaoSaudacao("Boa noite", "Ana")
funcaoSaudacao("Boa noite", "Cesar")
funcaoSaudacao("Boa noite", "Luiza")

#-------------------------------------------------
print("\n")

#Função com 2 argumentos
def funcaoComArgumentos(nome, sobrenome):
    print("Nome completo:", nome, sobrenome)

nomeInput = input("Digite o seu nome: ")
sobrenomeInput = input("Digite o seu sobrenome: ")

funcaoComArgumentos(nomeInput, sobrenomeInput)
