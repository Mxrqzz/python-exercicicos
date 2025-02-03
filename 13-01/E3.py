"""
Escreva um programa que, dado um número pelo usuário, imprima a tabuada dele de 1 a 10.
Exemplo:
Entrada: 5
Saída:
"""


def imprimirTabuada(numero):
    for tabuada in range(1, 11):
        print(f"{numero} x {tabuada} = {(numero*tabuada)}")


num = int(input("Digite o numero que deseja ver a tabuada: "))

imprimirTabuada(num)
