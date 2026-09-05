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



class BankName:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        try:
            enter_pin = int(input("Enter the pin: "))

            if enter_pin != self.pin:
                raise ValueError("Incorrect pin")

            return True

        except ValueError as e:
            print("Error:", e)
            return False

    def deposit(self):
        if self.check_pin():
            try:
                amount = int(input("Enter the amount to deposit: "))

                if amount > 0:
                    self.balance += amount
                    print(f"{amount} has been deposited")
                    print(f"After deposit balance: {self.balance}")
                else:
                    print("Enter a valid amount")

            except ValueError:
                print("Please enter a number")

    def withdraw(self): 
        if self.check_pin():
            try:
                amount = int(input("Enter the amount to withdraw: "))

                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print(f"{amount} has been debited")
                    print(f"After withdrawal balance: {self.balance}")
                else:
                    print("Insufficient balance or invalid amount")

            except ValueError:
                print("Please enter a number")

    def display(self):
        if self.check_pin():
            print(f"Bank balance is: {self.balance}")


acct = BankName("smith", 1234, 97000)

while True:
    print("\n----- BANK MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acct.deposit()

    elif choice == "2":
        acct.withdraw()

    elif choice == "3":
        acct.display()

    elif choice == "4":
        print("Thank you for using the bank.")
        break

    else:
        print("Invalid choice. Please try again.")