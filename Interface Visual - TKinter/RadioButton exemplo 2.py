import tkinter as tk

#Criando RadioButton em massa

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - RadioButton 2")

def imprimirItemSelecionado():

    print("Você selecionou a letra: " + variavelOpcaoSelecionada.get())

variavelOpcaoSelecionada = tk.StringVar(janela, "0") #janela, "0" - serve para deixar o botão desmarcado

opcoes = {"Letra A" : "A",
          "Letra B" : "B",
          "Letra C": "C",
          "Letra D": "D",
          "Letra E": "E",
          "Letra F": "F",
          "Letra G": "G",
          "Letra H": "H",
          "Letra I": "I",
          "Letra J": "J",
          "Letra K": "K",
          }

#Criando vários RadioButtons
for (textoColuna0,textoColuna1) in opcoes.items():

    tk.Radiobutton(janela, text=textoColuna0, font="Arial 26", value=textoColuna1, variable=variavelOpcaoSelecionada, command=imprimirItemSelecionado).pack()

# Exibe a janela (deve vir por último)
janela.mainloop()