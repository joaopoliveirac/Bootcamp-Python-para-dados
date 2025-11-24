# 1- Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# lista = [1 + i for i in range(0,10)]
# for numero in lista:
#     print(numero ** 2)

# 2- Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove('C++')
# print(linguagens)

# 3- Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# from collections import namedtuple
# Livro = namedtuple('Livro', ['id', 'autor', 'ano'])
# livros = {'O conto das fadas': Livro(1,'joao pedro', 2025)}
# print(livros['O conto das fadas'].autor)

# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
#resoulcao com biblioteca
# from collections import Counter
# texto = 'eu sou o joao pedro oliveira carvalho lalalalala '
# frequencia = Counter(texto)
# print(frequencia)

#resolucao sem biblio
# texto = 'eu sou o joao pedro oliveira carvalho lalalalala '
# dados = {}
# for caracter in texto:
#     if caracter in dados:
#         dados[caracter] += 1
#     else:
#         dados[caracter] = 1
# print(dados)

# 5- Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# itens = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = 0

# for iten in itens:
#     if iten in precos:
#         total += precos[iten]
# print(total)

# 6- Eliminação de Duplicatas. Dada uma lista de emails, remover todos os duplicados.
# emails = ['joaopo@gmail.com', 'joaopo2@gmail.com', 'joao@hotmail.com', 'teste@gmail.com', 'teste@gmail.com', 'teste@hotmail.com']
# email = list(dict.fromkeys(emails))
# print(email)

# 7- Filtragem de Dados. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [10, 20, 30, 15, 13, 12, 18, 23, 29, 29]
# maiores = [idade for idade in idades if idade >= 18]
# print(maiores)

# 8- Ordenação Personalizada. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [{'nome': 'joao pedro'}, {'nome': 'yan'}, {'nome': 'pedro lucas'}]
# pessoas_ordenadas = sorted(pessoas, key= lambda x: x['nome'])
# print(pessoas_ordenadas)

# 9- Agregação de Dados. Dado um conjunto de números, calcular a média.
# import statistics
# numeros = [5,10,16,10,23]
# print(statistics.mean(numeros))

# 10- Divisão de Dados em Grupos. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# numeros = [2,3,7,9,10,15,20,35]
# impares = [numero for numero in numeros if (numero % 2 != 0)]
# pares = [numero for numero in numeros if (numero % 2 == 0)]
# print(f'pares: {pares}')
# print(f'impares: {impares}')

# 11- Atualização de Dados. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [{'nome': 'livro', 'preco': 20.79}, {'nome': 'notebook', 'preco' : 39.90}]
# for produto in produtos:
#     if produto['nome'] == 'livro':
#         produto['preco'] = 199

# print(produtos)

# 12- Fusão de Dicionários. Dados dois dicionários, fundi-los em um único dicionário.
# dicio1 = {'nome': 'joao pedro', 'idade': 16}
# dicio2 = {'nome': 'luiz', 'idade': 28}
# dicio3 = dicio1 | dicio2
# print(dicio3)

# 13- Filtragem de Dados em Dicionário. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# produtos = [{'produto': 'arroz', 'quantidade' : 0}, {'produto': 'arroz branco', 'quantidade' : 89}, {'produto': 'arroz vermelho', 'quantidade' : 0}]
# filtrados = [produto['produto'] for produto in produtos if produto['quantidade'] > 0]
# print(filtrados)

# 14- Extração de Chaves e Valores. Dado um dicionário, criar listas separadas para suas chaves e valores.
# produtos = {'produto': 'livro', 'quantidade': 50, 'teste': 78}
# listas = [[chave, valor] for chave, valor in produtos.items()]
# print(listas)

# 15- Contagem de Frequência de Itens. Dada uma string, contar a frequência de cada caractere usando um dicionário.
# from collections import Counter
# frase = 'eu sou o joao, joao é muito legal, legal e legal e joao, sou sou.'
# frase = frase.lower()
# for ch in '.,!:':
#     frase = frase.replace(ch, '')
# frase = frase.split()
# print(Counter(frase))

# 16- Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# def somar(lista: list):
#     soma = sum(lista)
#     return soma
# teste = somar([10,20,30,50])
# print(teste)


# 17- Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# def par_ou_impar(numero: int) -> bool:
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
# print(par_ou_impar(3))

# 18- Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def receba(texto: str):
    return texto[::-1]

print(receba('joao'))

# 19- Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20- Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas