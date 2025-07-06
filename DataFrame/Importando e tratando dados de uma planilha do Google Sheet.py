import pandas as pd

#Lendo planilha do Google Sheet
planilha_id = "1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD"

dados_DataFrame = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

print("\n dataFrame Google Sheets \n")
print(dados_DataFrame)
print("\n")

#del - deleta 1 coluna/linha por vez
#.drop - deletando mais de uma coluna/linha
dados_DataFrame = dados_DataFrame.drop(columns=["Produto", "Data Venda"])

print("\n dataFrame Google Sheets Vendedor e Total Vendas \n")
print(dados_DataFrame)
print("\n")

"""
Os dados da coluna Total Vendas do DataFrame estão como strings e não permitem que seja feita uma soma com a função .sum()
É necessário tratar os dados 
"""
#Trocar vírgula decimal para ponto decimal
dados_DataFrame["Total Vendas"] = dados_DataFrame["Total Vendas"].str.replace('.', '') #remover pontos de milhar
dados_DataFrame["Total Vendas"] = dados_DataFrame["Total Vendas"].str.replace(',', '.') #trocar vírgula decimal para ponto decimal

#Convertendo a coluna "Total Vendas" para numérico (float)
dados_DataFrame["Total Vendas"] = pd.to_numeric(dados_DataFrame["Total Vendas"], errors='coerce')


#Usando a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas
#.reset_index() para continuar como DataFrame
vendedorSomaTotal_dataFrame = dados_DataFrame.groupby("Vendedor")["Total Vendas"].sum().reset_index()
print("\n dataFrame Google Sheets resumo Vendedor e soma do Total Vendas \n")
print(vendedorSomaTotal_dataFrame)
print("\n")

#.to_excel -> transfere as informações do DataFrame para um arquivo excel
vendedorSomaTotal_dataFrame.to_excel('DataFrameVendedoresXTotalVendas.xlsx', sheet_name='Dados', index=False)



