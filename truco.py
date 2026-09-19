import random
from utils import criar_baralho

def preparar_baralho_truco():
    # O Truco tradicional usa o baralho "limpo" (sem 8, 9 e 10)
    baralho_completo = criar_baralho()
    baralho_truco = [carta for carta in baralho_completo if carta['valor'] not in ['8', '9', '10']]
    # Re-embaralha após limpar
    random.shuffle(baralho_truco)
    return baralho_truco

def exibir_cartas_truco(jogador, mao):
    print(f"\nSua mão ({jogador}):")
    for i, carta in enumerate(mao):
        print(f"[{i + 1}] {carta['valor']}{carta['naipe']}", end="  ")
    print()

def jogar_truco():
    print("\n" + "="*30)
    print("        BEM-VINDO AO TRUCO")
    print("="*30)
    
    tentos_jogador = 0
    tentos_robo = 0
    
    # O jogo termina quando alguém chega a 12 tentos
    while tentos_jogador < 12 and tentos_robo < 12:
        print(f"\nPlacar Atual -> Você: {tentos_jogador} tentos | Robô: {tentos_robo} tentos")
        print("-" * 40)
        
        baralho = preparar_baralho_truco()
        
        # Distribui 3 cartas para cada
        mao_jogador = [baralho.pop(), baralho.pop(), baralho.pop()]
        mao_robo = [baralho.pop(), baralho.pop(), baralho.pop()]
        
        # Define o Vira
        vira = baralho.pop()
        print(f"🃏 CARTA VIRA NA MESA: {vira['valor']}{vira['naipe']}")
        
        exibir_cartas_truco("Jogador", mao_jogador)
        
        # Simulação temporária de uma rodada simples (passo inicial)
        print("\n[Mecanismo de queda em desenvolvimento]")
        print("Para este teste, quem tiver a maior primeira carta ganha 2 tentos!")
        
        input("\nPressione Enter para simular a rodada...")
        
        # Simulação rápida apenas para testar a estrutura do placar loop
        if random.choice([True, False]):
            print("\n🎉 Você ganhou a mão!")
            tentos_jogador += 2
        else:
            print("\n🤖 O Robô ganhou a mão!")
            tentos_robo += 2
            
        if tentos_jogador >= 12:
            print("\n🏆 PARABÉNS! Você venceu a partida de Truco!")
        elif tentos_robo >= 12:
            print("\n🃏 Fim de jogo! O Robô venceu a partida.")
            
    input("\nPressione Enter para voltar ao menu principal...")
