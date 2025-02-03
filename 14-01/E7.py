"""
7. Verifique se uma string é um anagrama
Crie uma função que receba duas strings e verifique se uma é anagrama da outra. 
Exemplo: "amor" e "roma" são anagramas.
"""


def recebeStrings():
    """
    Recebe duas strings
    """
    stringUm = input("Digite a primeira palavra: ").strip().upper()
    stringDois = (
        input(
            "Digite a segunda palavra para verificar se são anagramas uma da outras: "
        )
        .strip()
        .upper()
    )

    return stringUm, stringDois


def conferirStrings(stringUm, stringDois):
    """
    Apos chamar a função de ordenar lista compara as duas listas
    """

    palavraUm = ordenarLista(stringUm)
    palavraDois = ordenarLista(stringDois)

    if palavraUm == palavraDois:
        print(f"A palavra {stringUm} é um anagrama de {stringDois}")
    else:
        print(f"A palavra {stringUm} não é um anagrama de {stringDois}")


def ordenarLista(string):
    """
    Transforma uma string em lista e ordena os caracteres em ordem alfabetica
    """
    lista = []

    for letra in string:
        lista.append(letra)

    novaLista = sorted(lista)
    print(novaLista)

    return novaLista


string1, string2 = recebeStrings()

if string1 and string2:
    print(f"Palavra 1 : {string1}, Palavra 2 : {string2}")
    conferirStrings(string1, string2)
else:
    print("Erro ao receber as strings.")
