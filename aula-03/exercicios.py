from datetime import time
# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = float(input('informe a quantidade'))
# preco = float(input('informe o preço'))
# if quantidade > 0 and preco > 0:
#     print('numeros validos!')
# else:
#     print('dados invalidos.')

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# temperatura = 60
# if temperatura >= 60:
#     print('temperatura alta')
# elif temperatura < 60 and temperatura > 20:
#     print('temperatura normal')
# else:
#     print('temperatura baixa!')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'].upper() == 'ERROR':
#     print(log['message'])
# else:
#     print('tudo certo.') 

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# idade: int = int(input('informe a idade'))
# email: str = str(input('informe o email'))

# if not (idade >= 18 and idade <= 65):
#     print('idade invalida.')
# if not ('@' in email):
#     print('email invalido')
# else:
#     print('Dados validos!')
    

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao: dict[str, int]  = {'valor': 9000, 'hora': 21}
# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 20:
#     print('TRANSACAO SUSPEITA!')
# else:
#     print('transacao normal, pode seguir.')

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# resolucao 1
# texto = 'eu sou um cara que estuda dados em python, eu gosto de estudar todos os dias. eu amo esse cara, python, cara, teste, teste, teste'
# texto = texto.lower()
# texto = texto.replace(',', '')
# texto = texto.split()
# quantidade = {}
# for palavra in texto:
#     if palavra in quantidade:
#         quantidade[palavra] += 1
#     else:
#         quantidade[palavra] = 1
# print(quantidade)

# resolucao 2, mais direta
# from collections import Counter
# texto = 'eu sou um cara que estuda dados em python, eu gosto de estudar todos os dias. eu amo esse cara, python, cara, teste, teste, teste'
# texto = texto.lower()
# for char in ",.!?;:":
#     texto.replace(char, '')
# quantidade = Counter(texto.split())
# print(quantidade)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# import numpy as np
# numeros = [10, 20, 30, 40]
# min_val = min(numeros)  # 10
# max_val = max(numeros)  # 40
# normalizados = [(x - min_val) / (max_val - min_val) for x in numeros]
# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "João", "idade": 25, "email": "joao@email.com"},
#     {"nome": "Maria", "idade": 30},  # faltando e-mail
#     {"nome": "Ana", "idade": 22, "email": "ana@email.com"},
#     {"nome": "Pedro"}]  # faltando idade e e-mail
# campos_obrigatorios = ['nome', 'idade', 'email']

# for usuario in usuarios:
#     faltando = [campo for campo in campos_obrigatorios if campo not in usuario]
#     if faltando:
#         texto = ", ".join(faltando)
#         print(f'O usuario {usuario['nome']} está com o campo {texto} incompleto.')

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# numeros = [10,20,15,19,30,45,60]
# pares = [num for num in numeros if (num % 2) == 0]
# print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"id": 1, "produto": "Camisa", "quantidade": 3, "preco": 79.90, "vendedor": "Ana", "cidade": "São Paulo", "categoria": "Vestuário"},
#     {"id": 2, "produto": "Tênis", "quantidade": 1, "preco": 299.90, "vendedor": "João", "cidade": "Rio de Janeiro", "categoria": "Calçados"},
#     {"id": 3, "produto": "Calça Jeans", "quantidade": 2, "preco": 149.90, "vendedor": "Ana", "cidade": "São Paulo", "categoria": "Vestuário"},
#     {"id": 4, "produto": "Boné", "quantidade": 5, "preco": 49.90, "vendedor": "Marcos", "cidade": "Belo Horizonte", "categoria": "Acessórios"},
#     {"id": 5, "produto": "Meias", "quantidade": 10, "preco": 9.90, "vendedor": "João", "cidade": "Curitiba", "categoria": "Vestuário"},
#     {"id": 6, "produto": "Camisa", "quantidade": 1, "preco": 79.90, "vendedor": "Ana", "cidade": "Rio de Janeiro", "categoria": "Vestuário"},
#     {"id": 7, "produto": "Tênis", "quantidade": 2, "preco": 299.90, "vendedor": "Marcos", "cidade": "São Paulo", "categoria": "Calçados"},
# ]

# categorias = {v["categoria"] for v in vendas}
# total = {categoria: sum(venda['quantidade'] * venda['preco'] for venda in vendas if venda['categoria'] == categoria)
#          for categoria in categorias}

# print(total)



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.