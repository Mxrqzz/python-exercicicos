"""
8. Ordene uma lista em ordem crescente
Escreva uma função que receba uma lista de números 
e retorne a lista ordenada em ordem crescente 
(sem usar métodos embutidos como .sort() ou sorted()).
"""


def receberLista():
    """
    Recebe numeros informados pelo usuario e adicionar na lista
    """
    numeros = []
    while True:
        try:
            numero = float(input("Digite o número que deseja adicionar na lista: "))
            if numero:
                numeros.append(numero)
        except ValueError:
            print("Digite um número válido.")
            continue

        parar = input("Deseja adicionar mais um número? (s/n) ").strip().lower()
        if parar == "n":
            print(numeros)
            break

    return numeros


def ordenarLista(lista):
    """
    Recebe uma lista e ordena ela em ordem crescente
    """
    totalNum = len(lista)
    for num in range(totalNum):
        # Percorre a lista até o penultimo num não ordenado
        for indice in range(0, totalNum - num - 1):
            if lista[indice] > lista[indice + 1]:
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
    return lista


listaNumeros = receberLista()

listaOrdenada = ordenarLista(listaNumeros)


print(listaOrdenada)