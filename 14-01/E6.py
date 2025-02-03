"""
6. Converta uma lista de temperaturas em Celsius para Fahrenheit
Escreva uma função que receba uma lista de temperaturas em graus Celsius 
e retorne uma nova lista com as temperaturas convertidas para Fahrenheit.
°F=(°C x 1.8)+32
"""


def receberTemperaturasC():
    """
    Função para receber temperaturas em celsius
    """
    temperaturasC = []

    while True:
        try:
            temperatura = float(
                input("Digite a Temperatura em celsius que deseja adicionar a lista: ")
            )
            temperaturasC.append(temperatura)

        except ValueError:
            print("Digite uma temperatura válida. ")
            continue

        parar = (
            input("Deseja adicionar mais uma temperatura na lista? (s/n).")
            .strip()
            .lower()
        )
        if parar == "n":
            print(temperaturasC)
            break

    return temperaturasC


def converterListaParaF(lista):
    """
    Recebe a lista de temperaturas em Celsius e Converte para Fahrenheit
    """
    temperaturasF = []

    if lista:
        for temp in lista:
            tempF = (temp * 1.8) + 32
            temperaturasF.append(tempF)

        return temperaturasF


listaCelsius = receberTemperaturasC()

listaFahrenheit = converterListaParaF(listaCelsius)

print(listaFahrenheit)
