"""
Operador
and Operador (E)
or Operador (OU)
not Operador (NÃO)
"""

numero1 = 25
numero2 = 21
numero3 = 40

#Operador "and"
if numero1 > numero2 and numero3 > numero1:
    print("Ambas as condições são verdadeiras")

nome = "Matheus"
idade = 21

if nome == "Matheus" and idade >= 18:
    print("Matheus é maior de idade")

usuario = "Jorge"
senha = 123

if usuario == "Jorge" and senha == 123:
    print("Usuário logado com sucesso!")
else:
    print("Usuário ou senha inválidos")


#Operador "or"
n1 = 10
n2 = 15
n3 = 20

if n1 > n2 or n1 > 5:
    print("Pelo menos uma das condições é VERDADEIRO")

fruta = "Laranja"

if fruta == "Maça" or fruta == "Laranja":
    print("A fruta é Maça ou Laranja")

#Operador "not"

letra = ""

if not letra:
    print("Não foi encontrado nenhuma letra")

numeroTestado = 0

if not numeroTestado:
    print("O número não pode ser 0 popis 0 é considerado um boleano do tipo FALSE")