import tkinter as tk  # biblioteca de interface grafica


def gerar_mensagem():
    nome = nomeD.get()  # nome recebe o get de nomeD
    mensagem = f"{nome}, candidato(a) do processo seletivo shinier iot"
    mensagem_pronta.config(text=mensagem)


# cria a janela principal "Gerar Mensagem"
janela = tk.Tk()
janela.title("Gerar Mensagem")
janela.geometry("400x200")  # tamanho da janela fixo
fonte = ("Arial", 12)

# texto principal
texto_orientacao = tk.Label(janela, text="Digite o seu nome:", font=fonte)
texto_orientacao.grid(column=0, row=0)  # posiciona o texto na janela
texto_orientacao.pack(pady=10)

# caixa de entrada do nome
nomeD = tk.Entry(janela, font=fonte)
nomeD.pack()

# botão
fonte_botao = ("Arial", 14)
botao_fg = "blue"  # cor do texto
botao_mostrar_mensagem = tk.Button(
    janela,
    text="Mostrar Mensagem",
    font=fonte_botao,
    fg=botao_fg,
    command=gerar_mensagem,
)
botao_mostrar_mensagem.pack(pady=20)

mensagem_pronta = tk.Label(janela, text="", font=fonte)
mensagem_pronta.pack(pady=10)

# inicia o loop principal da interface gráfica
janela.mainloop()
