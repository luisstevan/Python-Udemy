#1) ler 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos
valores = []
for i in range(6):
    valores.append(input(f"digite o {i+1}º valor: "))
print(valores)

#2) possua uma lista A que armazena 6 numeros.
#a)atribua valores da lista: 1,0,5,-2,-5,7
lista = []
lista.extend([1,0,5,-2,-5,7])
print (lista)
#b)soma dos valores na lista
soma = lista[0] + lista[1] + lista[5]
print(soma)
#c) modifique o valor do 5 elemento da lista
lista[5] = 100
print (lista)
#d) imprima todos os elementos da lista
for i in lista:
    print(i)
    

#3)faca um programa que leia 10 valores inteiros e armazene em uma lista e veja quantos pares ele possui

valores = []
for i in range(10):
    valores.append(int(input(f"digite o {i+1}º valor: ")))
print(valores)
pares = 0
for i in valores:
    if i % 2 == 0:
        pares = pares + 1
print(f"Quantidade de pares: {pares}")

