from git import Repo  # biblioteca para interação com o github
import os
import shutil
import tkinter as tk
import subprocess
from interface import Aviso


def UpdateInt():
    # remove o arquivo desafado do diretório principal
    def MoveDef(arq_ant, saves):
        # mover o arquivo 'arq_ant' da pasta principal para a pasta 'saves'
        shutil.move(arq_ant, os.path.join(saves, os.path.basename(arq_ant)))

    # clona o repositorio do link completo
    def CloneInt(repo_url, arq_temp_interface, arq_fim, temp):
        # clonar o repositório no diretório 'temp' e mover o arquivo 'arq_ant'
        # da pasta 'temp_clone' para a pasta principal
        repo = Repo.clone_from(repo_url, temp)
        shutil.move(arq_temp_interface, arq_fim)

    def reiniciar():
        # executa o arquivo main.py novamente
        # colocar caminho completo da main
        subprocess.call(["python3", "./main.py"])

    # localizacoes dos arquivos
    # adicionar caminho COMPLETO
    repo_url = "https://github.com/analiviagarbin/psel-shinier-2023-iot"
    arq_ant = "./interface.py"
    arq_fim = "./"
    arq_temp_interface = "./temp_clone/interface.py"
    temp = "./temp_clone"
    saves = "./saves"

    # se as pastas já nao existirem, cria uma nova
    if not os.path.exists(temp):
        os.makedirs(temp)

    if not os.path.exists(saves):
        os.makedirs(saves)

    MoveDef(arq_ant, saves)
    CloneInt(repo_url, arq_temp_interface, arq_fim, temp)

    # apaga as pastas temporarias
    shutil.rmtree(saves)
    shutil.rmtree(temp)

    Aviso()
    reiniciar()
