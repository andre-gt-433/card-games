from utils import criar_baralho

def calcular_pontuacao(mao):
    pontos = 0
    ases = 0
    
    for carta in mao:
        valor = carta['valor']
        if valor in ['J', 'Q', 'K']:
            pontos += 10
        elif valor == 'A':
            pontos += 11
            ases += 1
        else:
            pontos += int(valor)
            
    while pontos > 21 and ases > 0:
        pontos -= 10
        ases -= 1
        
    return pontos

def exibir_mao(jogador, mao, esconder_primeira=False):
    print(f"\nMão do {jogador}:")
    for i, carta in enumerate(mao):
        if i == 0 and esconder_primeira:
            print("[Carta Oculta]")
        else:
            print(f"{carta['valor']}{carta['naipe']}", end=" ")
    print()

def jogar_blackjack():
    print("\n" + "="*30)
    print("      BEM-VINDO AO BLACKJACK")
    print("="*30)
    
    baralho = criar_baralho()
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_banca = [baralho.pop(), baralho.pop()]
    
    # Turno do Jogador
    while True:
        exibir_mao("Jogador", mao_jogador)
        exibir_mao("Dealer (Banca)", mao_banca, esconder_primeira=True)
        
        pontos_jogador = calcular_pontuacao(mao_jogador)
        print(f"Sua pontuação atual: {pontos_jogador}")
        
        if pontos_jogador == 21:
            print("Blackjack! Você atingiu 21!")
            break
        elif pontos_jogador > 21:
            print("Você estourou os 21 pontos! Fim de jogo.")
            break
            
        escolha = input("\nVocê quer [C]omprar outra carta ou [P]assar? ").strip().upper()
        
        if escolha == 'C':
            mao_jogador.append(baralho.pop())
        elif escolha == 'P':
            break
        else:
            print("Opção inválida! Escolha C ou P.")

    pontos_jogador = calcular_pontuacao(mao_jogador)
    
    # Turno da Banca (só joga se o jogador não tiver estourado)
    if pontos_jogador <= 21:
        print("\n" + "-"*30)
        print("Turno do Dealer (Banca):")
        print("-"*30)
        
        while calcular_pontuacao(mao_banca) < 17:
            mao_banca.append(baralho.pop())
            
        exibir_mao("Jogador", mao_jogador)
        exibir_mao("Dealer (Banca)", mao_banca)
        
        pontos_banca = calcular_pontuacao(mao_banca)
        print(f"\nPontuação Final - Você: {pontos_jogador} | Banca: {pontos_banca}")
        
        if pontos_banca > 21:
            print("A banca estourou! Você venceu! 🎉")
        elif pontos_jogador > pontos_banca:
            print("Você venceu o Dealer! 🏆")
        elif pontos_jogador < pontos_banca:
            print("A banca venceu. Mais sorte na próxima! 🃏")
        else:
            print("Empate! 🤝")
            
    input("\nPressione Enter para voltar ao menu principal...")
