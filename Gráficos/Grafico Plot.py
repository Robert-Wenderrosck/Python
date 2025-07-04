import pandas as pd
import matplotlib.pyplot as grafico

frutas_dataFrame = pd.read_excel("Base_Grafico.xslx")

print("\n DataFrame Frutas \n")
print(frutas_dataFrame)
print("\n")

#plot = gráfico de linhas
grafico.plot(frutas_dataFrame["Frutas"], frutas_dataFrame["Total Vendas"])
grafico.title("Vendas Frutas")
grafico.xlabel("Nome das Frutas")
grafico.ylabel("Total de Vendas")
grafico.show()  #.show - cria e apresenta o gráfico
























