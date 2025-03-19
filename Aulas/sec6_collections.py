# Modulo collections - Counter ********************************
# Collections -> High Performance Container Datatypes

from collections import Counter

lista = [1,1,1,2,2,3,2,5,7,8,9,1,532,43]

#verificar quantas vezes um elemento aparece na lista chave/nº de ocorrencias
qnts = Counter(lista)
print(qnts)
print(type(qnts))

print(Counter('Geek University'))

texto = 'Em Python, um objeto não é iterável quando ele não implementa o método especial __iter__() ou __getitem__(). Isso significa que ele não pode ' \
'ser percorrido diretamente em um loop for ou usado com funções que exigem iteráveis, como list() ou tuple().'

palavras = texto.split()
qnts = Counter(palavras)
print(qnts)

print(qnts.most_common(3))


# Modulo collections - Default Dict ********************************

dicionario = {"curso": "Python"}
print(dicionario["curso"])
#print(dicionario["outro"]) (nao funciona)

from collections import defaultdict
dicionario = defaultdict(lambda: 0)#cria um dicionário que retorna um valor padrão (0) sempre que tentamos acessar uma chave inexistente.
dicionario["curso"] = "Java"
print(dicionario["curso"])
print(dicionario["outro"])
print(texto)

# Modulo collections - ordered Dict ********************************
#em um dicionario comum, as chaves nao sao ordenadas nao é garantido
dicionario = {"a": 1, "b": 2, "c": 3}
print(dicionario)

from collections import OrderedDict
dicionario = OrderedDict({"a": 1, "b": 2, "c": 3})
print(dicionario)


#diferencas entre dict e ordered dict
dict1 = {"a":1, "b":2, "c":3}
dict2 = {"b" :1, "a":2, "c":3}
print(dict1 == dict2) #True

odict = OrderedDict({"b":1, "a":2, "c":3})
print(dict1 == odict) #False



# Modulo collections - named tuples ********************************
from collections import namedtuple

Cachorro = namedtuple('Cachorro', ['idade', 'raca', 'nome'])
cachorro1 = Cachorro(idade=2, raca='Vira lata', nome='Vira-lata')


#forma 1 acessar elementos
print(cachorro1[0]) #idade
print(cachorro1[1]) #raca
print(cachorro1[2]) #nome

#forma 2 acessar elementos
print(cachorro1.idade) #idade
print(cachorro1.raca) #raca
print(cachorro1.nome) #nome

print(cachorro1.index('Vira-lata')) #indice
print(cachorro1.count('Vira-lata')) #quantas ocorrencias

# Modulo collections - Deque (lista de alta performance)********************************
from collections import deque
deq = deque("luis")
print(deq)
deq.append("y")
deq.appendleft("x")
print(deq)

print(deq.pop())
print(deq.popleft())
print(deq)

