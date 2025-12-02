# 1-Calcular Média de Valores em uma Lista
# valores = [10,5,9,10]
# def media(valores: list) -> float:
#     media = sum(valores) / len(valores)
#     return media
# print(media(valores))

# 2-Filtrar Dados Acima de um Limite
# dados = [3,9,7,10,15,60,3,1]
# def filtro(valores: list) -> list:
#     acima_limite = [x for x in valores if x >= 10]
#     return acima_limite
# print(filtro(dados))

# 3-Contar Valores Únicos em uma Lista
# valores = [10,10,15,20,30,65,65,65,5]
# def count_value(valores: list) -> int:
#     unicos = set(valores)
#     return len(unicos)
# print(count_value(valores))

# 4-Converter Celsius para Fahrenheit em uma Lista
# cel = 10
# def conversao(celsius: float) -> float:
#     conver = (celsius * 1.8) + 32
#     return conver
# print(conversao(cel))

# 5-Calcular Desvio Padrão de uma Lista
# import statistics
# dados = [10,15,30,60]
# def calcular_desvio(dados: list) -> float:
#     desvio = statistics.stdev(dados)
#     return desvio
# print(calcular_desvio(dados))

# 6-Encontrar Valores Ausentes em uma Sequência
# lista = [1,3,9]

# def ausentes(valores: list) -> list:
#     completos = set(range(min(valores), max(valores) + 1 ))
#     return list(completos - set(valores))
# print(ausentes(lista))

# Desafio: Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, 
# processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.

# import csv

# def leitura(arquivo: str) -> list:
#     lista = []
#     with open(arquivo, mode='r', encoding='utf-8') as vendas:
#         csv_reader = csv.DictReader(vendas)
#         for linha in csv_reader:
#             lista.append(linha)
#     return lista

# def calculo(dados: list):
#     vendas = {}
#     for dado in dados:
#         categoria = dado.get('Categoria')
#         valor = float(dado.get('Venda'))
#         quantidade = float(dado.get('Quantidade'))
#         total = valor * quantidade

#         if categoria in vendas:
#             vendas[categoria] += total
#         else:
#             vendas[categoria] = total

#     return vendas

# dados = leitura('vendas.csv')
# print(calculo(dados))