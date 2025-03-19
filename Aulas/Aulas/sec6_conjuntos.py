#conjuntos são chamados de sets
#conjuntos nao aceitam repeticão
#conjuntos nao aceitam indexação
#conjuntos nao possuem valores ordenados

#Diferenças entre conjuntos e mapas (Dicionarios)

#conjuntos nao aceitam repeticão
#   -um dicionario tem chave e valor
#   -um conjunto tem apenas valor

#forma 1
s = set({1, 2, 3, 4, 5 , 5, 6})
print(s)
print(type(s))

#forma 2 mais comum
s = {1, 2, 3, 4, 5, 5, 6}
print(s)
print(type(s))  


if 3 in s:
    print('Tem o 3')
else:
   print('Nao tem o 3')

lista = [99, 45, 12, 99, 45, 12, 99, 45, 12]
print(lista)

tupla = (99, 45, 12, 99, 45, 12, 99, 45, 12)
print(tupla)

dicionario = {}.fromkeys(lista, "dict")
print(dicionario)

conjunto = {99, 45, 12, 99, 45, 12, 99, 45, 12}
print(conjunto) 

s = {1,"b", True,34.33}
print(s)
print(type(s))

for valor in s:
    print(valor)

#usos interessantes com sets
#imagine que fizemos um cadastro de clientes
#iformam a cidade que o cliente mora
#nós adcionamos cada cidade em uma lista, ja que podemos adcionar e ter repeticao

cidades =  {"Belo Horizonte" , "Sao Paulo", "Salvador", "Rio de Janeiro", "Rio de Janeiro"}
print(cidades)
print(len(cidades))

#adicionando elementos em um conjunto
cidades.add("Curitiba")
cidades.add("Curitiba") #ignorado, pois nao aceita repeticão
print(cidades)
print(len(cidades))

# forma 1 removendo elementos em um conjunto
cidades.remove("Salvador") #nao retorna salvador depois de removido
print(cidades)
print(len(cidades)) 

# forma 2 removendo elementos em um conjunto
cidades.discard("Rio de Janeiro") #retorna o valor removido
print(cidades)
print(len(cidades))

#copiando um conjunto para outro deep copy
novo = cidades.copy() 
novo.add("Rio de Janeiro")
print(novo)
print(cidades)

#copiando um conjunto para outro shallow copy
novo = cidades
novo.add("Rio de Janeiro")
print(novo)
print(cidades)

#removendo todos os elementos de um conjunto
cidades.clear()
print(cidades)

#conjuntos de alunos de python e java
estudantes_python = {"maria", "joao", "pedro", "marcos"}
estudantes_java = {"luis", "maria", "joao", "ana"}

#froma 1 uniao de conjuntos 
uniao = estudantes_python.union(estudantes_java) # junta os dois conjuntos
print(uniao)

#forma 2 uniao de conjuntos 
uniao = estudantes_python | estudantes_java # junta os dois conjuntos
print(uniao)

# interseccao de conjuntos, quem está em ambos os cursos
ambos = estudantes_python.intersection(estudantes_java) # retorna os elementos que estao nos dois conjuntos
print(ambos)

#gerar um conjunto de estudantes que só fazem python e só java
python_solo = estudantes_python.difference(estudantes_java)
print(python_solo)

java_solo = estudantes_java.difference(estudantes_python)
print(java_solo)

 
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))
