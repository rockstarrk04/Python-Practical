"""
Write a Python program using the CSV module to create an employee management system. The program should provide a menu interface with the following options:

Add employee details – Accept the number of employees and store each employee's name, salary, designation, department number, and annual salary in a CSV file named employee.csv. Calculate annual salary as salary × 12.

Display employees – Read and display all employee details stored in the CSV file.

Display annual salary – Display each employee's name along with their annual salary.

Exit – Terminate the program.

The program should use separate functions for adding employee details, displaying employee records, and displaying annual salaries.
"""





import csv

filename = 'employee.csv'

# function to add employee
def add_employee():
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)                      

        n = int(input('Enter number of employees: '))

        for i in range(n):
            ename = input('Enter employee name: ')
            sal = int(input('Enter salary: '))
            job = input('Enter employee designation: ')
            deptno = int(input('Enter department number: '))
            annual = sal * 12
            writer.writerow([ename, sal, job, deptno, annual])
            print('Data stored successfully')

# function to display employees
def display():
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print('\nename  sal  job  deptno  annual')
        print('-' * 40)
        for row in reader:
            if len(row) < 5:
                continue  # skip incomplete or empty rows
            print(f'{row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}')

# function to display annual salary
def annual_salary():
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print('\nEmployee Annual Salary')
        print('Name\tAnnual Salary')
        print('-' * 25)
        for row in reader:
            if len(row) < 5:
                continue  # skip incomplete or empty rows
            print(f'{row[0]}\t{row[4]}')

# main menu loop
while True:
    print("\n1. Add employee details")
    print("2. Display employees")
    print("3. Annual salary")
    print("4. Exit")

    choice = int(input('Enter your choice: '))

    if choice == 1:
        add_employee()
    elif choice == 2:
        display()
    elif choice == 3:
        annual_salary()
    elif choice == 4:
        print('Exit')
        break
    else:
        print('Invalid choice')

