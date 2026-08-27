class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'Customer Name : {self.name}')
        print(f'Initial Balance : {self.balance}')
        return self

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError ("Amount must be greater than 0")
        else:
            self.balance = self.balance + amount
            print(f'{amount} has been deposited')
        return self

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        elif amount <= 0:
            raise ValueError ("Amount must be greater than 0")
        else:
            self.balance = self.balance - amount
            print(f'{amount} has been debited successfully')
        return self


class SavingsAccount(Bank):
    # constructor chaining
    def __init__(self, name, balance, contact_number):
        super().__init__(name, balance)
        self.contact_number = contact_number

    # method overriding
    def display(self):
        super().display()
        print(f"Customer Contact Details : {self.contact_number}")
        return self


obj = SavingsAccount("Ram",50000,9838179810)
obj.display().deposit(5000).withdraw(10000)