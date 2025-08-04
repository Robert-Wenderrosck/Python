import numpy as np
import tkinter as tk
import random
import time

alpha =0.1 #Define a taxa de aprendizado, influenciando a rapidez com que o moedlo se ajusta a novos dados
gamma= 0.9 #Define o fator de desconto que pondera a importância das recompensas futuras no aprendizado
epsilon = 0.1 #Define a probabilidade de escolher uma ação aleatória, promovendo a exploração do espaço de ações
num_episodios = 5000 #Estabelece o número total de episódios que o  modelo passará treinando

temp_min = 15
temp_max = 30
intervalo_ideal = (20, 25)
janela_aberta = True #Inicializa a variável que controla se a janela da interface gráfica está aberta

historico_temperaturas = []

def controlar_temperatura():

    global temperatura_atual, janela_aberta, historico_temperaturas

    estado = temperatura_atual - temp_min
    while janela_aberta:
        janela.update()
        time.sleep(1)

        acao = np.argmax(q_table[estado])

        nova_temperatura, acao_tomada = executar_acao(temperatura_atual, acao)

        historico_temperaturas.append(f"Temperatura: {temperatura_atual} °C -> {acao_tomada} -> {nova_temperatura} °C")

        atualizar_historico()

        temperatura_atual = nova_temperatura

        if janela_aberta:
            label_temp.config(text=f"Temperatura Atual: {temperatura_atual} °C")

            if intervalo_ideal[0] <= temperatura_atual <= intervalo_ideal[1]:
                label_status.config(text="Temperatura está no intervalo ideal!", fg="green")

            else:
                label_status.config(text="Temperatura fora do intervalo ideal!", fg="red")

        estado = temperatura_atual - temp_min


def atualizar_historico():
    texto_historico.delete(1.0, tk.END)

    for item in historico_temperaturas:
        texto_historico.insert(tk.END, item + "\n")



def calcular_recompensa(temperatura):
    if intervalo_ideal[0] <= temperatura <= intervalo_ideal[1]:
        return 10
    else:
        return -abs(temperatura - sum(intervalo_ideal) / 2)

def escolher_acao(estado, q_table):

    if np.random.rand() < epsilon: #Gera um número aleatório entre 0 e 1. Se este número for menor que a probabilidade de exploração (epsilon, 0.1), então uma ação aleatória é escolhida. Isso ajuda a explorar novas ações além das já conhecidas.
        return np.random.choice(3) #Escolhe uma entre três ações possíveis (0, 1 ou 2) aleatoriamente.
    else:
        return np.argmax(q_table[estado]) #Se o número gerado for maior ou igual a epsilon, a ação escolhida é aquela que tem a maior estimativa de recompensa futura no estado atual, conforme registrado na tabela Q

def executar_acao(temperatura, acao):
    if acao == 0:
        return min(temperatura + 1, temp_max), "Aumentar"
    elif acao == 1:
        return max(temperatura - 1, temp_min), "Diminuir"
    else:
        return temperatura, "Manter"


def q_learning():
    q_table = np.zeros((temp_max - temp_min + 1, 3))

    for episodio in range(num_episodios):
        temperatura = random.randint(temp_min, temp_max)

        while True:
            estado = temperatura - temp_min
            acao = escolher_acao(estado, q_table)

            nova_temperatura, _ = executar_acao(temperatura, acao)

            recompensa = calcular_recompensa(nova_temperatura)

            novo_estado = nova_temperatura - temp_min

            q_table[estado, acao] = (1 - alpha) * q_table[estado, acao] + alpha * (recompensa + gamma * np.max(q_table[novo_estado]))

            temperatura = nova_temperatura

            if intervalo_ideal[0] <= temperatura <= intervalo_ideal[1]:
                break
    return q_table



janela = tk.Tk()
janela.title("Controle de Temperatura com Q-Learning")

temperatura_atual = random.randint(temp_min, temp_max)

q_table = q_learning() #Chama a função q_learning para treinar o modelo de Q-Learning. Esta função ajusta a tabela Q baseada em um número pré-definido de episódios de aprendizado

label_temp = tk.Label(janela, text=f"Temperatura Atual: {temperatura_atual}°C", font=("Arial", 14))

label_temp.pack(pady=10)

label_status = tk.Label(janela, text="", font=("Arial", 14))
label_status.pack(pady=10)

texto_historico = tk.Text(janela, height=10, width=50)
texto_historico.pack(pady=10)

botao_iniciar = tk.Button(janela, text="Iniciar Controle de Temperatura", command=controlar_temperatura, font=("Arial", 14))
botao_iniciar.pack(pady=10)

botao_fechar = tk.Button(janela, text="Fechar", command=janela.destroy, font=("Arial", 14))
botao_fechar.pack(pady=10)



janela.mainloop()