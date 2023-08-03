#! /usr/bin/env python3
import schedule
import time
from interface import janela
from update import UpdateInt
import threading

schedule.every(1).minutes.do(UpdateInt)


# abre a interface
def interface():
    janela()


def agendamento():
    # loop para continuar agendando e executando as tarefas agendadas
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    # cria e inicia as threads para as funcoes serem
    # executadas simultaneamente
    thread_interface = threading.Thread(target=interface)
    thread_aviso = threading.Thread(target=agendamento)

    thread_interface.start()
    thread_aviso.start()
