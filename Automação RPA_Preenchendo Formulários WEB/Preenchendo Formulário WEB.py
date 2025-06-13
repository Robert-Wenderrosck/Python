from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

#Tempo para o computador abrir o formulário
tempoEspera.sleep(4)

#Preenche o campo Nome
navegador.find_element(By.NAME, "q3_nome[first]").send_keys("Robert")

tempoEspera.sleep(1)

#Preenche o campo Sobrenome
navegador.find_element(By.NAME, "q3_nome[last]").send_keys("Carvalho")

tempoEspera.sleep(1)

#Preenche o campo Email
navegador.find_element(By.NAME, "q4_email").send_keys("wenderrosckrc@gmail.com")

tempoEspera.sleep(2)

#Seleciona o estado civil "Solteiro"
pegaDropDown = navegador.find_element(By.ID, "input_5")
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(1)

tempoEspera.sleep(2)

filho = "Não"

if filho == "Sim":

    navegador.find_element(By.ID, "label_input_6_0").click()

elif filho == "Não":

    navegador.find_element(By.ID, "label_input_6_1").click()

tempoEspera.sleep(4)

#Seleciona a cor preta
navegador.find_element(By.ID, "label_input_7_4").click()

tempoEspera.sleep(4)

#Seleciona a cor azul
navegador.find_element(By.ID, "label_input_7_0").click()

tempoEspera.sleep(4)

#Marcou 5 estrelas como avaliação
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()

tempoEspera.sleep(3)

#Marca a opção "Muito satisfeito" no Campo Qualidade do Serviço
navegador.find_element(By.ID, "input_9_0_3").click()

tempoEspera.sleep(3)

#Marca a opção "Satisfeito" no Campo Grau de Dificuldade
navegador.find_element(By.ID, "input_9_1_2").click()

tempoEspera.sleep(3)

#Clica no botão enviar
navegador.find_element(By.ID, "input_2").click()
