"""
Escreva uma função que receba uma string e retorne o texto invertido.
Exemplo:
Entrada: "Python"
Saída: "nohtyP"
"""

def inverterString(string):
    return string[::-1]

palavra = input("Digite a palavra que deseja inverter: ")

resultado = inverterString(palavra)
print(f"A palavra invertida fica dessa forma: {resultado}")


