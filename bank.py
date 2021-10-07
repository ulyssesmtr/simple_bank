class Account:

    def __init__(self, account_number):
        self.__number = account_number
        self.__balance = 0

    def withdraw(self, value):
        self.__balance -= value

    def deposit(self, value):
        self.__balance += value

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f'Account number: {self.__number} - Balance:{self.__balance}'


class Bank:

    def __init__(self):
        self.__accounts = []

    def create_account(self, account_number):
        account = Account(account_number)
        self.__accounts.append(account)

        return account
        # return f'The account number: {account.number} with a balance of {account.balance} was created'

    @property
    def account_list(self):
        return self.__accounts

    @property
    def accounts_numbers(self):
        return list(map(lambda account: account.number, self.__accounts))

    def show_balance(self, account_number):
        index = self.accounts_numbers.index(account_number)
        account = self.account_list[index]
        return account.balance

        # return f'The account {account.number} has a balance of {account.balance}'

    def make_deposit(self, account_number, value):
        try:
            index = self.accounts_numbers.index(account_number)
            account = self.account_list[index]
            account.deposit(value)
            return account.balance
        except ValueError:
            return 'Value or account number are invalid'

    def make_withdraw(self, account_number, value):
        try:
            index = self.accounts_numbers.index(account_number)
            account = self.account_list[index]
            account.withdraw(value)
            return account.balance
        except ValueError:
            return 'Value or account number are invalid'

    def transfer(self, account_number1, account_number2, value):
        try:
            index1 = self.accounts_numbers.index(account_number1)
            index2 = self.accounts_numbers.index(account_number2)
            account1 = self.account_list[index1]
            account2 = self.account_list[index2]
            account1.withdraw(value)
            account2.deposit(value)
            return account1.balance, account2.balance
        except ValueError:
            return 'Value or account number are invalid'

    def delete_account(self, account_number):
        index = self.accounts_numbers.index(account_number)
        account = self.account_list[index]
        self.__accounts.remove(account)

    def print_accounts(self):
        all_accounts_string = ''
        if len(self.account_list) > 0:
            for account in self.account_list:
                all_accounts_string += f'Account: {account.number} - Balaance: {account.balance} \n'
            return all_accounts_string





















