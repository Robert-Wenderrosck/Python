import tkinter as tk
from tkinter import ttk
from sklearn.tree import DecisionTreeClassifier

#Peso em toneladas / Número de Rodas / Capacidade de Passageiros
dados = [
        [1.5, 4, 5],
        [1.3, 4, 5],
        [1.8, 4, 4],
        [1.6, 4, 4],
        [2.0, 4, 7],


        [5.0, 6, 2],
        [7.0, 6, 2],
        [4.5, 6, 3],
        [8.0, 8, 2],
        [6.0, 8, 3],

        [0.2, 2, 2],
        [0.25, 2, 2],
        [0.3, 2, 2],
        [0.35, 2, 2],
        [0.4, 2, 2]
        ]

rotulos = ["Carro", "Carro", "Carro", "Carro", "Carro",
           "Caminhão", "Caminhão", "Caminhão", "Caminhão", "Caminhão",
           "Moto", "Moto", "Moto", "Moto", "Moto"]

clf = DecisionTreeClassifier() #Criando uma instância da classe 'DecisionTreeClassifier'
clf.fit(dados, rotulos) #Treinando o classificador com os dados e rótulos fornecidos. Método 'fit' ajusta o modelo aos dados fornecidos, permitindo que ele aprenda as relações.

def prever_veiculo():
    try:
        peso = float(entrada_peso.get())
        rodas = int(entrada_rodas.get())
        passageiros = int(entrada_passageiros.get())

        if peso < 0 or rodas < 0 or passageiros < 0:
            rotulo_resultado.config(text="Valores negativos não são permitidos.", fg="red")
            return

        novo_veiculo = [[peso, rodas, passageiros]]
        tipo_predito = clf.predict(novo_veiculo)
        rotulo_resultado.config(text=f"Classificação: {tipo_predito[0]}", fg="green")


    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos.", fg="red")

janela = tk.Tk()
janela.title("Classificação de Veículos - Árvore de Decisão")
janela.geometry("400x300")
janela.configure(bg="#f0f0f0")

quadro = ttk.Frame(janela, padding=20, relief="solid", borderwidth=2)
quadro.pack(pady=20)

rotulo_titulo = ttk.Label(quadro, text="Classificação de Veículos", font=("Arial", 14, "bold"))
rotulo_titulo.grid(row=0, column=0, columnspan=2, pady=10)

#---------------------
rotulo_peso = ttk.Label(quadro, text="Peso do veículo (toneladas):")
rotulo_peso.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entrada_peso = ttk.Entry(quadro)
entrada_peso.grid(row=1, column=1, padx=10, pady=5)
#----------------------
rotulo_rodas = ttk.Label(quadro, text="Número de rodas:")
rotulo_rodas.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entrada_rodas = ttk.Entry(quadro)
entrada_rodas.grid(row=2, column=1, padx=10, pady=5)
#---------------------
rotulo_passageiros = ttk.Label(quadro, text="Capacidade de passageiros:")
rotulo_passageiros.grid(row=3, column=0, padx=10, pady=5, sticky='e')

entrada_passageiros = ttk.Entry(quadro)
entrada_passageiros.grid(row=3, column=1, padx=10, pady=5)

botao_classificar = ttk.Button(quadro, text="Classficar", command=prever_veiculo)
botao_classificar.grid(row=4, column=0, columnspan=2, pady=5)

rotulo_resultado = tk.Label(quadro, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
rotulo_resultado.grid(row=5, column=0, columnspan=2, pady=10)





janela.mainloop()





