"""
Verifique se um número é perfeito
Crie uma função que receba um número inteiro e verifique se ele é perfeito 
(a soma de seus divisores próprios é igual ao próprio número).
"""


def numero_perfeito(numero):
    if numero <= 0:
        return False

    # Encontrar os divisores próprios (excluindo o próprio número)
    divisores = [i for i in range(1, numero) if numero % i == 0]

    return sum(divisores) == numero


numero = int(input("Digite um numero para saber se o mesmo é um numero perfeito"))
if numero_perfeito(numero):
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")
