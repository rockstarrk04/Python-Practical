class Employee:
    company_name = 'Microsoft'
    def __init__(self , name , sal , job):
        self.name = name
        self.sal = sal
        self.job = job

    def display(self):
        print(f'The company name is {Employee.company_name}')
        print(f'Employee name is {self.name} and salary is {self.sal} and designation is {self.job}')

e1 = Employee('Ram' , 90000 , 'Manager')  
e2 = Employee('Sam' , 80000 , 'Salesman')  
e3 = Employee('Tom' , 70000 , 'Clerk')  
e4 = Employee('Bob' , 60000 , 'Supervisor')

e1.display()
e2.display()
e3.display()
e4.display()        
