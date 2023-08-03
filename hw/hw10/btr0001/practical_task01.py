class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        newvalue = self.__balance - amount
        if newvalue < 0:
            print("Insufficient funds")
        else:
            self.__balance = newvalue

    def check_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder

    account_holder = property(get_account_holder)


my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

print(my_account.check_balance())

my_account.deposit(500.0)
print(my_account.check_balance())

my_account.withdraw(250.0)
print(my_account.check_balance())

try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

my_account.withdraw(5000.0)