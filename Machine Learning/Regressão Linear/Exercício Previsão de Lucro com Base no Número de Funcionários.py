import numpy as np
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def mostrar_tela(tela):
    tela_principal.pack_forget()
    tela.pack()

def exibir_grafico(funcionarios, tempo_operacao, lucros, modelo, entrada_prever=None, previsao_lucro=None):
    plt.figure(figsize=(10.6, 6))
    plt.scatter(funcionarios, lucros, color='blue', label='Funcionários vs Lucro', s=100)
    plt.plot(funcionarios, modelo.predict(np.hstack((funcionarios, tempo_operacao))), color='red', label='Linha de Regressão', linewidth=3)

    if entrada_prever is not None and prever_lucro is not None:
        plt.scatter(entrada_prever[:, 0], previsao_lucro, color='green', label=f'Previsão: {entrada_prever[0][0]} funcionários, Lucro: R$ {previsao_lucro[0]:,.2f}', marker='x', s=200)

    plt.title('Previsão de Lucro com base no Número de Funcionários e Tempo de Operação', fontsize=16)
    plt.xlabel('Número de Funcionários', fontsize=14)
    plt.ylabel('Lucro (R$)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='upper left', fontsize=12)

    plt.tight_layout()
    plt.show()


def exibir_dados_reais():
    dados_texto = "\nDados Reais (Número de Funcionários, Tempo de Operação e Lucro):\n"
    for i in range(len(funcionarios)):
        dados_texto += f"Empresa {i + 1}: {funcionarios[i][0]} funcionários, {tempo_operacao[i][0]} anos - lucro: R$ {lucros[i]:,.2f} \n"

    mensagem_dados.config(text=dados_texto)

def prever_lucro():
    try:
        num_funcionarios = float(entrada_funcionarios_prever.get())
        tempo_op = float(entrada_tempo_operacao_prever.get())
        entrada_prever = np.array([[num_funcionarios, tempo_op]])
        previsao_lucro = modelo.predict(entrada_prever)

        messagebox.showinfo("Previsão de Lucro", f"Lucro previsto: R$ {previsao_lucro[0]:,.2f}")
        exibir_grafico(funcionarios, tempo_operacao, lucros, modelo, entrada_prever, previsao_lucro)


    except ValueError:
        messagebox.showerror("Error", "Por favor, insira valores numéricos válidos.")

def voltar():
    for widget in janela_principal.winfo_children(): #Obtém uma lista de todos os widgets filhos da janela principal
        widget.pack_forget() #remove cada widget filho do gerenciador de geometria 'pack' (limpa a janela princiál de quaisquer telas ou widgets que foram adicionados anteriormente)

    tela_principal.pack()

funcionarios = [[10], [20], [30], [40], [50], [60], [70], [80], [90], [100]] #Número de funcionários em uma empresa específica
tempo_operacao = [[2], [3], [4], [5], [6], [7], [8], [9], [10], [11]] #Tempo de operação em anos em várias empresas
lucros = [100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000] #Lucros de várias empresas, representa o lucro total anual de uma empresa em reais

funcionarios = np.array(funcionarios)
tempo_operacao = np.array(tempo_operacao)
lucros = np.array(lucros)
modelo = LinearRegression()
entradas = np.hstack((funcionarios, tempo_operacao))
modelo.fit(entradas, lucros)




janela_principal = tk.Tk()
janela_principal.title("Previsão de Lucro de Empresas")

tela_principal = tk.Frame(janela_principal)
tela_principal.pack()

label_menu = tk.Label(tela_principal, text="Menu de Opções", font=("Arial", 20))
label_menu.pack(pady=10)

btn_exibir_dados = tk.Button(tela_principal, text="1 - Exibir Dados Reais", font=("Arial", 20), width=30, command=lambda: mostrar_tela(tela_dados))
btn_exibir_dados.pack(pady=5)
tela_dados = tk.Frame(janela_principal)

btn_prever = tk.Button(tela_principal, text="2 - Prever Lucro", font=("Arial", 20), width=30, command=lambda: mostrar_tela(tela_previsao))
btn_prever.pack(pady=5)
tela_previsao = tk.Frame(janela_principal)

btn_grafico = tk.Button(tela_principal, text="3 - Exibir Gráfico de Regressão", font=("Arial", 20), width=30, command=lambda: exibir_grafico(funcionarios, tempo_operacao, lucros, modelo))
btn_grafico.pack(pady=5)

btn_sair = tk.Button(tela_principal, text="4 - Sair", font=("Arial", 20), width=30, command=janela_principal.destroy)
btn_sair.pack(pady=5)

tela_dados = tk.Frame(janela_principal)
btn_voltar_dados = tk.Button(tela_dados, text="Voltar", font=("Arial", 20), command=voltar)
btn_voltar_dados.pack(pady=10)

mensagem_dados = tk.Label(tela_dados, text="", font=("Arial", 20))
mensagem_dados.pack()

exibir_dados_reais()

tela_previsao = tk.Frame(janela_principal)
label_previsao = tk.Label(tela_previsao, text="Prever Lucro", font=("Arial", 20))
label_previsao.pack(pady=10)

label_funcionarios_prever = tk.Label(tela_previsao, font=("Arial", 20), text="Número de Funcionários:")
label_funcionarios_prever.pack()

entrada_funcionarios_prever = tk.Entry(tela_previsao, font=("Arial", 20))
entrada_funcionarios_prever.pack()

label_tempo_operacao_prever = tk.Label(tela_previsao, font=("Arial", 20), text="Tempo de Operação (anos):")
label_tempo_operacao_prever.pack()

entrada_tempo_operacao_prever = tk.Entry(tela_previsao, font=("Arial", 20))
entrada_tempo_operacao_prever.pack()

btn_prever_lucro = tk.Button(tela_previsao, text="Prever", font=("Arial", 20), command=prever_lucro)
btn_prever_lucro.pack(pady=10)

btn_voltar_previsao = tk.Button(tela_previsao, text="Voltar", font=("Arial", 20), command=voltar)
btn_voltar_previsao.pack(pady=10)


tela_principal.mainloop()