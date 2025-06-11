from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera
import pyautogui as funcoesTeclado

import pandas as pd

navegador = opcoesSelenium.Chrome()

#Preparando o site
navegador.get("https://www.magazineluiza.com.br/")

#Procura pelo campo ID e digita o nome do produto
navegador.find_element(By.ID, "input-search").send_keys("geladeira")

#Tempo para o computador processar as informações
tempoEspera.sleep(2)

#Digita "enter" para procurar o produto
funcoesTeclado.press("enter")

tempoEspera.sleep(10)

#Criando o DataFrame/vetor que vai receber os dados
listaDataFrame = []

#No site, para pegar cada produto foi necessário utilizar a Classe para obter as informações (variação nessa etapa depende do site)
listaProdutos = navegador.find_elements(By.CLASS_NAME, "fdofhQ")

for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

#Código para pegar o nome do produto (Nome pode estar em uma das 2 classes)
#sc-dxlmjS / NMyym

    if nomeProduto == "":

        try:
            #Tenta pegar o nome (texto) utilizando uma das CLasses do produto para colocar na variável
            nomeProduto = item.find_element(By.CLASS_NAME, "NMyym").text

        except Exception:
            pass

    elif nomeProduto == "":

        try:
            # Tenta pegar o nome (texto) utilizando a outra Classe do produto para colocar na variável
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-dxlmjS").text

        except Exception:
            pass

#-----------------------------------------------------------
#Código para pegar o preço do produto (Nome pode estar em uma das 4 classes)
#sc-dcJsrY / eLxcFM / sc-hgRRfv / dfAhbD

    if precoProduto == "":

        try:
            #Tenta pegar o preço (texto) utilizando uma das CLasses do produtol
            precoProduto = item.find_element(By.CLASS_NAME, "dfAhbD").text

        except Exception:
            pass

    elif precoProduto == "":

        try:
            #Tenta pegar o preço (texto) utilizando uma das CLasses do produto
            precoProduto = item.find_element(By.CLASS_NAME, "sc-hgRRfv").text

        except Exception:
            pass

    elif precoProduto == "":

        try:
            #Tenta pegar o preço (texto) utilizando uma das CLasses do produto
            precoProduto = item.find_element(By.CLASS_NAME, "eLxcFM").text

        except Exception:
            pass

    elif precoProduto == "":

        try:
            #Tenta pegar o preço (texto) utilizando uma das CLasses do produto
            precoProduto = item.find_element(By.CLASS_NAME, "sc-dcJsrY").text

        except Exception:
            pass

    else:
        #Se não achar o preço em nenhuma das classes vai colocar 0
        precoProduto = "0"

#------------------------------------------------------------
#Código para pegar a url do produto

    if urlProduto == "":

        try:
            #Tenta pegar a url (texto) do produto
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")

        except Exception:
            pass

    else:

        urlProduto = "-"

    print(nomeProduto, "-", precoProduto)
    print(urlProduto)

    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto

    #Populando o DataFrame/vetor com as informações
    listaDataFrame.append(dadosLinha)

#Criando excel para salvar os dados
arquivoExcel = pd.ExcelWriter('dados_Magalu_Geladeira.xlsx', engine='xlsxwriter')
arquivoExcel.close()

dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dados_Magalu_Geladeira.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

#salva as informações no arquivo Excel // Nova biblioteca panda não usa mais ".save()"
arquivoExcel.close()
