# 18 is a number , sum of the digits should divide the original number with 0 as remainder
#  i.e the sum of the digits must be a factor of that original number

num = 1729
sum = 0
temp = num

while temp > 0:
    last_digit = temp % 10 
    sum = sum + last_digit
    temp = temp // 10

if num % sum == 0:   # 1729 % 19 
    print(f"{num} is a harshad number")
else:
    print(f"{num} is not a harshad number") 