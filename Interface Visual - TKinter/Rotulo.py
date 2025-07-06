import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.title("Interface gráfica")
janela.geometry("900x600")

# Cria os textos (Labels)
#relief - relevo (borda decorativa) -> Ex.: flat / raised / sunken / groove / ridge
#backgroud - cor do fundo
#foreground - cor do texto
rotulo1 = tk.Label(janela, text="Python", relief="flat", background="green", foreground="white", font="Arial 30")
rotulo2 = tk.Label(janela, text="Python", relief="raised", background="green", foreground="white", font="Arial 30")
rotulo3 = tk.Label(janela, text="Python", relief="sunken", background="green", foreground="white", font="Arial 30")
rotulo4 = tk.Label(janela, text="Python", relief="groove", background="green", foreground="white", font="Arial 30")
rotulo5 = tk.Label(janela, text="Python", relief="ridge", background="green", foreground="white", font="Arial 30")
rotulo1.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()

texto = """Curso de TKinter
Aprendendo como criar
Interface gráfica com 
Python.
"""
rotulo6 = tk.Label(janela, font= "Arial 40 bold", text= texto)
rotulo6.pack()

# Exibe a janela (deve vir por último)
janela.mainloop()

"""
Para salvar como um arquivo executável:
Certificar-se que na pasta do arquivo está instalado "pyinstaller" e "pyinstaller-hooks-contrib" --> Clica na pasta --> "Settings" --> "Python Interpreter"
Salvar o arquivo em "Save as" diretamente na pasta principal (Nesse caso, pasta "TKinter")
No terminal digitar 'pyinstaller -w "Rotulo.py" -> Enter
Na pasta do projeto no computador -> Na pasta "dist" -> Na pasta com o nome do arquivo estará o arquivo executável 

"""