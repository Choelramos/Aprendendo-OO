# Criando funções de ondem superior

# def multiplicar_por(multiplicador):
#     def mult(multiplicando):
#         return multiplicando * multiplicador
#     return mult
#
#
# multiplicar_por_10 = multiplicar_por(10)
# print(multiplicar_por_10(1))
# print(multiplicar_por_10(2))
#
#
# multiplicar_por_5 = multiplicar_por(5)
# print(multiplicar_por_5(1))
# print(multiplicar_por_5(2))

# Usando função anônima lambda para resolver o mesmo problema

def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicador * multiplicando


multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(1))
print(multiplicar_por_10(2))

multiplicar_por_5 = multiplicar_por(5)
print(multiplicar_por_5(1))
print(multiplicar_por_5(2))

