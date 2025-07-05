import pandas as pd
import matplotlib.pyplot as grafico

frutas_dataFrame = pd.read_excel("Base_Grafico.xlsx")

print("\n DataFrame Frutas \n")
print(frutas_dataFrame)
print("\n")

figura = grafico.figure(figsize=(15,5))

frutas = frutas_dataFrame["Frutas"]
total = frutas_dataFrame["Total Vendas"]

#2 = linha, 3 = colunas, 1 = posição do gráfico na imagem

figura.add_subplot(231) #.add_subplot adiciona um gráfico na parte de uma figura
grafico.plot(frutas, total, label="plot")
grafico.legend()
grafico.title("Gráfico 1")
grafico.annotate(frutas[0], (frutas[0], total[0]))
grafico.annotate(frutas[1], (frutas[1], total[1]))
grafico.annotate(frutas[2], (frutas[2], total[2]))
grafico.annotate(frutas[3], (frutas[3], total[3]))
grafico.annotate(frutas[4], (frutas[4], total[4]))
grafico.xticks([]) #Deixa a legenda do eixo x sem nada escrito
grafico.show()

#-----------------------------------------------------------
#2 = linha, 3 = colunas, 2 = posição do segundo gráfico na imagem
figura.add_subplot(232)
grafico.bar(frutas, total, label="bar")
grafico.legend()
grafico.title("Gráfico 2")
grafico.annotate(frutas[0], (frutas[0], total[0]))
grafico.annotate(frutas[1], (frutas[1], total[1]))
grafico.annotate(frutas[2], (frutas[2], total[2]))
grafico.annotate(frutas[3], (frutas[3], total[3]))
grafico.annotate(frutas[4], (frutas[4], total[4]))
grafico.xticks([]) #Deixa a legenda do eixo x sem nada escrito
grafico.show()

#-----------------------------------------------------------
#2 = linha, 3 = colunas, 3 = posição do terceiro gráfico na imagem
figura.add_subplot(233)
grafico.pie(total, labels = frutas)
grafico.title("Gráfico 3")
grafico.show()

#-----------------------------------------------------------
#2 = linha, 3 = colunas, 5 = posição do quarto gráfico na imagem (no meio da segunda linha)
figura.add_subplot(235)
grafico.stem(frutas, total, label="stem")
grafico.legend()
grafico.title("Gráfico 4")
grafico.annotate(frutas[0], (frutas[0], total[0]))
grafico.annotate(frutas[1], (frutas[1], total[1]))
grafico.annotate(frutas[2], (frutas[2], total[2]))
grafico.annotate(frutas[3], (frutas[3], total[3]))
grafico.annotate(frutas[4], (frutas[4], total[4]))
grafico.xticks([]) #Deixa a legenda do eixo x sem nada escrito
grafico.show()














