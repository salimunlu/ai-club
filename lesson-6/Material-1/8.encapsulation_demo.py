from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner

        self.__balance = balance
        self.__transaction_history = []

    def get_balance(self):   # hesaptaki miktarı gösterir
        return self.__balance

    def get_transaction_history(self):   # işlem geçmişini döndürür
        return self.__transaction_history

    def deposit(self, amount):     # para yatırma
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"{self.__generate_timestamp()} - Deposited: ${amount}")
            print(f"Deposited: ${amount}\nBalance: ${self.__balance}")

    def withdraw(self, amount):     # para çekme
        if amount < self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"{self.__generate_timestamp()} - Withdrawn: ${amount}")
            print(f"Withdrawn ${amount}\nBalance: ${self.__balance}")
        else:
            print("Insufficient Balance")

    def __generate_timestamp(self):     #zaman damgası oluştur
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


account1 = BankAccount("Ahmet")
account1.get_transaction_history()
account1.get_balance()
account1.__generate_timestamp()   # AttributeError: 'BankAccount' object has no attribute '__generate_timestamp'

account1.deposit(1000)
account1.withdraw(1001)
account1.withdraw(300)
account1.get_transaction_history()

