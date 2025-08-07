import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier

#Altura em metros / Presença de folhas (1 para sim, 0 para não) / Precisa de muita água (1 para sim, 0 para não)
dados = [
        [0.5, 1,1], [0.6, 1,1], [0.7, 1,1], [0.8, 1,1], [0.9, 1,1],

        [10, 1, 1], [12, 1, 1], [15, 1, 1], [20, 1, 0], [25, 1, 0],

        [1.0, 0, 0], [1.2, 0, 0], [0.8, 0, 0], [0.9, 0, 0], [1.5, 0, 0]
        ]

rotulos = [
            "Flor", "Flor", "Flor", "Flor", "Flor",

            "Árvore", "Árvore", "Árvore", "Árvore", "Árvore",

            "Cacto", "Cacto", "Cacto", "Cacto", "Cacto"
           ]

clf = RandomForestClassifier(n_estimators=10) #Random Forest é um método de aprendizado de máquina que opera construindo uma multiplicidade de árvores de decisão durante o treinamento e produzindo a classe que é a moda das classes (classificação) das árvores individuais.
clf.fit(dados, rotulos) #Treinando o classificador com os dados e rótulos fornecidos

def prever_planta():
    try:
        altura = float(entrada_altura.get())
        tem_folhas = 1 if entrada_folhas.get().lower() == "sim " else 0
        muita_agua = 1 if entrada_agua.get().lower() == "sim" else 0

        if altura < 0:
            rotulo_resultado.config(text="Altura não pode ser negativa.", fg="red")
            return

        
        nova_planta = [[altura, tem_folhas, muita_agua]]

        tipo_predito = clf.predict(nova_planta)

        rotulo_resultado.config(text=f"Classificação: {tipo_predito}", fg="green")


    except ValueError:
        rotulo_resultado.config(text="Por favor, insira valores numéricos válidos!", fg="red")



janela = tk.Tk()
janela.title("Classificação de Plantas - Random Forest")
janela.geometry("400x300")
janela.configure(bg="#f0f0f0")

quadro = ttk.Frame(janela, padding=20, relief="solid", borderwidth=2)
quadro.pack(pady=20)

rotulo_titulo = ttk.Label(quadro, text="Classificação de Plantas", font=("Arial", 14, "bold"))
rotulo_titulo.grid(row=0, column=0, columnspan=2, pady=10)

rotulo_altura = ttk.Label(quadro, text="Altura da planta (em metros):")
rotulo_altura.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entrada_altura = ttk.Entry(quadro)
entrada_altura.grid(row=1, column=1, padx=10, pady=5)


rotulo_folhas = ttk.Label(quadro, text="Tem folhas (sim/não):")
rotulo_folhas.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entrada_folhas = ttk.Entry(quadro)
entrada_folhas.grid(row=2, column=1, padx=10, pady=5)


rotulo_agua = ttk.Label(quadro, text="Precisa de muita água (sim/não):")
rotulo_agua.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entrada_agua = ttk.Entry(quadro)
entrada_agua.grid(row=3, column=1, padx=10, pady=5)


botao_classificar = ttk.Button(quadro, text="Classificar", command=prever_planta)
botao_classificar.grid(row=4, column=0, columnspan=2, pady=10)

rotulo_resultado = tk.Label(quadro, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
rotulo_resultado.grid(row=5, column=0, columnspan=2, pady=10)


janela.mainloop()



