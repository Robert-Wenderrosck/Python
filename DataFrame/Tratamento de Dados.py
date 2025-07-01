import pandas as pd

dadosDataFrame = pd.read_excel("Tratamento_Dados.xlsx")
print(dadosDataFrame)
print("\n")

dadosDataFrame["Total Vendas"] = dadosDataFrame["Total Vendas"].fillna(dadosDataFrame["Total Vendas"].mean())
print("\n fillna - Preenche os valores vazios com a média \n")
print(dadosDataFrame)
print("\n")

"""Se quisesse trocar os valores em branco da Coluna "Total Vendas" por um valor fixo:
dadosDataFrame["Total Vendas"] = dadosDataFrame["Total Vendas"].fillna(5)
"""

"""Se quisesse trocar os valores em branco da Coluna "Total Vendas" pelo último registro válido dessa coluna:
dadosDataFrame["Total Vendas"] = dadosDataFrame["Total Vendas"].ffill()
"""


qtdVendas = dadosDataFrame["Vendedor"].value_counts()
print("\n value_counts = conta quantas linhas/ vendas foram feitas de acordo com uma coluna ('Vendedor')\n")
print(qtdVendas)
print("\n")

vendaVendedor = dadosDataFrame.groupby("Vendedor")[["Total Vendas"]].sum()
print("\n groupby = agrupa as informações /.sum soma as informações agrupadas\n")
print(vendaVendedor)
print("\n")
