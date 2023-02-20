# Algumas boas práticas de programação

# Maps, é uma função pura e de ordem superior, pois depende apenas de seus parâmetros
# e recebe uma função como parâmetro, sintaxe: map(função, iterável1, iterável2)

# ------------------------------------------------------------------------------------------------------------------

# implementação comum:

# lista = [1, 2, 3, 4, 5]
#
#
# def triplica_itens(iteravel):
#     lista_ = []
#     for item in iteravel:
#         lista_.append(item*3)
#     return lista_
#
#
# nova_lista = triplica_itens(lista)
# print(nova_lista)

# ------------------------------------------------------------------------------------------------------------------

# implementação com maps

# lista = [1, 2, 3, 4, 5]
#
#
# def triplica_item(item):
#     return item*3
#
#
# nova_lista = map(triplica_item, lista)
# print(list(nova_lista))

# ------------------------------------------------------------------------------------------------------------------

# aplicando lambda na mesma implementação

# lista = [1, 2, 3, 4, 5]
#
# nova_lista = map(lambda item: item * 3, lista)
#
# print(list(nova_lista))

# --------------------------------------------------------------------------------------------------------------------------------


# Método Filter, usada para filtrar elementos iteraveis, onde iremos fazer três scripts com a mesma filtragem de
# elementos ípares:

# lista = [1, 2, 3, 4, 5]
#
#
# def impares(itens):
#     lista_aux = []
#     for numero in itens:
#         if numero % 2 != 0:
#             lista_aux.append(numero)
#     return lista_aux
#
#
# nova_lista = impares(lista)
# print(nova_lista)

# ------------------------------------------------------------------------------------------------------------------
# Usando o filter:

# lista = [1, 2, 3, 4, 5]
#
#
# def impares(item):
#     return item % 2 != 0
#
#
# nova_lista = filter(impares, lista)
# print(list(nova_lista))

# ------------------------------------------------------------------------------------------------------------------
# Usando Filter com Lambda:

lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)
print(list(nova_lista))
