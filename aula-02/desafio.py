# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try:
    nome = str(input('digite seu nome: '))
    salario = float(input('informe seu salario: '))
    bonus = float(input('informe o bonus em %: '))
    valor_bonus = (bonus / 100) * salario
    print(f'{nome} tem {salario} de salario e recebeu {valor_bonus} de bonus.')
except Exception as e:
    print(e)