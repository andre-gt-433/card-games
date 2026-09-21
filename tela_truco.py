import tkinter as tk
from tkinter import messagebox
import random
from utils import gerar_baralho_truco

class TrucoGame:
    def __init__(self, container, hub_instance):
        self.container = container
        self.hub = hub_instance  # Referência ao Hub principal
        
        self.baralho = []
        self.mao_jogador = []
        self.mao_robo = []
        self.vira = None
        
        self.tentos_jog = 0
        self.tentos_robo = 0
        self.valor_rodada = 1
        self.quedas_jog = 0
        self.quedas_robo = 0
        
        self.construir_tela()

    def construir_tela(self):
        tk.Label(self.container, text="⚔️ ARENA DE TRUCO", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
        
        self.lbl_placar = tk.Label(self.container, text="Você: 0 tentos | Robô: 0 tentos", font=("Arial", 12, "bold"), bg="#2c3e50", fg="#f1c40f")
        self.lbl_placar.pack()

        # Mesa central (Vira e Ações)
        self.frame_mesa = tk.LabelFrame(self.container, text="Mesa (Vira & Jogadas)", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), pady=10)
        self.frame_mesa.pack(fill="x", padx=20, pady=10)
        
        self.lbl_vira = tk.Label(self.frame_mesa, text="Vira: ?", font=("Arial", 13, "bold"), bg="#2c3e50", fg="#e67e22")
        self.lbl_vira.pack()
        
        self.lbl_acoes_mesa = tk.Label(self.frame_mesa, text="Clique em 'Distribuir Mão' para começar.", font=("Arial", 11), bg="#2c3e50", fg="white")
        self.lbl_acoes_mesa.pack(pady=5)

        # Painel das Cartas do Jogador
        self.frame_jog = tk.LabelFrame(self.container, text="Suas Cartas (Clique em uma para jogar)", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), pady=10)
        self.frame_jog.pack(fill="x", padx=20, pady=10)
        
        self.frame_cartas_botoes = tk.Frame(self.frame_jog, bg="#2c3e50")
        self.frame_cartas_botoes.pack()

        # Painel de Comandos (Truco / Nova Mão)
        self.frame_ctrl = tk.Frame(self.container, bg="#2c3e50")
        self.frame_ctrl.pack(pady=10)
        
        self.btn_pedir = tk.Button(self.frame_ctrl, text="Gritar TRUCO!", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), width=15, command=self.gritar_truco, state="disabled")
        self.btn_pedir.grid(row=0, column=0, padx=5)
        
        self.btn_nova_mao = tk.Button(self.frame_ctrl, text="Distribuir Mão", bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), width=15, command=self.nova_mao)
        self.btn_nova_mao.grid(row=0, column=1, padx=5)

        tk.Button(self.container, text="↩ Voltar ao Menu", bg="#7f8c8d", fg="white", font=("Arial", 10, "bold"), command=self.hub.mostrar_menu_principal).pack(pady=10)

    def nova_mao(self):
        if self.tentos_jog >= 12 or self.tentos_robo >= 12:
            self.tentos_jog = 0
            self.tentos_robo = 0
            
        self.baralho = gerar_baralho_truco()
        self.mao_jogador = [self.baralho.pop(), self.baralho.pop(), self.baralho.pop()]
        self.mao_robo = [self.baralho.pop(), self.baralho.pop(), self.baralho.pop()]
        self.vira = self.baralho.pop()
        
        self.valor_rodada = 1
        self.quedas_jog = 0
        self.quedas_robo = 0
        
        self.lbl_vira.config(text=f"🃏 CARTA VIRA: {self.vira['valor']}{self.vira['naipe']}")
        self.lbl_acoes_mesa.config(text=f"Mão iniciada valendo {self.valor_rodada} tento!")
        
        self.btn_nova_mao.config(state="disabled")
        self.btn_pedir.config(state="normal", text="Gritar TRUCO!")
        self.renderizar_cartas()

    def renderizar_cartas(self):
        for w in self.frame_cartas_botoes.winfo_children():
            w.destroy()
            
        for idx, carta in enumerate(self.mao_jogador):
            btn = tk.Button(
                self.frame_cartas_botoes, 
                text=f"{carta['valor']}{carta['naipe']}", 
                font=("Arial", 12, "bold"), bg="#ffffff", fg="#2c3e50",
                width=8, height=2, command=lambda i=idx: self.jogar_carta(i)
            )
            btn.grid(row=0, column=idx, padx=10)

    def calcular_forca(self, carta):
        ordem = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
        naipes = ['♦', '♠', '♥', '♣']
        idx_v = ordem.index(self.vira['valor'])
        manilha = ordem[(idx_v + 1) % len(ordem)]
        if carta['valor'] == manilha:
            return 100 + naipes.index(carta['naipe'])
        return ordem.index(carta['valor'])

    def jogar_carta(self, idx):
        c_jog = self.mao_jogador.pop(idx)
        c_robo = self.mao_robo.pop(0)
        
        f_jog = self.calcular_forca(c_jog)
        f_robo = self.calcular_forca(c_robo)
        
        txt_queda = f"Você jogou: {c_jog['valor']}{c_jog['naipe']}  |  Robô jogou: {c_robo['valor']}{c_robo['naipe']}\n"
        
        if f_jog > f_robo:
            txt_queda += "👉 Você venceu esta queda!"
            self.quedas_jog += 1
        elif f_robo > f_jog:
            txt_queda += "👉 O Robô venceu esta queda!"
            self.quedas_robo += 1
        else:
            txt_queda += "👉 Empachou!"
            self.quedas_jog += 1
            self.quedas_robo += 1
            
        self.lbl_acoes_mesa.config(text=txt_queda)
        self.renderizar_cartas()
        
        if self.quedas_jog >= 2 or self.quedas_robo >= 2 or len(self.mao_jogador) == 0:
            self.finalizar_mao()

    def gritar_truco(self):
        if self.valor_rodada == 1: novo_val = 3; g_nome = "SEIS!"
        elif self.valor_rodada == 3: novo_val = 6; g_nome = "NOVE!"
        elif self.valor_rodada == 6: novo_val = 9; g_nome = "DOZE!"
        else: return
            
        if random.random() < 0.75:
            self.valor_rodada = novo_val
            self.lbl_acoes_mesa.config(text=f"O Robô aceitou! A rodada agora vale {self.valor_rodada} tentos.")
            self.btn_pedir.config(text=f"Pedir {g_nome}")
        else:
            messagebox.showinfo("Fuga", "O Robô correu da rodada! Você levou os pontos.")
            self.tentos_jog += 1 if self.valor_rodada == 1 else self.valor_rodada
            self.fechar_ciclo_mao()

    def finalizar_mao(self):
        if self.quedas_jog > self.quedas_robo:
            self.tentos_jog += self.valor_rodada
            messagebox.showinfo("Mão Finalizada", f"Você ganhou a mão e levou {self.valor_rodada} tento(s)!")
        elif self.quedas_robo > self.quedas_jog:
            self.tentos_robo += self.valor_rodada
            messagebox.showinfo("Mão Finalizada", f"O Robô ganhou a mão e levou {self.valor_rodada} tento(s)!")
        else:
            messagebox.showinfo("Mão Finalizada", "Empate completo na rodada!")
        self.fechar_ciclo_mao()

    def fechar_ciclo_mao(self):
        self.lbl_placar.config(text=f"Você: {self.tentos_jog} tentos | Robô: {self.tentos_robo} tentos")
        for w in self.frame_cartas_botoes.winfo_children(): 
            w.destroy()
        
        if self.tentos_jog >= 12:
            messagebox.showinfo("🏆 VENCEDOR", "Parabéns! Você chegou a 12 pontos e ganhou a partida!")
        elif self.tentos_robo >= 12:
            messagebox.showinfo("🤖 DERROTA", "O Robô chegou a 12 pontos primeiro.")
            
        self.btn_nova_mao.config(state="normal")
        self.btn_pedir.config(state="disabled")
