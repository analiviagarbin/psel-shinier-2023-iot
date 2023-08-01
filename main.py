import tkinter as tk  # biblioteca de interface grafica
import git  # biblioteca de interacao com repositorios git
import subprocess  # executar comandos no sistema operacional
import schedule  # biblioteca para agendar verificacao
import time


def gerar_mensagem():
    nome = nomeD.get()  # nome recebe o get de nomeD
    mensagem = f"{nome}, candidato(a) do processo seletivo Shinier IoT"
    mensagem_pronta.config(text=mensagem)


# cria a janela principal "Gerar Mensagem"
janela = tk.Tk()
janela.title("Gerar Mensagem")
janela.geometry("400x200")  # tamanho da janela fixo
fonte = ("Arial", 12)

# texto principal
texto_orientacao = tk.Label(janela, text="Digite o seu nome:", font=fonte)
texto_orientacao.grid(column=0, row=0)  # posiciona o texto na janela
texto_orientacao.pack(pady=20)

# caixa de entrada do nome
nomeD = tk.Entry(janela, font=fonte)
nomeD.pack()
nomeD.focus()

# botão
botao_bg = "#32CD99"
botao_fg = "white"  # cor do texto
botao_mostrar_mensagem = tk.Button(
    janela,
    text="Mostrar Mensagem",
    font=fonte,
    fg=botao_fg,
    bg=botao_bg,
    command=gerar_mensagem,
)
botao_mostrar_mensagem.pack(pady=10)

mensagem_pronta = tk.Label(janela, text="", font=fonte)
mensagem_pronta.pack(pady=10)

largura_janela = 400
altura_janela = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = int((largura_tela - largura_janela) / 2)
posicao_y = int((altura_tela - altura_janela) / 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# inicia o loop principal da interface grafica
janela.mainloop()


# auto atualização
# funcao de atualizacao a partir do repositorio
# fonte: repositorio de parametro para atualizacao
# update: arquivo a ser atualizado
def update_git(fonte, main_cod):
    try:
        # se o repositorio nao existe na maquina, tentativa de clonar
        repo = git.Repo.fonte(fonte, "temp_fonte", branch="main")
    except git.exc.GitCommandError:
        # caso o repositorio ja exista localmente, realizar um pull para atualizar
        repo = git.Repo("temp_fonte")
        repo.remotes.origin.pull()

    # atualiza o arquivo alvo com a versao mais recente
    # abre o arquivo main_cod em modo de escrita 'w'
    with open(main_cod, "w") as target:
        # le o conteudo do arquivo temporario e escreve no main_cod (target)
        with open(f"temp_fonte/{main_cod}") as source:
            target.write(source.read())

    # limpa o repositorio temporario apos a atualizacao
    subprocess.run(["rm", "-rf", "temp_fonte"])


def update_h():
    git_url = "https://github.com/analiviagarbin/psel-shinier-2023-iot"  # define a URL do repositorio Git e o arquivo alvo para atualizar
    main_cod = "main.py"  # arquivo principal
    update_git(git_url, main_cod)  # chama a funcao para atualizar o arquivo alvo


if __name__ == "__main__":
    # agendando a funcao de atualizacao para ser executada a cada 1 hora
    schedule.every(1).hour.do(update_h)

    # loop para continuar agendando e executando as tarefas agendadas
    while True:
        schedule.run_pending()
        time.sleep(1)
