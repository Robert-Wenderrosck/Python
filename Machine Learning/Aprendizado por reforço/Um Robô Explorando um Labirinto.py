import tkinter as tk
import numpy as np
import time
import random

janela_aberta = True #Usado para verificar se a janela Tkinter está aberta ou fechada
matriz_labirinto = [] #Inicializada como uma lista vazia. Esta lista será preenchida com informações sobre o labirinto. Cada célula pode ser 0 (caminho aberto), 1 (parede), 2 (início) ou 3 (fim).
q_tabela = np.zeros((16, 4)) #Tabela Q armazena os valores Q para cada par estado-ação. Temos 16 estados possíveis (uma posição para cada célula em uma matriz 4x4) e 4 ações possíveis (cima, baixo, esquerda, direita).

def labirinto_solucionavel():
    visitados = set() #Inicializa um conjunto 'visitados' para manter um registro de todas as células já visitadas no labirinto
    pilha = [(0,0)] #Inicializa uma pilha 'pilha' e coloca a posição inicial (0,0) como primeiro elemento

    #Enquanto a pilha não estiver vazia, continua a busca
    while pilha:
        (linha, coluna) = pilha.pop() #Desempilha a posição atual (linha, coluna) do topo da pilha

        if (linha, coluna) == (3,3): #verifica se a posição atual é o destino (3,3). Se for, retorna True.
            return True

        for (dlinha, dcoluna) in [(-1, 0), (1,0), (0, -1), (0,1)]: #Varre as direções possíveis
            nova_linha, nova_coluna = linha + dlinha, coluna + dcoluna #Calcula a nova posição somando as coordenadas atuais com as direções possíveis

            if 0 < nova_linha < 4 and 0 <= nova_coluna <4: #Verifica se a nova posição está dentro dos limites do tabuleiro
                if matriz_labirinto[nova_linha][nova_coluna] != 1 and (nova_linha, nova_coluna) not in visitados: #Verifica se a nova célula não é uma parede (valor 1) e ainda não foi visitada.
                    pilha.append((nova_linha, nova_coluna))
                    visitados.add((nova_linha, nova_coluna))

    return False #Se o loop terminar e a função ainda não tiver retornado True, então o labirinto não é solucionável

def mudar_labirinto():

    global matriz_labirinto

    while True:
        criar_labirinto()
        if labirinto_solucionavel():
            break

    painel.delete("all")

    desenhar_labirinto()

    treinar_modelo()

def treinar_modelo():
    global q_tabela, matriz_labirinto
    alpha = 0.1
    gamma= 0.9
    epsilon = 0.1
    num_episodios = 5000

    q_tabela = np.zeros((16, 4))
    for episodio in range(num_episodios):
        estado = 0

        while estado != 15:
            if np.random.rand() < epsilon:
                acao = np.random.choice(4)
            else:
                acao = np.argmax(q_tabela[estado])

            estado_seguinte = proximo_estado(estado, acao)

            recompensa = -100 if matriz_labirinto[estado_seguinte // 4][estado_seguinte % 4] == 1 else 0

            if estado_seguinte == 15:
                recompensa = 100

            q_tabela[estado, acao] = (1 - alpha) * q_tabela[estado, acao] + alpha * (recompensa + gamma * np.max(q_tabela[estado_seguinte]))

            estado = estado_seguinte

def proximo_estado(estado_atual, acao_atual):
    linha, coluna = divmod(estado_atual, 4)

    if acao_atual == 0:
        linha = max(linha -1, 0)

    elif acao_atual == 1:
        linha = min(linha +1, 3)

    elif acao_atual == 2:
        coluna = max(coluna -1, 0)

    elif acao_atual == 3:
        coluna = min(coluna + 1, 3)

    return linha * 4 + coluna


def desenhar_labirinto():
    global matriz_labirinto
    for i in range(4):
        for j in range(4):

            cor = 'black' if matriz_labirinto[i][j] == 1 else 'white'

            if matriz_labirinto[i][j] == 2:
                cor = 'green'

            if matriz_labirinto[i][j] == 3:
                cor = 'red'

            #Responsável por desenhar um único retângulo na tela, que é uma célula do labirinto
            painel.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=cor)



def criar_labirinto():
    global matriz_labirinto

    matriz_labirinto = [[0 for _ in range(4)] for _ in range(4)] #Cria uma matriz 4x4 preenchida com zeros (Um zero indica uma célula vazia na matriz do labirinto)
    matriz_labirinto[0][0] = 2 #Define a célula de partida (canto superior esquerdo) como sendo do tipo 2 (número 2 serve como um marcador para indicar o ponto de partida do agente)
    matriz_labirinto[3][3] = 3 ##Define a célula de destino (canto inferior direito) como sendo do tipo 3 (número 3 serve como um marcador para indicar o ponto de chegada do agente)

    #Inicia um loop que será executado 5 vezes para colocar obstáculos no labirinto
    for _ in range(5):
        linha, coluna = random.randint(0, 3), random.randint(0, 3) #Gera coordenadas aleatórias para a linha e coluna dentro dos limites da matriz 4x4
        if matriz_labirinto[linha][coluna] == 0: #Verifica se a célula escolhida aleatoriamente está vazia (Contém um zero)
            matriz_labirinto[linha][coluna] = 1 #Se a célula está vazia ela se torna um obstáculo, marcado com o número 1.

def mover_agente():
    global janela_aberta, matriz_labirinto, q_tabela

    estado = 0

    while estado != 15:
        if not janela_aberta:
            return

        acao = np.argmax(q_tabela[estado])

        estado_seguinte = proximo_estado(estado, acao)

        linha, coluna = divmod(estado_seguinte, 4)
        painel.create_oval(coluna * 50 + 10, linha * 50 + 10, coluna * 50 + 40, linha * 50 + 40, fill='blue', tags='agente')

        painel.update()
        time.sleep(1)
        painel.delete('agente')

        estado = estado_seguinte

def fechar_janela():

    global janela_aberta
    janela_aberta = False
    janela_principal.destroy()

janela_principal = tk.Tk()
janela_principal.title("Labirinto com Q-Learning")

painel = tk.Canvas(janela_principal, width=200, height=200)
painel.pack()

botao_andar = tk.Button(janela_principal, text="Andar", command=mover_agente)
botao_andar.pack()

botao_mudar_labirinto = tk.Button(janela_principal, text="Mudar Labirinto", command=mudar_labirinto)
botao_mudar_labirinto.pack()
mudar_labirinto()

janela_principal.protocol("WM_DELETE_WINDOW", fechar_janela) #Quando a janela for fechada, a função 'fechar_janela()' será chamada.


janela_principal.mainloop()


