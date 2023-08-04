#! /usr/bin/env python3
from interface import janela
from update import UpdateInt
import threading


# abre a interface
def interface():
    janela()


if __name__ == "__main__":
    # cria e inicia as threads para as funcoes serem
    # executadas simultaneamente
    tempo_espera = 3600
    thread_interface = threading.Thread(target=interface)
    thread_aviso = threading.Timer(tempo_espera, UpdateInt)

    thread_aviso.start()
    thread_interface.start()
