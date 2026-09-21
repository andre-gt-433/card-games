import tkinter as tk
from tkinter import messagebox
from tela_blackjack import BlackjackGame  # Importa o jogo de Blackjack que criamos
from tela_truco import TrucoGame
from tela_uno import UnoGame

class AppHubJogos:
    def __init__(self, root):
        self.root = root
        self.root.title("Hub de Jogos de Cartas Clássicos")
        self.root.geometry("500x550")
        self.root.configure(bg="#2c3e50")
        
        self.saldo = 500
        self.container = tk.Frame(self.root, bg="#2c3e50")
        self.container.pack(fill="both", expand=True)
        
        self.mostrar_menu_principal()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        self.limpar_tela()
        self.root.geometry("500x550")
        
        lbl_titulo = tk.Label(self.container, text="🃏 HUB DE JOGOS DE CARTAS 🃏", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
        lbl_titulo.pack(pady=30)
        
        lbl_saldo = tk.Label(self.container, text=f"Seu Dinheiro: ${self.saldo}", font=("Arial", 14, "bold"), bg="#2c3e50", fg="#f1c40f")
        lbl_saldo.pack(pady=10)
        
        estilo_btn = {"font": ("Arial", 11, "bold"), "fg": "white", "width": 25, "bd": 0, "pady": 10, "cursor": "hand2"}
        
        tk.Button(self.container, text="Blackjack (21)", bg="#3498db", command=self.abrir_blackjack, **estilo_btn).pack(pady=10)
        tk.Button(self.container, text="Truco Paulista", bg="#2ecc71", command=self.abrir_truco, **estilo_btn).pack(pady=10)
        tk.Button(self.container, text="Uno Colorido", bg="#e74c3c", command=self.abrir_uno, **estilo_btn).pack(pady=10)
        tk.Button(self.container, text="Recarregar Fichas (+$500)", bg="#9b59b6", command=self.recarregar_fichas, **estilo_btn).pack(pady=10)
        tk.Button(self.container, text="Sair", bg="#95a5a6", command=self.root.quit, **estilo_btn).pack(pady=20)

    def recarregar_fichas(self):
        self.saldo += 500
        messagebox.showinfo("Banco", "Você ganhou mais $500 créditos!")
        self.mostrar_menu_principal()

    def abrir_blackjack(self):
        self.limpar_tela()
        self.root.geometry("650x550")
        BlackjackGame(self.container, self)

    def abrir_truco(self):
     self.limpar_tela()
     self.root.geometry("650x600")
     TrucoGame(self.container, self)


    def abrir_uno(self):
     self.limpar_tela()
     self.root.geometry("680x580")
     UnoGame(self.container, self)


if __name__ == "__main__":
    janela = tk.Tk()
    jogo_completo = AppHubJogos(janela)
    janela.mainloop()
