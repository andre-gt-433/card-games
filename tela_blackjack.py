import tkinter as tk
from tkinter import messagebox
from utils import criar_baralho

class BlackjackGame:
    def __init__(self, container, hub_instance):
        self.container = container
        self.hub = hub_instance  # Guarda a referência para o saldo e menu
        
        self.baralho = []
        self.mao_jogador = []
        self.mao_dealer = []
        self.aposta = 50
        
        self.construir_tela()

    def construir_tela(self):
        tk.Label(self.container, text="🃏 CASINO BLACKJACK", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
        
        self.lbl_info = tk.Label(self.container, text="", font=("Arial", 12), bg="#2c3e50", fg="#f1c40f")
        self.lbl_info.pack()

        # Painel do Dealer
        self.frame_dealer = tk.LabelFrame(self.container, text="Mão da Banca (Dealer)", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.frame_dealer.pack(fill="x", padx=20, pady=10)
        self.lbl_cartas_dealer = tk.Label(self.frame_dealer, text="Clique em 'Dar as Cartas'", font=("Arial", 14), bg="#2c3e50", fg="#e74c3c")
        self.lbl_cartas_dealer.pack()

        # Painel do Jogador
        self.frame_jog = tk.LabelFrame(self.container, text="Sua Mão", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.frame_jog.pack(fill="x", padx=20, pady=10)
        self.lbl_cartas_jog = tk.Label(self.frame_jog, text="Para iniciar a rodada", font=("Arial", 14), bg="#2c3e50", fg="#3498db")
        self.lbl_cartas_jog.pack()

        # Botões de Ação
        self.frame_botoes = tk.Frame(self.container, bg="#2c3e50")
        self.frame_botoes.pack(pady=20)
        
        self.btn_hit = tk.Button(self.frame_botoes, text="Pedir Carta (Hit)", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=15, command=self.hit, state="disabled")
        self.btn_hit.grid(row=0, column=0, padx=5)
        
        self.btn_stand = tk.Button(self.frame_botoes, text="Parar (Stand)", bg="#e67e22", fg="white", font=("Arial", 10, "bold"), width=15, command=self.stand, state="disabled")
        self.btn_stand.grid(row=0, column=1, padx=5)
        
        self.btn_iniciar = tk.Button(self.frame_botoes, text="Dar as Cartas", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), width=15, command=self.iniciar_rodada)
        self.btn_iniciar.grid(row=0, column=2, padx=5)

        tk.Button(self.container, text="↩ Voltar ao Menu", bg="#7f8c8d", fg="white", font=("Arial", 10, "bold"), command=self.hub.mostrar_menu_principal).pack(pady=10)
        self.atualizar_textos(ocultar=False)

    def calcular_pontos(self, mao):
        pontos = 0
        ases = 0
        for c in mao:
            if c['valor'] in ['J', 'Q', 'K']: pontos += 10
            elif c['valor'] == 'A': pontos += 11; ases += 1
            else: pontos += int(c['valor'])
        while pontos > 21 and ases > 0:
            pontos -= 10
            ases -= 1
        return pontos

    def iniciar_rodada(self):
        if self.hub.saldo < self.aposta:
            self.aposta = self.hub.saldo
            
        if self.hub.saldo <= 0:
            messagebox.showwarning("Sem fundos", "Você faliu! Recarregue fichas no menu.")
            return

        self.hub.saldo -= self.aposta
        self.baralho = criar_baralho()
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop()]
        self.mao_dealer = [self.baralho.pop(), self.baralho.pop()]
        
        self.btn_iniciar.config(state="disabled")
        self.btn_hit.config(state="normal")
        self.btn_stand.config(state="normal")
        
        self.atualizar_textos(ocultar=True)
        
        if self.calcular_pontos(self.mao_jogador) == 21:
            self.stand()

    def atualizar_textos(self, ocultar=True):
        self.lbl_info.config(text=f"Seu Dinheiro: ${self.hub.saldo}  |  Aposta Fixa: ${self.aposta}")
        if not self.mao_jogador: return
        
        txt_jog = " ".join([f"{c['valor']}{c['naipe']}" for c in self.mao_jogador])
        self.lbl_cartas_jog.config(text=f"{txt_jog}  (Total: {self.calcular_pontos(self.mao_jogador)})")
        
        if ocultar:
            self.lbl_cartas_dealer.config(text=f"{self.mao_dealer[0]['valor']}{self.mao_dealer[0]['naipe']}  [Carta Oculta]")
        else:
            txt_dlr = " ".join([f"{c['valor']}{c['naipe']}" for c in self.mao_dealer])
            self.lbl_cartas_dealer.config(text=f"{txt_dlr}  (Total: {self.calcular_pontos(self.mao_dealer)})")

    def hit(self):
        self.mao_jogador.append(self.baralho.pop())
        self.atualizar_textos(ocultar=True)
        if self.calcular_pontos(self.mao_jogador) > 21:
            self.finalizar_partida("Você estourou os 21 pontos! O Dealer venceu. 🃏")

    def stand(self):
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")
        
        while self.calcular_pontos(self.mao_dealer) < 17:
            self.mao_dealer.append(self.baralho.pop())
            
        p_jog = self.calcular_pontos(self.mao_jogador)
        p_dlr = self.calcular_pontos(self.mao_dealer)
        
        self.atualizar_textos(ocultar=False)
        
        if p_dlr > 21:
            self.hub.saldo += self.aposta * 2
            self.finalizar_partida("O Dealer estourou! Você Venceu! 🎉🏆")
        elif p_jog > p_dlr:
            self.hub.saldo += self.aposta * 2
            self.finalizar_partida("Você fez mais pontos e venceu o Dealer! 🏅")
        elif p_jog < p_dlr:
            self.finalizar_partida("O Dealer fez mais pontos e ganhou a rodada. 🃏")
        else:
            self.hub.saldo += self.aposta
            self.finalizar_partida("Empate! Suas fichas foram devolvidas. 🤝")

    def finalizar_partida(self, msg):
        self.atualizar_textos(ocultar=False)
        messagebox.showinfo("Resultado", msg)
        self.btn_iniciar.config(state="normal")
        self.btn_hit.config(state="disabled")
        self.btn_stand.config(state="disabled")
        self.lbl_info.config(text=f"Seu Dinheiro: ${self.hub.saldo}  |  Aposta Fixa: ${self.aposta}")
