"""
1. Encontre o menor valor em uma lista
Escreva uma função que receba uma lista de números e retorne o menor valor.
"""


def receberLista():
    lista = []
    while True:
        try:
            numero = int(input("Digite o número que deseja adicionar a lista. "))
            lista.append(numero)
        except ValueError:
            print("Digite um número valido. ")
            continue

        adicionarMais = input("Deseja adicionar mais um número? (s/n) ").strip().lower()

        if adicionarMais == "n":
            print(lista)
            break

    return lista


def MenorNumero(lista):
    """
    Retorna o menor numero de uma lista
    """
    menorNum = min(lista)

    return menorNum


lista = receberLista()

if lista:
    menorNum = MenorNumero(lista)
    print(menorNum)
