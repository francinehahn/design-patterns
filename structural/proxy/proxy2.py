from abc import ABC, abstractmethod

# Interface
class Wallet:
    @abstractmethod
    def pay(self):
        pass

# Real Object
class Bank(Wallet):
    def __init__(self):
        self.debit_card = None
        self.account = None
    
    def __get_account(self):
        return self.account
        
    def __has_balance(self):
        print(f'Checking the balance from account {self.__get_account()}')
        return True
    
    def set_debit_card(self, debit_card):
        self.debit_card = debit_card
        
    def set_account(self, account):
        self.account = account
        
    def pay(self):
        if self.__has_balance():
            print('Bank: paying the bill...')
            return True
        else:
            print('Bank: Sorry, you do not have balance')

# Proxy
class DebitCard(Wallet):
    def __init__(self):
        self.bank = Bank()

    def pay(self):
        debit_card_number = input('Proxy: What is the credit card number? ')
        self.bank.set_debit_card(debit_card=debit_card_number)

        account_number = input('Proxy: What is the bank account number? ')
        self.bank.set_account(account=account_number)
        return self.bank.pay()

# Client
class Client:
    def __init__(self):
        print('Client: I would like to buy a beer.')
        self.debit_card = DebitCard()
        self.bought = None
    
    def pay(self):
        self.bought = self.debit_card.pay()
    
    def __del__(self):
        if self.bought:
            print('I will finally drink a beer!')
        else:
            print('I wish I had more money...')

if __name__ == '__main__':
    client = Client()
    client.pay()
    