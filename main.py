import customtkinter as ctk  # biblioteca de interface grafica


# interface
def gerar_mensagem():
    nome = nomeD.get()  # nome recebe o get de nomeD
    mensagem = f"{nome}, candidato(a) do processo seletivo Shinier IoT"
    mensagem_pronta.configure(text=mensagem)


ctk.set_appearance_mode("ligth")
ctk.set_default_color_theme("green")

# cria a janela principal "Gerar Mensagem"
janela = ctk.CTk()
janela.title("Gerar Mensagem")
janela.geometry("400x200")  # tamanho da janela fixo
fonte = ("Arial", 12)

# texto principal
texto_orientacao = ctk.CTkLabel(janela, text="Digite o seu nome:", font=fonte)
texto_orientacao.pack(pady=10, padx=10)

# caixa de entrada do nome
nomeD = ctk.CTkEntry(
    janela, placeholder_text="Seu nome", font=fonte, fg_color="transparent"
)
nomeD.pack(padx=10)

# botão
fonte_botao = ("Arial", 14)
botao_mostrar_mensagem = ctk.CTkButton(
    janela,
    text="Mostrar Mensagem",
    font=fonte_botao,
    command=gerar_mensagem,
)
botao_mostrar_mensagem.pack(padx=10, pady=5)

mensagem_pronta = ctk.CTkLabel(janela, text="", font=fonte)
mensagem_pronta.pack(pady=10, padx=10)

# inicia o loop principal da interface grafica
janela.mainloop()
