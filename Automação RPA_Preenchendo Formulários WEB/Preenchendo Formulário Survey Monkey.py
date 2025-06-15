from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from selenium.webdriver.support.select import Select


navegador = opcoesSelenium.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")

tempoEspera.sleep(5)

#Preenche o nome
navegador.find_element(By.NAME, "72542598").send_keys("Robert Carvalho")

tempoEspera.sleep(3)

#Preenche o email
navegador.find_element(By.NAME, "72542821").send_keys("wenderrosckrc@gmail.com")

tempoEspera.sleep(3)

sexo = "Masculino"

if sexo == "Masculino":

    #Seleciona o campo Masculino
    navegador.find_element(By.ID, "583517054").click()

else:

    #Seleciona o campo Feminino
    navegador.find_element(By.ID, "583517055").click()

tempoEspera.sleep(3)

#Selecionar a cor PRETA como favorita
pegaDropDown = navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/form/div[4]/div/div/div/div/fieldset/div/select')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(5)

tempoEspera.sleep(4)

#Clicar no botão de enviar
navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/footer/div/div/button').click()

tempoEspera.sleep(4)

