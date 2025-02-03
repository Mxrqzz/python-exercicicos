"""
Verifique se duas listas são iguais
Escreva uma função que receba duas listas e verifique se elas são iguais (mesmos elementos, na mesma ordem).
"""

listaUm = [1, 2, 3, 4, 5]

listaDois = [1, 2, 32, 4, 5]

listaTres = [1, 2, 3, 4, 5]



def listasIguais(lista1, lista2):
    return lista1 == lista2


print(listasIguais(listaUm, listaDois))
print(listasIguais(listaUm, listaTres))