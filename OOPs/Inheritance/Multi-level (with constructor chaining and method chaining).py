# Multi-level Inheritance with constructor chaining and method chaining

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_details(self):
        print(f"Person name : {self.name}")
        print(f"Person age : {self.age}")

        return self

class Employee(Person):
    def __init__(self, name, age, empno, salary):
        super().__init__(name, age)
        self.empno = empno
        self.salary = salary

    def employee_details(self):
        print(f"Employee number : {self.empno}")
        print(f"Employee Salary : {self.salary}")

        return self

class Manager(Employee):
    def __init__(self, name, age, empno, salary, department):
        super().__init__(name, age, empno, salary)
        self.department = department

    def manager_details(self):
        print(f"Manager Department name : {self.department}")

        return self

# Object creation
obj = Manager("Allen" , 25 , 12345 , 98000 , "HR")
# obj.person_details().employee_details().manager_details()


#======================================================================

class Bank:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

class Deposit(Bank):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def deposit(self,amount):
        try:
            if amount <= 0:
                raise ValueError ("Amount must be greater than 0")
            self.balance += amount
            print(f"{amount} has been deposited")
            print(f"After deposit , balance is : {self.balance}")

        except ValueError as e:
            print("Error : ",e)

        return self

class Withdraw(Deposit):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self,amount):
        try:
            if amount <= 0:
                raise ValueError ("Amount must be greater than 0")
            elif amount > self.balance:
                raise ValueError ("Insufficient Balance")
            
            self.balance -= amount
            print(f"{amount} has been deposited")
            print(f"After deposit , balance is : {self.balance}")

        except ValueError as e:
            print("Error : ",e)

        return self

    def check_balance(self):
        print(f"Customer Name : {self.name}")
        print(f"Balance Amount : {self.balance}")
        return self

# object creation
acc = Withdraw("Smith" , 5000)
# acc.check_balance().deposit(400).withdraw(1000)
