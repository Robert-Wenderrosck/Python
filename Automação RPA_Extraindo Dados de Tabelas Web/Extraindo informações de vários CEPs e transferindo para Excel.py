from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd

listaDataFrame = []

navegador = opcoesSelenium.Chrome()
navegador.get("https://www.invertexto.com/consulta-cep")

#Tempo para o computador carregar as informações
tempoEspera.sleep(4)

#Dicionário
dicionarioCEPS = {
    "CEP 1": "28945-000",
    "CEP 2": "23548-057",
    "CEP 3": "27945-290"
}

#Tempo para o computador carregar as informações
tempoEspera.sleep(3)

for contador in dicionarioCEPS.values():

    tempoEspera.sleep(4)

    #Pesquisar cada linha(contador) do dicionário de CEPS
    navegador.find_element(By.ID, "cep-input").send_keys(contador)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/span/button').click()

    tempoEspera.sleep(4)

    #Pega os elementos de cada CEP
    rua = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div[2]').text
    print("Rua:", rua)

    bairro = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[3]/div[2]').text
    print("Bairro:", bairro)

    cidade = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[4]/div[2]').text
    print("Cidade:", cidade)

    cep = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[1]/div[2]').text
    print("CEP:", cep)

    dadosLinha = rua + ";" + bairro + ";" + cidade + ";" + cep

    listaDataFrame.append(dadosLinha)

    navegador.find_element(By.ID, "cep-input").clear()

#Criando excel para salvar os dados
arquivoExcel = pd.ExcelWriter('informacoes_varios_CEP.xlsx', engine='xlsxwriter')
arquivoExcel.close()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Rua;Bairro;Cidade;CEP'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('informacoes_varios_CEP.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

#salva as informações no arquivo Excel // Nova biblioteca panda não usa mais ".save()"
arquivoExcel.close()