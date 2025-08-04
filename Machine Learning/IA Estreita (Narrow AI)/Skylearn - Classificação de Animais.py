from sklearn import tree
import tkinter as tk


janela = tk.Tk()
janela.title("Classificação de Animais")
janela.config(bg="#f0f0f0")


tk.Label(text="Peso (kg):", font=("Arial", 11)).grid(row=0, column=1, padx=5, pady=5)
peso = tk.Entry(janela)
peso.grid(row=0, column=2)

tk.Label(text="Altura (cm):", font=("Arial", 11)).grid(row=1, column=1, padx=5, pady=5)
altura = tk.Entry(janela)
altura.grid(row=1, column=2)

# Características dos animais: [peso, altura]
caracteristicas = [

        [20, 50],
        [5, 25],
        [30, 60],
        [4, 20],
        [35, 70],
        [3, 18],
        [28, 55],
        [6, 30],
    ]

# Rótulo dos animais: 0 = Gato, 1 = Cachorro
rotulos = [

        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0
    ]

classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(caracteristicas, rotulos)

def botao_prever():

    campo_texto.delete("1.0", tk.END)


    try:
        pegaAltura = float(altura.get().strip())
        pegaPeso = float(peso.get().strip())
        previsao = classificador.predict([[pegaPeso, pegaAltura]])

        if previsao == 1:
            campo_texto.insert(tk.END, "Este animal é um cachorro!")

        else:
            campo_texto.insert(tk.END, "Este animal é um Gato!")

    except ValueError:
        campo_texto.insert(tk.END, "Por favor, insira valores números válidos!")
        return


botaoPrever= tk.Button(janela, text="Prever", font=("Arial", 11), command=botao_prever, padx=5, pady=5)
botaoPrever.grid(row=2, column=2)

def dicas():
    campo_texto.delete("1.0", tk.END)

    texto = """
    Exemplos de dados e resultados:
    -------------------------------
    Peso: 20kg, Altura: 50cm -> Cachorro
    Peso: 5kg, Altura: 25cm -> Gato
    Peso: 30kg, Altura: 60cm -> Cachorro
    Peso: 4kg, Altura: 20cm -> Gato
    Peso:28kg, Altura: 55cm -> Cachorro
    """
    campo_texto.insert(tk.END, texto)

botaoExemplos = tk.Button(janela, text="Dica de Exemplos", font=("Arial", 11), command=dicas, padx=5, pady=5)
botaoExemplos.grid(row=3, column=2)

campo_texto = tk.Text(janela, width=40, height=10)
campo_texto.grid(row=5, column=1, columnspan=3, pady=10)

janela.mainloop()


