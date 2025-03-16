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

