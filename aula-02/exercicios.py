# ### Exercícios

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input('num1'))
# num2 = int(input('num2'))
# resultado = num1 + num2
# print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# resultado = num1 % num2
# print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# resultado = num1 * num2
# print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input('num1: '))
# num2 = int(input('num2: '))
# resultado = num1 // num2
# print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num = int(input('informe o numero: '))
# print(f'O quadrado do numero informado é: {num ** 2}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input('num1: '))
# num2 = float(input('num2: '))
# print(f'A soma é: {num1 + num2}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input('num1: '))
# num2 = float(input('num2: '))
# print(f'A media dos numeros é: {(num1 + num2) / 2}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input('informe a base: '))
# potencia = float(input('informe a potencia: '))
# print(f'A potencia de {base} é: {base ** potencia}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input('informe a temperatura em celsius: '))
# convertido = (celsius * 1.8) + 32
# print(convertido)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# raio = float(input('informe o raio: '))
# area = math.pi * (raio ** 2)
# print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input('informe a string')
# print(palavra.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input('informe o nome completo : ')
# print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input('informe uma frase: ')
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input('digite uma data no formato: "dd/mm/aaaa"')
# data_formatada = data.split('/')
# print(f'dia: {data_formatada[0]}')
# print(f'mes: {data_formatada[1]}')
# print(f'ano: {data_formatada[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# palavra1 = input('informe o primeiro nome: ')
# palavra2 = input('informe o segundo nome: ')
# print(palavra1 + palavra2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = True
# valor2 = False
# print(valor1 and valor2)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1 = True
# valor2 = False
# print(valor1 or valor2)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valor1 = True
# valor2 = False
# print(not valor1)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = False
# valor2 = False
# print(valor1 == valor2)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = True
# valor2 = True
# print(valor1 != valor2)