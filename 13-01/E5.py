"""
Crie uma função que verifica se uma palavra é um palíndromo (lida da mesma forma de trás para frente).
Exemplo:
Entrada: "arara"
Saída: True
"""


def verificarPalindromo(string):
    """Verifica se uma palavra ou frase é uma palíndromo."""
    stringLimpa = "".join(char for char in string if char.isalnum()).lower()
    stringInvertida = stringLimpa[::-1]

    return stringLimpa == stringInvertida


def receberEVerificarString():
    """Recebe entradas do usuario e verifica se são palíndromos."""
    while True:
        palavra = input(
            "\nDigite uma palavra ou frase para ver se ela é um palíndromo: "
        ).strip()
        if verificarPalindromo(palavra):
            print(f"A palavra/frase '{palavra}' é um palíndromo.")
        else:
            print(f"A palavra/frase '{palavra}' não é um palíndromo.")

        repeat = input("Deseja verificar outra palavra? (s/n)").strip().lower()
        if repeat == "n":
            print("Progama encerrado.")
            break


receberEVerificarString()
