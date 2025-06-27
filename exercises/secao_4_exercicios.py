"""
Exercícios da Seção 4 do curso de Python da Geek University
"""

# 1 - Faça um programa que receba 2 números inteiros e mostre qual deles é o maior

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 > numero2:
    print(f"O maior número é o {numero1}")
elif numero1 == numero2:  # Incluindo uma condicional para caso os valores sejam iguais
    print(f"Os números são iguais")
else:
    print(f"O maior número é o {numero2}")


# 2 - Faça um programa que leia um número inteiro fornecido pelo usuário; Se este número for positivo, calcule a raiz
# quadrada do número e apresente-a; Se o número for negativo, mostre uma mensagem dizendo que o número é inválido

valor = int(input("Digite um número: "))

if valor <= 0:
    print(f"Número inválido")
else:
    print(f"A raiz quadrada de {valor} é {valor**0.5:.2f}")  # Fazendo formatação para exibir no máximo duas casas
    # decimais

# 3 - Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar

valor = int(input("Digite um número e te direi se par ou ímpar: "))

if valor % 2 == 0:
    print(f'O número {valor} é par')
else:
    print(f'O número {valor} é ímpar')