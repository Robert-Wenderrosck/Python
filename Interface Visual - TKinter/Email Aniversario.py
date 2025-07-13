import pandas as pd
from datetime import date
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import win32com.client as win32

#Preparando o outlook
outlook = win32.Dispatch("outlook.application")

#----------------------Criando a interface gráfica-------------------------------

janela =tk.Tk()

estilo = ttk.Style()
estilo.theme_use("alt")
estilo.configure(".", font="Arial 20", rowheight=30)

#Criando a treeview com 3 colunas
treeviewDados = ttk.Treeview(janela, columns=(1, 2, 3), show="headings")

#Renomeando as colunas
treeviewDados.column("1", anchor="center")
treeviewDados.heading("1", text="Nome")

treeviewDados.column("2", anchor="center")
treeviewDados.heading("2", text="Nascimento")

treeviewDados.column("3", anchor="center")
treeviewDados.heading("3", text="Email")

treeviewDados.grid(row=2, column=0, columnspan=8, sticky="NSEW")



#----------------------Tratando dados para selecionar os aniversariantes-------------------------------

arquivoAniversario = pd.read_excel("Aniversario.xlsx")

arquivoAniversario["Nascimento"] = arquivoAniversario["Nascimento"].astype(str) #Converte a coluna nascimento para texto



arquivoAniversario["Ano"] = arquivoAniversario["Nascimento"].str[:4] #Cria uma coluna nova chamada ano e adiciona os 4 primeiros digitos de cada linha da coluna Nascimento

arquivoAniversario["Mes"] = arquivoAniversario["Nascimento"].str[5:7] #Cria uma coluna nova chamada mês e adiciona os 2 digitos que representa os meses

arquivoAniversario["Dia"] = arquivoAniversario["Nascimento"].str[-2:] #Cria uma coluna nova chamada dia e adiciona os 2 últimos digitos que representa os dias


arquivoAniversario["Data Atual"] = date.today()

arquivoAniversario["Data Atual"] = arquivoAniversario["Data Atual"].astype(str) #Converte a coluna Data Atual para texto


arquivoAniversario["Ano Atual"] = arquivoAniversario["Data Atual"].str[:4]

arquivoAniversario["Mes Atual"] = arquivoAniversario["Data Atual"].str[5:7]

arquivoAniversario["Dia Atual"] = arquivoAniversario["Data Atual"].str[-2:]

#Comparando mês e dia e descobrindo os aniversariantes
arquivoAniversario["Aniversario"] = np.where((arquivoAniversario["Mes"] == arquivoAniversario["Mes Atual"]) &
                                             (arquivoAniversario["Dia"] == arquivoAniversario["Dia Atual"]), "Sim", "")



#loc - localiza e limita por um critério (filtra e deixa somente os aniversariantes do dia)
arquivoAniversario = arquivoAniversario.loc[arquivoAniversario["Aniversario"] != "", ["Nome", "Nascimento", "Email"]]

print(arquivoAniversario)

#Pega o email dos aniversariantes do dia
for linha in range(len(arquivoAniversario)):

    print(arquivoAniversario.iloc[linha, 2])
    #Populando os itens na TreeView com os dados dos aniversariantes do dia
    treeviewDados.insert("", "end", values=(str(arquivoAniversario.iloc[linha, 0]), #Nome
                                                         str(arquivoAniversario.iloc[linha, 1]), #Aniversário
                                                         str(arquivoAniversario.iloc[linha, 2]))) #Email


#----------------------Criando campos para preencher e botões de funções na treeview-------------------------------

#Label que exibe informações para o usuário
nome = tk.Label(text="Nome: ", font="Arial 12", )
nome.grid(row=0, column=0, sticky="W")
#Campo de entrada de dados
exibirNome = tk.Entry(font="Arial 12")
exibirNome.grid(row=0, column=1, sticky="W")

#Label que exibe informações para o usuário
nascimento = tk.Label(text="Nascimento: ", font="Arial 12", )
nascimento.grid(row=0, column=2, sticky="W")
#Campo de entrada de dados
exibirNascimento = tk.Entry(font="Arial 12")
exibirNascimento.grid(row=0, column=3, sticky="W")

#Label que exibe informações para o usuário
email = tk.Label(text="Email: ", font="Arial 12", )
email.grid(row=0, column=4, sticky="W")
#Campo de entrada de dados
exibirEmail = tk.Entry(font="Arial 12")
exibirEmail.grid(row=0, column=5, sticky="W")


def deletarItemTreeview():

    itens = treeviewDados.selection()

    for item in itens:

        #Deletando o item que está selecionado
        treeviewDados.delete(item)

        messagebox.showinfo(title="Atenção!", message="Item deletado com sucesso")

        contarNumeroLinhas()

#Criando botão de adicionar
botaoDeletar = tk.Button(text="Deletar", font="Arial 20", command= deletarItemTreeview)
botaoDeletar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

def adicionarItemTreeview():

    if exibirNome.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite um nome")

    elif exibirNascimento.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite uma data de nascimento")

    elif exibirEmail.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite um email")

    else:

        treeviewDados.insert("", "end", values=(str(exibirNome.get()),
                                                             str(exibirNascimento.get()),
                                                             str(exibirEmail.get())
                                                             ))

        messagebox.showinfo(title="Atenção!", message="Item cadastrado com sucesso")

        #Removendo as informações do campos digitáveis depois que o item for adicionado
        exibirNome.delete(0, "end")
        exibirNascimento.delete(0, "end")
        exibirEmail.delete(0, "end")

        contarNumeroLinhas()


#Criando botão de adicionar
botaoAdicionar = tk.Button(text="Adicionar", font="Arial 20", command= adicionarItemTreeview)
botaoAdicionar.grid(row=1, column=2, columnspan=2, sticky="NSEW")

def alterarItemTreeview():

    if exibirNome.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite um nome")

    elif exibirNascimento.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite uma data de nascimento")

    elif exibirEmail.get() == "":
        messagebox.showinfo(title="Atenção!", message="Digite um email")

    else:

        #Pega o item selecionado e altera pelos valores que estão nos campos preenchidos
        itemSelecionado = treeviewDados.selection()[0]
        treeviewDados.item(itemSelecionado,
                           values=(str(exibirNome.get()),
                                   str(exibirNascimento.get()),
                                   str(exibirEmail.get())
                                   ))

        # Removendo as informações do campos digitáveis depois que o item for adicionado
        exibirNome.delete(0, "end")
        exibirNascimento.delete(0, "end")
        exibirEmail.delete(0, "end")

        messagebox.showinfo(title="Atenção!", message="Item alterado com sucesso")


#Criando botão de alterar
botaoAlterar = tk.Button(text="Alterar", font="Arial 20", command= alterarItemTreeview)
botaoAlterar.grid(row=1, column=4, columnspan=2, sticky="NSEW")

def criarItemTreeview():

    for numeroLinha in treeviewDados.get_children():     #get_children pega todos os dados do treeview
        dadosDaLinha = treeviewDados.item(numeroLinha)["values"]    #Pega os dados das linhas

        #Criando um novo email
        emailOutlook = outlook.CreateItem(0)

        nome = treeviewDados.item(numeroLinha)["values"][0]
        aniversario = treeviewDados.item(numeroLinha)["values"][1]
        email = treeviewDados.item(numeroLinha)["values"][2]

        emailOutlook.To = email
        emailOutlook.Subject = "Feliz Aniversário " + str(nome)

        #Colocar o 'f' antes deixa juntar texto com variáveis // <b> coloca o texto seguinte em negrito // <p> pula liinha // <a href=""> para colocar um hyperlink // <img src=""> - para colocar uma imagem
        emailOutlook.HTMLBody = f"""  
        <p>Parabéns, <b>{nome}</b>!</p>
        <p><font color="green">Esse é um dia especial, aproveite seu dia!</font></p>
        <p><a href="https://www.mensagemaniversario.com.br/img/f2/19/desejo-um-dia-com-grandes-alegrias-md.jpg">Clique aqui para acessar seu presente.</a></p>
        <p> Atenciosamente, Robert! </p>
        """

        emailOutlook.save()  # .save() - Salva como rascunho // .send() - Envia

    messagebox.showinfo(title="Atenção!", message="Emails criados com sucesso!")

#Criando número de aniversariantes no final da treeview
labelNumeroLinhas = tk.Label(text="Linhas: ", font="Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, sticky="W")

#Função para contar o total de aniversariantes
def contarNumeroLinhas(item=""): #Passa linha por linha até encontrar uma vazia
    numero = 0
    linhas = treeviewDados.get_children(item)

    for linha in linhas:
        numero +=1

    labelNumeroLinhas.config(text="Aniversariantes: " + str(numero))

contarNumeroLinhas()


#Criando botão de criar email
botaoCriarEmail = tk.Button(text="Criar email", font="Arial 20", command= criarItemTreeview)
botaoCriarEmail.grid(row=1, column=6, columnspan=2, sticky="NSEW")


def passaDadosParaEntry(event): #Event = clicar 2x
    item = treeviewDados.selection()

    for linha in item:

        #Limpa os campos do Entry
        exibirNome.delete(0, "end")
        exibirNascimento.delete(0, "end")
        exibirEmail.delete(0, "end")

        #Passando os itens da treeviewDados para os campos digitáveis
        exibirNome.insert(0, treeviewDados.item(linha, "values")[0])
        exibirNascimento.insert(0, treeviewDados.item(linha, "values")[1])
        exibirEmail.insert(0, treeviewDados.item(linha, "values")[2])


#Double-1: quando clicar 2x ele vai chamar a função para passar os dados da linha da treeview para os campos Entry
treeviewDados.bind("<Double-1>", passaDadosParaEntry)

janela.mainloop()