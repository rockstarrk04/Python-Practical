## Magic Number

def is_magic(num):
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum = sum + last_digit

        if sum == 1:
            return True
        num = num // 10
        
    if num == 0:
        num = sum
        sum = 0

# def is_magic(num):
#     while num > 9:
#         sum = 0

#         while num > 0:
#             sum = sum + (num % 10)
#             num = num // 10

#         num = sum

#     return num == 1


num = int(input('Enter a number : '))
if is_magic(num):
    print(f"{num} is a magic number")
else:
    print(f"{num} is not a magic number")