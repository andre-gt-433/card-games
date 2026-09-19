import random
from utils import criar_baralho

def preparar_baralho_truco():
    baralho_completo = criar_baralho()
    baralho_truco = [carta for carta in baralho_completo if carta['valor'] not in ['8', '9', '10']]
    random.shuffle(baralho_truco)
    return baralho_truco

def obter_forca_carta(carta, vira):
    ordem_padrao = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
    ordem_naipes = ['♦', '♠', '♥', '♣']
    
    idx_vira = ordem_padrao.index(vira['valor'])
    idx_manilha = (idx_vira + 1) % len(ordem_padrao)
    valor_manilha = ordem_padrao[idx_manilha]
    
    if carta['valor'] == valor_manilha:
        peso_naipe = ordem_naipes.index(carta['naipe'])
        return 100 + peso_naipe
    
    return ordem_padrao.index(carta['valor'])

def exibir_cartas_truco(mao):
    for i, carta in enumerate(mao):
        print(f"[{i + 1}] {carta['valor']}{carta['naipe']}", end="  ")
    print()

def jogar_truco():
    print("\n" + "="*30)
    print("        BEM-VINDO AO TRUCO")
    print("="*30)
    
    tentos_jogador = 0
    tentos_robo = 0
    
    while tentos_jogador < 12 and tentos_robo < 12:
        print(f"\nPlacar Geral -> Você: {tentos_jogador} | Robô: {tentos_robo}")
        print("-" * 40)
        
        baralho = preparar_baralho_truco()
        mao_jogador = [baralho.pop(), baralho.pop(), baralho.pop()]
        mao_robo = [baralho.pop(), baralho.pop(), baralho.pop()]
        
        vira = baralho.pop()
        print(f"🃏 CARTA VIRA NA MESA: {vira['valor']}{vira['naipe']}\n")
        
        quedas_jogador = 0
        quedas_robo = 0
        valor_rodada = 1  
        quem_pode_aumentar = "ambos"
        fugiu = False
        quem_fugiu = ""
        
        # Loop para as 3 quedas da rodada
        for rodada in range(1, 4):
            if fugiu:
                break
                
            print(f"--- {rodada}ª Queda (Valendo {valor_rodada} tentos) ---")
            
            # Chance de o Robô pedir Truco/Aumento antes da rodada começar
            if quem_pode_aumentar in ["ambos", "robo"] and valor_rodada < 12 and random.random() < 0.15:
                proximo_valor = 3 if valor_rodada == 1 else valor_rodada + 3
                nome_grito = "TRUCO" if proximo_valor == 3 else str(proximo_valor)
                print(f"\n🤖 O Robô gritou: \"{nome_grito}!\"")
                
                # Loop de resposta interativa (Aceitar, Fugir ou Retrucar)
                while True:
                    texto_opcao_6 = ""
                    valor_retruco = 6 if proximo_valor == 3 else proximo_valor + 3
                    if valor_retruco <= 12:
                        texto_opcao_6 = f" ou [R] pedir {valor_retruco}"
                        
                    resposta = input(f"O Robô quer {proximo_valor}! [A]ceitar, [F]ugir{texto_opcao_6}? ").strip().upper()
                    
                    if resposta == 'A':
                        valor_rodada = proximo_valor
                        quem_pode_aumentar = "jogador"
                        print(f"🤠 Você aceitou! A rodada agora vale {valor_rodada} tentos.\n")
                        break
                    elif resposta == 'F':
                        print("🏳️ Você aceitou a derrota nesta mão e fugiu.")
                        fugiu = True
                        quem_fugiu = "jogador"
                        break
                    elif resposta == 'R' and texto_opcao_6 != "":
                        print(f"\n🤠 Você contra-atacou e gritou: \"{valor_retruco}!\"")
                        # Decisão do robô para o seu contra-ataque (80% aceita, 20% foge)
                        if random.random() < 0.8:
                            valor_rodada = valor_retruco
                            quem_pode_aumentar = "robo"
                            print(f"🤖 O Robô aceitou o {valor_rodada}! O jogo segue valendo mais.\n")
                            break
                        else:
                            print("🤖 O Robô correu do seu aumento!")
                            fugiu = True
                            quem_fugiu = "robo"
                            break
                    else:
                        print("Opção inválida! Escolha uma das letras indicadas.")
                
                if fugiu:
                    break

            print("Suas cartas disponíveis:")
            exibir_cartas_truco(mao_jogador)
            
            # Menu de Ação do Jogador para a sua jogada normal
            while True:
                texto_truco = ""
                if quem_pode_aumentar in ["ambos", "jogador"] and valor_rodada < 12:
                    proximo_valor = 3 if valor_rodada == 1 else valor_rodada + 3
                    nome_grito = "TRUCO" if proximo_valor == 3 else str(proximo_valor)
                    texto_truco = f" ou [T] pedir {nome_grito}"
                    
                escolha_acao = input(f"Escolha o número da carta{texto_truco}: ").strip().upper()
                
                if escolha_acao == 'T' and texto_truco != "":
                    proximo_valor = 3 if valor_rodada == 1 else valor_rodada + 3
                    nome_grito = "TRUCO" if proximo_valor == 3 else str(proximo_valor)
                    print(f"\n🤠 Você gritou: \"{nome_grito}!\"")
                    
                    # Decisão do robô (75% aceita, 15% corre, 10% pede o próximo aumento se puder)
                    decisao_robo = random.random()
                    
                    if decisao_robo < 0.75:
                        valor_rodada = proximo_valor
                        quem_pode_aumentar = "robo"
                        print(f"🤖 O Robô disse: \"Caiu!\" A rodada agora vale {valor_rodada} tentos.\n")
                        continue
                    elif decisao_robo < 0.90 or proximo_valor >= 12:
                        print("🤖 O Robô correu da mão!")
                        fugiu = True
                        quem_fugiu = "robo"
                        break
                    else:
                        # Robô retruca pedindo 6, 9 ou 12
                        valor_retruco = 6 if proximo_valor == 3 else proximo_valor + 3
                        print(f"🤖 O Robô retrucou e gritou: \"{valor_retruco}!\"")
                        resp_jog = input(f"Você aceita ir para {valor_retruco}? [A]ceitar ou [F]ugir: ").strip().upper()
                        if resp_jog == 'A':
                            valor_rodada = valor_retruco
                            quem_pode_aumentar = "jogador"
                            print(f"🤠 Você aceitou o desafio! Valendo {valor_rodada} tentos.\n")
                            continue
                        else:
                            print("🏳️ Você correu do retruco do robô.")
                            fugiu = True
                            quem_fugiu = "jogador"
                            break
                
                try:
                    num_carta = int(escolha_acao) - 1
                    if 0 <= num_carta < len(mao_jogador):
                        carta_jogador = mao_jogador.pop(num_carta)
                        break
                    else:
                        print("Escolha um número válido de carta.")
                except ValueError:
                    print("Comando inválido! Digite o número da carta.")
            
            if fugiu:
                break
                
            # Escolha do Robô
            carta_robo = mao_robo.pop(0)
            
            print(f"\nVocê jogou: {carta_jogador['valor']}{carta_jogador['naipe']}")
            print(f"O Robô jogou: {carta_robo['valor']}{carta_robo['naipe']}")
            
            forca_jog = obter_forca_carta(carta_jogador, vira)
            forca_rob = obter_forca_carta(carta_robo, vira)
            
            if forca_jog > forca_rob:
                print("👉 Você ganhou esta queda!\n")
                quedas_jogador += 1
            elif forca_rob > forca_jog:
                print("👉 O Robô ganhou esta queda!\n")
                quedas_robo += 1
            else:
                print("👉 Empachou (empate)!\n")
                quedas_jogador += 1
                quedas_robo += 1
                
            if quedas_jogador >= 2 or quedas_robo >= 2:
                break
                
        # Contabilização de pontos pós-mão
        if fugiu:
            if quem_fugiu == "robo":
                print(f"🎉 O Robô fugiu. Você ganhou {valor_rodada} tento(s)!")
                tentos_jogador += valor_rodada
            else:
                print(f"🤖 Você fugiu. O Robô ganhou {valor_rodada} tento(s)!")
                tentos_robo += valor_rodada
        else:
            if quedas_jogador > quedas_robo:
                print(f"🎉 Você ganhou a mão e levou {valor_rodada} tento(s)!")
                tentos_jogador += valor_rodada
            elif quedas_robo > quedas_jogador:
                print(f"🤖 O Robô ganhou a mão e levou {valor_rodada} tento(s)!")
                tentos_robo += valor_rodada
            else:
                print("🤝 Empate geral na mão! Ninguém pontua.")
            
        if tentos_jogador >= 12:
            print("\n🏆 PARABÉNS! Você atingiu 12 tentos e venceu a partida de Truco!")
        elif tentos_robo >= 12:
            print("\n🃏 Fim de jogo! O Robô atingiu 12 tentos e venceu.")
            
    input("\nPressione Enter para voltar ao menu principal...")
