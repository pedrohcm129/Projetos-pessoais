def cabecalho(nome=str, menu=list, verificador_de_opcao=False):
    print('-' * 50)
    print(f'{nome:^50}')
    print('-' * 50)
    if verificador_de_opcao:
        for c in range(len(menu)):
            print(f'\033[1;33m{c + 1}\033[m - \033[34m{menu[c]}\033[m')
        print('-' * 50)