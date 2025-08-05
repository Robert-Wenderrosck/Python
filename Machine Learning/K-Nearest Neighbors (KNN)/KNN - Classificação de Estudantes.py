from sklearn.neighbors import KNeighborsClassifier

#Nota do aluno / N° de faltas
dados = [
        [6.0, 5],
        [6.5, 4],
        [7.0, 2],
        [7.5, 3],
        [8.0, 3],
        [8.5, 2],
        [9.0, 1],
        [9.5, 0],
        [10.0, 1],

        [2.5, 9],
        [3.0, 10],
        [3.5, 9],
        [4.0, 8],
        [4.5, 7],
        [5.0, 6],
        [5.5, 5],
        [5.5, 8],
        [5.8, 4]
]

#Situação do aluno de acordo com a nota e o n° de faltas
rotulos = ["Aprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado", "Aprovado",
           "Reprovado", "Reprovado", "Reprovado", "Reprovado", "Reprovado", "Reprovado", "Reprovado", "Reprovado", "Reprovado"]

knn =KNeighborsClassifier(n_neighbors=3) #Algoritmo analisa para os 3 estudantes mais próximos (em termos de nota e faltas)
knn.fit(dados, rotulos) 

def classificar_estudante():
    print("\n--- Menu de Classificação de Estudante ---")

    try:
        nota = float(input("Digite a nota do aluno: "))
        faltas = int(input("Digite o número de faltas do aluno: "))

        if nota < 0 or faltas < 0:
            print("Nota ou faltas não podem ser negativas. Tente novamente.")
            return

        novo_estudante = [[nota, faltas]]
        classe_predita = knn.predict(novo_estudante)
        print(f"O aluno foi classificado como: {classe_predita[0]}")

    except ValueError:
        print("Por favor, insira valores válidos (números).")

def main():
    while True:
        classificar_estudante()

        continuar = input("Deseja classificar outro aluno? (s/n): ").lower()

        if continuar != 's':
            print("Encerrando o programa.")
            break

main()