#Enquanto houver memória podemos adcionar elementos na lista em python, 
# o que não acontece em C,JAVA,etc
x = 2
lista1 = [1 , 99 , 4 , 27 , 15 , 3 , 42 , 33 , 56]
lista2 = ["L", "O", "G", "I", "C", "A"]
lista3 = []
lista4 = list(range(11))    #cria uma lista com 11 elementos
lista5 = list("LOGICA")

print(lista1)
print(lista2)           
print(lista3)
print(lista4)
print(lista5)

#imprime a classe do objeto
print(type(lista1))
print(type(lista2))  

if 18 in lista4:
    print("Encontrei o número 18")
else:
    print("Não encontrei o número 18")  


lista1.sort() #Ordena a lista
print(lista1)

if lista1.count(1):
    print(f"o numero 1 aparece {lista1.count(1)} vez na lista")
else: 
    print(f"o numero 1 aparece {lista1.count(1)} vezes na lista")

if lista5.count("A") == 1:
    print(f'a letra A aparece {lista5.count("A")} vez na lista')
else:
    print(f'a letra A aparece {lista5.count("A")} vezes na lista') 

lista1.append(42) #Adiciona o elemento 42 na lista
print(lista1) #só é possivel adicionar um elemento por vez

lista1.append([8,3,1]) #Adiciona a lista [8,3,1] como um elemento na lista
lista1.append(lista2) #Adiciona a lista2 como um elemento
print(lista1)

lista1.extend([123,44,67]) #Adiciona os elementos 123,44,67 na lista
print(lista1)

lista1.insert(2, "Novo valor") #Adiciona o elemento na posição 2
#mas não substitui o valor que estava na posição 2, ele vai para a posição 3
print(lista1)

lista1.reverse() #Inverte a lista
print(lista1)
print(lista1[::-1]) #Inverte a lista

print(len(lista1)) #Tamanho da lista 

lista1.pop() #Remove o último elemento da lista
print(lista1)

lista1.pop(2) #Remove o elemento da posição 2 
#os elementos que estavam a direita do elemento removido, vão para a esquerda
print(lista1)    

lista1.clear() #Limpa a lista
print(lista1)   

curso = "python c" 
curso = curso.split() #Transforma a string em uma lista
#sepada a string por espaço
print(curso)

curso2= "python,c,java,php"

curso2 = curso2.split(",") #Transforma a string em uma lista
print(curso2)   

lista6 = ['eu', 'amo', 'programar', 'em', 'python']
curso_string = " ".join(lista6) #Transforma a lista em uma string e separa por espaço
print(curso_string)       

curso4 = "c$java$php$python"
curso4 = curso4.split("$")   #Transforma a string em uma lista e separa por $
print(curso4)   

curso4 = "$".join(lista6) #Transforma a lista em uma string e separa por $
print(curso4)   

lista7 = [1,2.34,True,"teste",235235235, [1,2,3], "g"]
print(lista7)

for elemento in lista7:
    print(f"O elemento {elemento} da lsita vale {elemento}")


soma=0
for elemento in lista4:
    print(f"O elemento {elemento} da lista vale {elemento}")
    soma = soma + elemento
print(f"A soma dos elementos da lista é {soma}")    

print(lista4)

soma = ''
for elemento in lista2:
    print(f"O elemento {elemento} da lista vale {elemento}")
    soma = soma + elemento  #concatenação
print(f"A soma dos elementos da lista é {soma}")


#carrinho de compras que só pode ter 5 produtos 

carrinho = []
produto = ''    
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
    if len(carrinho)== 5 :
        print("Carrinho cheio")
        break
print(carrinho)
        

for produto in carrinho:
    print(produto)

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

print(cores[-1]) #último elemento
print(cores[-2]) #penúltimo elemento
print(cores[-3]) #antepenúltimo elemento
print(cores[-4]) #primeiro elemento
#imagina que a lista é um circulo

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

for indice, cor in enumerate(cores):
    print(indice, cor) 

numbers = [32,2,3,4,5]
print(numbers.index(32)) #retorna o indice do elemento 1

#print(numbers.index(32, 1)) #retorna o indice do elemento 1 a partir do indice 1
#print(numbers.index(32, 2)) #retorna o indice do elemento 1 a partir do indice 2
#print(numbers.index(32, 3)) #retorna o indice do elemento 1 a partir do indice 3
#print(numbers.index(32, 4)) #retorna o indice do elemento 1 a partir do indice 4
#print(numbers.index(4,2,4)) #retorna o indice do elemento 1 a partir do indice 2 até o 4   
 

lista = [1,2,3,4,5,6,7,8,9]
print(lista[1:4]) #vai do indice 1 até o 4
print(lista[1:7:2]) #vai do indice 1 até o 7 pulando de 2 em 2
print(lista[::2]) #vai do indice 0 até o final pulando de 2 em 2
print(lista[1::2]) #vai do indice 1 até o final pulando de 2 em 2
print(lista[1:7:2]) #vai do indice 1 até o 7 pulando de 1 em 1
print(lista[1:7:1]) #vai do indice 1 até o 7 pulando de 1 em 1
print(lista[:7]) #vai do indice 0 até o 7
print(lista[1:]) #vai do indice 1 até o final
print(lista[:]) #vai do indice 0 até o final
print(lista[::]) #vai do indice 0 até o final
print(lista[::-1]) #inverte a lista
print(lista[-1:-8:-1]) #inverte a lista

print(sum(lista)) #soma os elementos da lista
print(max(lista)) #retorna o maior elemento da lista    
print(min(lista)) #retorna o menor elemento da lista    

print(type(lista)) #retorna o tipo da lista
tupla = tuple(lista) #transforma a lista em uma tupla   
print(type(tupla)) #retorna o tipo da tupla


#deep copy
lista = [1,2,3]

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

#shallow copy
lista = [1,2,3]
nova = lista
print(nova)  