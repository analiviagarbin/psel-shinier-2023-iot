import git  # biblioteca de interacao com repositorios git
import subprocess  # executar comandos no sistema operacional


# auto atualização
# funcao de atualizacao a partir do repositorio
# fonte: repositorio de parametro para atualizacao
# update: arquivo a ser atualizado
def update_git(fonte, main_cod):
    try:
        if os.path.exists("temp_fonte"):
            # Caso a pasta temp_fonte exista, puxar as atualizações
            repo = git.Repo("temp_fonte")
            repo.remotes.origin.pull()
        else:
            # Se a pasta temp_fonte não existir, clonar o repositório
            repo = git.Repo.clone_from(fonte, "temp_fonte", branch="main")

        # Atualiza o arquivo alvo com a versão mais recente
        shutil.copy(f"temp_fonte/{main_cod}", main_cod)

    except git.exc.GitCommandError as e:
        print(f"Erro ao atualizar: {e}")


def update_h():
    git_url = "https://github.com/analiviagarbin/psel-shinier-2023-iot"
    main_cod = "main.py"
    update_git(git_url, main_cod)
    gerar_mensagem()
