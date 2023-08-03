#! /usr/bin/env python3
import schedule
import time
from interface import janela
from update import UpdateInt


schedule.every(1).minutes.do(UpdateInt)

# abre a interface
janela()

# loop para continuar agendando e executando as tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(60)
