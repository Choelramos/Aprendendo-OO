# Alguns exemplos de programação funcional

# -------------------------------------------------------------------------------------------------

# Neste exemplo estamos adicionando mais um ao elemento:
# import operator
# from functools import partial
# adiciona_um = partial(operator.add, 1)
#
# print(adiciona_um(5))

# -------------------------------------------------------------------------------------------------

# transformando todos os nomes em maiúsculo

# veiculos = ['avião', 'carro', 'navio', 'onibus']
#
#
# def letras_maiusculas(itens):
#     return itens.upper()
#
#
# carros = map(letras_maiusculas, veiculos)
# print(list(carros))

# -------------------------------------------------------------------------------------------------

# imprimindo apenas números pares:

# lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# pares = filter(lambda item: item % 2 == 0, lista)
# print(list(pares))

# -------------------------------------------------------------------------------------------------
# Arredondando os valores da lista de números na mesma ordem da lista de precisão:

lista_numeros = [9.15613, 7.84651, 3.00123, 6.5648]
lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x, y: round(x, y)

resultado = list(map(arredondamento, lista_numeros, lista_precisao))
print(resultado)
