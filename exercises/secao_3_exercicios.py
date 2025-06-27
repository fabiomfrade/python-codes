"""
Exercícios da Seção 3 do curso de Python da Geek University
"""

# Exercício 1: Faça um programa que leia um número inteiro e imprima-o

numero = int(input("Insira um número: "))
print(numero)
print(type(numero))

# Exercício 2: Faça um programa que peça para o usuário digitar 3 valores inteiros e imprima a soma deles

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
soma = numero1 + numero2 + numero3
print(soma)
# Outra forma de print
print(numero1 + numero2 + numero3)

# Melhor forma de fazer o proposto:
contador = 0
numero = 0
while contador < 3:
    tmp = int(input("Digite um número inteiro: "))
    numero += tmp
    contador +=1

print(numero)

# Exercício 3: Faça um programa que recebe 3 valores e apresente a soma dos quadrados dos valores lidos

quadrado1 = int(input("Digite o primeiro número inteiro: "))
quadrado2 = int(input("Digite o segundo número inteiro: "))
quadrado3 = int(input("Digite o terceiro número inteiro: "))

print(f"A soma dos quadrados do que digitou é: ",quadrado1**2 + quadrado2**2 + quadrado3**2)