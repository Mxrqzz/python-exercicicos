"""
Converta uma string para CamelCase
Crie uma função que converta uma string para o formato CamelCase.
Exemplo:
Entrada: "python é incrível"
Saída: "PythonÉIncrível"
"""

frase = input("Digite a frase que deseja converter para camelCase: ").strip().lower()


def converterParaCamelCase(frase):

    palavras = frase.split()  # Separa as palavras depois de cada espaço
    listaPalavras = []

    for palavra in palavras:
        palavraFormatada = (
            palavra.capitalize()
        )  # Altera a primeira letra de cada palavra para maiuscula
        listaPalavras.append(palavraFormatada)  # Adiciona a palavra na nova lista

    newString = "".join(listaPalavras)  # Concatena todos os item das lista

    return newString


fraseConvetida = converterParaCamelCase(frase)

print(fraseConvetida)
