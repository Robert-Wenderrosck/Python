#Desafio para preencher os campos de um formulário WEB (os quais alteram suas posições e atributos a cada envio) utilizando informações de funcionários de uma empresa de uma planilha excel
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from openpyxl import load_workbook

navegador = opcoesSelenium.Chrome()

#Abre o arquivo do excel
nome_arquivo_dados = "C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação RPA_Preenchendo Formulários WEB\\challenge.xlsx"
planilhaDados = load_workbook(nome_arquivo_dados)

#Seleciona a planilha "Sheet1"
sheet_selecionada = planilhaDados["Sheet1"]

#Abre o site
navegador.get("https://rpachallenge.com/?lang=EN")

tempoEspera.sleep(5)

#Clica em Start
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

tempoEspera.sleep(3)

#Para cada linha da coluna A, a partir da segunda linha até a última linha da planilha (inclusive)
for linha in range(2, len(sheet_selecionada["A"]) + 1):

    #Pegando o valor de cada linha das colunas e transformando o conteúdo em texto
    primeiroNome = sheet_selecionada['A%s' % linha].value
    ultimoNome = sheet_selecionada['B%s' % linha].value
    nomeEmpresa = sheet_selecionada['C%s' % linha].value
    cargoEmpresa = sheet_selecionada['D%s' % linha].value
    endereco = sheet_selecionada['E%s' % linha].value
    email = sheet_selecionada['F%s' % linha].value
    numero = sheet_selecionada['G%s' % linha].value


    # Preenche o primeiro nome
    navegador.find_element(By.XPATH, '//label[text()="First Name"]/following-sibling::input').send_keys(primeiroNome)
    print(primeiroNome)

    tempoEspera.sleep(3)

    # Preenche o ùltimo nome
    navegador.find_element(By.XPATH, '//label[text()="Last Name"]/following-sibling::input').send_keys(ultimoNome)
    print(ultimoNome)

    tempoEspera.sleep(3)

    #Preenche o nome da empresa
    navegador.find_element(By.XPATH, '//label[text()="Company Name"]/following-sibling::input').send_keys(nomeEmpresa)
    print(nomeEmpresa)

    tempoEspera.sleep(3)

    #Preenche o cargo na empresa
    navegador.find_element(By.XPATH, '//label[text()="Role in Company"]/following-sibling::input').send_keys(cargoEmpresa)
    print(cargoEmpresa)

    tempoEspera.sleep(3)

    # Preenche o endereço
    navegador.find_element(By.XPATH, '//label[text()="Address"]/following-sibling::input').send_keys(endereco)
    print(endereco)

    tempoEspera.sleep(3)

    # Preenche o email
    navegador.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input').send_keys(email)
    print(email)

    tempoEspera.sleep(3)

    # Preenche o número
    navegador.find_element(By.XPATH, '//label[text()="Phone Number"]/following-sibling::input').send_keys(numero)
    print(numero)

    tempoEspera.sleep(3)

    #Clica em Submit
    navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

    tempoEspera.sleep(4)

    print()




