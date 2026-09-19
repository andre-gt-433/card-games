import random

def criar_baralho_uno():
    cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo']
    valores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Bloqueio', 'Inverte', '+2']
    baralho = []
    
    for cor in cores:
        for valor in valores:
            baralho.append({'cor': cor, 'valor': valor})
            # No Uno real existem duas de cada (exceto o 0), mas uma de cada simplifica e funciona muito bem no terminal
    
    random.shuffle(baralho)
    return baralho

def exibir_mao_uno(mao):
    for i, carta in enumerate(mao):
        print(f"[{i + 1}] {carta['cor']} {carta['valor']}", end="  |  ")
    print()

def jogar_uno():
    print("\n" + "="*30)
    print("         BEM-VINDO AO UNO")
    print("="*30)
    
    baralho = criar_baralho_uno()
    
    # Distribui 7 cartas para cada jogador
    mao_jogador = [baralho.pop() for _ in range(7)]
    mao_robo = [baralho.pop() for _ in range(7)]
    
    # Define a primeira carta da mesa (garantindo que seja um número)
    while True:
        topo_descarte = baralho.pop()
        if topo_descarte['valor'] not in ['Bloqueio', 'Inverte', '+2']:
            break
        baralho.insert(0, topo_descarte) # Devolve se for especial e tenta de novo
        
    turno = "jogador"
    
    # O jogo roda enquanto ninguém esvaziar a mão
    while len(mao_jogador) > 0 and len(mao_robo) > 0:
        print(f"\n--------------------------------------------------")
        print(f"🔥 CARTA NO TOPO DO DESCARTE: {topo_descarte['cor']} {topo_descarte['valor']}")
        print(f"Cartas do Robô: {len(mao_robo)}")
        print(f"--------------------------------------------------")
        
        if turno == "jogador":
            print("\nSua mão atual:")
            exibir_mao_uno(mao_jogador)
            
            # Filtra quais cartas você PODE jogar na rodada
            cartas_validas = []
            for i, carta in enumerate(mao_jogador):
                if carta['cor'] == topo_descarte['cor'] or carta['valor'] == topo_descarte['valor']:
                    cartas_validas.append(i)
            
            # Se não tiver nenhuma carta válida, é obrigado a comprar
            if not cartas_validas:
                print("\n[Aviso] Você não tem cartas válidas para jogar!")
                input("Pressione Enter para comprar uma carta...")
                nova_carta = baralho.pop()
                mao_jogador.append(nova_carta)
                print(f"Você comprou: {nova_carta['cor']} {nova_carta['valor']}")
                
                # Checa se a carta comprada pode ser jogada na hora
                if nova_carta['cor'] == topo_descarte['cor'] or nova_carta['valor'] == topo_descarte['valor']:
                    opcao_jogar = input("Você pode jogar essa carta que comprou! Quer jogar? [S/N]: ").strip().upper()
                    if opcao_jogar == 'S':
                        topo_descarte = mao_jogador.pop()
                        print(f"Você jogou {topo_descarte['cor']} {topo_descarte['valor']}!")
                turno = "robo"
                continue
                
            # Loop de escolha de jogada do jogador
            while True:
                try:
                    escolha = input("Escolha o número da carta para jogar (ou digite 'C' para comprar mesmo assim): ").strip().upper()
                    
                    if escolha == 'C':
                        mao_jogador.append(baralho.pop())
                        print("Você escolheu comprar uma carta.")
                        turno = "robo"
                        break
                        
                    num_carta = int(escolha) - 1
                    if 0 <= num_carta < len(mao_jogador):
                        carta_escolhida = mao_jogador[num_carta]
                        
                        # Validação de correspondência de Cor ou Valor
                        if carta_escolhida['cor'] == topo_descarte['cor'] or carta_escolhida['valor'] == topo_descarte['valor']:
                            topo_descarte = mao_jogador.pop(num_carta)
                            print(f"\nVocê jogou: {topo_descarte['cor']} {topo_descarte['valor']}")
                            
                            # Efeito das cartas especiais aplicadas ao robô
                            if topo_descarte['valor'] in ['Bloqueio', 'Inverte']:
                                print("🚫 Você travou o turno do robô! Joga novamente.")
                                turno = "jogador"
                            elif topo_descarte['valor'] == '+2':
                                print("💥 O robô comprou +2 cartas e perdeu o turno!")
                                mao_robo.append(baralho.pop())
                                mao_robo.append(baralho.pop())
                                turno = "jogador"
                            else:
                                turno = "robo"
                            break
                        else:
                            print("Movimento inválido! A carta precisa ter a mesma Cor ou o mesmo Valor.")
                    else:
                        print("Escolha um número válido da lista.")
                except ValueError:
                    print("Digite um comando válido (Número da carta ou 'C').")
                    
            if len(mao_jogador) == 1:
                print("\n🗣️ VOCÊ GRITOU: \"UNO!!!\"")
                
        else:
            # TURNO DO ROBÔ (Inteligência Artificial Simples)
            print("\n🤖 Turno do Robô...")
            input("Pressione Enter para ver a jogada do robô...")
            
            jogou = False
            for i, carta in enumerate(mao_robo):
                if carta['cor'] == topo_descarte['cor'] or carta['valor'] == topo_descarte['valor']:
                    topo_descarte = mao_robo.pop(i)
                    print(f"🤖 O Robô jogou: {topo_descarte['cor']} {topo_descarte['valor']}")
                    
                    if topo_descarte['valor'] in ['Bloqueio', 'Inverte']:
                        print("🚫 O Robô te travou! Ele joga novamente.")
                        turno = "robo"
                    elif topo_descarte['valor'] == '+2':
                        print("💥 Você comprou +2 cartas e perdeu o turno!")
                        mao_jogador.append(baralho.pop())
                        mao_jogador.append(baralho.pop())
                        turno = "robo"
                    else:
                        turno = "jogador"
                    jogou = True
                    break
                    
            if not jogou:
                print("🤖 O Robô não tinha cartas válidas e comprou uma.")
                mao_robo.append(baralho.pop())
                turno = "jogador"
                
            if len(mao_robo) == 1:
                print("\n🚨 O Robô gritou: \"UNO!!!\"")

    # Fim de Jogo
    if len(mao_jogador) == 0:
        print("\n🏆 PARABÉNS! Você descartou todas as cartas e venceu o UNO!")
    else:
        print("\n🃏 Fim de jogo! O Robô descartou tudo primeiro e venceu o UNO.")
        
    input("\nPressione Enter para voltar ao menu principal...")
