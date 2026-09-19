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
