#!/usr/bin/python3
class BankAccount:

    def __init__(self, balance):

        self.__balance = balance
    
    def desposit(self, amount):
        self.__balance += amount
        print(f"{amount} Añadidos, {self.__balance} Restantes")
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount} Retirados, {self.__balance} Restantes")
        else:
            print(f"Sin fondos suficientes")

    def get_balance(self):
        print(f"{self.__balance}")


micuenta = BankAccount(3000)
BankAccount.desposit(micuenta, 1000)
BankAccount.withdraw(micuenta, 3000)
BankAccount.get_balance(micuenta)
BankAccount.withdraw(micuenta, 9999)
BankAccount.get_balance(micuenta)