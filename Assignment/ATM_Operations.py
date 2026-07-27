balance = 10000
while True:
    print('-----------ATM OPERATIONS--------------')
    print('1.Check Balance')
    print('2.Deposit Money')
    print('3.Withdraw Money')
    print('4.Exit')

    choice = int(input('Enter choice : '))

    if choice == 1:
        print(f'The Account balance = {balance}')
    elif choice == 2 : 
        deposit_amount = int(input('Enter amount to deposit :'))
        balance = balance + deposit_amount
        print(f'{deposit_amount} has been deposited in the account')
        print(f'The Account balance = {balance}')
    elif choice == 3 :
        withdraw_amount = int(input('Enter amount to deposit :'))
        if withdraw_amount <= balance:
            balance = balance - withdraw_amount
            print(f'{withdraw_amount} has been withdrawn in the account') 
            print(f'The Account balance = {balance}')
        else:
            print('Insufficient Balance')
    elif choice == 4 : 
        print('Thank You for Banking with Us!')
        break
    else:
        print('Invalid Choice, Please try again.')
        
