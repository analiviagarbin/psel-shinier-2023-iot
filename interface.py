import tkinter as tk  # biblioteca de interface grafica


def janela():
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
    texto_orientacao = tk.Label(janela, text="Digite o MUDEI seu nome:", font=fonte)
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
    botao_mostrar_mensagem.pack(pady=5)

    mensagem_pronta = tk.Label(janela, text="", font=fonte)
    mensagem_pronta.pack(pady=10)

    # posiciona a janela no centro do display
    largura_janela = 400
    altura_janela = 200
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posicao_x = int((largura_tela - largura_janela) / 2)
    posicao_y = int((altura_tela - altura_janela) / 2)
    janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

    # inicia o loop principal da interface grafica
    janela.mainloop()


def Aviso():
    aviso = tk.Tk()
    aviso.title("Aviso - Update")
    aviso.geometry("400x100")
    fonte = ("Arial", 12)

    # texto principal
    texto = tk.Label(
        aviso, text="A interface foi atualizada e será reiniciada.", font=fonte
    )
    texto.grid(column=0, row=2)  # posiciona o texto na janela
    texto.pack(pady=20)

    def FecharAviso():
        aviso.destroy()

    # botão
    botao_bg = "#32CD99"
    botao_fg = "white"  # cor do texto
    botao_aviso = tk.Button(
        aviso,
        text="Reiniciar",
        font=fonte,
        fg=botao_fg,
        bg=botao_bg,
        command=FecharAviso,
    )
    botao_aviso.pack(padx=10)

    # posiciona a aviso no centro do display
    largura_aviso = 400
    altura_aviso = 100
    largura_tela = aviso.winfo_screenwidth()
    altura_tela = aviso.winfo_screenheight()
    posicao_x = int((largura_tela - largura_aviso) / 2)
    posicao_y = int((altura_tela - altura_aviso) / 2)
    aviso.geometry(f"{largura_aviso}x{altura_aviso}+{posicao_x}+{posicao_y}")

    aviso.mainloop()
