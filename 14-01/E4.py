"""
4. Conte quantas vezes um elemento aparece em uma lista
Crie uma função que receba uma lista e um elemento, e conte quantas vezes o elemento aparece na lista.
"""


def recebeListaElemento():
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
            elemento = int(
                input("Digite o número que deseja contar quantas vezes aparece")
            )
            break

    return lista, elemento


def contarElemento(lista, elemento):
    contador = 0
    for busca in lista:
        if busca == elemento:
            contador += 1
    print(contador)

    return contador


lista, elemento = recebeListaElemento()

contagem = contarElemento(lista, elemento)
