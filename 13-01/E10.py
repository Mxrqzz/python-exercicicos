'''
Escreva uma função que retorne todos os números pares de uma lista fornecida.
Exemplo:
Entrada: [1, 2, 3, 4, 5, 6]
Saída: [2, 4, 6]
'''

def receberLista():
    lista = []
    while True:
        try:
            numero = int(input("Digite o número que deseja adicionar a lista. "))
            lista.append(numero)
        except ValueError:
            print("Digite um número valido. ")
            continue
        
        
        adicionarMais = input("Deseja adicionar mais um número? (s/n) ").strip().lower()
        
        if adicionarMais == "n":
            print(lista)
            break
        
    return lista

def SepararParesDoImpares(lista):
    '''
    Separa os numeros por impar e par
    '''
    impares = []
    pares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

    return pares, impares
    
    

lista = receberLista()

SepararParesDoImpares(lista)