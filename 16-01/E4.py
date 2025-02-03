"""
Calcule a diferença entre o maior e o menor número de uma lista
Crie uma função que receba uma lista de números e retorne a diferença entre o maior e o menor número.
"""


def receberLista():
    """
    Recebe um número e adiciona o mesmo na lista de números, logo após pergunta se deseja adicionar mais um número

    """
    numeros = []

    while True:
        try:
            numero = int(input("Digite o número que deseja adicionar a lista: "))
            numeros.append(numero)
        except ValueError:
            print("Digite um número válido. ")
            continue

        parar = input("Deseja adicionar mais um número? (s/n)").strip().lower()

        if parar == "n":
            print(numeros)
            break

    return numeros


def diferencaEntreMaiorMenor(lista):
    
    menorNum = min(lista)
    maiorNum = max(lista)
    
    diferenca = maiorNum - menorNum
    
    return diferenca

listaNumeros = receberLista()

diferenca = diferencaEntreMaiorMenor(listaNumeros)

print(diferenca)
