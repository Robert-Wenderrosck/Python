import tkinter as tk
import random
import heapq
from tkinter import messagebox

LARGURA_TELA = 400
ALTURA_TELA = 400
TAMANHO_CELULA = 20
VELOCIDADE = 100
pontuacao = 0
frutas_comidas = 0
modo_jogador = False

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def reiniciar_variaveis():

    global direcao, cobra, alimento, jogando, pontuacao, frutas_comidas

    direcao = "direita" #Inicializa a direção do movimento da cobra como 'direita'. Isso define o movimento inicial da cobra quando o jogo começa.

    cobra = [(LARGURA_TELA // 2, ALTURA_TELA // 2)] #Cria uma lista contendo uma única tupla, que define a posição inicial da cobra no centro do campo de jogo.

    alimento = gerar_primeiro_alimento()

    jogando = True
    pontuacao = 0
    frutas_comidas = 0

def gerar_primeiro_alimento():
    x_cobra, y_cobra = cobra[0] #Extrai a posição inicial da cabeça da cobra do primeiro elemento da lista 'cobra'. A variável 'cobra' é uma lista de tuplas, cada tupla representando uma parte da cobra no tabuleiro.

    x = x_cobra + TAMANHO_CELULA * 3 #Calcula a posição horizontal 'x' para a primeira fruta. A fruta é posicionada três células à direita da cabeça da cobra, mantendo-a na mesma linha 'y'

    #Verifica se a posição calculada para 'x' não ultrapassa os limites da tela do jogo. 'LARGURA_TELA' é a largura total da área de jogo. Se 'x' for maior ou igual a 'LARGURA_TELA' significaria que a fruta estaria fora da tela.
    if x >= LARGURA_TELA:
        x = LARGURA_TELA - TAMANHO_CELULA #Ajusta 'x' para que a fruta apareça na última célula permitida da tela, evitando que fique invisível

    return (x, y_cobra) #Retorna a posição da fruta como uma tupla (x, y_cobra), onde 'y_cobra' é a linha onde a cobra começou.


def iniciar_jogo():
    reiniciar_variaveis()

    #Verifica se o modo de jogo está configurado para controle pelo jogador (modo_joagdor = True)
    if modo_jogador:
        janela.bind("<KeyPress>", controle_teclas) #Permite que o jogador use o teclado para controlar a cobra

    else:
        janela.unbind("<KeyPress>") #Desvincular controle manual se IA estiver ativa

    mover() #Chama a função 'mover' que inicia o movimento da cobra no jogo.

#Define a função 'mover', responsável por atualizar a posição da cobra a cada ciclo do jogo
def mover():

    global jogando, cobra, alimento, pontuacao, frutas_comidas

    if jogando:
        if not modo_jogador:
            nova_direcao = IA_busca_astar()
            mudar_direcao(nova_direcao) #Atualiza a direção da cobra com a nova direção retornada pela IA

        x, y = cobra[0] #Obtém a posição atual da cabeça da cobra (primeiro segmento)

        #Atualiza a posição da cobra baseada na direção atual do movimento
        if direcao == "cima":
            y -= TAMANHO_CELULA
        elif direcao == "baixo":
            y += TAMANHO_CELULA
        elif direcao == "esquerda":
            x -= TAMANHO_CELULA
        elif direcao == "direita":
            x += TAMANHO_CELULA

        nova_posicao = (x, y) #Cria uma nova posição para a cabeça da cobra, com base nos cálculos anteriores.

        #Verifica se a nova posição da cabeça da cobra resulta em uma colisão (bater na parede ou em seu próprio corpo)
        if (x < 0 or x >= LARGURA_TELA or y < 0 or y >= ALTURA_TELA or nova_posicao in cobra):
            jogando = False
            messagebox.showinfo("Fim de jogo", "A IA perdeu ao se colidir!")
            janela.destroy()
            return

        #Atualiza a lista que representa a cobra no jogo. A nova posição da cabeça é adicionada ao início da lista 'cobra'. O último segmento da cobra (representado por 'cobra[:-1'] é removido, a menos que a cobra tenho comido uma fruta.
        cobra = [nova_posicao] + cobra[:-1]

        #Verifica se a cabeça da cobra (primeiro elemento da lista 'cobra') está na mesma posição do alimento.
        if cobra[0] == alimento:
            cobra.append(cobra[-1]) #Se a cobra come o alimento, o último segmento da cobra é duplicado, efetivamente aumentando o tamanho da cobra por não remover o último segmento no próximo movimento.
            alimento = gerar_alimento()
            pontuacao += 10
            frutas_comidas += 1

            if frutas_comidas >= 50:
                messagebox.showinfo("Parabéns!", "Você comeu 50 frutas! Jogo encerrado.")
                janela.destroy()
                return #Retorna a função para evitar mais execuções já que o jogo terminou.

        desenhar()

        janela.after(VELOCIDADE, mover) #Agenda a próxima execução da função 'mover' após um intervalo definido pela constante 'VELOCIDADE'. Isso cria um loop de animação que continua enquanto o jogo estiver ativo.

def IA_busca_astar():

    #Função heurística é usada para estimar o custo do caminho mais barato entre dois pontos no grid
    def heuristica(a, b):
        #Recebe dois pontos 'a' e 'b' onde cada ponto é uma tupla contendo coordenadas x e y (x1, y1) para 'a' e (x2, y2) para 'b'
        (x1, y1) = a
        (x2, y2) = b

        #Calcula a distância entre os dois pontos: a soma das diferenças absolutas de suas coordenadas x e y
        return abs(x1 - x2) + abs(y1 - y2)

    def astar(cobra, alimento):
        inicio = cobra[0] #Inicializa o ponto de partida do algoritmo como a posição atual da cabeça da cobra
        fila = [] #Cria uma lista de prioridade 'fila' onde serão armazenados os nós a serem explorados juntamente com suas prioridades calculadas
        heapq.heappush(fila, (0, inicio)) #'heapq.heappush' é usado para adicionar o ponto de partida à fila com prioridade 0.
        veio_de = {} #Dicionário 'veio_de' usado para rastrear o caminho de volta ao ponto de partida. Armazena qual ponto veio antes de outro, criando um caminho reverso até a origem
        custo_ate_agora = {} #Dicionário que mantém o custo acumulado para alcançar cada ponto no grid
        veio_de[inicio] = None #Inicializa o ponto de partida no dicionário 'veio_de' indicando que não tem ponto anterior
        custo_ate_agora[inicio] = 0 #O custo para alcançar o ponto de partida é zero

        #Continua o loop enquanto houver elementos na fila de prioridade
        while fila:

            #Remove e retorna o item com a menor prioridade na fila, que é uma combinação de custo atual e heurística. O underscore (_) é usado para descartar o primeiro valor da tupla que é a prioridade usada apenas internamente pelo heapq
            _, atual = heapq.heappop(fila)

            if atual == alimento:
                break

            #Itera sobre as possíveis direções de movimento da cobra
            for dx, dy, direcao_nova in [(-TAMANHO_CELULA, 0, "esquerda"),
                                         (TAMANHO_CELULA, 0, "direita"),
                                         (0, -TAMANHO_CELULA, "cima"),
                                         (0, TAMANHO_CELULA, "baixo")]:

                #Calcula as novas coordenadas x e y ajustando o ponto atual com os deltas das direções
                novo_x, novo_y = atual[0] + dx, atual[1] + dy

                #Cria uma nova posição com as coordenadas atualizadas
                nova_posicao = (novo_x, novo_y)

                #Verifica se a nova posição é válida dentro dos limites da tela e não está ocupada pela própria cobra.
                if (0 <= novo_x < LARGURA_TELA and 0 <= novo_y < ALTURA_TELA and nova_posicao not in cobra):
                    novo_custo = custo_ate_agora[atual] + 1 #Calcula o novo custo para chegar à nova posição, assumindo um custo constante de 1 por movimento

                    if nova_posicao not in custo_ate_agora or novo_custo < custo_ate_agora[nova_posicao]:

                        custo_ate_agora[nova_posicao] = novo_custo

                        prioridade = novo_custo + heuristica(alimento, nova_posicao)

                        heapq.heappush(fila, (prioridade, nova_posicao))

                        veio_de[nova_posicao] = (atual, direcao_nova)

        caminho = []

        atual = alimento

        if atual not in veio_de:
            return direcao

        while atual != inicio:

            atual, direcao_nova = veio_de[atual]

            caminho.append(direcao_nova)

        return caminho[::-1]

    caminho = astar(cobra, alimento)

    if caminho:
        return caminho[0]

    else:
        return direcao



def gerar_alimento():

    while True:

        x = random.randint(0, (LARGURA_TELA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA

        y = random.randint(0, (ALTURA_TELA // TAMANHO_CELULA) - 1) * TAMANHO_CELULA

        if (x, y) not in cobra:
            return (x, y)

def desenhar():

    canvas.delete(tk.ALL)

    for x, y in cobra:

        canvas.create_rectangle(x, y, x + TAMANHO_CELULA, y + TAMANHO_CELULA, fill="green")

    x, y = alimento

    canvas.create_oval(x, y, x + TAMANHO_CELULA, y + TAMANHO_CELULA, fill="red")

    canvas.create_text(LARGURA_TELA//2, 10, text=f"Pontuação: {pontuacao}      Frutas:{frutas_comidas}/50", fill="white", font=("Arial", 14), anchor="n")


def mudar_direcao(nova_direcao):

    global direcao

    #Verifica se a nova direção é válida. Uma nova direção é considerada válida se não for diretamente oposta à direção atual (evita que a cobra 'vire sobre si mesma' e morra)
    if (nova_direcao == "cima" and direcao != "baixo") or \
       (nova_direcao == "baixo" and direcao != "cima") or \
       (nova_direcao == "esquerda" and direcao != "direita") or \
       (nova_direcao == "direita" and direcao != "esquerda"):
        direcao = nova_direcao




#Parâmetro 'event' contém informações sobre o evento do teclado, incluindo qual tecla foi pressionada
def controle_teclas(event):

    #Se o 'modo_jogador' for True, o jogador pode controlar a cobra com o teclado
    if modo_jogador:
        if event.keysym in ["Up", "Down", "Left", "Right"]: #Verifica se a tecla pressionada está entre as teclas de direção permitidas
            direcoes = {"Up": "cima", "Down": "baixo", "Left": "esquerda", "Right": "direita"} #Cria um dicionário chamado 'direcoes' que mapeia as teclas de direção para as direções correspondentes no jogo (Converte o 'keysym' - símbolo da tecla - para uma string que representa a direção no jogo)

        mudar_direcao(direcoes[event.keysym])


def escolher_modo():
    janela_inicial = tk.Tk()
    janela_inicial.title("Escolha o Modo de Jogo")
    centralizar_janela(janela_inicial, 300, 200)

    def jogar_com_IA():
        global modo_jogador
        modo_jogador = False
        janela_inicial.destroy()
        iniciar_janela_jogo()

    def jogar_sozinho():
        global modo_jogador
        modo_jogador = True
        janela_inicial.destroy()
        iniciar_janela_jogo()

    tk.Label(janela_inicial, text="Escolha o modo de jogo:", font=("Arial", 14)).pack(pady=10)

    tk.Button(janela_inicial, text="Jogar com IA", font=("Arial", 12), command=jogar_com_IA).pack(pady=5)
    tk.Button(janela_inicial, text="Jogar sozinho", font=("Arial", 12), command=jogar_sozinho).pack(pady=5)


    janela_inicial.mainloop()

def iniciar_janela_jogo():
    global janela, canvas
    janela = tk.Tk()
    janela.title("Jogo Snake")

    canvas = tk.Canvas(janela, width=LARGURA_TELA, height=ALTURA_TELA, bg="black")
    canvas.pack()

    centralizar_janela(janela, LARGURA_TELA, ALTURA_TELA)
    iniciar_jogo()

    janela.mainloop()


escolher_modo()
