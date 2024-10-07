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

# Описание логики кода:
# 1. Создаем класс BankAccount. В инициализатор добавляем приватную переменную - balance. Она нужна для того, чтобы
#    защитить внутренние данные класса от изменения (Например, у нас есть счет в банке и мы хотим, чтобы баланс счета
#    был верным и менялсся только если положим деньги на счет или снимем деньги. Поменять значение баланса вне банка могут
#    мошенники, поэтому атрибут приватный).
# 2. Создаем функцию deposit. Она увеличивает баланс на заданную переменную (при выполнении условия)
# 3. Создаем функцию withdraw. Она отвечает за списание средств с аккаунта (при выполнении условия)
# 4. Создаем функцию get_balance. Она выводит текущий баланс (после применения функций)