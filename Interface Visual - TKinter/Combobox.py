import tkinter as tk
from tkinter import ttk

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - Combobox")


tk.Label(janela, text= "Selecione um mês:", font="Arial 20").grid(row=0, column=0)

#Criando combobox
comboboxMesSelecionado = ttk.Combobox(janela, font="Arial 20")

#Adicionando os valores na combobox
comboboxMesSelecionado["values"] = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

#Colocando a comboboxMesSelecionado na tela
comboboxMesSelecionado.grid(row=0, column=1)

"""
Para fazer a combobox começar em um valor específico criar um comando: comboboxMesSelecionado.current() --> colocar o valor desejado do item dentro do parênteses
"""

#Criando a função que pega o item da combobox e imprime
def itemSelecionado():
    print(str(comboboxMesSelecionado.get()))


botaoPegaItemSelecionado = tk.Button(janela, text="Item Selecionado", font="Arial 20", command=itemSelecionado)

botaoPegaItemSelecionado.grid(row=1, column=0, columnspan=2, sticky="NSEW") #columnspan aumenta o grid para mais de uma coluna // sticky aumenta a área do campo de seleção do botão


# Exibe a janela (deve vir por último)
janela.mainloop()