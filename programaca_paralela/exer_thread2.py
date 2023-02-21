# Nesse exercício estou usando thread para implementar duas tarefas: Elevar ao quadrado e ao cubo

from threading import Thread
from time import sleep


def execucao(tipo, n1, n2, tempo):
    print(tipo)
    print(f'Executando calculo: {n1 ** n2}')
    sleep(tempo)
    print("\nFim do cálculo!")


c1 = Thread(target=execucao, args=("Cálculo 2 ao CUBO:", 2, 3, 3))
c1.start()
c1.join()
c2 = Thread(target=execucao, args=("Cálculo 2 ao QUADRADO:", 2, 2, 2))
c2.start()
c2.join()




