class BankAccount:

    all_accounts=[]

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds")
            return self
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'current balance is {self.balance}',f'current interest rate is {self.int_rate}', sep="\n")
        return self

    def yield_interest(self):
        if self.balance <=0:
            print("you have no money")
            return self
        else:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

    @classmethod
    def all_balances(cls):
        for accounts in cls.all_accounts:
            print (f'balance:{accounts.balance}')

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.checking = BankAccount(int_rate=0.2,balance=0)
        self.savings = BankAccount(int_rate=0.4,balance=0)


    def checking_deposit(self,amount):
        self.checking.deposit(amount)
        return self

    def savings_deposit(self,amount):
        self.savings.deposit(amount)
        return self

    def checking_withdrawal(self,amount):
        self.checking.withdraw(amount)
        return self

    def savings_withdrawal(self,amount):
        self.savings.withdraw(amount)
        return self

    def display_user_balance(self):
        self.checking.display_account_info()
        self.savings.display_account_info()
        return self
    




tony=User("tony","tonybaromagic@gmail.com")

tony.display_user_balance()

tony.checking_deposit(5000).checking_deposit(200).display_user_balance().savings_deposit(500).checking_withdrawal(200).display_user_balance()