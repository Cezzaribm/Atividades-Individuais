# Questão 01
nome = str(input("Digite seu primeiro nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
print("Bem-Vindo(a),", nome, sobrenome + "!")

# Questão 02
frase = str(input("Digite a frase: "))
espaco = frase.count(" ")
print("Quantidade de espaços:", espaco)

# Questão 03
for i in range(1, len(nome) + 1):
    print(nome[:i])
# Questão 04
numero = input("Digite o número: " )
if len(numero) == 8:
    numero = "9" + numero
    print("Número completo: ", numero[:5] + "-" + numero[5:])
elif len(numero) == 9 and numero[0] == "9":
    print("Número completo: ", numero[:5] + "-" + numero[5:])
else:
    print("Número inválido!")

# Questão 05 

vogais = "aeiouAEIOU"
indices = []
total = 0

for i in range(len(frase)):
    if frase[i] in vogais:
        indices.append(str(i))
        total += 1

print("Índices das vogais:", ", ".join(indices))
print("Total:", total, "vogais")
