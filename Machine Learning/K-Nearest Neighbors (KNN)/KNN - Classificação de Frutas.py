from sklearn.neighbors import KNeighborsClassifier

#2 características: Peso em gramas e textura (0=lisa / 1=regular)
dados = [
        [145,0], #Maçã
        [150, 0],
        [155, 0],
        [160, 0],
        [165, 0],
        [170, 0],
        [175, 0],
        [180, 0],
        [185, 0],
        [190, 0],
        [195, 0],
        [200, 0],
        [205, 0],
        [210, 0],

        [145,1], #Laranja
        [150, 1],
        [155, 1],
        [160, 1],
        [165, 1],
        [170, 1],
        [175, 1],
        [180, 1],
        [185, 1],
        [190, 1],
        [195, 1],
        [200, 1],
        [205, 1],
        [210, 1]
]

rotulos = ["Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã", "Maçã",
           "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja", "Laranja"]

knn = KNeighborsClassifier(n_neighbors=3) #Criando uma instância do classificador KNN com 3 vizinhos (considera os 3 vizinhos mais próximos para fazer a classificação)
knn.fit(dados, rotulos) #Treinando o modelo KNN com os dados de frutas e seus respectivos rótulos

nova_fruta = [[162, 1]] #Define uma nova amostra para classificação, representando uma nova fruta (fruta com 162 gramas e textura irregular - 1)

classe_predita = knn.predict(nova_fruta) #Usando o modelo treinado para prever a classe da nova fruta
print(f"A nova fruta é classificada como: {classe_predita[0]}")

