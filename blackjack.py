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

def jogar_blackjack(saldo_atual):
    print("\n" + "="*30)
    print("      BEM-VINDO AO BLACKJACK")
    print("="*30)
    print(f"Seu saldo atual: ${saldo_atual}")
    
    if saldo_atual <= 0:
        print("\nVocê está sem fichas! Vá ao menu principal para recarregar.")
        input("\nPressione Enter para voltar ao menu...")
        return saldo_atual

    # Sistema de Apostas com validação rigorosa
    while True:
        try:
            aposta = int(input(f"Quanto deseja apostar? (1 - {saldo_atual}): "))
            if 1 <= aposta <= saldo_atual:
                break
            else:
                print(f"Valor inválido. Você deve apostar entre 1 e {saldo_atual}.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

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
            print("Blackjack! Você atingir 21!")
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
    
    # Processamento do Resultado e Atualização do Saldo
    if pontos_jogador > 21:
        print(f"\nVocê perdeu sua aposta de ${aposta}.")
        saldo_atual -= aposta
    else:
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
            print(f"A banca estourou! Você venceu e ganhou ${aposta}! 🎉")
            saldo_atual += aposta
        elif pontos_jogador > pontos_banca:
            print(f"Você venceu o Dealer! Ganhou ${aposta}! 🏆")
            saldo_atual += aposta
        elif pontos_jogador < pontos_banca:
            print(f"A banca venceu. Você perdeu ${aposta}. 🃏")
            saldo_atual -= aposta
        else:
            print("Empate! Você recebe sua aposta de volta. 🤝")
            
    print(f"\nNovo Saldo: ${saldo_atual}")
    input("\nPressione Enter para voltar ao menu principal...")
    return saldo_atual
