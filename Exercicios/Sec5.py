#1)programa que mostra os 5 primeiros multiplos de 3

for i in range(1,6):
    multiplo_3= i*3
    print(f"O {i}º multiplo de 3 é {multiplo_3}")

#2)use o comando while para fazer uma contagem regressiva de 10 a 0
n = 10
while n >= 0:
    print(n)
    n = n - 1
   # if n == 0

#3)faca um programa que declare um inteiro inicia com 0 incremnta de 1000 em 1000 e imprima seu valor ate 100000
for i in range(0,100001,1000):
    print(i)
    
print("fim")

n = 10 
while n > 0:
    print(n)
    n = n - 1
    if n == 0:
        print("fim")
        break

f = (int(input("Digite um numero: ")))


for i in range(0,100000,1000 + f):
    print(i)