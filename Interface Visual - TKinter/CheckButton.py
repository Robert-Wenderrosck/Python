import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox


# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - CheckButton")
janela.geometry("400x400")

labelInformacao = tk.Label(janela, text="Selecione a opção desejada:", foreground="blue", font="Arial 20").pack()

def funcaoAzulClicado():

    messagebox.showinfo("Mensagem", varAzul.get())

def funcaoAmareloClicado():

    messagebox.showinfo("Mensagem", varAmarelo.get())

def funcaoVerdeClicado():

    messagebox.showinfo("Menssagem", varVerde.get())


#Criando as variáveis de controle (vincular uma variável Python ao conteúdo visual de um widget --> atualiza automaticamente na tela)
varAzul = StringVar()
varAmarelo = StringVar()
varVerde = StringVar()

checkAzul = tk.Checkbutton(janela, text="Azul", font="arial 20", variable=varAzul, onvalue="Clicou na cor Azul", offvalue="", command=funcaoAzulClicado).pack()

checkAmarelo = tk.Checkbutton(janela, text="Amarelo", font="arial 20", variable=varAmarelo, onvalue="Clicou na cor Amarelo", offvalue="", command=funcaoAmareloClicado).pack()

checkVerde = tk.Checkbutton(janela, text="Verde", font="arial 20", variable=varVerde, onvalue="Clicou na cor Verde", offvalue="", command=funcaoVerdeClicado).pack()

# Exibe a janela (deve vir por último)
janela.mainloop()