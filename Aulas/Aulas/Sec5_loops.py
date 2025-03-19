Nome = 'Luis Stevan'
lista = [1,2,3,4,5]
numeros = range(1,10)

print("letras do nome: ")
for letra in Nome:
    print(letra)

print("letras do nome sem pular linha: ")
for letra in Nome:
    print(letra, end="")

print("\n")

print("numeros da lista: ")
for numero in lista:
    print(numero)

print("numeros da range: ")
for numero in range(1,10):
        print(numero)

for indice, letra in enumerate(Nome):
    print(f"{indice}:{letra}")

for i in enumerate(Nome):
    print(i)    

qtd = int(input("quantas vezes o programa deve rodar?" ))
for i in range(1, qtd+1):
     print(f"imprimindo {i}")

qtd = int(input("quantas vezes o programa deve rodar?" ))  
soma = 0  
for i in range(1, qtd+1):
     num = int(input(f"digite o numero {i}/{qtd}: "))
     soma = soma + num
print(f"a soma de todos é {soma}")

for _ in range(3):
    for num in range(1,11):
        print('\U0001F60D' * num),


for num in range(1,11,2): #vai de 2 em 2, o 11 é descartado ***(1,11) = (1,11,(1 implicito))***
        print(num)

for num in range(10,0,-1): #vai de 10 a 1
        print(num)

lista = list(range(10))
print(lista[1])

lista = list(range(10))
print(lista[-2])#penultimo da lista

lista = list(range(10))
print(lista[-1])
#********************************************************************************************************************
#while

while num < 10:
    print(num)
    num = num + 1

#while reposta != 'sim':
    #reposta = input("ja acabou mano? ")
#********************************************************************************************************************
#break
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print("saiu do loop") 

while True:
    resposta = input("digite 'sair' para sair: ")
    if resposta == 'sair':
        break

