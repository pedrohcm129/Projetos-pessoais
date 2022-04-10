from ast import Continue
import modulos as md
from os import system
from time import sleep
md.menu_principal(nome='BlackJack')
dict_jogadores = md.jogadores()
baralho = md.baralho()
# Primeira e segunda rodada de cartas automático
for k in dict_jogadores.keys():
    for c in range(0, 2):
        md.jogada(k, dict_jogadores, baralho)
# A partir da segunda rodada...
while True:
    system('cls')
    md.mostrador_placar(dict_jogadores)
    for k in dict_jogadores.keys():
        if md.solicitador_compra_carta(k):
            md.jogada(k, dict_jogadores, baralho)
            system('cls')
            md.mostrador_placar(dict_jogadores)
        else:
            system('cls')
            md.mostrador_placar(dict_jogadores)
            continue
    while True:    
        opcao = str(input('Deseja continuar o jogo?[SIM ou NÃO] '))[0].upper().strip()
        if opcao in 'SN':
            break
        else:
            print('\033[31mTENTE NOVAMENTE\033[m')
    if opcao == 'N':
        vencedor = md.verficador_vencedor(dict_jogadores)
        if vencedor == 'Empate':
            system('cls')
            md.menu_principal(f'{md.cor("azul")}O jogo deu empate!!!{md.cor("branco")}'.upper())
        else:
            system('cls')
            md.menu_principal(nome=f'{md.cor("amarelo")}Parabéns jogador {vencedor}, você venceu!!!!{md.cor("branco")}')
        break
    else:
        continue
    