print("Welcome to Book My Show!")

while True: 
    theater_name = input("\nEnter the name of the theater (PVR, INOX) or type 'exit' to quit: ")

    if theater_name.lower() == "exit":
        print("Thank you for using Book My Show!")
        break

    if theater_name.upper() == "PVR" or theater_name.upper() == "INOX":

        if theater_name == "PVR":
            print("\nMovies available at PVR:")
            movie1 = "Avatar: The Way of Water - RS 850"
            movie2 = "The Batman - RS 800"
            ticket_price1 = 850
            ticket_price2 = 800
        else:
            print("\nMovies available at INOX:")
            movie1 = "Mission: Impossible - Fallout - RS 900"
            movie2 = "Jurassic World: Dominion - RS 950"
            ticket_price1 = 900
            ticket_price2 = 950

        print(f"1. {movie1}")
        print(f"2. {movie2}")

        movie_choice = input("\nEnter the number of your chosen movie (1 or 2): ")

        if movie_choice == "1" or movie_choice == "2":

            if movie_choice == "1":
                selected_movie = movie1
                ticket_price = ticket_price1
            else:
                selected_movie = movie2
                ticket_price = ticket_price2

            print(f"\nYou have selected: {selected_movie}")
            print(f"Ticket Price: RS {ticket_price}")

            confirmation = input("\nDo you want to confirm the booking? (yes/no): ")

            if confirmation.lower() == "yes":
                print(f"\nYour ticket for '{selected_movie}' has been booked successfully!")
            else:
                print("\nTicket booking has been canceled.")

        else:
            print("Invalid movie choice. Please try again.")
    else:
        print("Sorry, the theater name is not available.")