# Multi-level Inheritance without constructor chaining and method chaining

class Person:
    def person_details(self):
        self.name = 'Allen'
        self.age = 25

class Employee(Person):
    def employee_details(self):
        self.empno = 1234
        self.salary = 98000

class Manager(Employee):
    def manager_details(self):
        self.department = "HR"

    def display(self):
        super().person_details()
        super().employee_details()
        self.manager_details()

        print(f"Person name : {self.name}")
        print(f"Person age : {self.age}")
        print(f"Employee Number : {self.empno}")
        print(f"Employee Salary : {self.salary}")
        print(f"Manager department : {self.department}")

obj = Manager()
# obj.display()

#==============================================================

class Bank():
    def account_details(self):
        self.name = "Allen"
        self.balance = 50000

class Deposit(Bank):
    def deposit(self,amount):
        try:
            if amount <= 0:
                raise ValueError ("Amount must be greater than 0")
            self.balance += amount
            print(f"{amount} has been deposited")
            print(f"After deposit , Updated balance : {self.balance}")
        except ValueError as e:
            print("Error : ",e)

class Withdraw(Deposit):
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError ("Amount must be greater than 0")
            elif amount > self.balance:
                raise ValueError ("Insufficient Balance")
            self.balance -= amount
            print(f"{amount} has been withdrawn")
            print(f"After withdrawn , Updated balance : {self.balance}")
        except ValueError as e:
            print("Error : ",e)

    
        