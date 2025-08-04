import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression

def prever_preco():
    try:

        tamanho = float(entry_tamanho.get())
        previsao_preco = modelo.predict([[tamanho]])
        label_resultado.config(text=f"O preço estimado para uma casa de {tamanho} m² é: R${previsao_preco[0]:.2f} mil")

    #Exibe uma mensagem de erro pedindo que o usuário insira um número válido
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")

    #Captura qualquer outro tipo de erro que possa ocorrer (que não seja um erro de valor)
    except Exception as e:
        label_resultado.config(text=f"Erro ao fazer a previsão: {e}")

def carregar_dados():

    try:
        dados = pd.read_excel('preco_casas.xlsx')

        tamanhos = dados['Tamanho (m²)'].values.reshape(-1, 1) #.reshape(-1, 1) -> ajusta os dados para o formato adequado para o modelo de regressão (n linhas e 1 coluna)
        precos = dados['Preço (mil reais)'].values

        global modelo

        modelo = LinearRegression()
        modelo.fit(tamanhos, precos)
        label_status.config(text="Modelo carregado e treinado com sucesso!", fg='green')


    except Exception as e:
        label_status.config(text=f"Erro ao carregar os dados: {e}", fg='red')

janela = tk.Tk()
janela.title("Previsão de Preço de Casas")
janela.geometry("550x350")

janela.option_add("*Font", "Arial 12")
janela.config(bg="#f0f0f0")

titulo = tk.Label(janela, text="Previsão de Preço de Casas", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)

frame_status = tk.Frame(janela, bg="#f0f0f0")
frame_status.pack(fill="x", padx=20)

label_status = tk.Label(frame_status, text="Carregando modelo...", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="blue")
label_status.pack()

frame_input = tk.Frame(janela, bg="#f0f0f0")
frame_input.pack(pady=20)

rotulo_tamanho = tk.Label(frame_input, text="Tamanho da Casa (m²):", bg="#f0f0f0")
rotulo_tamanho.grid(row=0, column=0, padx=10, pady=10)

entry_tamanho = ttk.Entry(frame_input, width=15)
entry_tamanho.grid(row=0, column=1, padx=10, pady=10)

botao_prever = ttk.Button(janela, text="Prever Preço", command=prever_preco)
botao_prever.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="black")
label_resultado.pack(pady=20)

carregar_dados()



janela.mainloop()