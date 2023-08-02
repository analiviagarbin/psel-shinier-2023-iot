#! /usr/bin/env python3
import schedule
import time
from interface import janela
from update import UpdateInt

# abre a interface
janela()

# agenda o update do arquivo interface para a cada 1 hora
# if __name__ == "__main__":
#    schedule.every(1).hour.do(UpdateInt)

# loop para continuar agendando e executando as tarefas agendadas
#    while True:
#        schedule.run_pending()
#        time.sleep(1)
