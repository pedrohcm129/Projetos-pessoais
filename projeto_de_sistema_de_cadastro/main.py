import lib_menu_principal
import lib_arquivo
from os import system
lista_cabecalho = ['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema']
while True:
    system('cls')
    lib_menu_principal.cabecalho('MENU PRINCIPAL', lista_cabecalho, True)
    while True:
        response = str(input(f'\033[1;32mSua opção: \033[m'))
        if response in '123' and response.isnumeric():
            break
        else:
            print('\033[31mTENTE NOVAMENTE\033[m')
    if not lib_arquivo.vericar_arquivo():
        arquivo = open('projeto_de_sistema_de_cadastro/dados1.txt', 'a')
        arquivo.close()
    system('cls')
    validador = lib_arquivo.opcao_arquivo(response)
    if validador:
        break
