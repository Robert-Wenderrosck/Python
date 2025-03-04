import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=1134, y=1076)

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(1134, 1076)

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Digitando o nome do navegador Microsoft Edge
posicaoMouse.typewrite('Microsoft Edge')

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Aperta enter para abrir o Microsoft Edge
posicaoMouse.press('enter')

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Digitando a palavra Dólar para pesquisar no navegador
posicaoMouse.typewrite('Dolar hoje')

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(3)

#Aperta enter para pesquisar o dolar
posicaoMouse.press('enter')

