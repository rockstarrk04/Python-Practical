# Iterator in Python


# numbers = [1,2,3,4,5,6,7,8,9,10]

# iterator = iter(numbers)

# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     print('no more elements left to iterate')



# todo : list
# numbers = [1,2,3,4,5,6,7,8,9,10]

# iterator = iter(numbers)

# for value in iterator:
#     print(value)



# todo : string
# string = "python"

# iterator = iter(string)

# for value in iterator:
#     print(value)


# todo : Tuple
# tuple = (1,2,3,4,5,6,7,8,9,10)
# iterator = iter(tuple)

# for value in iterator:
#     print(value)




# ? Create a custom iterator class that generates numbers from 1 to N.

# class Number:
#     def __init__(self,N):
#         self.N = N
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.N:
#             Value = self.current
#             self.current += 1
#             return Value
#         raise StopIteration

# obj = Number(10)
# it = iter(obj)

# try:
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print('no more elements left to iterate')