#mais comum de se usar diconarios é para armazenar informações de um mesmo objeto
paises = {"br": "Brasil", "eua" : "Estados Unidos", "par" :"Paraguai", "ru" :"Russia"}
print(paises) #chave:valor
print(type(paises))

#menos comum de se usar dicionarios é para armazenar informações de objetos diferentes
paises = dict(br="Brasil", eua="Estados Unidos", par="Paraguai", ru="Russia")
print(paises)
print(type(paises))  
          

# Acessando elementos pela chave forma 1
print(paises["br"])
print(paises["eua"])

# Acessando elementos pela via get forma 2 = recomendada

print(paises.get("br"))
print(paises.get("eua"))    

pais = paises.get("ru")
if pais:
    print(f"Encontrei o pais {pais}")
else:
    print("Não encontrei o pais")

#ou

pais = paises.get("ru", "Não encontrado")
print(f"Encontrei o pais {pais}")



# Verificando se a chave está no dicionario
print("br" in paises)#true
print("ru" in paises) #true
print("Brasil" in paises) #false

if "ru" in paises:
    russian = paises["ru"] #russian recebe o valor da chave "ru" = Russia
print(russian)

localidades = {
    (35.6895, 39.6917): "Escritorio em Tokyo",
    (40.7128, 74.0060): "Escritorio em New York",
    (37.7749, 122.4194): "Escritorio em San Francisco"
}
print(localidades)
print(type(localidades))    
 
 #forma 1 adicionando elementos em um dicionario
lucro = {"jan": 10000, "fev": 12000, "mar": 5000}
print(lucro)
print(type(lucro))

receita = {"jan": 20}
print(receita)

#forma 2 de adicionar elementos em um dicionario
novo_dado = {"fev": 15000}
lucro.update(novo_dado)
print(lucro)


#forma 1 de remover elementos de um dicionario
ret = lucro.pop("mar")
print(ret) #retorna o valor da chave removida = 5000
print(lucro)

#forma 2 de remover elementos de um dicionario
del lucro["fev"]
print(lucro)
# nesse caso não é possivel retornar o valor da chave removida


#carrinho de compras usando lista
carrinho = []   
produto1 = {"whey", 1, 100.00}
produto2 = {"albumina", 1, 50.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#carrinho de compras usando tuplas
produto1 = ("whey", 1, 100.00)  
produto2 = ("albumina", 1, 50.00)   
carrinho = (produto1, produto2)
print(carrinho)

#carinho de compras usando dicionarios
carrinho = []
produto1 = {"nome": "whey", "quantidade": 1, "preco": 100.00}
produto2 = {"nome": "albumina", "quantidade": 1, "preco": 50.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#metodos de dicionarios
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
#limpar o dicionario
d.clear()
print(d)

#copiando um dicionario para outro
novo = d.copy() #deep copy, se fizermos alterações em um dicionario não afeta o outro
print(novo)
print(d)

#shallow copy, se fizermos alterações em um dicionario afeta o outro
novo = d
print(novo)
print(d)
novo["d"] = 4
print(novo)
print(d)

#forma não usual de criação de dicionarios
outro = {}.fromkeys("a", "b") #chave:valor 
print(outro)
print(type(outro))

#o valor "desconhecido" será atribuido a todas as chaves
usuario = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")
print(usuario)
print(type(usuario))

veja = {}.fromkeys("teste","valor") #itera sobre "teste" e torna cada letra uma chave (.fromkeys faz isso)
print(veja)


receita = {"jan": 10000, "fev": 12000, "mar": 5000}
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

print(receita.values()) #retorna os valores do dicionario

for valores in receita.values(): #mesma coisa que 
    print(valores)

for chave, valores in receita.items():
    print(chave, valores)

print(receita.items())
print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))
