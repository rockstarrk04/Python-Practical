print('Welcome to BookMyShow!')
theatre_name = input('Enter the name of the theatre (PVR,INOX) : ')
print()

if theatre_name == 'PVR' or theatre_name == 'INOX' : 
    if theatre_name == 'PVR' :
        print('Movies available at PVR :')
        movie1 = 'Avatar : The way of Water'
        movie2 = 'The Batman'
        price1 = 850
        price2 = 800

    elif theatre_name == 'INOX' :
        print('Movies available at PVR :')
        movie1 = 'Mission Impossible : Fallout'
        movie2 = 'Jurassic World : Dominion'
        price1 = 900
        price2 = 950

    print(f'1.{movie1}')
    print(f'2.{movie2}')

    print()
    movie_choice = int(input('Enter the number to select movie (1/2) :'))

    if movie_choice == 1 or movie_choice == 2 :
        if movie_choice == 1:
            selected_movie = movie1
            selected_price = price1
        elif movie_choice == 2:
            selected_movie = movie2
            selected_price = price2

        print(f'You selected: {selected_movie} - Price: {selected_price}')
        print()
        confirmation = input(f'Do you want to confirm the ticket for {selected_movie} (yes/no) : ')

        if confirmation == 'yes' :
            print(f'\nThe ticket  for "{selected_movie}" has been booked successfully!')

         

    else:
        print('Invalid movie choice.Please try again')
else:
    print('Sorry, the theatre name is not available')