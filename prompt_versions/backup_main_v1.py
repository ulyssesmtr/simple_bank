class Contas:
    counter = 5000

    def __init__(self):
        self.__numero = Contas.counter
        self.__saldo = 0
        Contas.counter += 1

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def __str__(self):
        return f'Conta número: {self.__numero} - Saldo:{self.__saldo}'


class Banco:

    def __init__(self):
        self.__contas = []

    def criar_conta(self, conta):
        self.__contas.append(conta)
        print(f'A conta de numero {conta.numero} foi criada com saldo {conta.saldo}.')

    @property
    def mostrar_contas(self):
        return self.__contas

    @property
    def mostrar_numero_contas(self):
        return list(map(lambda conta: conta.numero, self.__contas))


def mostrar_saldo(banco):
    try:
        num_conta = int(input('Digite o numero da conta cujo saldo deve ser mostrado: '))
        index = banco.mostrar_numero_contas.index(num_conta)
        conta = banco.mostrar_contas[index]
        print(f'O saldo da conta {num_conta} é {conta.saldo}')
    except ValueError:
        print('Valor inválido para conta.')


def efetuar_deposito(banco):
    try:
        num_conta = int(input('Digite o número da conta em que será feito o deposito: '))
        valor = int(input('Digite o valor a ser depositado: '))
        index = banco.mostrar_numero_contas.index(num_conta)
        banco.mostrar_contas[index].depositar(valor)
    except ValueError:
        print('Valor ou número da conta inválido')


def efetuar_saque(banco):
    try:
        num_conta = int(input('Digite o número da conta da qual irá sacar: '))
        valor = int(input('Digite o valor a ser sacado: '))
        index = banco.mostrar_numero_contas.index(num_conta)
        banco.mostrar_contas[index].sacar(valor)
    except ValueError:
        print('Valor ou número da conta inválido')


def efetuar_transferencia(banco):
    try:
        num_conta1 = int(input('Digite o número da conta que irá transferir: '))
        num_conta2 = int(input('Digite o número da conta que irá receber: '))
        valor = int(input('Digite o valor a ser transferido: '))

        index1 = banco.mostrar_numero_contas.index(num_conta1)
        index2 = banco.mostrar_numero_contas.index(num_conta2)

        banco.mostrar_contas[index1].sacar(valor)
        banco.mostrar_contas[index2].depositar(valor)
    except ValueError:
        print('Valor ou número da conta inválido')


def printa_contas(banco):
    if len(banco.mostrar_contas) > 0:
        for conta in banco.mostrar_contas:
            print(conta)


def main():

    banco1 = Banco()

    while True:
        print('===========================================')
        print("1. Criar conta.\n2. Mostrar saldo.\n3. Efetuar depósito\n4. Efetuar saque.")
        print('5. Transferir\n6. Listar contas.\n7. Sair')
        print('===========================================')
        option = input()

        if option == '1':
            banco1.criar_conta(Contas())
        elif option == '2':
            mostrar_saldo(banco1)
        elif option == '3':
            efetuar_deposito(banco1)
        elif option == '4':
            efetuar_saque(banco1)
        elif option == '5':
            efetuar_transferencia(banco1)
        elif option == '6':
            printa_contas(banco1)
        elif option == '7':
            break

main()



















