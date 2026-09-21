import tkinter as tk
from tkinter import messagebox
import sys
from blackjack import jogar_blackjack
from truco import jogar_truco
from uno import jogar_uno

class HubJogosCartas:
    def __init__(self, root):
        self.root = root
        self.root.title("Hub de Jogos de Cartas")
        self.root.geometry("450x500")
        self.root.configure(bg="#2c3e50")
        
        # Variável de saldo persistente
        self.saldo_jogador = 500
        
        # Título Principal na Janela
        self.label_titulo = tk.Label(
            root, text="HUB DE JOGOS DE CARTAS", 
            font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        self.label_titulo.pack(pady=20)
        
        # Exibição do Saldo do Jogador
        self.label_saldo = tk.Label(
            root, text=f"Seu Saldo Atual: ${self.saldo_jogador}", 
            font=("Helvetica", 12, "bold"), bg="#2c3e50", fg="#f1c40f"
        )
        self.label_saldo.pack(pady=10)
        
        # Estilo padrão dos botões
        estilo_botao = {
            "font": ("Helvetica", 11, "bold"),
            "fg": "#ffffff",
            "width": 25,
            "bd": 0,
            "pady": 10,
            "cursor": "hand2"
        }
        
        # Botão Blackjack
        self.btn_blackjack = tk.Button(root, text="🃏 Jogar Blackjack (21)", bg="#3498db", command=self.iniciar_blackjack, **estilo_botao)
        self.btn_blackjack.pack(pady=10)
        
        # Botão Truco
        self.btn_truco = tk.Button(root, text="⚔️ Jogar Truco", bg="#2ecc71", command=self.iniciar_truco, **estilo_botao)
        self.btn_truco.pack(pady=10)
        
        # Botão Uno
        self.btn_uno = tk.Button(root, text="🔥 Jogar Uno", bg="#e74c3c", command=self.iniciar_uno, **estilo_botao)
        self.btn_uno.pack(pady=10)
        
        # Botão Recarregar Fichas
        self.btn_recarregar = tk.Button(root, text="💰 Recarregar Fichas (+$500)", bg="#9b59b6", command=self.recarregar_fichas, **estilo_botao)
        self.btn_recarregar.pack(pady=10)
        
        # Botão Sair
        self.btn_sair = tk.Button(root, text="🚪 Sair do Programa", bg="#95a5a6", command=self.sair, **estilo_botao)
        self.btn_sair.pack(pady=20)

    def atualizar_saldo_tela(self):
        self.label_saldo.config(text=f"Seu Saldo Atual: ${self.saldo_jogador}")

    def iniciar_blackjack(self):
        messagebox.showinfo("Blackjack", "O jogo vai iniciar! Acompanhe as cartas informadas no terminal do VS Code enquanto usa o painel.")
        # Executa a lógica atualizada puxando o saldo da interface gráfica
        self.saldo_jogador = jogar_blackjack(self.saldo_jogador)
        self.atualizar_saldo_tela()

    def iniciar_truco(self):
        messagebox.showinfo("Truco", "Partida iniciada! Use o terminal do VS Code para fazer suas jogadas.")
        jogar_truco()

    def iniciar_uno(self):
        messagebox.showinfo("Uno", "Partida iniciada! Use o terminal do VS Code para gerenciar suas cartas.")
        jogar_uno()

    def recarregar_fichas(self):
        self.saldo_jogador += 500
        self.atualizar_saldo_tela()
        messagebox.showinfo("Sucesso", "Mais $500 fichas adicionadas à sua carteira!")

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja fechar o Hub de Jogos?"):
            self.root.destroy()
            sys.exit()

if __name__ == "__main__":
    app_janela = tk.Tk()
    hub = HubJogosCartas(app_janela)
    app_janela.mainloop()
