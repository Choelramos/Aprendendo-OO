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

veiculos = ['avião', 'carro', 'navio', 'onibus']


def letras_maiusculas(itens):
    return itens.upper()


carros = map(letras_maiusculas, veiculos)
print(list(carros))





