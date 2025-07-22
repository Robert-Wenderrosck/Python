import pyodbc

import tkinter as tk
from tkinter import ttk, Label


def verifica_credenciais():


    #Estabelece conexão com o banco de dados
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver}; Server=localhost;Database=Projeto_Compras.db") #SQLite3 ODBC Driver - Programa instalado // Projeto_Compras.db - Arquivo SQL criado na mesma pasta desse arquivo
    cursor = conexao.cursor() #É uma ferramenta para executar os comandos e SQL

    #Verifica se as informações que foram inseridas no campo Entry são compatíveis com as do banco de dado (Nome e Senha)
    cursor.execute("Select * From Usuarios Where Nome = ? AND Senha = ?", (nome_usuario_entry.get(), senha_entry.get()))

    #fetchall - Passa os dados do banco para a variável
    usuario = cursor.fetchall() #Recebendo o resultado da Query

    if usuario:

        print("Logado com sucesso!")

        #Se a pessoa conseguir logar, encerra uma tela e cria uma outra
        janela_principal.destroy()

        def lista_dados():
            #Limpar os valores da treeview (se tiver algum)
            for linha in treeview.get_children():
                treeview.delete(linha)

            cursor.execute("SELECT * From Produtos") #Executa os valores retornados pelo comando SQL em uma variável
            valores = cursor.fetchall() #Armazena os valores retornados pelo comando SQL em uma variável = VALORES

            #Pega os elementos da variável VALORES e adiciona na treeview
            for linha in valores:
                treeview.insert("", "end", values=(linha[0], linha[1], linha[2], linha[3],))

        janela = tk.Tk()
        janela.title("Cadastro de Produtos")

        janela.configure(background="#F5F5F5")
        #janela.attributes("-fullscreen", True) #Coloca a tela em tela cheia

        #Cria um Label e uma Combobox chamado Nome
        Label(janela, text="Nome do Produto", font="Arial 16", background="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        nome_produto = ttk.Combobox(janela, font="Arial 16")
        nome_produto.grid(row=0, column=3, padx=10, pady=10, sticky="NSEW")

        #Pega valores únicos da coluna NomeProduto e ordena em ordem crescente
        cursor.execute("SELECT DISTINCT NomeProduto FROM Produtos ORDER BY NomeProduto ASC")

        #Armazena os valores retornados pelo comando SQL em uma variável
        valores = cursor.fetchall()

        #Cria uma lista com os valores retornados
        nomes_produtos = [valor[0] for valor in valores]

        #Define a lista de valores da combobox nome_produto
        nome_produto['values'] = nomes_produtos
        #---------

        # Cria um Label e uma Combobox chamado Descrição do Produto
        Label(janela, text="Descrição do Produto", font="Arial 16", background="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        descricao_produto = ttk.Combobox(janela, font="Arial 16")
        descricao_produto.grid(row=0, column=6, padx=10, pady=10, sticky="NSEW")

        # Pega valores únicos da coluna NomeProduto e ordena em ordem crescente
        cursor.execute("SELECT DISTINCT Descricao FROM Produtos ORDER BY Descricao ASC")

        # Armazena os valores retornados pelo comando SQL em uma variável
        valoresDescricao = cursor.fetchall()

        # Cria uma lista com os valores retornados
        descricao_produtos = [valor[0] for valor in valoresDescricao]

        # Define a lista de valores da combobox nome_produto
        descricao_produto['values'] = descricao_produtos

        #---------

        def cadastrar():

            #Cria uma nova janela em segundo plano para cadastrar produtos
            janela_cadastrar = tk.Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")

            janela_cadastrar.config(background="#FFFFFF")

            # Define a largura e altura da janela Cadastrar
            largura_janela = 500
            altura_janela = 250

            # Obtém a largura e altura da tela do computador
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()

            # Calcula a posição da janela para centralizar na tela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            # Define a posição da janela (no centro do monitor do usuário)
            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

            #Criação de Label e Entry para digitar o nome de um NOVO PRODUTO
            Label(janela_cadastrar, text="Nome do Produto", font="Arial 14", background="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")
            nome_produto_cadastrar = tk.Entry(janela_cadastrar, font="Arial 14")
            nome_produto_cadastrar. grid(row=0, column=1, padx=10, pady=10)

            #Criação de Label e Entry para digitar o nome de uma DESCRIÇÃO PARA O PRODUTO
            Label(janela_cadastrar, text="Descrição do Produto", font="Arial 14", background="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky="W")
            descricao_produto_cadastrar = tk.Entry(janela_cadastrar, font="Arial 14")
            descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)

            # Criação de Label e Entry para digitar o nome de um PREÇO DO PRODUTO
            Label(janela_cadastrar, text="Preço do Produto", font="Arial 14", background="#FFFFFF").grid(row=2,column=0,padx=10,pady=10,sticky="W")
            preco_produto_cadastrar = tk.Entry(janela_cadastrar, font="Arial 14")
            preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)

            #-----------------------------------

            def salvar_dados():

                #Cria uma tupla ('lista') com os valores dos campos de texto
                novo_produto_cadastrar = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get());

                #Executa um comando SQL para inserir os dados na tabela de produtos
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) VALUES (?, ?, ?)", novo_produto_cadastrar)

                conexao.commit() #Confirma o salvamento no banco de dados

                #Chama a função para listar os dados e atualizar na treeview
                lista_dados()

                janela_cadastrar.destroy() #Fecha a janela depois de salvar

                # Chama a função que soma a coluna de preço e conta a quantidade de linha
                calcula_soma_preco()


            botao_salvar_dados = tk.Button(janela_cadastrar, text="Salvar", command=salvar_dados, font="Arial 20")
            botao_salvar_dados.grid(row=4, column=0, columnspan=2, sticky="NSEW", pady=5, padx=5)

            botao_cancelar = tk.Button(janela_cadastrar, text="Cancelar", command=janela_cadastrar.destroy, font="Arial 20")
            botao_cancelar.grid(row=5, column=0, columnspan=2, sticky="NSEW", pady=5, padx=5)

            # Centralizar os widgets (campos) na janela
            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)


        botao_gravar = tk.Button(janela, text="Novo", command= cadastrar, font="Arial 26")
        botao_gravar.grid(row=5, column=0, columnspan=4, sticky="NSEW", pady=5)

        #------------------------------------------

        #Define o estilo da treeview
        style = ttk.Style(janela)
        treeview = ttk.Treeview(janela,style="mystyle.Treeview")
        style.theme_use("default")
        style.configure("mystyle.Treeview", font="Arial 14")

        #Nomeia e define as colunas da treeview
        colunas = ["ID", "Nome do Produto", "Descrição", "Preço"]
        treeview["columns"] = colunas

        #Chama a função para listar os valores do banco de dados na Treeview
        lista_dados()

        #Populo o cabeçalho da Treeview
        for col in colunas:

            treeview.heading(col, text=col)

        #Exibindo treeview na tela
        treeview.grid(row=4, column=0, columnspan=10, padx=5, pady=5, sticky="NSEW")

        #Ocutando a coluna 0 da treeview
        treeview.column("#0", width=0, stretch=False)

        def limpaDados():
            #Limpa todos os dados da treeview
            for linha in treeview.get_children():
                treeview.delete(linha)

        #------------------------------------------------

        soma_label = Label(janela, text="Total: R$ 0.00", font="Arial 20", background="#FFFFFF")
        soma_label.grid(row=3, column=0, columnspan=10, sticky="NSEW", padx=10, pady=10) #row=3 para ficar em cima da treeview

        def calcula_soma_preco():

            total = 0
            qtd_registros = 0

            for linha in treeview.get_children():
                valores = treeview.item(linha)['values']

                if valores:
                    #total = total + preço
                    total += float(valores[3]) #Coluna de preço // float para converter a coluna de preço que está como string e transformar em float (n° reais)
                    qtd_registros +=1

            soma_label.config(text=f"Total: R$ {total:.2f} - Itens: {qtd_registros}") #:.2f - Serve para colocar o separador de milhares

        #Chama a função que soma a coluna de preço e conta a quantidade de linha
        calcula_soma_preco()

        def editar_dados(event):

            #Obtém o item selecionado da treeview
            item_selecionado = treeview.selection()[0]

            valores_selecionados = treeview.item(item_selecionado)['values']



            # Cria uma nova janela em segundo plano para cadastrar produtos
            janela_edicao = tk.Toplevel(janela)
            janela_edicao.title("Editar Produto")

            janela_edicao.config(background="#FFFFFF")

            # Define a largura e altura da janela Cadastrar
            largura_janela = 500
            altura_janela = 250

            # Obtém a largura e altura da tela do computador
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()

            # Calcula a posição da janela para centralizar na tela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            # Define a posição da janela (no centro do monitor do usuário)
            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

            # Criação de Label e Entry para digitar o nome de um NOVO PRODUTO
            Label(janela_edicao, text="Nome do Produto", font="Arial 14", background="#FFFFFF").grid(row=0, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        sticky="W")
            nome_produto_edicao = tk.Entry(janela_edicao, font="Arial 14", textvariable=tk.StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)

            # Criação de Label e Entry para digitar o nome de uma DESCRIÇÃO PARA O PRODUTO
            Label(janela_edicao, text="Descrição do Produto", font="Arial 14", background="#FFFFFF").grid(row=1,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10,
                                                                                                             sticky="W")
            descricao_produto_edicao = tk.Entry(janela_edicao, font="Arial 14", textvariable=tk.StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1, column=1, padx=10, pady=10)

            # Criação de Label e Entry para digitar o nome de um PREÇO DO PRODUTO
            Label(janela_edicao, text="Preço do Produto", font="Arial 14", background="#FFFFFF").grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=10,
                                                                                                         sticky="W")
            preco_produto_edicao = tk.Entry(janela_edicao, font="Arial 14", textvariable=tk.StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2, column=1, padx=10, pady=10)

            # -----------------------------------

            def salvar_edicao():

                novo_nome = nome_produto_edicao.get()
                nova_descricao = descricao_produto_edicao.get()
                novo_preco = preco_produto_edicao.get()

                #Atualiza os valores do item selecionado na treeview
                treeview.item(item_selecionado, values=(valores_selecionados[0], novo_nome, nova_descricao, novo_preco))


                # Executa um comando SQL para alterar os dados na tabela de produtos
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ?",
                               (novo_nome, nova_descricao, novo_preco, valores_selecionados[0]))

                conexao.commit()  # Confirma o salvamento no banco de dados

                # Chama a função para listar os dados e atualizar na treeview
                lista_dados()

                #Chama a função que soma a coluna de preço e conta a quantidade de linha
                calcula_soma_preco()

                janela_edicao.destroy()  # Fecha a janela depois de salvar

            botao_salvar_edicao = tk.Button(janela_edicao, text="Editar", command=salvar_edicao, font="Arial 16", background="#008000", foreground="#FFFFFF")
            botao_salvar_edicao.grid(row=4, column=0, pady=20, padx=20)

            def deletar_registro():

                #Recupera o ID do registro
                selected_item = treeview.selection()[0]

                #Recupera o valor do registro
                id_selecionado = treeview.item(selected_item)['values'][0]

                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE Id=?", (id_selecionado,))

                conexao.commit()

                janela_edicao.destroy()

                #Chama a função para listar os dados e atualizar na treeview
                lista_dados()

                # Chama a função que soma a coluna de preço e conta a quantidade de linha
                calcula_soma_preco()


            botao_deletar_edicao = tk.Button(janela_edicao, text="Deletar", command=deletar_registro, font="Arial 16", background="#FF0000", foreground="#FFFFFF")
            botao_deletar_edicao.grid(row=4, column=1, pady=20, padx=20)

            # Centralizar os widgets (campos) na janela
            for i in range(5):
                janela_edicao.grid_rowconfigure(i, weight=1)

            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)

        #Evento de duplo clique na treeview para chamar a tela de editar dados
        treeview.bind("<Double-1>", editar_dados)

        # ------------------------------------------


        def filtrar_dados(nome_produto, descricao_produto):
            #Verifica se as combobox estão vazias
            if nome_produto.get() == "" and descricao_produto.get() == "":

                lista_dados() #Lista todos os dados na treeview

                #Chama a função que soma a coluna de preço e conta a quantidade de linha
                calcula_soma_preco()

                return #Sai da função

            #Monta a consulta SQL dinamicamente
            sql = "SELECT * FROM Produtos"

            params = []

            if nome_produto.get():

                #sql = SELECT * FROM Produtos WHERE NomeProduto LIKE ?
                sql += " WHERE NomeProduto LIKE ?"
                params.append('%' + nome_produto.get() + '%')

            if descricao_produto.get():

                if nome_produto.get():

                    sql += " AND"

                else:

                    sql += " WHERE"
                sql += " Descricao LIKE ?"
                params.append('%' + descricao_produto.get() + '%')

            cursor.execute(sql, tuple(params))
            produtos = cursor.fetchall()

            limpaDados()

            for dado in produtos:

                treeview.insert("", "end", values=(dado[0], dado[1], dado[2], dado[3]))

            # Chama a função que soma a coluna de preço e conta a quantidade de linha
            calcula_soma_preco()


        #Quando digitar qualquer letra na combobox faz o filtro
        nome_produto.bind('<KeyRelease>', lambda e:filtrar_dados(nome_produto, descricao_produto))
        descricao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))

        #Quando selecionar qualquer item da combobox faz o filtro
        nome_produto.bind('<<ComboboxSelected>>', lambda e: filtrar_dados(nome_produto, descricao_produto))
        descricao_produto.bind('<<ComboboxSelected>>', lambda e: filtrar_dados(nome_produto, descricao_produto))

        def deletar():

            # Recupera o ID do registro
            selected_item = treeview.selection()[0]

            # Recupera o valor do registro
            id_selecionado = treeview.item(selected_item)['values'][0]

            # Deleta o registro do banco de dados
            cursor.execute("DELETE FROM Produtos WHERE Id=?", (id_selecionado,))

            conexao.commit()

            # Chama a função para listar os dados e atualizar na treeview
            lista_dados()

            # Chama a função que soma a coluna de preço e conta a quantidade de linha
            calcula_soma_preco()


        botao_deletar = tk.Button(janela, text="Deletar", command=deletar, font="Arial 26")
        botao_deletar.grid(row=5, column=4, columnspan=4, sticky="NSEW", pady=5)


        #----------------------------------------------
        #Configura a janela para utilizar a barra de menus criada
        menu_barra = tk.Menu(janela)
        janela.config(menu=menu_barra)

        menu_arquivo = tk.Menu(menu_barra, tearoff=0) #Fixa o menu na barra superior da janela
        menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

        menu_arquivo.add_command(label="Cadastrar", command=cadastrar) #Cria uma opção no menu "Arquivo" chamada "Cadastrar"
        menu_arquivo.add_command(label="Sair", command=janela.destroy)  # Cria uma opção no menu "Arquivo" chamada "Sair"

        janela.mainloop() #Inicia a nova janela

        #Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

    else:

        messagem_lbl = tk.Label(janela_principal, text="Nome de usuário ou senha incorreta!", foreground="red")
        messagem_lbl.grid(row=3, column= 0, columnspan=2)

#----------------------------------------------------------

#Criando a tela TKinter
janela_principal = tk.Tk()
janela_principal.title("Tela de Login")
janela_principal.config(background="#F5F5F5")

#Define a largura e altura da janela
largura_janela = 450
altura_janela = 300

#Obtém a largura e altura da tela do computador
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

#Calcula a posição da janela para centralizar na tela
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

#Define a posição da janela (no centro do monitor do usuário)
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela, pos_x,pos_y))

#------------------------------------------------------------------




#Criando os rótulos
titulo_lbl = tk.Label(janela_principal,text="Tela de Login", font="Arial 20", foreground="blue", background="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

nome_usuario_lbl = tk.Label(janela_principal,text="Nome do Usuário", font="Arial 14", foreground="black", background="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, sticky="E")

senha_usuario_lbl = tk.Label(janela_principal,text="Senha", font="Arial 14", foreground="black", background="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, sticky="E")

#Criando os campos digitáveis
nome_usuario_entry = tk.Entry(janela_principal, font="Arial 18")
nome_usuario_entry.grid(row=1, column=1, pady=10)

senha_entry = tk.Entry(janela_principal, font="Arial 18", show="*") #show="*" faz com que a senha digitada no campo Entry apareça como *
senha_entry.grid(row=2, column=1, pady=10)

#Criando botões para logar e sair
entrar_btn = tk.Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

sair_btn = tk.Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")


#Centralizar os widgets (campos) na janela
for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)

for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

#Ajusta o tamanho dos botões para que fiquem uniformes
entrar_btn.config(width=10)
sair_btn.config(width=10)


janela_principal.mainloop()







