"""
Soma de números pares em uma lista
Escreva uma função que receba uma lista de números e retorne a soma de todos os números pares.
"""


def receberLista():
    """
    Recebe um número e adiciona o mesmo na lista de números, logo após pergunta se deseja adicionar mais um número

    """
    numeros = []

    while True:
        try:
            numero = int(input("Digite o número que deseja adicionar a lista: "))
            numeros.append(numero)
        except ValueError:
            print("Digite um número válido. ")
            continue

        parar = input("Deseja adicionar mais um número? (s/n)").strip().lower()

        if parar == "n":
            print(numeros)
            break

    return numeros


def somarNumerosPares(lista):
    """
    Recebe uma lista de número e soma apenas os números que forem pares
    """
    somaPares = sum(x for x in lista if x % 2 == 0)

    return somaPares


listaNumeros = receberLista()

somaPares = somarNumerosPares(listaNumeros)

print(somaPares)
