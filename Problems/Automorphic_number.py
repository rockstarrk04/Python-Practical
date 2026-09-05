# Automorphic number is number where the original number's last digit and last digit of that original number's square 
# is same then it is called as automorphic number


num = 76
last_digit_original = num % 10  # 6

square_value = num * num
last_digit_square = square_value % 10 # 6

if last_digit_original == last_digit_square:
    print(f"{num} is Automorphic number")
else:
    print(f"{num} is not Automorphic number")