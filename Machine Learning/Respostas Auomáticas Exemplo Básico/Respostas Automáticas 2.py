import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import os
from Levenshtein import distance as levenshtein_distance
import numpy as np

def carregar_dados():
    perguntas = []
    respostas = []

    caminho_arquivo = 'perguntas.txt'

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as f:

            for linha in f:
                try:
                    pergunta, resposta = linha.strip().split('|')

                    perguntas.append(pergunta)
                    respostas.append(resposta)

                except ValueError:
                    print(f"Erro ao processar a linha: {linha.strip()}")



    return perguntas, respostas

perguntas_treino, respostas_treino = carregar_dados()
vocabulario = set(" ".join(perguntas_treino).split())

if perguntas_treino and respostas_treino:
    vectorizer = TfidfVectorizer()
    modelo = make_pipeline(vectorizer, MultinomialNB())
    modelo.fit(perguntas_treino, np.arange(len(respostas_treino)))

def corrigir_texto(texto, vocabulario):
    palavras_corrigidas = []

    for palavra in texto.split():
        min_dist = float("inf")
        palavra_correta = palavra

        for vocab in vocabulario:
            dist = levenshtein_distance(palavra, vocab)

            if dist < min_dist:
                min_dist = dist
                palavra_correta = vocab

        palavras_corrigidas.append(palavra_correta)
    return " ".join(palavras_corrigidas)


def responder_pergunta():
    if not perguntas_treino or not respostas_treino:
        caixa_resposta.delete(1.0, tk.END)
        caixa_resposta.insert(tk.END, "O conjunto de treinamento está vazio")

    pergunta = entrada_pergunta.get()
    pergunta_corrigida = corrigir_texto(pergunta, vocabulario)

    print(pergunta_corrigida)

    if pergunta_corrigida:
        idx = modelo.predict([pergunta_corrigida])[0]
        prob = np.max(modelo.predict_proba([pergunta_corrigida]))

        print(f"Probabilidade: {prob}")

        caixa_resposta.delete(1.0, tk.END)
        caixa_resposta.insert(tk.END, f"Resposta: {respostas_treino[idx]}")



janela = tk.Tk()
janela.geometry("700x350")
janela.title("Sistema de Resposta Automática")

lbl_instrucao = tk.Label(janela, text="Faça uma pergunta:", font=("Arial", 16))
lbl_instrucao.pack(pady=10)

entrada_pergunta = tk.Entry(janela, width=50, font=("Arial", 16))
entrada_pergunta.pack(pady=5)

btn_responder = tk.Button(janela, text="Responder", command=responder_pergunta, font=("Arial", 16))
btn_responder.pack(pady=10)

caixa_resposta = tk.Text(janela, wrap=tk.WORD, width=50, height=10, font=("Arial", 16))
caixa_resposta.pack(pady=10)




janela.mainloop()


