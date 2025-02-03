import math

"""
3. Verifique se um número é primo
Escreva uma função que receba um número inteiro e retorne True se for primo e False caso contrário.
"""


def VerificarNumPrimo(numero):
    """
    Realiza teste para verificar se um número é primo
    """

    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    limite = int(math.sqrt(numero)) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


while True:
    try:
        num = int(input("Digite o número que deseja verificar se é primo: "))
        if VerificarNumPrimo(num):
            print(f" O número {num} é um número primo.")
        else:
            print(f"O número {num} não é um número primo.")
    except ValueError:
        print("Digite um Número Valido.")
        continue

    parar = input("Deseja verificar outro número? (s/n) ").strip().lower()

    if parar == "n":
        print("Progama encerrado")
        break
