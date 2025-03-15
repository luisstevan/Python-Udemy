#1) Ler um numero e imprimir
n = 10
print(n)

#2) Ler 3 numeros e imprimir a soma
n1 = int(input(f"Digite o primeiro numero: "))
n2 = int(input(f"Digite o segundo numero: "))   
n3 = int(input(f"Digite o terceiro numero: "))    

soma = n1 + n2 + n3
print(f"a soma dos tres numeros é: {soma}")

#3) Ler 3 numeros e imprimir a soma dos quadrados
q1 = 5
q2 = 4
q3 = 8

soma_quadrados= q1**2+q2**2+q3**2
print(f"a soma dos quadrados é: {soma_quadrados}")

#4) Faca um programa que mostre qual o maior dos dois numeros
N1= input("primeiro número: ")
N2= input("segundo número: ")
if N1 > N2:
    print(f"{N1} é maior")
else: 
    print (f"{N2} é maior")

#5) Faca um programa que mostre a raiz quadrada de um numero positivo
# e se for egativo mostre a mensagem "numero invalido"

Numero = int(input("Escolha um numero pra ter a raiz quadrada: "))

if Numero >= 0:
    raiz = Numero ** 0.5
    print(f"a raiz quadrada de {Numero} é {raiz:.2f}")
else:
	print("numero invalido")
       

#6) Faca um programa que mostre se um numer o é par ou impar
Numero = int(input("Escolha um numero pra ver se é par ou impar: "))

if Numero % 2 == 0:
    print("o numero é par")
else:
	print(f"{Numero} é impar")

