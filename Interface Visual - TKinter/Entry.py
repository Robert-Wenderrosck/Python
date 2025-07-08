import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - Entry")
janela.geometry("800x600")

#grid - divide a tela em grades/partes (como uma planilha)
#sticky - usa-se para preencher o item na tela toda (opções= NSEW: North, South, East, West)
nome = tk.Label(text="Nome: ", font="Arial 20")
nome.grid(row=1, column=0, sticky="W")

exibirNome = tk.Entry(font= "Arial 40")
exibirNome.grid(row=1, column=1, sticky="W")

#-------------------------------------------------------

sobrenome = tk.Label(text="Sobrenome: ", font="Arial 20")
sobrenome.grid(row=2, column=0, sticky="W")

exibirSobrenome = tk.Entry(font= "Arial 40")
exibirSobrenome.grid(row=2, column=1, sticky="W")

# Exibe a janela (deve vir por último)
janela.mainloop()