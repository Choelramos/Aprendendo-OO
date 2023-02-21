from threading import Thread
from time import sleep


def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando Tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'\nConclusão da tarefa {mensagem}')


thread = Thread(target=tarefa, args=(2, 'Thread em execução'))
thread.start()
print('\nAguardando execução da Thread...')
thread.join()
print("Execução concluída!")
