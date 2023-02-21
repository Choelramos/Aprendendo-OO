# Entendendo conceitos básicos da programação paralela

import threading
import time


def funcao():
    for i in range(3):
        print(i, 'Executando a Thread!')
        time.sleep(1)  # Função usada para pausar a execução


print('Inicializando o programa!')
threading.Thread(target=funcao).start()
print('Finalizando o programa!')
