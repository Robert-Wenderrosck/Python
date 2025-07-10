import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - Treeview")

#Inserindo títulos e campos para digitar as informações da treeview
id = tk.Label(text="ID: ", font="Arial 12").grid(row=1, column=0, sticky="E")

exibirID = tk.Entry(font="Arial 12")
exibirID.grid(row=1, column=1, sticky="W")

#----------------------------------------------------------------------------------

nome = tk.Label(text="Nome: ", font="Arial 12").grid(row=1, column=2, sticky="E")

exibirNome = (tk.Entry(font="Arial 12"))
exibirNome.grid(row=1, column=3, sticky="W")

#----------------------------------------------------------------------------------

idade = tk.Label(text="Idade: ", font="Arial 12").grid(row=1, column=4, sticky="E")

exibirIdade = tk.Entry(font="Arial 12")
exibirIdade.grid(row=1, column=5, sticky="W")

#----------------------------------------------------------------------------------

sexo = tk.Label(text="Sexo: ", font="Arial 12").grid(row=1, column=6, sticky="E")

exibirSexo = tk.Entry(font="Arial 12")
exibirSexo.grid(row=1, column=7, sticky="W")

#----------------------------------------------------------------------------------

def addItemTreeView():

    if exibirID.get() == "":
        messagebox.showinfo("Atenção!", "Digite um ID")

    elif exibirNome.get() == "":
        messagebox.showinfo("Atenção!", "Digite um Nome")

    elif exibirIdade.get() == "":
        messagebox.showinfo("Atenção!", "Digite uma Idade")

    elif exibirSexo.get() == "":
        messagebox.showinfo("Atenção!", "Digite um Sexo")

    else:

        #cadastrando o item
        treeviewDados.insert("", "end", values=(
            str(exibirID.get()),
            str(exibirNome.get()),
            str(exibirIdade.get()),
            str(exibirSexo.get())
        ))

        exibirID.delete(0, "end")
        exibirNome.delete(0, "end")
        exibirIdade.delete(0, "end")
        exibirSexo.delete(0, "end")

botaoAdicionar = tk.Button(text="Cadastrar", font="Arial 20", command= addItemTreeView)
botaoAdicionar.grid(row=2, column=0, columnspan=8, sticky="NSEW")

estilo = ttk.Style()
estilo.theme_use("alt")
estilo.configure(".")

treeviewDados = ttk.Treeview(janela, columns=(1, 2, 3, 4), show="headings")

#Populando o título
treeviewDados.column("1", anchor=tk.CENTER)
treeviewDados.heading("1", text="ID")

treeviewDados.column("2", anchor=tk.CENTER)
treeviewDados.heading("2", text="Nome")

treeviewDados.column("3", anchor=tk.CENTER)
treeviewDados.heading("3", text="Idade")

treeviewDados.column("4", anchor=tk.CENTER)
treeviewDados.heading("4", text="Sexo")

treeviewDados.insert("", "end", text="1", values=("1", "Allan", 29, "Masculino"))
treeviewDados.insert("", "end", text="2", values=("2", "Ana", 41, "Feminino"))
treeviewDados.insert("", "end", text="3", values=("3", "Berenice", 50, "Feminino"))
treeviewDados.insert("", "end", text="4", values=("4", "Roger", 21, "Masculino"))
treeviewDados.insert("", "end", text="5", values=("5", "Pedro", 45, "Masculino"))


treeviewDados.grid(row=3, column=0, columnspan=8, sticky="NSEW")

# Exibe a janela (deve vir por último)
janela.mainloop()