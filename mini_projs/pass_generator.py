#!/usr/local/bin/python3

import secrets
import string

def cria_senha(tamanho):
    opcoes = string.digits + string.ascii_letters + string.punctuation
    senha = ''.join(secrets.choice(opcoes) for i in range(tamanho))
    return senha

def caracteres():
    while True:
        try:
            tamanho = int(input(f"Digite a quantidade de caracteres a senha deve ter: "))
            if tamanho <= 0:
                print("Você precisa digitar um número positivo")
                continue
            return tamanho
        except ValueError:
            print("Entrada não numérica detectada")

def main():
    while True:
        tamanho = caracteres()
        senha = cria_senha(tamanho)
        print(f"A senha gerada é {senha}\n")

        resp = input("Deseja criar outra? [s/n] ").strip().lower()
        if resp != 's':
            print("Até logo, volte quando quiser!")
            exit(0)

if __name__ == "__main__":
    main()