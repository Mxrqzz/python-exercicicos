"""
5. Inverta os elementos de uma lista
Crie uma função que receba uma lista e retorne os elementos em ordem inversa.
"""


def criarListaDeCompras():
    """
    Cria uma lista de compra e que armazena os item que o usuario inserir
    """
    listaDeCompras = []
    while True:
        item = (
            input("Digite o nome do item do que deseja adicionar a lista de compras: ")
            .strip()
            .lower()
        )
        if item:
            listaDeCompras.append(item)

        parar = (
            input("Deseja adicionar mais um item a sua lista de compras? (s/n) ")
            .strip()
            .lower()
        )

        if parar == "n":
            print(listaDeCompras)
            break

    return listaDeCompras


def inverterOrdem(lista):
    novaLista = lista[::-1]
    print(novaLista)

    return novaLista


lista = criarListaDeCompras()

novaLista = inverterOrdem(lista)
