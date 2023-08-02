from datetime import datetime
from time import sleep

data_hora_do_sistema = datetime.now()
data_formatada = data_hora_do_sistema.strftime("%d/%m/%Y %H:%M:%S")
operacoes_realizadas = []
saldo_em_conta = 0


def leia_int(msg):
    """
    Tenta ler um número inteiro digitado pelo usuário.

    Args:
        msg (str): A mensagem a ser exibida ao solicitar a entrada do usuário.

    Returns:
        int: O número inteiro lido a partir da entrada do usuário.

    Raises:
        ValueError: Se o valor digitado não for um número inteiro válido.
        TypeError: Se ocorrer um erro de tipo ao tentar converter a entrada para um inteiro.
        KeyboardInterrupt: Se o usuário interromper a execução da função através de Ctrl+C.

    Example:
        >>> leia_int("Digite um número inteiro: ")
        Digite um número inteiro: abc
        ERRO. Digite um numero inteiro valido!
        Digite um número inteiro: 10
        10
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO. Digite um numero inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[32mO usuario preferiu não digitar um valor!\033[m')
            return '→ Nenhum valor foi digitado...'
        else:
            return n


def opcao_saque(valor_do_saque):
    """
    Realiza um saque na conta bancária do usuário, desde que as condições sejam atendidas.

    Args:
        valor_do_saque (int): O valor do saque solicitado pelo usuário.

    Globals:
        saldo_em_conta (int): Variável global que representa o saldo disponível na conta bancária.
        operacoes_realizadas (list): Lista global que armazena as operações realizadas pelo usuário.
    Example:
        >>> saldo_em_conta = 1000.00
        >>> operacoes_realizadas = []
        >>> opcao_saque(300.00)
        Deseja realmente sacar R$: 300.0. 1 = SIM & 2 = NÃO: 1
        Saque de 300.0 realizado com sucesso
    Note:
        Essa função assume que as variáveis globais `saldo_em_conta` e `operacoes_realizadas`
        já foram declaradas e inicializadas corretamente fora do escopo da função.
    """
    global saldo_em_conta
    while True:
        if valor_do_saque <= 0:
            print('Digite um valor valido para saque!!')
        elif valor_do_saque > 500:
            print('Valor limite para saque é de 500 por transação')
        else:
            if len(operacoes_realizadas) == 3:
                print('Limite de saque diario atingido')
                sleep(1)
                print('Finalizando!!')
                sleep(1)
            else:
                if valor_do_saque <= saldo_em_conta:
                    confirma_saque = leia_int(f'Deseja realmente sacar R$: {valor_do_saque:.2f} 1 = SIM & 2 = NÃO: ')
                    if confirma_saque == 1:
                        print(f'Saque de {valor_saque:.2f} realizado com sucesso')
                        saldo_em_conta -= valor_do_saque
                        operacoes_realizadas.append(f'Saque de R${valor_do_saque:.2f} realizado em {data_formatada}')
                        break
                    elif confirma_saque == 2:
                        print('Finalizando!!!')
                        sleep(1)
                        break
                    else:
                        print('Opção invalida. Tente novamente!!')
                else:
                    print('Valor solicitado para saque maior que o saldo disponivel')
                    break


def opcao_deposito(valor_do_deposito):
    """
    Realiza um depósito na conta bancária do usuário, desde que o valor do depósito seja válido.

    Args:
        valor_do_deposito (int): O valor do depósito solicitado pelo usuário.

    Globals:
        saldo_em_conta (int): Variável global que representa o saldo disponível na conta bancária.
    Example:
    >>> saldo_em_conta = 1000.00
    >>> opcao_deposito(200.00)
    Deseja realmente depositar R$: 200.0. 1 = SIM & 2 = NÃO: 1
    Deposito de 200.0 realizado com sucesso. Volte sempre!!

    Note:
        Essa função assume que a variável global `saldo_em_conta` já foi declarada e inicializada
        corretamente fora do escopo da função.
    """
    global saldo_em_conta
    while True:
        if valor_do_deposito <= 0:
            print('Por favor! Digite um valor valido para depositar')
        else:
            confirma_deposito = leia_int(f'Deseja realmente depositar R$: {valor_do_deposito:.2f} 1 = SIM & 2 = NÃO: ')
            if confirma_deposito == 1:
                print(f'Deposito de {valor_do_deposito:.2f} realizado com sucesso. Volte sempre!!')
                saldo_em_conta += valor_do_deposito
                break
            elif confirma_deposito == 2:
                print('Finalizando!!!')
                sleep(1)
                break
            else:
                print('Opção invalida. Tente novamente!!')


def opcao_extrato(periodo=None):
    """
    Exibe o saldo da conta bancária do usuário e, opcionalmente, mostra as operações realizadas em um período.

    Args:
        periodo (str, optional): Período específico do extrato a ser exibido. Padrão é None.

    Globals:
        saldo_em_conta (int): Variável global que representa o saldo disponível na conta bancária.
        operacoes_realizadas (list): Lista global que armazena as operações realizadas pelo usuário.

    Example:
        >>> saldo_em_conta = 1500.0
        >>> operacoes_realizadas = ['Depósito no valor R$100.00 realizado em 2023-08-02',
                                    'Saque no valor R$50.00 realizado em 2023-08-02']
        >>> opcao_extrato()
        O saldo da conta R$: 1500.0
        Depósito no valor R$100.00 realizado em 2023-08-02
        Saque no valor R$50.00 realizado em 2023-08-02

        >>> opcao_extrato(periodo='2023-08-02')
        O saldo da conta R$: 1500.0
        A ser desenvolvido!!

    Note:
        Essa função assume que as variáveis globais `saldo_em_conta` e `operacoes_realizadas`
        já foram declaradas e inicializadas corretamente fora do escopo da função.
        A funcionalidade para exibir as operações do extrato em um período específico ainda não foi implementada.
    """
    print(f'O saldo da conta R$: {saldo_em_conta:.2f}')
    if periodo is None:
        for operacao in operacoes_realizadas:
            print(f'{operacao}')
    else:
        print('A ser desenvolvido!!')


print(f'{"Bem vindo ao banco DIO":=^80}')
print("""
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair""")
while True:
    print('=='*40)
    opcao_escolhida = leia_int('Escolha uma operação: ')
    if opcao_escolhida == 1:
        if saldo_em_conta == 0:
            print('Você não possui saldo disponivel para saque!!!')
        else:
            valor_saque = leia_int(f'O saldo disponivel na conta é {saldo_em_conta:.2f} Digite o valor do saque R$: ')
            opcao_saque(valor_saque)
    elif opcao_escolhida == 2:
        valor_deposito = leia_int('Digite o valor a ser depositado R$: ')
        opcao_deposito(valor_deposito)
    elif opcao_escolhida == 3:
        if len(operacoes_realizadas) == 0:
            sleep(1)
            print('Não fora realizada transação')
        else:
            opcao_extrato()
    elif opcao_escolhida == 0:
        sleep(1)
        print('Você escolheu sair')
        break
    else:
        print('\033[31mNão existe a opção informada! Por favor, tente novamente\033[m')
print('=='*40)
