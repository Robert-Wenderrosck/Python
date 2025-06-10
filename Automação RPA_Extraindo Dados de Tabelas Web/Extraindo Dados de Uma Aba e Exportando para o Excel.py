from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pandas as pd

navegador = opcoesSelenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")

# Lista para armazenar as linhas completas como texto único
dataFrameLista = []

for linhaAtual in linhas:
    texto = linhaAtual.text
    print(texto)  # opcional: mostra no terminal
    dataFrameLista.append(texto)

# Criar DataFrame com uma coluna (nome da coluna)
df = pd.DataFrame(dataFrameLista, columns=['Dados'])

# Salvar no Excel, mantendo o índice como coluna no arquivo
with pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter') as arquivoExcel:
    df.to_excel(arquivoExcel, sheet_name='Sheet1', index=True)  # index=True inclui o índice

navegador.quit()
