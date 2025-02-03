"""
Conte palavras únicas em uma frase
Escreva uma função que receba uma frase e conte quantas palavras únicas existem nela.
"""

frase = (
    input("Digite uma frase para contar o numero de palavras únicas na mesma: ")
    .strip()
    .lower()
)


def contarPalavrasUnicas(frase):
    """
    Recebe uma frase e conta quantas palavras unicas aparecem nessa frase.
    """
    palavras = frase.split()
    palavrasUnicas = []

    for palavra in palavras:
        if palavra not in palavrasUnicas:
            palavrasUnicas.append(
                palavra
            )  # se a palavra na estiver na lista ela é adicionada
        elif palavra in palavrasUnicas:
            palavrasUnicas.remove(
                palavra
            )  # caso a palavra ja tenha aparecido, remove ela da lista

    contagem = len(palavrasUnicas)  # pega o número de palavras unicas

    return contagem, palavrasUnicas


contagem, unicas = contarPalavrasUnicas(frase)

print(f"A frase: {frase}.")
print(f"Contém {contagem} palavras únicas .")
print(f"Sendo elas: {unicas}.")
