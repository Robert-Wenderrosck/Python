import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica")
janela.geometry("900x600")

for linha in range(5):
    for coluna in range(3):
        #master - representa a janela PAI
        tabela = tk.Frame(master= janela, relief= "raised", borderwidth= 1)
        tabela.grid(row=linha, column=coluna, padx=5, pady=5) #padx/pady espaçamento entre as linhas e colunas
        criaLabel = tk.Label(master=tabela, text=f"Linha {linha} \n Coluna {coluna} \n") #f""{} permite juntar texto com variável
        criaLabel.pack()

# Exibe a janela (deve vir por último)
janela.mainloop()

"""
Para salvar como um arquivo executável:
Certificar-se que na pasta do arquivo está instalado "pyinstaller" e "pyinstaller-hooks-contrib" --> Clica na pasta --> "Settings" --> "Python Interpreter"
Salvar o arquivo em "Save as" diretamente na pasta principal (Nesse caso, pasta "TKinter")
No terminal digitar 'pyinstaller -w "Rotulo em Grid.py" -> Enter
Na pasta do projeto no computador -> Na pasta "dist" -> Na pasta com o nome do arquivo estará o arquivo executável 

"""