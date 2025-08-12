import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np

perguntas_treino = ["Qual é o seu nome?", "Como você está?", "O que você faz?", "Você gosta de programar?"]
respostas_treino = ["Meu nome é Celso.", "Estou funcionando bem, obrigado!", "Eu respondo a perguntas.", "Sim, eu adoro programar!"]

vectorizer = TfidfVectorizer() #Inicializa o transformador TF-IDF
modelo = make_pipeline(vectorizer, MultinomialNB()) #Cria um pipeline que primeiro aplica o transformador TF-IDF e, em seguida, aplica o classificador Naive Bayes
modelo.fit(perguntas_treino, np.arange(len(respostas_treino))) #Treina o modelo usando as perguntas como entrada e os índices das respostas como saída (np.arange(len(respostas_treino)) cria um array de índices [0, 1, 2, ...]

def responder_pergunta():
    pergunta = entrada_pergunta.get()

    if pergunta:
        idx = modelo.predict([pergunta])[0]
        prob = np.max(modelo.predict_proba([pergunta]))

        if prob > 0.3:
            lbl_resposta['text'] = f"Resposta: {respostas_treino[idx]}"

        else:
            lbl_resposta['text'] = "Resposta não encontrada."



janela = tk.Tk()
janela.geometry("600x300")
janela.title("Sistema de Resposta Automática")

lbl_instrucao = tk.Label(janela, text="Faça uma pergunta:", font=("Arial", 16))
lbl_instrucao.pack(pady=10)

entrada_pergunta = tk.Entry(janela, width=50, font=("Arial", 16))
entrada_pergunta.pack(pady=5)

btn_responder = tk.Button(janela, text="Responder", command=responder_pergunta, font=("Arial", 16))
btn_responder.pack(pady=10)

lbl_resposta = tk.Label(janela, text="", font=("Arial", 16))
lbl_resposta.pack(pady=10)


janela.mainloop()

