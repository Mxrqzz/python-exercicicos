'''
Escreva uma função que substitua todos os espaços de uma string por hífens.
Exemplo:
Entrada: "Python é legal"
Saída: "Python-é-legal"
'''

def alterarEspaços(texto):
    texto_alterado = texto.replace(' ', '-')
    print(texto_alterado)

alterarEspaços('Vasco da Gama')