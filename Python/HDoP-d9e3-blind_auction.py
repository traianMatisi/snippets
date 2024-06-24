# 100 days of python - day 9
# Author: Traian - 24-6-24

import os

compradores = {}

def main():
    while True:
        nome = input("Digite seu nome: ")
        lance = int(input("Digite seu lance: $"))
        compradores[nome] = lance
        while True:
            novo_lance = input("Há mais lances a serem realizados? [S/N] ").upper()
            if novo_lance == 'N' or novo_lance == 'S':
                break
        os.system('cls' if os.name == 'nt' else 'clear')
        if novo_lance == 'N':
            break
    maior_oferta = max(compradores.values())
    print(f"Maior oferta: {maior_oferta}")
    for k, v in compradores.keys(), compradores.values():
        if v == maior_oferta:
            print(f"Comprador: {k}")

main()
