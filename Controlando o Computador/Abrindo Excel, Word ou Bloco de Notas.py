import pyautogui as escolha_opcao #escolha_opcao passa a ter todas as funções do pyautogui

#Criar uma caixa para escolher uma opção/botões
opcao = escolha_opcao.confirm('Clique no botão desejado',
             buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":

    #Estamos apertando as teclas Windows + r
    escolha_opcao.hotkey('win', 'r')

    #Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    #Digitar a palavra Excel na janela EXECUTAR
    escolha_opcao.typewrite('Excel')

    #Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    #Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    #Clicando na opção pasta de trabalho em branco
    escolha_opcao.click(x=414, y=267)

    #Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(3)

    #Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Excel')

    print("Você escolheu abrir o Excel")

elif opcao == "Word":

    # Estamos apertando as teclas Windows + r
    escolha_opcao.hotkey('win', 'r')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    # Digitar a palavra winword na janela EXECUTAR
    escolha_opcao.typewrite('winword')

    # Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    # Escolhendo a opção de criar um documento em branco
    escolha_opcao.press('Enter')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(3)

    # Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Word')

    print("Você escolheu abrir o Word")

else:

    # Estamos apertando as teclas Windows + r
    escolha_opcao.hotkey('win', 'r')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    # Digitar a palavra notepad na janela EXECUTAR
    escolha_opcao.typewrite('notepad')

    # Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(2)

    # Escolhendo a opção de criar um documento em branco
    escolha_opcao.press('Enter')

    # Aguarda 2 segundos para o computador processar
    escolha_opcao.sleep(3)

    # Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Bloco de Notas')

    print("Você escolheu abrir o Bloco de Notas")



