student_count = 0
while True:
    print('-------------Student Management System----------------')
    print('1.Add Student')
    print('2.View total Students')
    print('3.Remove Student')
    print('4.Exit')

    choice = int(input('Enter a choice : '))

    if choice == 1:
        s_name = input('Enter Student name : ')
        student_count = student_count + 1
        print(f'{s_name} has been added')

    elif choice == 2 : 
        print(f'Total Student Count = {student_count}')

    elif choice == 3:
        name = input('Enter Student name to remove : ')
        student_count = student_count - 1
        print(f'{name} has been removed from database')
    elif choice == 4 :
        print('Thank you for using the System')
        break
    else:
        print('Invalid choice , please try again')
