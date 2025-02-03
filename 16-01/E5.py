'''
Gerador de números Fibonacci
Escreva uma função que gere os primeiros N números da sequência de Fibonacci.
'''

def gerar_fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]  # Apenas o primeiro número
    elif numero == 2:
        return [0, 1]  # Os dois primeiros números

    # Inicializar a sequência com os dois primeiros números
    fibonacci = [0, 1]
    for i in range(2, numero):
        # Adiciona à lista a soma dos dois últimos números
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Exemplo de uso
numero = int(input("Digite um número: "))
print(gerar_fibonacci(numero))
