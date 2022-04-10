def linha():
    """
    linha --> Imprime um linha
    return: sem retorno
    """
    print('-' * 50)


def cor(nome_cor=str):
    """
    cor --> Função para mudar de cor uma string
    pram nome_cor: Nome da cor
    return: uma string com o código da cor
    """
    dict_cor = {'vermelho': '\033[31m', 'verde': '\033[32m ', 
              'amarelo': '\033[33m', 'azul': '\033[34m', 
              'branco': '\033[m', 'negrito': '\033[1m', 
              'cinza': '\033[37m'}
    return dict_cor[nome_cor]


def menu_principal(nome='', menu=[], verificador_de_opcao=False):
    """
    menu_principal --> Constroi a parte visual de um menu
    param nome: Nome do menu
    param menu: Opções que vão ser colocadas no menu
    param verificador_de_opcao: Verificador para se vai ser impreço ou não as opções
    return: sem retorno
    """
    print('-' * 50)
    print(f'{nome:^50}')
    print('-' * 50)
    if verificador_de_opcao:
        for c in range(len(menu)):
            print(f'\033[1;33m{c + 1}\033[m - \033[34m{menu[c]}\033[m')
        print('-' * 50)


def jogadores():
    """
    jogadores --> Recebe e guarda a quantidade e nome dos jogadores.
    return: dict_jogadores ---> Dicionário com o nome dos jogadores correspondendos as keys
    """
    dict_jogadores = {}
    quantidade_jogadores = int(input('\033[34mQuantos jogadores: \033[m'))
    for c in range(quantidade_jogadores):
        dict_jogadores[str(input(f'\033[33mNome do {c + 1}°: \033[m'))] = ['', 0]
    return dict_jogadores


def baralho():
    """
    baralho --> Cria um baralho completo
    return: Lista com as cartas do baralho
    """
    lista_baralho = []
    for c in range(4):
        lista_baralho.append('A')
        lista_baralho.append('J')
        lista_baralho.append('Q')
        lista_baralho.append('K')
        for k in range(2, 11):
            lista_baralho.append(f'{k}')
    return lista_baralho


def somador(jogador, dicionario_jogadores, carta_sorteada):
    """
    somador --> Soma a carta sorteada na função jogada ao valor no dict principal
    param jogador: Nome do jogador
    param dicionario_jogadores: Dicionário principal
    param carta_sorteada: Carta sorteada na função 'jogada'
    """
    dicionario_jogadores[jogador][0] += carta_sorteada

def jogada(jogador=str, dicionario_jogadores=dict, baralho_completo=dict):
    from random import choice
    carta_sorteada = choice(baralho_completo)
    baralho_completo.remove(carta_sorteada)
    return somador(jogador, dicionario_jogadores, carta_sorteada)


def solicitador_compra_carta(nome):  
    try:
        opcao = str(input(f'{nome}, deseja comprar mais uma carta?[SIM/NÃO] '))[0].upper().split()
    except (TypeError, ValueError):
        print(f'{cor("vermelho")}TENTE NOVAMENTE{cor("branco")}')
    else:
        if opcao[0] == 'S':
            return True
        else:
            return False


def mostrador_placar(dicionario_jogadores):
    menu_principal('PARTIDA EM ANDAMENTO')
    print('\033[32;1m', end='')
    print(f'{"Jogador":<25}{"Cartas":<21}{"Soma"}{cor("branco")}')
    lista_valores_vencedores_blackjack = ['KA', 'JA', 'QA', 'AK', 'AQ', 'AJ']
    for k, v in dicionario_jogadores.items():
        soma = 0
        if v[0] in lista_valores_vencedores_blackjack:
            soma = 21
        else:   
            for c in v[0]:
                if c in 'JQK1':
                    soma += 10
                elif c == 'A':
                    soma += 1
                else:
                    soma += int(c)
        dicionario_jogadores[k][1] = soma
        print(f'{k:<25}{str(v[0]):<21}{soma}')
    linha()
    return dicionario_jogadores


def verficador_vencedor(dicionario_jogadores=dict):
    valor_vencedor = 0
    nome_vencedor = ''
    lista_valores_vencedores_blackjack = ['KA', 'JA', 'QA', 'AK', 'AQ', 'AJ']   
    for k, v in dicionario_jogadores.items():
        if v[0] in lista_valores_vencedores_blackjack:
            return k
        else:
            if v[1] <= 21:   
                if valor_vencedor == 0:
                    valor_vencedor = v[1]
                    nome_vencedor = k
                else:
                    if valor_vencedor < v[1] <= 21:
                        valor_vencedor = v[1]
                        nome_vencedor = k
                    elif valor_vencedor == v[1]:
                        nome_vencedor = 'Empate'
    return nome_vencedor