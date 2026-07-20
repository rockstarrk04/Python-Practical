# relational operators

a = 10
b = 2
print(a < b)  # False

a = 2
b = 10
print(a < b)  # True

a = 10
b = 2
print(a == b)  # False

s1 = 'python'
s2 = 'java'
print(s1 > s2) # True

s1 = 'javascript'
s2 = 'java'
print(s1 > s2) # True

s1 = 'python'
s2 = 'java'
print(s1 == s2) # False

list1 = [10,20,30,40]
list2 = [10,20,30,40]
print(list1 == list2)  # '==' is used to compare the values inside the  two variables
# output : True

list1 = [10,20,30,40]
list2 = [10,20,30,40]
print(list1 is list2)  # 'is' is used to compare the memory of the  two variables
# output : False

a = 10
b = 3
print(a>=b) # True

a = 20
b = 21
print(b >= a)  # True

a = 20
b = 21
print(a >= b)  # False

num = 100
print(10 < num > 45) # True

num = 100
print(100 <= num >= 101) # False

ch = 'a'
print(ord(ch)) # 97

ch = 'A'
print(ord(ch)) # 65

ch = 'a'
print(chr(ord(ch) - 32))  # A

ch = 'b'
print(chr(ord(ch) - 32))  # B

ch = 'r'
print(chr(ord(ch) - 32))  # R

ch = 'A'
print(chr(ord(ch) + 32))  # a

ch = 'B'
print(chr(ord(ch) + 32))  # b

ch = 'R'
print(chr(ord(ch) + 32))  # r


## Swapping two numbers using third variable

a = 10
b = 20
print(f' before swapping, a is {a} and b is {b}')  #  before swapping, a is 10 and b is 20
temp = a
a = b
b = temp
print(f' after swapping, a is {a} and b is {b}')  #   after swapping, a is 20 and b is 10

## Swapping two numbers without using third variable

a = 10
b = 20
print(f' before swapping, a is {a} and b is {b}')  #  before swapping, a is 10 and b is 20

a,b = b,a

print(f' after swapping, a is {a} and b is {b}')  #   after swapping, a is 20 and b is 10


## Swapping two numbers without using third variable and using arithmetic operators

a = 10
b = 20
print(f' before swapping, a is {a} and b is {b}')  #  before swapping, a is 10 and b is 20

a = a + b # 30
b = a - b # 10
a = a - b # 20

print(f' after swapping, a is {a} and b is {b}')  #   after swapping, a is 20 and b is 10


## assignment Operators

a = 10
a+=5
print(a)  # 15

a = 10
a -=5
print(a)  # 5

a = 10
a *=5
print(a)  # 50

a = 10
a /=5
print(a)  # 2.0

a = 10
a //=5
print(a)  # 2

a = 10
a **=5
print(a)  # 100000

a = 10
a %=3
print(a)  # 1   





