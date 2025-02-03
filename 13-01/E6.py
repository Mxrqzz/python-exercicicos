'''
Escreva uma função que receba um número e retorne o seu fatorial.
Exemplo:
Entrada: 5
Saída: 120
'''

def fatorarNumero(numero):
    """retorna a Fatoração de um número"""
    for fator in range(1, numero):
        numero = numero * fator
    return numero

while True:
    try:
        num = int(input("Digite o número que deseja fazer a fatoração: "))
        if num:
            resultado = fatorarNumero(num)
            print(f"A fatoração de {num} é = {resultado}")

            repeat = input("Deseja fatorar outro número? (s/n)").strip().lower()
            if repeat == "n":
                print("Progama encerrado.")
                break

    except ValueError:
        print("Digite um número valido")
        continue
