# Question:
# Write a Python program using OOP concepts to create a simple Bank Account
# Management System.
#
# Create a class BankName with the following attributes:
# name  - Account holder's name
# pin   - Account PIN
# balance - Account balance

# Implement the following methods:  
#
# 1. __init__() - Initialize the account holder's name, PIN, and balance
#    using a parameterized constructor.
#
# 2. check_pin() - Ask the user to enter the PIN and verify whether it is
#    correct. Handle an incorrect PIN using exception handling.
#
# 3. deposit() - Ask the user for an amount to deposit, validate the amount,
#    update the balance, and display the new balance.
#
# 4. withdraw() - Ask the user for an amount to withdraw, check whether
#    sufficient balance is available, update the balance, and display the
#    remaining balance.
#
# 5. display() - Verify the PIN and display the current bank balance.
#
# 6. Create an object of the class with the account details and perform
#    deposit, withdrawal, and balance enquiry operations.
#


#? Sir's code
# class BankName:
#     def __init__(self, name, pin, balance):
#         self.name = name
#         self.pin = pin
#         self.balance = balance

#     def check_pin(self):
#         try:
#             enter_pin = int(input("Enter the pin: "))

#             if enter_pin != self.pin:
#                 raise ValueError("Incorrect pin")

#             return True

#         except ValueError as e:
#             print("Error:", e)
#             return False

#     def deposit(self):
#         if self.check_pin():
#             try:
#                 amount = int(input("Enter the amount to deposit: "))

#                 if amount > 0:
#                     self.balance += amount
#                     print(f"{amount} has been deposited")
#                     print(f"After deposit balance: {self.balance}")
#                 else:
#                     print("Enter a valid amount")

#             except ValueError:
#                 print("Please enter a number")

#     def withdraw(self): 
#         if self.check_pin():
#             try:
#                 amount = int(input("Enter the amount to withdraw: "))

#                 if amount > 0 and amount <= self.balance:
#                     self.balance -= amount
#                     print(f"{amount} has been debited")
#                     print(f"After withdrawal balance: {self.balance}")
#                 else:
#                     print("Insufficient balance or invalid amount")

#             except ValueError:
#                 print("Please enter a number")

#     def display(self):
#         if self.check_pin():
#             print(f"Bank balance is: {self.balance}")


# acct = BankName("smith", 1234, 97000)

# while True:
#     print("\n----- BANK MENU -----")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         acct.deposit()

#     elif choice == "2":
#         acct.withdraw()

#     elif choice == "3":
#         acct.display()

#     elif choice == "4":
#         print("Thank you for using the bank.")
#         break

#     else:
#         print("Invalid choice. Please try again.")





#! Ram's code

class Bank:
    def __init__(self , name , pin , balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    # deposit
    def deposit(self, amount=None):
            print('Deposit')
            print()
            if self.check_PIN():
                if amount is None:
                    try:
                        amount = int(input('Enter amount to deposit : '))
                        print(f'Rs.{amount} has been deposited successfully!')
                        self.balance = self.balance + amount
                        print(f'The Updated balance is : {self.balance}')
                        print()
                    except ValueError:
                        print('Invalid entered Amount')
            else:
                print('PIN is incorrect , Please try Again !')
    # check_PIN
    def check_PIN(self):
        print('Checking PIN')
        print()
        try:
            user_pin = int(input('Enter your PIN : '))
            if user_pin == self.pin:
                return True
            else:
                return False
        except ValueError:
            print('ValueError, Please enter the FOUR digit PIN')

    # withdraw
    def withdraw(self):
        print('Withdraw')
        print()
        if self.check_PIN():
            print(f"Available Balance : {self.balance}")
            try:
                withdraw_amount = int(input('Enter amount to withdraw : '))
                if withdraw_amount <= self.balance:
                    print(f'Rs.{withdraw_amount} has been withdrawn successfully')
                    self.balance = self.balance - withdraw_amount
                    print(f'Remaining balance : {self.balance}')
                else:
                    print('Insufficient Balance for Requested withdraw amount')
            except ValueError:
                print('ValueError, Please enter valid input')
                print()
        else:
            print('PIN is incorrect , Please try Again !')

    # check balance
    def check_balance(self):
        print('Check Account Balance')
        if self.check_PIN():
            print(f"Your Account Balance is : {self.balance} ")
            print()
        else:
            print('PIN is incorrect , Please try Again !')

user1 = Bank("Ram" , 1010 , 70000)

while True:
    print()
    print('=========BANK MENU=========')
    print('1.Deposit')
    print('2.Withdraw')
    print('3.Check Balance')
    print('4.Exit')

    try:
        choice = int(input('Enter your choice : '))
        print()

        if choice == 1 :
            user1.deposit()
        elif choice == 2 :
            user1.withdraw()
        elif choice == 3 :
            user1.check_balance()
        elif choice == 4:
            print('Thankyou for using the Bank , Visit Again!!')
            break
        else:
            print('Invalid Option , try 1-4')

    except ValueError:
        print('ValueError : Please enter digits')