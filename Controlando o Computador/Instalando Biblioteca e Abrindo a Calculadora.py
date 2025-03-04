import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

"""
# Comando para pegar as coordenadas após 5 segundos de onde o cursor do mouse estiver:
print(posicaoMouse.position())
"""

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=1134, y=1076)

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(1134, 1076)

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Escrevendo a palavra calculadora
posicaoMouse.typewrite('calculadora')

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)

#Movendo o mouse até o aplicativo da calculadora
posicaoMouse.moveTo(x=1019, y=487)

#Tempo de espera para que o computador possa processar as informações  // Só pra ver acontecer
tempoEspera.sleep(2)

#Clicando na opção da busca por calculadora
posicaoMouse.click(x=1019, y=487)

#Tempo de espera para que o computador possa processar as informações // Só pra ver acontecer
tempoEspera.sleep(2)