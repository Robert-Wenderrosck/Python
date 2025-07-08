import tkinter as tk
from tkinter import messagebox

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - CheckButton com números")
janela.geometry("400x400")

labelInformacao = tk.Label(janela, text="Selecione a opção desejada:", foreground="blue", font="Arial 20").pack()

total = 0
valorAntigo = 0

def funcaoSomar():

    global total #Acessa a mesma variável criada anteriormente
    global valorAntigo

    valorAntigo = total

    total += int(varNumero.get())

    print(valorAntigo, " + ", varNumero.get(), " = ", total)

#Criando a variável de controle (vincular uma variável Python ao conteúdo visual de um widget --> atualiza automaticamente na tela)
varNumero = tk.IntVar()


checkNumero5 = tk.Checkbutton(janela, text="5", font="arial 20", variable=varNumero, onvalue="5", offvalue="0", command=funcaoSomar).pack()

checkNumero10 = tk.Checkbutton(janela, text="10", font="arial 20", variable=varNumero, onvalue="10", offvalue="0", command=funcaoSomar).pack()

checkNumero15 = tk.Checkbutton(janela, text="15", font="arial 20", variable=varNumero, onvalue="15", offvalue="0", command=funcaoSomar).pack()

# Exibe a janela (deve vir por último)
janela.mainloop()