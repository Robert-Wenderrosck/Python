import tkinter as tk
from tkinter import messagebox

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - MessageBox ")
janela.geometry("400x400")

def mensagemInformacao():
    messagebox.showinfo("Informação", "Bem vindo(a) ao curso de TKinter")

def mensagemAviso():
    messagebox.showwarning("Aviso", "Você está usando TKinter")

def mensagemErro():
    messagebox.showerror("Erro", "Erro ao carregar o sistema")

def mensagemQuestao():
    resultado = messagebox.askquestion("Deletar", "Tem certeza que deseja deletar?")
    if resultado == "yes":
        print("O usuário deseja deletar")
    else:
        print("O usuário NÃO quer deletar")

def mensagemOkCancel():
    resultado = messagebox.askokcancel("Ok ou Cancelar?", "Quer procurar o valor?")
    if resultado:   #Por padrão o primeiro resultado é o OK
        print("O usuário quer procurar o valor")
    else:
        print("O usuário NÃO quer procurar o valor")

def mensagemRepetirCancelar():
    resultado = messagebox.askretrycancel("Repetir ou Cancelar?", "Quer tentar novamente?")
    if resultado:
        print("O usuário quer repetir")
    else:
        print("O usuário quer cancelar")

botaoInformacao = tk.Button(janela, text="Informação", font="Arial 20", pady= 10, padx=10, command=mensagemInformacao).pack()

botaoAviso = tk.Button(janela, text="Aviso", font="Arial 20", pady= 10, padx=10, command=mensagemAviso).pack()

botaoErro = tk.Button(janela, text="Erro", font="Arial 20", pady= 10, padx=10, command=mensagemErro).pack()

botaoQuestion = tk.Button(janela, text="Questão", font="Arial 20", pady= 10, padx=10, command=mensagemQuestao).pack()

botaoSimNao = tk.Button(janela, text="Sim ou Não", font="Arial 20", pady= 10, padx=10, command=mensagemOkCancel).pack()

botaoRepetirCancelar = tk.Button(janela, text="Repetir ou Cancelar", font="Arial 20", pady= 10, padx=10, command=mensagemRepetirCancelar).pack()


# Exibe a janela (deve vir por último)
janela.mainloop()