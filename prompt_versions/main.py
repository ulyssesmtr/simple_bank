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

    def criar_conta(self):
        conta = Contas()
        self.__contas.append(conta)

        return conta

    @property
    def mostrar_contas(self):
        return self.__contas

    @property
    def mostrar_numero_contas(self):
        return list(map(lambda conta: conta.numero, self.__contas))

    def mostrar_saldo(self, num_conta):
        try:
            index = self.mostrar_numero_contas.index(num_conta)
            conta = self.mostrar_contas[index]
            print(f'O saldo da conta {num_conta} é {conta.saldo}')
        except ValueError:
            print('Valor inválido para conta.')

    def efetuar_deposito(self, num_conta, valor):
        try:
            index = self.mostrar_numero_contas.index(num_conta)
            self.mostrar_contas[index].depositar(valor)
        except ValueError:
            print('Valor ou número da conta inválido')

    def efetuar_saque(self, num_conta, valor):
        try:
            index = self.mostrar_numero_contas.index(num_conta)
            self.mostrar_contas[index].sacar(valor)
        except ValueError:
            print('Valor ou número da conta inválido')

    def efetuar_transferencia(self, num_conta1, num_conta2, valor):
        try:
            index1 = self.mostrar_numero_contas.index(num_conta1)
            index2 = self.mostrar_numero_contas.index(num_conta2)
            self.mostrar_contas[index1].sacar(valor)
            self.mostrar_contas[index2].depositar(valor)
        except ValueError:
            print('Valor ou número da conta inválido')

    def printar_contas(self):
        if len(self.mostrar_contas) > 0:
            for conta in self.mostrar_contas:
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
            conta = banco1.criar_conta()
            print(f'A conta de numero {conta.numero} foi criada com saldo {conta.saldo}.')
        elif option == '2':
            num_conta = int(input('Digite o número da conta que deseja consultar o saldo: '))
            banco1.mostrar_saldo(num_conta)
        elif option == '3':
            num_conta = int(input('Digite o número da conta que deseja efetuar depósito: '))
            valor = int(input('Digite o valor a ser depositado: '))
            banco1.efetuar_deposito(num_conta, valor)
        elif option == '4':
            num_conta = int(input('Digite o número da conta da qual irá sacar: '))
            valor = int(input('Digite o valor a ser sacado: '))
            banco1.efetuar_saque(num_conta, valor)
        elif option == '5':
            num_conta1 = int(input('Digite o número da conta que irá transferir: '))
            num_conta2 = int(input('Digite o número da conta que irá receber: '))
            valor = int(input('Digite o valor a ser transferido: '))
            banco1.efetuar_transferencia(num_conta1, num_conta2, valor)
        elif option == '6':
            banco1.printar_contas()
        elif option == '7':
            break

main()



















