"""
Classes - São as especificações de um ou mais objetos, ou seja, é um conjunto de objetos/ regras
Objetos - É uma instância (um item da classe)

"""

class minhaPrimeiraClasse:
    idade = 30
    nome = "João"

pegaIdade = minhaPrimeiraClasse()
print(pegaIdade.idade)
print(pegaIdade.nome)
print("Nome:", pegaIdade.nome, "-Idade:", pegaIdade.idade)

print("\n")
#-------------------------------------------------------------------------------

class Aluno:
    #Propriedade (são os objetos)
    nome = " "
    idade = 0
    altura = 0

#Instanciar o objeto da classe
dados = Aluno()
dados.nome = "Cintia"
dados.idade = 21
dados.altura = 1.69

print("Estudante:", dados.nome)
print("Idade:", dados.idade)
print("Altura:", dados.altura)

print("\n")
#-------------------------------------------------------------------------------

class Turma:
    #def é um construtor - metodo construtor (O metodo construtor em Python é __init__), self é um parametro da propria classe
    def __init__(self, nomeAluno, idadeAluno, alturaAluno):
        self.nome = nomeAluno
        self.idade = idadeAluno
        self.altura = alturaAluno

    def imprimir(self):
        print("Estudante:", self.nome)
        print("Idade:", self.idade)
        print("Altura:", self.altura)
        print("------------------------")

#Instanciar o objeto da classe
aluno1 = Turma("Pedro", 31, 1.72)
aluno2 = Turma("Roseli", 21, 1.65)
aluno3 = Turma("Alberto", 25, 1.89)

aluno1.imprimir()
aluno2.imprimir()
aluno3.imprimir()




