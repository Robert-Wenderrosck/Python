import tkinter as tk

#Criando RadioButton manual

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - RadioButton")
janela.geometry("400x400")

def imprimirItemSelecionado():

    print("Você selecionou a letra: " + variavelOpcaoSelecionada.get())

variavelOpcaoSelecionada = tk.StringVar(janela, "0") #janela, "0" - serve para deixar o botão desmarcado

radiobutton_1 = tk.Radiobutton(janela, text="Letra A", font="Arial 26", value="A", variable=variavelOpcaoSelecionada, command=imprimirItemSelecionado).pack()

radiobutton_2 = tk.Radiobutton(janela, text="Letra B", font="Arial 26", value="B", variable=variavelOpcaoSelecionada, command=imprimirItemSelecionado).pack()

radiobutton_3 = tk.Radiobutton(janela, text="Letra C", font="Arial 26", value="C", variable=variavelOpcaoSelecionada, command=imprimirItemSelecionado).pack()

# Exibe a janela (deve vir por último)
janela.mainloop()