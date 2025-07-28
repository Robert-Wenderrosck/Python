import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient #Importa a classe MongoClient do módulo pymongo (MongoClient - usado para estabelecer uma conexão com o banco de dados MongoDB)

from bson.objectid import ObjectId  #ObjectId - é um identificador único utilizado pelo MongoDB para documentos

#Classe responsável pela lógica e interface gráfica do aplicativo
class GerenciadorTarefasApp:

    #Método construtor com o parâmetro 'janela', que é a janela principal do aplicativo
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gerenciador de tarefas")
        self.janela.geometry("950x700")
        self.janela.configure(bg="#f0f0f0")
        self.cliente = MongoClient("mongodb://localhost:27017") #Cria uma instância do MongoClient para conectar ao servidor MongoDB local na porta padrão 27017
        self.bd = self.cliente["gerenciador_tarefas_db"] #Acessa o banco de dados chamado 'gerenciador_tarefas_db'. Se o banco de dados não existir, ele será criado automaticamente ao inserir os primeiros dados
        self.colecao = self.bd["tarefas"] #Acessa a coleção 'tarefas' do banco de dados. Coleções no MongoDB são equivalentes a tabelas em banco de dados relacionais

        estilo = ttk.Style()
        estilo.theme_use('default')
        estilo.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fielbackground="#ffffff", font=("Arial", 11))
        estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        estilo.map("Treeview", background=[("selected", "black")], foreground=[("selected", "white")])

        quadro_entrada = tk.Frame(self.janela, bg="#f0f0f0") #Criação de um quadro para os campos de entrada de dados no aplicativo. Um quadro é um container que organiza e agrupa widgets dentro da janela principal.
        quadro_entrada.pack(pady=10, padx=10, fill="x") #Empacota o quadro dentro da janela principal

        #Criação de um título na tela
        rotulo_titulo = tk.Label(quadro_entrada, text="Titulo da Tarefa", font=("Arial", 12), bg="#f0f0f0")
        rotulo_titulo.grid(row=0, column=0, sticky='e', padx=5, pady=5)

        #Criação de um campo de entrada de dados na tela
        self.entrada_titulo = tk.Entry(quadro_entrada, width=55, font=("Arial", 11))
        self.entrada_titulo.grid(row=0, column=1, columnspan=3, sticky='w', padx=5, pady=5)

        rotulo_descricao = tk.Label(quadro_entrada, text="Descrição da Tarefa", font=("Arial", 12), bg="#f0f0f0")
        rotulo_descricao.grid(row=1, column=0, sticky='ne', padx=5, pady=5)

        #Criação de um widget de texto (Text) para a entrada da descrição da tarefa. O widget Text permite a inserção de múltiplas linhas de texto (diferente do Entry que é limitado a 1 linha)
        self.text_descricao = tk.Text(quadro_entrada, width=53, height=5, font=("Arial", 11))
        self.text_descricao.grid(row=1, column=1, columnspan=3, sticky='w', pady=5, padx=5)

        rotulo_status = tk.Label(quadro_entrada, text="Status", font=("Arial", 12), bg="#f0f0f0")
        rotulo_status.grid(row=2, column=0, sticky='we', pady=5, padx=5)

        #Criação da combobox com as opções 'Pendente' e 'Concluído'
        self.var_status = tk.StringVar() #Armazena a variável escolhida pelo usuário
        self.combo_status = ttk.Combobox(quadro_entrada, textvariable=self.var_status, values=["Pendente", "Concluída"], state='readonly', font=("Arial", 11))
        self.combo_status.grid(row=2, column=1, pady=5, padx=5)
        self.combo_status.current(0) #Deixa pré-selecionado na Combobox a opção 'Pendente'


        #Criação de um outro Quadro para colocar os botões
        quadro_botoes = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_botoes.pack(pady=10)

        #Criação dos botões
        botao_adicionar = tk.Button(quadro_botoes, text="Adicionar Tarefas", command=self.adicionar_tarefa, bg="#a5d6a7", font=("Arial", 11, "bold"), width=18)
        botao_adicionar.grid(row=0, column=0, padx=10, pady=5)

        botao_atualizar = tk.Button(quadro_botoes, text="Atualizar Tarefas", command=self.atualizar_tarefa, bg="#fff59d", font=("Arial", 11, "bold"), width=18)
        botao_atualizar.grid(row=0, column=1, padx=10, pady=5)

        botao_excluir = tk.Button(quadro_botoes, text="Excluir Tarefas", command=self.excluir_tarefa, bg="#ef9a9a", font=("Arial", 11, "bold"), width=18)
        botao_excluir.grid(row=0, column=2, padx=10, pady=5)

        #Criação de um Quadro apra colocar os filtros
        quadro_filtro = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_filtro.pack(pady=10)

        rotulo_filtro = tk.Label(quadro_filtro, text="Filtrar por Status: ", font=("Arial", 12), bg="#f0f0f0")
        rotulo_filtro.grid(row=0, column=0, padx=5)

        self.var_filtro = tk.StringVar()
        self.combo_filtro = ttk.Combobox(quadro_filtro, textvariable=self.var_filtro, values=["Todos", "Pendente", "Concluída"], state='readonly', font=("Arial", 11))
        self.combo_filtro.grid(row=0, column=1, padx=5)

        botao_filtro = tk.Button(quadro_filtro, text="Aplicar Filtro", command=self.aplicar_filtro, bg="#81d4fa", font=("Arial", 11, "bold"), width=15)
        botao_filtro.grid(row=0, column=2, padx=5)

        #Criação de um Quadro para colocar a TreeView
        quadro_arvore = tk.Frame(self.janela, bg="#f0f0f0")
        quadro_arvore.pack(pady=20, fill='both', expand=True) #Fill = 'both' - Faz com que  o quadro se expanda tanto na horizontal quanto na vertical, preenchendo o espaço disponível

        barra_rolagem = tk.Scrollbar(quadro_arvore, orient='vertical')
        barra_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

        self.arvore_tarefas = ttk.Treeview(quadro_arvore, columns=("Título", "Descrição", "Status"), show="headings", height=15, yscrollcommand=barra_rolagem.set)
        self.arvore_tarefas.heading("Título", text="Título")
        self.arvore_tarefas.heading("Descrição", text="Descrição")
        self.arvore_tarefas.heading("Status", text="Status")
        self.arvore_tarefas.column("Título", width=220)
        self.arvore_tarefas.column("Descrição", width=480)
        self.arvore_tarefas.column("Status", width=120)
        self.arvore_tarefas.bind("<<TreeviewSelect>>", self.ao_selecionar_tarefa)
        self.arvore_tarefas.pack(pady=10, padx=10, fill='both', expand=True)

        barra_rolagem.config(command=self.arvore_tarefas.yview)
        self.carregar_tarefas()
        self.id_tarefa_selecionada = None


    def carregar_tarefas(self, filtro_status=None):

        for item in self.arvore_tarefas.get_children():
            self.arvore_tarefas.delete(item)

        #Cria um dicionário vazio para a consulta ao banco de dados (este dicionário será usado como filtro para buscar tarefas específicas no MongoDB)
        consulta = {}

        #Verifica se o filtro 'filtro_status' é válido. Se 'filtro_status' não for None e estiver na lista ["Pendente", "Concluida"], atualiza o dicionário 'consulta'. O filtro "status será usado para buscar tarefas no banco de dados com o status correspondente.
        if filtro_status and filtro_status in ["Pendente", "Concluída"]:
            consulta = {"status": filtro_status}

        tarefas = self.colecao.find(consulta)

        for tarefa in tarefas:
            self.arvore_tarefas.insert("", tk.END,
                                       values=(tarefa["titulo"], tarefa["descricao"], tarefa["status"]),
                                       iid=str(tarefa["_id"]))


    def adicionar_tarefa(self):

        titulo = self.entrada_titulo.get().strip() #Obtém o texto do campo de entrada do título e remove quaisquer espaços em branco no início e no final da string
        descricao = self.text_descricao.get("1.0", tk.END).strip() #Obtém o texto do campo de descrição desde a posição 1.0 (primeira linha, primeira coluna) até o final // strip() é usado para remover espaços desnecessários
        status = self.var_status.get() #Obtém o valor selecionado no Combobox de status

        if not titulo:
            messagebox.showwarning("Aviso", "O título da tarefa não pode estar vazio.")
            return

        # Cria um dicionário representando a nova tarefa com os valores coletados dos campos de entrada
        nova_tarefa = {
                       "titulo": titulo, #Atribui o valor do título inserido
                       "descricao": descricao, #Atribui o valor da descrição inserida
                       "status": status #Atribui o status selecionado no Combobox
                       }


        self.colecao.insert_one(nova_tarefa) #Insere o dicionário 'nova_tarefa' no banco de dados MongoDB na coleção especificada
        self.carregar_tarefas() #Atualiza a treeview para refletir a nova tarefa adicionada
        self.limpar_campos_entrada()

        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")

    def limpar_campos_entrada(self):

        self.entrada_titulo.delete(0, tk.END)
        self.text_descricao.delete("1.0", tk.END)
        self.var_status.set("Pendente") #Redefine o Combobox de status para o valor padrão "Pendente"


    def atualizar_tarefa(self):

        if not self.id_tarefa_selecionada:

            messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada para atualizar")
            return

        titulo = self.entrada_titulo.get().strip()
        descricao = self.text_descricao.get("1.0", tk.END).strip()
        status = self.var_status.get()

        if not titulo:
            messagebox.showwarning("Aviso", "O título da tarefa não pode estar vazio.")
            return

        dados_atualizacao = {
                             "$set": {
                                     "titulo": titulo,
                                     "descricao": descricao,
                                     "status": status
                                     }
                             }
        self.colecao.update_one({"_id": ObjectId(self.id_tarefa_selecionada)}, dados_atualizacao)
        self.var_filtro.set("Todos")  # Muda o filtro visualmente para "Todos"
        self.carregar_tarefas(filtro_status=None)  # Carrega tudo sem filtro
        self.limpar_campos_entrada()
        self.id_tarefa_selecionada = None
        messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")

    def excluir_tarefa(self):

        if not self.id_tarefa_selecionada:
            messagebox.showwarning("Aviso", 'Nenhuma tarefa selecionada para excluir.')
            return
        confirmar = messagebox.askyesno("Confirmar Exclusão", "Deseja realmente excluir esta tarefa?")

        if confirmar:
            self.colecao.delete_one({"_id": ObjectId(self.id_tarefa_selecionada)})
            self.carregar_tarefas()
            self.id_tarefa_selecionada = None
            messagebox.showinfo("Sucesso", "Tarefa excluida com sucesso!")

    def aplicar_filtro(self):

        filtro_escolhido = self.var_filtro.get()

        if filtro_escolhido == "Todos":
            self.carregar_tarefas()
        else:
            self.carregar_tarefas(filtro_status=filtro_escolhido)

    def ao_selecionar_tarefa(self, event):

        selecionado = self.arvore_tarefas.selection()

        if selecionado:
            self.id_tarefa_selecionada = selecionado[0]
            dados_tarefa = self.colecao.find_one({"_id": ObjectId(self.id_tarefa_selecionada)})

            if dados_tarefa:
                self.entrada_titulo.delete(0, tk.END)
                self.entrada_titulo.insert(tk.END, dados_tarefa["titulo"])

                self.text_descricao.delete("1.0", tk.END)
                self.text_descricao.insert(tk.END, dados_tarefa["descricao"])

                self.var_status.set(dados_tarefa["status"])









janela_principal = tk.Tk()

#Cria uma instância da classe 'GerenciadorTarefasApp'. A janela principal criada anteriormente ('janela_principal') é passada como argumento para o construtor da classe. Isso permite que a interface gráfica definida na classe seja exibida na tela principal
app = GerenciadorTarefasApp(janela_principal)

janela_principal.mainloop()