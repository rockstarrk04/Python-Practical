class Bank:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance

    def account_details(self):
        print(f'Account Number : {self.account_no}')
        print(f'Initial Balance : {self.balance}')


class Saving_Account(Bank):

    def deposit(self,amount):
        try:

            if (amount == 0) or (amount < 0):
                raise ValueError ("Amount should not be 0 or negative")
            else:
                self.balance += amount
                print(f'{amount} has been deposited')
                print(f'Balance : {self.balance}')

        except ValueError as e:
            print(e)

    def withdraw(self,amount):
        try:

            if (amount == 0) or (amount < 0) :
                raise ValueError ("Amount should not be 0 or negative")
            elif (amount > self.balance):
                raise ValueError ("Insufficient Balance")
            else:
                self.balance -= amount
                print(f'{amount} has been withdrawn')
                print(f'Balance : {self.balance}')

        except ValueError as e:
            print(e)


    def updated_balance(self):
        print(f'Updated Balance : {self.balance}')



obj = Saving_Account(12345,50000)
obj.account_details()
obj.deposit(500)
obj.withdraw(1000)
obj.updated_balance()