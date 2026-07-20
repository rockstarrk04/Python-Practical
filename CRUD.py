a = 98
print(id(a)) # 140724617924760

print()

b = a
print(id(b)) # 140724617924760

print()

c = b
print(id(c)) # 140724617924760

a = 98.83
print(id(a)) # 2830309821936

print()

b = a
print(id(b)) # 2830309821936

print()

c = b
print(id(c)) # 2830309821936

c = 'ab'
print(id(c)) # 1151837962720

print()

d = 'ab'
print(id(d)) # 1151837962720


# Assigning same values for List - one of collection datatypes
list1 = [10,20,30]
print(id(list1)) # 2583568756096

print()

list2 = [10,20,30]
print(id(list2)) # 2583575524224

# Assigning same values as coping variable name to another new List - one of collection
# datatypes

# same id for both variable
list1 = [10,20,30]
print(id(list1)) # 2583575524864

print()

list2 = list1
print(id(list2)) # 2583575524864
