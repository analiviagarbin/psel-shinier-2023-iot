import git  # biblioteca de interacao com repositorios git
import subprocess  # executar comandos no sistema operacional


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
