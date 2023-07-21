menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3


while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do deposito'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito R$ {valor:.2f}\n'
        else:
            print('O valor digitado não é valido')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques= numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou, você esta sem saldo')
        elif excedeu_limite:
            print('Operação falhou! Você excedeu o valor limite de saque por dia')
        elif excedeu_saques:
            print('Operação falhou! Você excedeu a quantidade de saques por dia ')
        elif valor > 0:
            saldo -= valor
            extrato += f'saque R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! valor informado invalido')
    
    elif opcao == 'e':
        print('\n==============EXTRATO============')
        print('Não houve movimentações bancarias'if not extrato else extrato)
        print(f'\nSaldo bancario R$ {saldo:.2f}')
        print('=================================')
    
    elif opcao == 'x':
        break

    else:
        print('Opção invalida')

