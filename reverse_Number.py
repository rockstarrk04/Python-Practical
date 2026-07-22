## Reverse a given number and check it is palindrome or not.

num = int(input('Enter a number to check palindrome or not : '))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if rev == temp:
    print(f'{temp} is a palindrome number')
else:
    print(f'{temp} is not a palindrome number')


'''
NOTE : 
    {1-9} % 10 => {1-9}
    {1-9} // 10 => 0 (ALWAYS ANSWER WILL BE ZERO)

''' 