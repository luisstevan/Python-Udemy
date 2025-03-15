#1) Faca um programa que mostre qual o maior dos dois numeros
N1= int(input("primeiro número: "))
N2= int(input("segundo número: "))
if N1 > N2:
    print(f"{N1} é maior que {N2}")
else: 
    print(f"{N2} é maior que {N1}")

#2) Faca um programa que mostre a raiz quadrada de um numero positivo
# e se for egativo mostre a mensagem "numero invalido"

Numero = int(input("Escolha um numero pra ter a raiz quadrada: "))

if Numero >= 0:
    raiz = Numero ** 0.5
    print(f"a raiz quadrada de {Numero} é {raiz:.2f}")
else:
	print("numero invalido")
       

#3) Faca um programa que mostre se um numer o é par ou impar
Numero = int(input("Escolha um numero pra ver se é par ou impar: "))

if Numero % 2 == 0:
    print("o numero é par")
else:
	print("numero é impar")
