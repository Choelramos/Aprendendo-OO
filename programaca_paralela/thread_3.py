# sincronizando threads

import threading
import time

lista = []


def contador1(n):
    for i in range(1, n+1):
        print(i)
        lista.append(i)
        time.sleep(0.5)


def contador2(n):
    for i in range(6, n+1):
        print(i)
        lista.append(i)
        time.sleep(0.6)


x = threading.Thread(target=contador1, args=(5, ))
x.start()

x.join()

y = threading.Thread(target=contador2, args=(10, ))
y.start()

y.join()

print(lista)
