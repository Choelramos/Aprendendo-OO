# Algumas boas práticas de programação

# Maps, é uma função pura e de ordem superior, pois depende apenas de seus parâmetros
# e recebe uma função como parâmetro, sintaxe: map(função, iterável1, iterável2)

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

# implementação com maps

lista = [1, 2, 3, 4, 5]


def triplica_item(item):
    return item*3


nova_lista = map(triplica_item, lista)
print(list(nova_lista))
