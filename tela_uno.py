import tkinter as tk
from tkinter import messagebox
from utils import gerar_baralho_uno

class UnoGame:
    def __init__(self, container, hub_instance):
        self.container = container
        self.hub = hub_instance  # Referência ao Hub principal para saldo e menus
        
        self.baralho = []
        self.mao_jogador = []
        self.mao_robo = []
        self.topo = None
        
        self.construir_tela()
        self.iniciar_partida()

    def construir_tela(self):
        tk.Label(self.container, text="🔥 ARENA UNO COLORIDO", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=10)
        
        # Painel central da mesa
        self.frame_mesa = tk.LabelFrame(self.container, text="Mesa do Jogo", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), pady=10)
        self.frame_mesa.pack(fill="x", padx=20, pady=10)
        
        self.lbl_topo = tk.Label(self.frame_mesa, text="", font=("Arial", 14, "bold"), bg="#ffffff", pady=8, width=20)
        self.lbl_topo.pack()
        
        self.lbl_status = tk.Label(self.frame_mesa, text="", font=("Arial", 11), bg="#2c3e50", fg="white")
        self.lbl_status.pack(pady=5)

        # Painel das cartas do jogador
        self.frame_jog = tk.LabelFrame(self.container, text="Seu Baralho (Clique na carta válida para jogar)", bg="#2c3e50", fg="white", font=("Arial", 10, "bold"), pady=10)
        self.frame_jog.pack(fill="x", padx=20, pady=10)
        
        self.frame_botoes = tk.Frame(self.frame_jog, bg="#2c3e50")
        self.frame_botoes.pack(pady=5)

        # Controles extras
        tk.Button(self.container, text="➕ Comprar Carta do Monte", bg="#f1c40f", fg="#2c3e50", font=("Arial", 11, "bold"), command=self.comprar_carta).pack(pady=10)
        tk.Button(self.container, text="↩ Voltar ao Menu", bg="#7f8c8d", fg="white", font=("Arial", 10, "bold"), command=self.hub.mostrar_menu_principal).pack(pady=5)

    def iniciar_partida(self):
        self.baralho = gerar_baralho_uno()
        self.u_mao_jog = [self.baralho.pop() for _ in range(7)]
        self.u_mao_robo = [self.baralho.pop() for _ in range(7)]
        self.topo = self.baralho.pop()
        self.atualizar_tela()

    def atualizar_tela(self):
        hex_cores = {"Vermelho": "#e74c3c", "Azul": "#3498db", "Verde": "#2ecc71", "Amarelo": "#f1c40f"}
        cor_topo = hex_cores.get(self.topo['cor'], "#ffffff")
        fg_cor = "#ffffff" if self.topo['cor'] != "Amarelo" else "#2c3e50"
        
        self.lbl_topo.config(text=f"{self.topo['cor'].upper()} - {self.topo['valor']}", bg=cor_topo, fg=fg_cor)
        self.lbl_status.config(text=f"Robô possui {len(self.u_mao_robo)} cartas  |  Você possui {len(self.u_mao_jog)} cartas.")
        
        for w in self.frame_botoes.winfo_children(): 
            w.destroy()
            
        for idx, c in enumerate(self.u_mao_jog):
            bg_c = hex_cores.get(c['cor'], "#ffffff")
            fg_c = "#ffffff" if c['cor'] != "Amarelo" else "#2c3e50"
            
            btn = tk.Button(
                self.frame_botoes, text=f"{c['valor']}\n{c['cor'][:3]}", 
                bg=bg_c, fg=fg_c, font=("Arial", 9, "bold"), width=6, height=2,
                command=lambda i=idx: self.jogar_carta(i)
            )
            btn.grid(row=0, column=idx, padx=3)

    def jogar_carta(self, idx):
        carta = self.u_mao_jog[idx]
        if carta['cor'] == self.topo['cor'] or carta['valor'] == self.topo['valor']:
            self.topo = self.u_mao_jog.pop(idx)
            self.atualizar_tela()
            
            if len(self.u_mao_jog) == 0:
                messagebox.showinfo("Vitória", "🎉 Você esvaziou a sua mão e ganhou o UNO!")
                self.hub.mostrar_menu_principal()
                return
                
            if self.topo['valor'] in ['Bloqueio', 'Inverte']:
                messagebox.showinfo("Ação", "Carta especial jogada! O robô foi pulado.")
                return
            elif self.topo['valor'] == '+2':
                messagebox.showinfo("Ação", "O Robô comprou +2 cartas e perdeu o turno!")
                self.u_mao_robo.append(self.baralho.pop())
                self.u_mao_robo.append(self.baralho.pop())
                return
                
            self.turno_robo()
        else:
            messagebox.showwarning("Incompatível", "Esta carta não pode ser jogada! Combine cor ou valor.")

    def comprar_carta(self):
        if not self.baralho:
            self.baralho = gerar_baralho_uno()
        nova = self.baralho.pop()
        self.u_mao_jog.append(nova)
        messagebox.showinfo("Compra", f"Você comprou: {nova['cor']} {nova['valor']}")
        self.atualizar_tela()
        self.turno_robo()

    def turnos_robo_delay(self):
        self._processar_turno_robo()

    def turno_robo(self):
        self.container.after(600, self.turnos_robo_delay)

    def _processar_turno_robo(self):
        jogou = False
        for idx, c in enumerate(self.u_mao_robo):
            if c['cor'] == self.topo['cor'] or c['valor'] == self.topo['valor']:
                self.topo = self.u_mao_robo.pop(idx)
                messagebox.showinfo("Robô", f"🤖 O Robô jogou: {self.topo['cor']} {self.topo['valor']}")
                jogou = True
                
                if len(self.u_mao_robo) == 0:
                    messagebox.showinfo("Fim de Jogo", "O Robô venceu o UNO!")
                    self.hub.mostrar_menu_principal()
                    return
                    
                if self.topo['valor'] in ['Bloqueio', 'Inverte']:
                    messagebox.showinfo("Robô", "O Robô te travou com uma carta especial! Ele joga de novo.")
                    self.turno_robo()
                    return
                elif self.topo['valor'] == '+2':
                    messagebox.showinfo("Robô", "O Robô usou +2! Você comprou 2 cartas e perdeu a vez.")
                    self.u_mao_jog.append(self.baralho.pop())
                    self.u_mao_jog.append(self.baralho.pop())
                    self.turno_robo()
                    return
                break
                
        if not jogou:
            if not self.baralho:
                self.baralho = gerar_baralho_uno()
            self.u_mao_robo.append(self.baralho.pop())
            messagebox.showinfo("Robô", "🤖 O Robô não tinha cartas válidas e comprou do monte.")
            
        self.atualizar_tela()
