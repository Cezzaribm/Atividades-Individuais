from random import randint

# Questão 1

lista = []

qtd = int(input("Quantos números deseja digitar? (mínimo 4): "))

while qtd < 4:
    qtd = int(input("Digite uma quantidade maior ou igual a 4: "))

for i in range(qtd):
    lista.append(int(input("Digite um número: ")))

print("Lista original:", lista)
print("3 primeiros:", lista[:3])
print("2 últimos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Índices pares:", lista[::2])
print("Índices ímpares:", lista[1::2])


# Questão 2

urls = [
    "www.google.com",
    "www.gmail.com",
    "www.github.com",
    "www.reddit.com",
    "www.yahoo.com"
]

dominios = []

for url in urls:
    dominios.append(url[4:-4])

print("URLs:", urls)
print("Domínios:", dominios)


# Questão 3

lista = []

for i in range(10):
    lista.append(randint(-100, 100))

print("Lista ordenada:", sorted(lista))
print("Lista original:", lista)
print("Índice do maior:", lista.index(max(lista)))
print("Índice do menor:", lista.index(min(lista)))
print("Soma:", sum(lista))
print("Média:", sum(lista) / len(lista))


# Questão 4

lista1 = []
lista2 = []
lista3 = []

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))

print("Digite os elementos da lista 1:")
for i in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))

print("Digite os elementos da lista 2:")
for i in range(qtd2):
    lista2.append(int(input()))

menor = min(len(lista1), len(lista2))

for i in range(menor):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if len(lista1) > len(lista2):
    lista3.extend(lista1[menor:])
else:
    lista3.extend(lista2[menor:])

print("Lista intercalada:", lista3)


# Questão 5

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

interseccao = []

for num in lista1:
    if num in lista2 and num not in interseccao:
        interseccao.append(num)

interseccao.sort()

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)


# Questão 6

lista = []

for i in range(20):
    lista.append(randint(0, 100))

print("Lista original:")
print(lista)

tam = int(input("Digite o tamanho das sublistas: "))

sublistas = []

for i in range(0, len(lista), tam):
    sublistas.append(lista[i:i+tam])

print("Sublistas:")
print(sublistas)


# Questão 7

n = int(input("Digite n: "))

matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(i)
    matriz.append(linha)

print("Resultado:")

for linha in matriz:
    print(linha)
