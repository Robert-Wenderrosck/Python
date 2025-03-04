import supermercado as sp

sp.SupermercadoDoPovo()

print(sp.produtos["Macarrão"])

#-----------------------------------------------

from supermercado import produtos

print(produtos["Feijão"])
print("\n")

#Imprimindo o nome de todos os produtos
for item in produtos:
    print(item)

#Imprimindo o preço de todos os produtos
for i in produtos:
    print(produtos[i])

print("\n")

#Imprimindo o produto e o preço dos produtos
for prod, prec in produtos.items():
    print(prod, "-", prec)

print("\n")
#--------------------------------------------

from supermercado import departamento

for produto, preco in departamento.items(): #.items é o comando para pegar apenas os itens
    print(produto) #Imprime a categoria
    for produto, preco in preco.items():
        print("Produto:", produto, "R$", preco)


