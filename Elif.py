
### Simple Calculator

print('Simple Calculator')
print('Select operations : ')
print('1.Addition')
print('2.Subraction')
print('3.Multiplication')
print('4.Division')

choice = int(input('Enter choice 1/2/3/4 : '))
num1 = float(input('enter number 1: '))
num2 = float(input('enter number 2: '))

if choice == 1:
    print(f' The result of addition : {num1 + num2}')
elif choice == 2:
    print(f' The result of Subraction : {num1 - num2}')
elif choice == 3:
    print(f' The result of Multiplication : {num1 * num2}')
elif choice == 4:
    if num2 == 0:
        print('Error : Division by zero is not allowed')
    else:
        print(f' The result of Division : {num1 / num2}')
else:
    print('Error : Invalid choice')



### ATM Operations

print('--ATM Operations--')
print('Select operations : ')
print('1.Check Balance')
print('2.Deposit money')
print('3.Withdraw money')

balance = 5000

choice = int(input('Enter choice 1/2/3 : '))

if choice == 1:
    print(f'The balance amount is : {balance}')
elif choice == 2:
    deposit_amount = int(input('Enter amount to deposit : '))
    print(f'{deposit_amount} has been deposited')
    balance = balance + deposit_amount
    print(f'New balance is : {balance}')
elif choice == 3:
    