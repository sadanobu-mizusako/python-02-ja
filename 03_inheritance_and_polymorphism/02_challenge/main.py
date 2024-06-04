from abc import ABC, abstractmethod
import datetime

class Accout(ABC):
    def __init__(self, account_number , balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.history = []
        self.__interest = interest_rate

    def __str__(self):
        return f"The account number is {self.account_number}, the balance is {self.balance}"

    @abstractmethod
    def can_withdraw(self, amount):
        pass
    
    def deposit(self, amount):
        balance_old = self.balance
        self.balance += amount
        self.history.append(
            {
                "datetime": datetime.datetime.now(),
                "type": "deposit",
                "before": balance_old,
                "after": self.balance,
                "amount": amount
            }
        )
        return self

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            balance_old = self.balance
            self.balance -= amount
            self.history.append(
                {
                    "datetime": datetime.datetime.now(),
                    "type": "withdraw",
                    "before": balance_old,
                    "after": self.balance,
                    "amount": -amount
                }
            )
        else:
            print("balance is not enough!")
        return self

    def apply_interest(self):
        balance_old = self.balance
        amount = int(self.balance * self.__interest)
        self.balance += amount
        self.history.append(
            {
                "datetime": datetime.datetime.now(),
                "type": "withdraw",
                "before": balance_old,
                "after": self.balance,
                "amount": amount
            }
        )
        return self

    def get_transaction_history(self):
        return self.history
    
class SavingsAccount(Accout):
    def __init__(self, account_number , balance):
        super().__init__(account_number, balance, 0.01)

    def can_withdraw(self, amount):
        return self.balance >= amount
        
class CheckingAccount(Accout):
    def __init__(self, account_number , balance):
        super().__init__(account_number, balance, 0.02)

    def can_withdraw(self, amount):
        return self.balance >= amount
        

alice_savings = SavingsAccount("123456", 1000)
bob_checking = CheckingAccount("987654", 500)

accounts = [alice_savings, bob_checking]

print("Initial Account Details:")
print(alice_savings)
print(bob_checking)

print(alice_savings.deposit(200))
print(alice_savings.withdraw(500))
print(bob_checking.deposit(300))
print(bob_checking.withdraw(1000))

print(alice_savings.get_transaction_history())
print(bob_checking.get_transaction_history())

print(alice_savings)
print(bob_checking)

##################
print(alice_savings.apply_interest())
print(bob_checking.apply_interest())

print(alice_savings.get_transaction_history())
print(bob_checking.get_transaction_history())
