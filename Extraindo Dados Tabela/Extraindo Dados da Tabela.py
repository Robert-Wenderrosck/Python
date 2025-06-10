from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengeocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

linha = 1

for linhaAtual in linhas:

    print(linhaAtual.text)

    linha = linha + 1