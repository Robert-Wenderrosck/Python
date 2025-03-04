class Dados:
    def __init__(self, nome, idade, estadoCivil, salario):
        self.nome = nome
        self.idade = idade
        self.estadoCivil = estadoCivil
        self.salario = salario

    def imprimirDados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Estado Civil:", self.estadoCivil)
        print("salário:", self.salario)
        print("------------------------------")

