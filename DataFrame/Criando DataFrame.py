import pandas as opcoesPandas
import numpy as opcoesNumpy

#date_range = cria uma lista
#periods = quantos dias
#20221201 = ano/mês/dia
#freq = referência para o período que vai contar na lista
dataFrame_datas = opcoesPandas.date_range("20221201", periods=31, freq="D")
print(dataFrame_datas)

print("\n--------------DataFrame 12 meses com a freq Mês -----")
dataFrame_meses = opcoesPandas.date_range("20221231", periods=12, freq="ME")
print(dataFrame_meses)
print("\n")

#----------------------------------------

print("\n--------------DataFrame Números Aleatórios 5 linhas e 1 coluna --------\n")

numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5, 1))
print(numerosAleatorios)
print("\n")

print("\n--------------DataFrame Números Aleatórios 15 linhas e 10 colunas com números maiores que 0 --------\n")
numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15, 10)*100)
print(numerosAleatorios)
print("\n")


print("\n--------------DataFrame Números Aleatórios 15 linhas e 10 colunas com números maiores que 0 --------\n")
#columns = renomear os nomes das colunas
numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15, 10)*100, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(numerosAleatorios)
print("\n")

#Exibe o nome de todas as colunas
print(numerosAleatorios.columns)

#Criando DataFrame a partir de um dicionário
notasAlunos_dataFrame = opcoesPandas.DataFrame({
                                                "Nome": ["Ana", "Pedro", "João", "Marta", "Allan"],
                                                "Média": [9, 7, 10, 8, 9]
                                                })

print("\n------------------ DataFrame Dicionário Notas Alunos\n")
print(notasAlunos_dataFrame)
