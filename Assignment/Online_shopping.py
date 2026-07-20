print('--Online Shopping Management System--')
print()

bill = 0
cart_list = []

while True:
    print('1. View Products')
    print('2. Add Product to Cart')
    print('3. View Cart')
    print('4. Checkout')
    print('5. Exit')
    print()

    choice_selected = int(input('Enter the menu option (1/2/3/4/5) : '))
    print()

    # View product
    if choice_selected == 1:
        print('Available Product : ')
        print('1. T-Shirt , Price RS.900')
        print('2. Jeans   , Price RS.1000')
        print('3. Shoes   , Price RS.2000')
        print('4. Watch   , Price RS.3000')
        print()

    # Add product to cart
    elif choice_selected == 2:
        print('Available Product : ')
        print('1. T-Shirt')
        print('2. Jeans')
        print('3. Shoes')
        print('4. Watch')
        print()

        add_product_to_cart = int(input('Enter Product to add in cart (1/2/3/4) : '))
        print()

        if add_product_to_cart == 1:
            product_name = 'T-Shirt'
            product_price = 900
        elif add_product_to_cart == 2:
            product_name = 'Jeans'
            product_price = 1000
        elif add_product_to_cart == 3:
            product_name = 'Shoes'
            product_price = 2000
        elif add_product_to_cart == 4:
            product_name = 'Watch'
            product_price = 3000
        else:
            print('Invalid Product selected !')
            continue

        print(f'You have selected {product_name} and price per piece is {product_price}')
        qty = int(input('Enter Quantity: '))
        amount = product_price * qty
        bill = bill + amount

        cart_list.append((product_name, qty, amount))  # saving as tuple (immutable)
        print(f'The total amount to be paid is : {amount}')
        print('Added product to cart')
        print()

    # View cart
    elif choice_selected == 3:
        if len(cart_list) == 0:
            print('Your cart is empty')
        else:
            print('Your Cart :')
            for item in cart_list:
                print(f'{item[0]} | Qty: {item[1]} | Amount: RS.{item[2]}')
        print()

    # Checkout menu
    elif choice_selected == 4:
        print('Checkout')
        print()

        if len(cart_list) == 0:
            print('Your cart is empty')
            print()
            continue
            
        else:
            print('Your Cart :')
            for item in cart_list:
                print(f'{item[0]} | Qty: {item[1]} | Amount: RS.{item[2]}')

            print()
            print(f'Total Bill: RS.{bill}')

        print()
        print('Thank you for shopping')
        break

    elif choice_selected == 5:
        print('Exit')
        break

    else:
        print('Invalid Menu Input, Try again!')
        print()