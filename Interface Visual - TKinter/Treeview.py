import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from openpyxl import load_workbook

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
#função para criar item
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

        messagebox.showinfo("Atenção!", message="Item cadastrado com sucesso!")

        contarNumeroLinhas()

#----------------------------------------------------------------------------------
#função para deletar item
def deletarItemTreeView():
    selecionarItens = treeviewDados.selection()

    for item in selecionarItens:

        treeviewDados.delete(item) #Deletando o item selecionado

        messagebox.showinfo("Atenção!", message="Item deletado com sucesso!")

        exibirID.delete(0, "end")
        exibirNome.delete(0, "end")
        exibirIdade.delete(0, "end")
        exibirSexo.delete(0, "end")

        contarNumeroLinhas()

#----------------------------------------------------------------------------------
#função para criar item

def alterarItemTreeView():

    itemSelecionado = treeviewDados.selection()


    if exibirID.get() == "":
        messagebox.showinfo("Atenção!", "Digite um ID")

    elif exibirNome.get() == "":
        messagebox.showinfo("Atenção!", "Digite um Nome")

    elif exibirIdade.get() == "":
        messagebox.showinfo("Atenção!", "Digite uma Idade")

    elif exibirSexo.get() == "":
        messagebox.showinfo("Atenção!", "Digite um Sexo")

    else:

        treeviewDados.item(itemSelecionado, values=(
            str(exibirID.get()),
            str(exibirNome.get()),
            str(exibirIdade.get()),
            str(exibirSexo.get())
        ))

        exibirID.delete(0, "end")
        exibirNome.delete(0, "end")
        exibirIdade.delete(0, "end")
        exibirSexo.delete(0, "end")

        messagebox.showinfo("Atenção!", message="Item alterado com sucesso!")
        contarNumeroLinhas()

def exportarParaExcel():

    workbook = load_workbook(filename="C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\TKinter\\Interface Visual - TKinter\\Tratamento_Dados.xlsx") #Selecionando o arquivo
    sheet = workbook["Itens"] #Selecionando a aba da planilha
    sheet.delete_rows(idx=1, amount=30000) #Deletando linhas

    for numeroLinha in treeviewDados.get_children():

        #Pegando os dados da linha que estiver passando
        linha = treeviewDados.item(numeroLinha)["values"]

        #Passando os dados da linha para a planilha do Excel
        sheet.append(linha)

    #Salva a planilha com todas as informações do TreeView
    workbook.save(filename="C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\TKinter\\Interface Visual - TKinter\\Dados_Exportados_TreeView.xlsx")

    messagebox.showinfo("Atenção!", message="Itens exportados com sucesso!")


botaoAdicionar = tk.Button(text="Cadastrar", font="Arial 20", command= addItemTreeView)
botaoAdicionar.grid(row=2, column=0, columnspan=2, sticky="NSEW", padx=5, pady=5)

botaoExcluir = tk.Button(text="Excluir", font="Arial 20", command= deletarItemTreeView)
botaoExcluir.grid(row=2, column=2, columnspan=2, sticky="NSEW", padx=5, pady=5)

botaoAlterar = tk.Button(text="Alterar", font="Arial 20", command= alterarItemTreeView)
botaoAlterar.grid(row=2, column=4, columnspan=2, sticky="NSEW", padx=5, pady=5)

botaoExportar = tk.Button(text="Exportar", font="Arial 20", command= exportarParaExcel)
botaoExportar.grid(row=2, column=6, columnspan=2, sticky="NSEW", padx=5, pady=5)

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

labelNumeroLinhas = tk.Label(text="Linhas: ", font="Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, sticky="W")

def contarNumeroLinhas(item=""):
    numero = 0
    linhas = treeviewDados.get_children(item)

    for linha in linhas:

        numero += 1 #Somo linha por linha para contar quantas tem na TreeView

    #Imprimo o total de linha na label
    labelNumeroLinhas.config(text="Linhas: " + str(numero))

#Chamando a função que conta a quantidade de linhas na TreeView
contarNumeroLinhas()

# Exibe a janela (deve vir por último)
janela.mainloop()