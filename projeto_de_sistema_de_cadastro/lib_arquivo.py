def vericar_arquivo():
    try:
        open('projeto_de_sistema_de_cadastro/dados1.txt', 'a')

    except FileNotFoundError:
        return False
    else:
        return True


def opcao_arquivo(opcao=str):
    from lib_menu_principal import cabecalho
    from time import sleep
    if opcao == '1':
        cabecalho('PESSOAS CADASTRADAS')
        with open('projeto_de_sistema_de_cadastro/dados1.txt', 'r') as arquivo:
            print(f'\033[1;37m{"Nome":<25}{"Idade":<13}{"CPF"}\033[m')
            for linha in arquivo:
                linha = linha.split('-')
                linha[2] = linha[2].replace('\n', '')
                print(f'{linha[0]:<25}{linha[1]:<13}{linha[2]}')
        print('-' * 50)
        while True:
            enter = str(input('\'Enter\' para voltar ao menu: '))
            if enter == '':
                break
            else:
                print(f'\033[1;31mAPENAS ENTER\033[m')
    elif opcao == '2':
        cabecalho('NOVO CADASTRO')
        with open('projeto_de_sistema_de_cadastro/dados1.txt', 'a') as arquivo:
            # Validador de CPF
            while True:
                cpf = str(input('CPF: '))
                if len(cpf) == 11 and cpf.isnumeric():
                    cont = 0
                    for c in range(10, 1, -1):
                        primeiro_verificador += c * (int(cpf[cont]))
                        cont += 1
                    cont = 0
                    for c in range(11, 1, -1):
                        segundo_verificador += c * (int(cpf[cont]))
                        cont += 1
                    if primeiro_verificador * 10 % 11 == cpf[10] and segundo_verificador * 10 % 11 == cpf[11]:
                        break
                else:
                    print(f'\033[1;31mCPF INVÁLIDO...TENTE NOVAMENTE\033[m')
            # Escrição dos dados do cliente no arquivo txt
            arquivo.write(f'{str(input("Nome: ")).strip()}-{int(input("Idade: "))}-{cpf}\n')
        print(f'\033[1;37m{"NOVO CADASTRO FEITO COM SUCESSO":^50}\033[m')
        sleep(0.7)
    else:
        cabecalho(f'\033[1;37m{"SAINDO DO SISTEMA":^50}\033[m')
        return True