# Questão 1

def contagem_caracteres(texto):
    dicionario = {}

    for caractere in texto:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1

    return dicionario

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)

# Questão 2, não consegui baixar o filme ;-;

# Questão 3

def mesclar_dicionarios(dicionario1, dicionario2):
    resultado = dicionario1.copy()

    for chave in dicionario2:
        if chave in resultado:
            if dicionario2[chave] > resultado[chave]:
                resultado[chave] = dicionario2[chave]
        else:
            resultado[chave] = dicionario2[chave]

    return resultado

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}

resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

# Questão 4

def filtrar_dicionario(dados, chaves_filtradas):
    resultado = {}

    for chave in chaves_filtradas:
        if chave in dados:
            resultado[chave] = dados[chave]

    return resultado

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']

resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

# Questão 5

def resultado_votacao(votos):
    totais = {}
    total_geral = 0

    for sessao in votos:
        for candidato in sessao:
            if candidato in totais:
                totais[candidato] += sessao[candidato]
            else:
                totais[candidato] = sessao[candidato]

            total_geral += sessao[candidato]

    resultado = {}

    for candidato in totais:
        percentual = (totais[candidato] / total_geral) * 100
        resultado[candidato] = (totais[candidato], round(percentual, 2))

    return resultado

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105}
]

resultado = resultado_votacao(votos)
print(resultado)