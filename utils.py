import random

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = []
    
    for naipe in naipes:
        for valor in valores:
            baralho.append({'valor': valor, 'naipe': naipe})
            
    random.shuffle(baralho)
    return baralho

def gerar_baralho_truco():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
    baralho = [{'valor': v, 'naipe': n} for n in naipes for v in valores]
    random.shuffle(baralho)
    return baralho

def gerar_baralho_uno():
    cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo']
    valores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Bloqueio', 'Inverte', '+2']
    baralho = [{'cor': c, 'valor': v} for c in cores for v in valores]
    random.shuffle(baralho)
    return baralho
