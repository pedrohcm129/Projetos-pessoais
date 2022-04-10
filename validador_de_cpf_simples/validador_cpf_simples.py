def validar_CPF(valor_cpf = str):
    # Veridicador de quantidade de números no CPF
    if len(valor_cpf) == 11 and valor_cpf.isnumeric():
        # Validação de CPF a partir de seus dígitos verificadores
        primeiroVerificador = 0    
        segundoVerificador = 0
        for v in range(10, 1, -1):
            primeiroVerificador += int(valor_cpf[10 - v]) * v
        for v in range(11, 1, -1):
            segundoVerificador += int(valor_cpf[11 - v]) * v
        if primeiroVerificador * 10 % 11 == int(valor_cpf[9]) and segundoVerificador * 10 % 11 == int(valor_cpf[10]):
            return True
        else:
            return False
    else:
        return False

# Main
if validar_CPF(str(input('CPF: '))):
    print("\nCPF válido.")
else:
    print("\nCPF inválido.")