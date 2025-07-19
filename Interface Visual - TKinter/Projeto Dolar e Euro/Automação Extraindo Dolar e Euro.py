import tkinter as tk
from tkinter import ttk
import random
import time

def pesquisarItem():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

    # Configurações do Chrome
    opcoes = Options()
    opcoes.add_argument("--disable-blink-features=AutomationControlled")
    opcoes.add_argument("--headless=new")  # Oculta o navegador
    opcoes.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
    opcoes.add_experimental_option('useAutomationExtension', False)

    servico = Service(ChromeDriverManager().install())
    meuNavegador = webdriver.Chrome(service=servico, options=opcoes)

    try:
        meuNavegador.get("https://www.google.com.br/")
        time.sleep(random.uniform(2, 3)) #random.uniform - faz com que gere um tempo de espera aleatório para evitar o ReCAPTCHA do Chrome

        campoPesquisa = meuNavegador.find_element(By.NAME, "q")
        campoPesquisa.click()
        time.sleep(random.uniform(1, 2))

        textoPesquisa = moedaSelecionada.get() + " hoje"

        for letra in textoPesquisa:
            campoPesquisa.send_keys(letra)
            time.sleep(random.uniform(0.1, 0.25))

        campoPesquisa.send_keys(Keys.RETURN)
        time.sleep(random.uniform(3, 5))

        # Tenta pegar cotação
        try:
            valorDolarPeloGoogle = meuNavegador.find_element(By.XPATH, '//*[@data-exchange-rate]').get_attribute("data-exchange-rate")
        except:
            valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

        valorMoeda.config(text=str(moedaSelecionada.get()) + ": " + str(valorDolarPeloGoogle))

    except Exception as erro:
        valorMoeda.config(text="Erro ao buscar valor")
        print("Erro:", erro)

    finally:
        time.sleep(1)
        meuNavegador.quit()

# GUI com Tkinter
janela = tk.Tk()
janela.title("Cotação de Moedas")

tk.Label(janela, text="Moeda: ", font="Arial 20").grid(row=0, column=0)

moedaSelecionada = ttk.Combobox(janela, font="Arial 20")
moedaSelecionada["values"] = (
    "Dólar", "Euro", "Peso Argentino", "Libra Esterlina", "Iene Japonês",
    "Franco Suíço", "Dólar Canadense", "Dólar Australiano", "Yuan Chinês", "Bitcoin"
)
moedaSelecionada.grid(row=0, column=1)
moedaSelecionada.current(0)

botaoPesquisar = tk.Button(text="Pesquisar", font="Arial 20", command=pesquisarItem)
botaoPesquisar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

valorMoeda = tk.Label(janela, text="Valor: 0", font="Arial 20")
valorMoeda.grid(row=2, column=0, columnspan=2, sticky="W")

janela.mainloop()
