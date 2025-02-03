"""
Crie uma função que conte quantas palavras existem em uma frase.
Exemplo:
Entrada: "Aprender Python é divertido"
Saída: 4
"""


def contarPalavras(string):
    palavras = string.split()
    return len(palavras)


frase = (
    input("Digite uma frase para poder contar o número de palavras nessa frase. ")
    .strip()
    .upper()
)

resultado = contarPalavras(frase)
print(f"A frase {frase} contém {resultado} palavras.")
