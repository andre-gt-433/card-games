# 🃏 Hub de Jogos de Cartas Clássicos com Interface Gráfica (GUI)

Este é um projeto desenvolvido em **Python** utilizando a biblioteca **Tkinter** para criar uma interface gráfica completa de usuário. Desenvolvido no **VS Code** e integrado ao **GitHub**, o Hub reúne três jogos clássicos de cartas rodando de forma 100% visual em uma mesma janela dinâmica.

---

## 🚀 Jogos Incluídos (Todos Concluídos)

O projeto gerencia de forma dinâmica a transição entre telas e compartilha um saldo unificado para o jogador:

*   **🎰 Casino Blackjack (21) [Concluído]:** Dispute contra a inteligência da banca (Dealer). Sistema automático de contagem de pontos, regras de "Hit" (Pedir) e "Stand" (Parar), além de apostas fixas que debitam e multiplicam o seu saldo em tempo real.
*   **⚔️ Truco Paulista [Concluído]:** Partidas completas de melhor de três quedas contra o robô com placar até 12 tentos. Sistema de força de cartas regulado, identificação dinâmica da Manilha com base no "Vira" da mesa e botões interativos para gritar e aumentar o valor da rodada (Truco, 6, 9 e 12).
*   **🔥 Uno Colorido [Concluído]:** Descarte suas cartas combinando cor ou valor com o topo da mesa. O jogo possui validação inteligente de movimentos, descarte de cartas especiais (Bloqueio, Inverte e +2) com efeitos aplicados na vez do robô e sistema de compra automatizado.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **Tkinter** (Para o desenvolvimento da Interface Gráfica nativa)
*   **Git & GitHub** (Para controle de versão)
*   **VS Code** (Ambiente de desenvolvimento)

---

## 📂 Estrutura Final do Projeto

O repositório está modularizado da seguinte forma para garantir organização e evitar erros de importação:

```text
├── .gitignore          # Arquivos ignorados pelo Git (ex: __pycache__/)
├── README.md           # Documentação completa do projeto
├── app_gui.py          # Arquivo principal (Menu Inicial e gerenciamento de telas/saldo)
├── utils.py            # Engine de criação e distribuição de baralhos aleatórios
├── tela_blackjack.py   # Interface e lógica completa do Blackjack (21)
├── tela_truco.py       # Interface e lógica completa do Truco Paulista
└── tela_uno.py         # Interface e lógica completa do Uno Colorido
```

---

## 🎮 Como Executar o Jogo

### Pré-requisitos
Certifique-se de ter o [Python](https://python.org) instalado em sua máquina. Como o `tkinter` é uma biblioteca nativa do Python, nenhuma instalação externa pelo `pip` é necessária.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd NOME_DO_REPOSITORIO
   ```

3. **Execute o Hub Gráfico:**
   ```bash
   python app_gui.py
   ```

---

## 🤝 Aprendizados Consolidados

*   Manipulação avançada de layouts, contêineres (`Frames`, `LabelFrames`) e widgets do Tkinter.
*   Gestão de estados dinâmicos (passagem de variáveis de saldo e pontuação entre arquivos).
*   Modularização de código em Python utilizando imports relativos.
*   Controle de fluxo assíncrono básico com o uso de temporizadores (`.after`) para simular os turnos do robô.

---

Desenvolvido com 🧠, dedicação e ☕ por André Gimenez (https://github.com).
