"""
Intersecção entre duas listas
Crie uma função que receba duas listas e retorne uma nova lista contendo os elementos que aparecem em ambas.
"""

listaUm = ["maça", "uva", "banana", "pera", "acabaxi", "couve", "tomate"]

listaDois = ["ameixa", "uva", "maça", "figo", "kiwi", "maracuja", "tomate"]


def interseccaoDuasListas(lista1, lista2):
    """
    Recebe duas lista e cria uma nova lista apenas com os elementos que aparecem em ambas
    """
    ElementosEmComum = []

    for elemento in lista1:
        if elemento in lista2:
            ElementosEmComum.append(elemento)

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Elementos em comum em ambas as listas: {ElementosEmComum}")


interseccaoDuasListas(listaUm, listaDois)
