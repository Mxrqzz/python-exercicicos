"""
Crie uma função que receba uma lista de números e retorne o maior valor.
Exemplo:
Entrada: [5, 2, 9, 1]
Saída: 9
"""


def receberNumero():
    numeros = []

    while True:
        try:
            numero = int(input("Digite um número que deseja adicionar a lista. "))
            numeros.append(numero)
            print(numeros)
        except ValueError:
            print("Digite um número válido")
            continue

        adicionarOutroNumero = (
            input("Deseja adicionar outro número? (s/n)").strip().lower()
        )
        if adicionarOutroNumero == "n":
            print("Progama encerrado.")
            break

    return numeros


def pegarMaiorNumLista(lista):
    """
    Retorna o maior numero da lista
    """
    maiorNumero = max(lista)

    print(maiorNumero)


lista = receberNumero()

if lista:
    print(lista)
    pegarMaiorNumLista(lista)
else:
    print("A lista está vazia")
