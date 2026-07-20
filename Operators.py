## Operators in python

## Arithmetic Operator
        
# 1.Addition ( + )


print(10 + 12)  # 22

print('ram' + 10)  # TypeError: can only concatenate str (not "int") to str

print(str(98) + 'ram')  # 98ram

print('pyspider' + ' python')   # pyspider python


list1 = [1,2,3,4]
list2 = [10,20,30]
print(list1 + list2) # [1, 2, 3, 4, 10, 20, 30]

print(9 + True)  # 10

print(100 + 98.45)  # 198.45

print(56 + (10 + 5j))   # (66+5j)

print((1,2,3,4) + (10,20,30,40))    # (1, 2, 3, 4, 10, 20, 30, 40)

# Subraction ( - )

print(98 - 45)  # 53

print('pyspider' - ' python')   # TypeError

print(980 - (10 + 5j)) # (970-5j)

print(55.98 - 45)   # 10.979999999999997

list1 = [10,20,30]
list2 = [1,2,3]
print(list1 - list2) # TypeError

s1 = {10,20,30}
s2 = {1,2,3}
print(s1 - s2) # {10, 20, 30}

print(s2 - s1) # {1, 2, 3}

s1 = {10,20,30}
s2 = {10,2,30}
print(s1 - s2) # {20}

s1 = {10,20,30}
s2 = {10,2,30}
print(s2 - s1) # {2}


# Multiplication ( * )

print(6 * 2) # 12

print(('python ') * 2)   # python python 

list1 = [1,2,3]
list2 = 2
print(list1 * 2) # [1, 2, 3, 1, 2, 3]


t1 = (1,2,3,4)
t2 = 3
print(t1 * t2) # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

s1 = {1,2,3,4}
s2 = 2
print(s1 * s2) # TypeError

d1 = {'ename' : 'ram'}
d2 = 2
print(d1 * 2) # TypeError


#True Division ( / )

print(10 / 2) # 5.0






