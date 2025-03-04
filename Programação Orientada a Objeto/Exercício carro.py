class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = 0  # Inicialmente zero

    def drive(self, km):
        if km > 0:
            self.quilometragem += km
        else:
            print("A quilometragem percorrida deve ser positiva.")

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano}): {self.quilometragem} km"

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Dirigindo o carro por 150 km
meu_carro.drive(150)

# Imprimindo a descrição do carro
print(meu_carro.descricao())

