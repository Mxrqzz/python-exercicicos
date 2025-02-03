"""
Crie uma função que receba uma lista de números e retorne a soma de todos eles.
Exemplo:
Entrada: [1, 2, 3, 4]
Saída: 10
"""


def criarListaDeNumeros():
    """Função que pede ao usuario para informar os numeros que deseja adicionar a lista"""
    numeros = []
    while True:
        try:
            numero = int(input("Digite o número que deseja adicionar na lista: "))
            numeros.append(numero)
        except ValueError:
            print("Por Favor, insira um número válido,")
            continue
        novoNumero = input("Deseja adicionar um novo número? (S/N) ").strip().lower()
        if novoNumero == "n":
            break

    return numeros


def somarListaDeNumeros(lista):
    """Função que retorna o tamanho da lista e soma os numeros que fazem parte da lista"""
    tamanhoLista = len(lista)
    somaLista = sum(lista)
    return tamanhoLista, somaLista


lista = criarListaDeNumeros()
lenLista, totalLista = somarListaDeNumeros(lista)

if lista:
    print(f"A sua Lista possui {lenLista} numeros")
    print(f"Sendo eles: {lista}")
    print(f"A soma de todos os números é: {totalLista}")
else:
    print("Nenhum número foi adicionado à lista.")
