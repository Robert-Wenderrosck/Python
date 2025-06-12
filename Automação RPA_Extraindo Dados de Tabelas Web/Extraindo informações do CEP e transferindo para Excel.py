from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd


navegador = opcoesSelenium.Chrome()
navegador.get("https://www.invertexto.com/consulta-cep")

#Tempo para o computador carregar as informações
tempoEspera.sleep(4)

#Inserindo um CEP na campo de CEP do site
navegador.find_element(By.ID, "cep-input").send_keys("28945-000")

#Tempo para o computador carregar as informações
tempoEspera.sleep(2)

#Clica no botão de pesquisar
navegador.find_element(By.XPATH, '//*[@id="pesquisar"]').click()

#Tempo para o computador carregar as informações
tempoEspera.sleep(6)

#Pega os dados da rua no site pelo XPATH
rua = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div[2]').text
print("Rua:", rua)

#Pega os dados do bairro no site pelo XPATH
bairro = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[3]/div[2]').text
print("Bairro:", bairro)

#Pega os dados da cidade no site pelo XPATH
cidade = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[4]/div[2]').text
print("Cidade:", cidade)

#Pega os dados do CEP no site pelo XPATH
cep = navegador.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div[1]/div[2]').text
print("CEP:", cep)

listaDataFrame = []

dadosLinha = rua + ";" + bairro + ";" + cidade + ";" + cep

#Populando o DataFrame/vetor com as informações
listaDataFrame.append(dadosLinha)

#Criando excel para salvar os dados
arquivoExcel = pd.ExcelWriter('informacoes_do_CEP.xlsx', engine='xlsxwriter')
arquivoExcel.close()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Rua;Bairro;Cidade;CEP'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('informacoes_do_CEP.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

#salva as informações no arquivo Excel // Nova biblioteca panda não usa mais ".save()"
arquivoExcel.close()