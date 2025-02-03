'''
2. Calcule a média de uma lista de números
Crie uma função que receba uma lista de números e retorne a média aritmética.
'''
aluno = input("Informe o nome do aluno: ").strip().upper()


def obterNotas():
    global aluno
    '''
    Receber as medias de um Aluno
    '''
    countNotas = 0
    notas = []
    while countNotas < 4:

        for numNotas in range(1,5):
            nota = float(input(f"{aluno}, Informe a {numNotas}° Nota: "))
            notas.append(nota)
            countNotas += 1
        
        print(notas)
        
        return notas
        

def calcularMedia(lista):
    
    soma = sum(lista)
    media = soma / len(lista)
    
    print(media)

notasLista = obterNotas()

media = calcularMedia(notasLista)

        
        