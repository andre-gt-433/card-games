import random
from utils import criar_baralho

def preparar_baralho_truco():
    baralho_completo = criar_baralho()
    baralho_truco = [carta for carta in baralho_completo if carta['valor'] not in ['8', '9', '10']]
    random.shuffle(baralho_truco)
    return baralho_truco

def obter_forca_carta(carta, vira):
    # Ordem de força padrão do Truco (do menor para o maior)
    ordem_padrao = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
    ordem_naipes = ['♦', '♠', '♥', '♣'] # Ouro, Espadas, Copas, Paus
    
    # Determina qual valor é a manilha baseada no Vira
    idx_vira = ordem_padrao.index(vira['valor'])
    idx_manilha = (idx_vira + 1) % len(ordem_padrao)
    valor_manilha = ordem_padrao[idx_manilha]
    
    # Se for manilha, ganha um peso extra muito alto + bônus do naipe
    if carta['valor'] == valor_manilha:
        peso_naipe = ordem_naipes.index(carta['naipe'])
        return 100 + peso_naipe
    
    # Se for carta comum, retorna o índice da ordem padrão
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
        
        # Loop para as 3 quedas da rodada (Melhor de 3)
        for rodada in range(1, 4):
            print(f"--- {rodada}ª Queda ---")
            print("Suas cartas disponíveis:")
            exibir_cartas_truco(mao_jogador)
            
            # Escolha do Jogador com validação de entrada
            while True:
                try:
                    escolha = int(input(f"Escolha uma carta para jogar (1-{len(mao_jogador)}): ")) - 1
                    if 0 <= escolha < len(mao_jogador):
                        carta_jogador = mao_jogador.pop(escolha)
                        break
                    else:
                        print("Escolha uma carta válida da lista.")
                except ValueError:
                    print("Por favor, digite um número.")
            
            # Escolha simples do Robô (ele sempre joga a primeira carta da mão dele)
            carta_robo = mao_robo.pop(0)
            
            print(f"\nVocê jogou: {carta_jogador['valor']}{carta_jogador['naipe']}")
            print(f"O Robô jogou: {carta_robo['valor']}{carta_robo['naipe']}")
            
            # Calcula e compara as forças
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
                
            # Verifica se alguém já ganhou a melhor de 3 imediatamente
            if quedas_jogador >= 2 or quedas_robo >= 2:
                break
                
        # Atribuição dos tentos (pontos) após as quedas
        if quedas_jogador > quedas_robo:
            print("🎉 Você ganhou a mão e levou 2 tentos!")
            tentos_jogador += 2
        elif quedas_robo > quedas_jogador:
            print("🤖 O Robô ganhou a mão e levou 2 tentos!")
            tentos_robo += 2
        else:
            print("🤝 Empate geral na mão! Ninguém pontua.")
            
        if tentos_jogador >= 12:
            print("\n🏆 PARABÉNS! Você atingiu 12 tentos e venceu a partida de Truco!")
        elif tentos_robo >= 12:
            print("\n🃏 Fim de jogo! O Robô atingiu 12 tentos e venceu.")
            
    input("\nPressione Enter para voltar ao menu principal...")
