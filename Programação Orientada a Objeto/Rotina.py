class Rotina:

    def __init__(self, nome, dormindo=False, dirigindo=False):
        self.nome = nome
        self.dormindo = dormindo
        self.dirigindo = dirigindo


    def dormir(self):

        if self.dirigindo:
            print(self.nome + " não pode dormir enquanto dirige")
            return #para encerrar a operação

        if self.dormindo:
            print(self.nome + " já está dormindo")
            return #para encerrar a operação

        print("O " + self.nome + " está dormindo")
        self.dormindo = True

    def acordar(self):

        if not self.dormindo:
            print(self.nome + "já está acordado!")
            return

        print("O " + self.nome + " acordou")
        self.dormindo = False

    def dirigir(self):

        if self.dormindo:
            print(self.nome + " não pode dirigir enquanto está dormindo")
            return

        if self.dirigindo:
            print(self.nome + " já está dirigindo")
            return

        print("O " + self.nome + " está dirigindo")
        self.dirigindo = True

    def pararDeDirigir(self):

        if not self.dirigindo:
            print(self.nome + " já parou de dirigir")

        print("O " + self.nome + " parou de dirigir")
        self.dormindo = False
