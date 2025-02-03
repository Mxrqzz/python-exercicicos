"""
Crie uma função que receba uma string e conte o número de vogais nela.
Exemplo:
Entrada: "Python é incrível!"
Saída: 6
"""


def contarVogaisENaoVogais(palavra):
    vogais = "AEIOUaeiou"
    numero_vogais = 0
    numero_consoantes = 0

    for letra in palavra:
        if letra in vogais:
            numero_vogais += 1
        elif letra.isalpha():
            numero_consoantes += 1

    return numero_vogais, numero_consoantes


def contarCaracteresPalavra():
    while True:
        palavra = input(
            "\nDigite uma palavra para contar quantas vogais ela tem: "
        ).strip()
        vogaisNumero, consoantesNumero = contarVogaisENaoVogais(palavra)

        print(
            f"A palavra : {palavra} possui {vogaisNumero} vogais e {consoantesNumero} consoantes."
        )

        contarDnv = (
            input("Deseja contar o número de caracteres de outra palavra? (S/N) ")
            .strip()
            .lower()
        )
        if contarDnv == "n":
            print("Progama encerrado")
            break


contarCaracteresPalavra()
