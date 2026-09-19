import sys
from blackjack import jogar_blackjack

def exibir_menu():
    while True:
        print("\n" + "="*35)
        print("      HUB DE JOGOS DE CARTAS")
        print("="*35)
        print("1. Jogar Blackjack (21)")
        print("2. Jogar Truco (Em desenvolvimento)")
        print("3. Jogar Uno (Em desenvolvimento)")
        print("4. Sair do Programa")
        print("="*35)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == '1':
            jogar_blackjack()
        elif opcao == '2':
            print("\n[Aviso] O Truco estará disponível em breve!")
            input("Pressione Enter para continuar...")
        elif opcao == '3':
            print("\n[Aviso] O Uno estará disponível em breve!")
            input("Pressione Enter para continuar...")
        elif opcao == '4':
            print("\nObrigado por jogar! Até logo.")
            sys.exit()
        else:
            print("\nOpção inválida! Digite um número de 1 a 4.")

if __name__ == "__main__":
    exibir_menu()
