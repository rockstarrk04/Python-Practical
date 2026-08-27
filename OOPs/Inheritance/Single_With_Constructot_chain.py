# Single Level Inheritance with Constructor Chaining

class Bank():
    def __init__(self , acctno , balance):
        self.acctno = acctno
        self.balance = balance
        print('Parent class (BANK) constructor executed')

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError ("Amount must be greater than 0")
            self.balance += amount
            print(f"{amount} has been deposited successfully")

        except ValueError as e:
            print("Deposit Error",e)

    def withdraw(self , amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                raise ValueError ("Insufficient Balance")
            self.balance -= amount
            print(f"{amount} has been withdrawn successfully")

        except ValueError as e:
            print("Withdraw Error : ",e)


class Saving_Account(Bank):
    def __init__(self, acctno, balance, branch):
        super().__init__(acctno, balance)
        self.branch = branch
        print('Child class (Saving_Account) constructor executed')


obj = Saving_Account(12345,50000,"Pune")

obj.deposit(10000)
print(f"Balance After Deposit : {obj.balance}")

obj.withdraw(35000)
print(f"Balance After Withdraw : {obj.balance}")

obj.deposit(-500)
obj.withdraw(100000000000)