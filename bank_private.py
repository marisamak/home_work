class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # приватная перемнная

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance()) # 1500
# account.__balance # вызовет ошибку, так как __balance приватная