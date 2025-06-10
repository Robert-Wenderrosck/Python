from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

#Para controlar as teclas do computador e gerar um tempo de espera entre operações
import pyautogui as tempoEspera

#Para trabalhar com a ferramenta Excel
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengeocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#Criação de um vetor para armazenar os dados das tabelas
listaDataFrame = []

linha = 1

i = 1

#Copiar as informações da 3 abas do site
while i < 4:

    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)

        #Colocar os dados das tabelas no vetor
        listaDataFrame.append(linhaAtual.text)

        linha = linha + 1

    i += 1

    #Tempo para o computador processar os dados da tabela antes de ir para próxima aba
    tempoEspera.sleep(2)

    #Procura o XPATH do botão próximo e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # Tempo para o computador processar os dados da tabela antes de ir para próxima aba
    tempoEspera.sleep(2)

else:
    print("Dados extraídos com sucesso!")

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel.close()

dataFrame = pd.DataFrame(listaDataFrame, columns=['#;ID;Due Date'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

#salva as informações no arquivo Excel // Nova biblioteca panda não usa mais ".save()"
arquivoExcel.close()


