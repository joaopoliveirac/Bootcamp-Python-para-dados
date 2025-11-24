import csv

caminho = 'vendas.csv'
dados = []

with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    
    for linha in leitor_csv:
        dados.append(linha)

print(dados)
