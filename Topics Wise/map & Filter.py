# map() in python

# numbers = [1,2,3,4,5]
# res = map(lambda x : x*x , numbers)
# print(list(res))


# numbers = [1,2,3,4,5]
# res = map(lambda x : (x**2, x**3) , numbers)
# print(list(res))

# names = ['Allen' , 'Anna' , 'Tom' , 'Henry' , 'Jonh' , 'Anto']
# res = map(lambda name : name if name[0] in "aA" else None , names)
# print(list(res))


# ===================================================

# filter() in python

names = ['Allen' , 'Anna' , 'Tom' , 'Henry' , 'Jonh' , 'Anto']
res = filter(lambda name : name if name[0] in "aA" else None , names)
print(list(res))