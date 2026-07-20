print('--Flight Ticket Booking System--')
print()

bill = 0
booking_list = []

while True:
    print('1. View Available Flights')
    print('2. Book Flight Ticket')
    print('3. View Booking Cart')
    print('4. Checkout')
    print('5. Exit')
    print()

    choice_selected = int(input('Enter the menu option (1/2/3/4/5) : '))
    print()

    # View flights
    if choice_selected == 1:
        print('Available Flights : ')
        print('1. New York to Los Angeles | Price: $250')
        print('2. London to Paris        | Price: $150')
        print('3. Dubai to Singapore     | Price: $300')
        print('4. Tokyo to Bangkok       | Price: $200')
        print()

    # Book flight ticket
    elif choice_selected == 2:
        print('Available Flights : ')
        print('1. New York to Los Angeles')
        print('2. London to Paris')
        print('3. Dubai to Singapore')
        print('4. Tokyo to Bangkok')
        print()

        flight_choice = int(input('Enter Flight to book (1/2/3/4) : '))
        print()

        if flight_choice == 1:
            flight_name = 'New York to Los Angeles'
            ticket_price = 250
        elif flight_choice == 2:
            flight_name = 'London to Paris'
            ticket_price = 150
        elif flight_choice == 3:
            flight_name = 'Dubai to Singapore'
            ticket_price = 300
        elif flight_choice == 4:
            flight_name = 'Tokyo to Bangkok'
            ticket_price = 200
        else:
            print('Invalid Flight selected !')
            continue

        print(f'You have selected {flight_name} and price per ticket is ${ticket_price}')
        num_tickets = int(input('Enter Number of Tickets: '))
        amount = ticket_price * num_tickets
        bill = bill + amount

        booking_list.append((flight_name, num_tickets, amount))  # saving as tuple (immutable)
        print(f'The total amount to be paid is : ${amount}')
        print('Added tickets to cart')
        print()

    # View booking cart
    elif choice_selected == 3:
        if len(booking_list) == 0:
            print('Your cart is empty')
        else:
            print('Your Booking Cart :')
            for item in booking_list:
                print(f'{item[0]} | Tickets: {item[1]} | Amount: ${item[2]}')
        print()

    # Checkout menu
    elif choice_selected == 4:
        print('Checkout')
        print()

        if len(booking_list) == 0:
            print('Your cart is empty')
            print()
            continue
            
        else:
            print('Your Booking Cart :')
            for item in booking_list:
                print(f'{item[0]} | Tickets: {item[1]} | Amount: ${item[2]}')

            print()
            print(f'Total Bill: ${bill}')

        print()
        print('Thank you for booking with us!')
        break

    elif choice_selected == 5:
        print('Exit')
        break

    else:
        print('Invalid Menu Input, Try again!')
        print()