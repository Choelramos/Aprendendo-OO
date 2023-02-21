from threading import Thread
from time import sleep


def thread(mensagem, tempo_execucao):
    print(f'\nExecutando a {mensagem}')
    sleep(tempo_execucao)
    print(f'\nFinalizando a {mensagem}')


thread1 = Thread(target=thread, args=("Thread 1", 3))
thread2 = Thread(target=thread, args=("Thread 2", 2))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("\nExecução concluída")



