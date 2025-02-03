"""
Multiplicação dos elementos de uma lista
Crie uma função que receba uma lista de números e retorne o produto (multiplicação) de todos os elementos.
"""

numeros = []
while True:
    try:
        numero = int(input("Digite o número que deseja adicionar na lista: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    novoNumero = input("Deseja adicionar um novo número? (S/N) ").strip().lower()
    if novoNumero == "n":
        break


def multiplicar_elementos_lista(lista):
    """
    Recebe uma lista de números e retorna a multiplicação de todos eles.
    """
    if not lista:
        return None

    produto = 1
    for num in lista:
        produto *= num
    return produto


resultado = multiplicar_elementos_lista(numeros)
if resultado is not None:
    print(f"O produto dos elementos da lista {numeros} é: {resultado}")
else:
    print("A lista está vazia. Nenhum cálculo foi realizado.")
