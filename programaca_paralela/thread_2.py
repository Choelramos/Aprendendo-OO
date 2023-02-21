# Mesma função que no exemplo do programa thread_1, porém a função recebe parâmetro

import threading
import time


def funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)


print('Iniciando o programa!')
x = threading.Thread(target=funcao, args=('Executando!',))
x.start()
print('Fim do programa!')

