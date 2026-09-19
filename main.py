import sys
from blackjack import jogar_blackjack
from truco import jogar_truco
from uno import jogar_uno  # <-- NOVA IMPORTAÇÃO

def exibir_menu():
    saldo_jogador = 500
    
    while True:
        print("\n" + "="*35)
        print("      HUB DE JOGOS DE CARTAS")
        print("="*35)
        print(f" Seu Saldo Atual: ${saldo_jogador}")
        print("-"*35)
        print("1. Jogar Blackjack (21)")
        print("2. Jogar Truco")
        print("3. Jogar Uno")  # <-- ATUALIZADO
        print("4. Recarregar Fichas (+$500)")
        print("5. Sair do Programa")
        print("="*35)
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == '1':
            saldo_jogador = jogar_blackjack(saldo_jogador)
        elif opcao == '2':
            jogar_truco()
        elif opcao == '3':
            jogar_uno()  # <-- CHAMA O UNO AQUI
        elif opcao == '4':
            saldo_jogador += 500
            print(f"\n$500 fichas adicionadas! Novo saldo: ${saldo_jogador}")
            input("Pressione Enter para continuar...")
        elif opcao == '5':
            print("\nObrigado por jogar! Até logo.")
            sys.exit()
        else:
            print("\nOpção inválida! Digite um número de 1 a 5.")

if __name__ == "__main__":
    exibir_menu()
