from git import Repo  # biblioteca para interação com o github
import os
import shutil
from interface import janela
import tkinter as tk
import sys


def UpdateInt():
    # remove o arquivo desafado do diretório principal
    def MoveDef(arq_ant, saves):
        # mover o arquivo 'arq_ant' da pasta principal para a pasta 'saves'
        shutil.move(arq_ant, os.path.join(saves, os.path.basename(arq_ant)))

    # clona o repositorio do link completo
    def CloneInt(repo_url, arq_ant, temp):
        # clonar o repositório no diretório 'temp' e mover o arquivo 'arq_ant'
        # da pasta 'temp_clone' para a pasta principal
        repo = Repo.clone_from(repo_url, temp)
        shutil.move(
            arq_temp_interface, os.path.join(os.getcwd(), os.path.basename(arq_ant))
        )

    def Aviso():
        aviso = tk.Tk()
        aviso.title("Aviso - Update")
        aviso.geometry("400x100")
        fonte = ("Arial", 12)

        # texto principal
        texto = tk.Label(
            aviso, text="A interface foi atualizada e deve ser reiniciada.", font=fonte
        )
        texto.grid(column=0, row=2)  # posiciona o texto na janela
        texto.pack(pady=20)

        aviso.mainloop()

    # localizacoes dos arquivos
    repo_url = "https://github.com/analiviagarbin/testes"
    arq_ant = "./interface.py"
    arq_temp_interface = "./temp_clone/interface.py"
    temp = "./temp_clone"
    saves = "./saves"

    # se as pastas já nao existirem, cria uma nova
    if not os.path.exists(temp):
        os.makedirs(temp)

    if not os.path.exists(saves):
        os.makedirs(saves)

    MoveDef(arq_ant, saves)
    CloneInt(repo_url, arq_ant, temp)

    # apaga as pastas temporarias
    shutil.rmtree(saves)
    # shutil.rmtree(temp)  # ainda nao funciona, erro de permissao

    Aviso()
    sys.exit()
