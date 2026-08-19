class Bank:
    bank_name = 'State Bank of India'

    def details(self , cname , balance):
        self.cname = cname
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        print(f'Amount Deposited : {amount}')

    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount withdrawn : {amount}')
        else:
            print('Insufficient Balance to Withdraw')

    def display(self):
        print(f'Bank name : {Bank.bank_name}')
        print(f'Customer name : {self.cname}')
        print(f'Balance Amount : {self.balance}')

# customer1

c1 = Bank()
c1.details('Ram' , 100000)
c1.display()
c1.deposit(50000)
c1.withdraw(10000)


print()

# customer2

c2 = Bank()
c2.details('Sam' , 550000)
c2.display()
c2.deposit(50000)
c2.withdraw(90000)

print()

# customer3

c3 = Bank()
c3.details('Nithin' , 900000)
c3.display()
c3.deposit(50000)
c3.withdraw(50000)