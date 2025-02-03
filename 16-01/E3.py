"""
Verifique se uma palavra está em uma frase
Escreva uma função que receba uma frase e uma palavra, e verifique se a palavra está presente na frase.
"""


def ReceberFraseEPalavra(palavra, frase):
    """
    Recebe uma frase e uma palavra e verifica se a palavra está presente na frase.
    """
    if palavra in frase:
        return True
    else:
        return False


frase = input("Digite uma frase: ").strip().lower()
palavra = (
    input("Agora digite a palavra que deseja verificar se a mesma está na frase: ")
    .strip()
    .lower()
)

palavraNaFrase = ReceberFraseEPalavra(palavra, frase)

if palavraNaFrase == True:
    print(f"A palavra '{palavra}' se encontra presente na frase: '{frase}'")
else:
    print(f"A palavra '{palavra}' não se encontra presente na frase: '{frase}'")
