import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica - Calculadora")


def enviarNumeroPara(char):

    global calculoOperacoes
    calculoOperacoes += str(char) #char - pode passar apenas 1 item
    textoDeEntrada.set(calculoOperacoes) #Colocando todo o texto na variável que está linkado com o campo Entry

def deletarNumero():

    global calculoOperacoes

    textoSemUltimoDigito = calculoOperacoes[:-1] #Pego todo o texto que está no entry e excluo apenas o útimo digito
    calculoOperacoes = textoSemUltimoDigito #Colocando na variável o texto da operação sem o último digito
    textoDeEntrada.set(calculoOperacoes)

def limparTudo():

    global calculoOperacoes

    calculoOperacoes = "" #Limpando todo o texto da variável global
    textoDeEntrada.set(calculoOperacoes) #Substituindo todo o texto da variável pelo vazio (linha anterior)

def funcaoIgual():

    global calculoOperacoes

    resultadoCalculo = str(eval(calculoOperacoes)) #eval - Avalia se é um cálculo válido e efetua o cálculo de acordo com o sinal que está na variável global
    textoDeEntrada.set(resultadoCalculo)

    calculoOperacoes = resultadoCalculo #Mudo a variável que tinha a operação e coloco apenas o resultado do cálculo na variável

calculoOperacoes = ""
textoDeEntrada = tk.StringVar()

#Caixa de texto que exibe o resultado e as operações
textoExibeOperacoesResultado = tk.Entry(janela, font=("Arial 20 bold"), textvariable=textoDeEntrada, border=5, background="#BBBBBB", foreground="black",).grid(row=1, columnspan=5, padx=10, pady=15)

#Botão para o usuário digitar o número 7 na calculadora e esse número ficar armazenado na variável global
#lambda - Permite enviar vários dados em uma função
botaoNumero7 = tk.Button(janela, text="7", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("7")).grid(row=2, column=0, sticky="NSEW")

botaoNumero8 = tk.Button(janela, text="8", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("8")).grid(row=2, column=1, sticky="NSEW")

botaoNumero9 = tk.Button(janela, text="9", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("9")).grid(row=2, column=2, sticky="NSEW")

botaoDeletar = tk.Button(janela, text="DEL", border=5, foreground= "black", background= "#DB701F", font=("Arial 20 bold"), command = deletarNumero).grid(row=2, column=3, sticky="NSEW")

botaoDeletarTudo = tk.Button(janela, text="AC", border=5, foreground= "black", background= "#DB701F", font=("Arial 20 bold"), command = limparTudo).grid(row=2, column=4, sticky="NSEW")

botaoNumero4 = tk.Button(janela, text="4", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("4")).grid(row=3, column=0, sticky="NSEW")

botaoNumero5 = tk.Button(janela, text="5", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("5")).grid(row=3, column=1, sticky="NSEW")

botaoNumero6 = tk.Button(janela, text="6", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("6")).grid(row=3, column=2, sticky="NSEW")

botaoMultiplicacao = tk.Button(janela, text="*", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("*")).grid(row=3, column=3, sticky="NSEW")

botaoDivisao = tk.Button(janela, text="/", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("/")).grid(row=3, column=4, sticky="NSEW")

botaoNumero1 = tk.Button(janela, text="1", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("1")).grid(row=4, column=0, sticky="NSEW")

botaoNumero2 = tk.Button(janela, text="2", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("2")).grid(row=4, column=1, sticky="NSEW")

botaoNumero3 = tk.Button(janela, text="3", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("3")).grid(row=4, column=2, sticky="NSEW")

botaoAdicao = tk.Button(janela, text="+", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("+")).grid(row=4, column=3, sticky="NSEW")

botaoSubtracao = tk.Button(janela, text="-", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("-")).grid(row=4, column=4, sticky="NSEW")

botaoNumero0 = tk.Button(janela, text="0", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara("0")).grid(row=5, column=0, sticky="NSEW")

botaoPonto = tk.Button(janela, text=".", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = lambda:enviarNumeroPara(".")).grid(row=5, column=1, sticky="NSEW")

botaoIgual = tk.Button(janela, text="=", border=5, foreground= "black", background= "#BBBBBB", font=("Arial 20 bold"), command = funcaoIgual).grid(row=5, column=2, columnspan=3, sticky="NSEW") #columnspan - prolonga a coluna pelo número indicado
janela.mainloop()






