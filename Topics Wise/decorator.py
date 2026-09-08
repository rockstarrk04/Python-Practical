
# todo : Example 1
# def decorator(func):
#     def inner():
#         print("Before Execution")
#         func()
#         print("After Execution")
#     return inner


# @decorator
# def wish():
#     print("Hello student")
# wish()


# todo : Example 2
# def decorator(func):
#     def inner(*args, **kwargs):
#         print('Before execution')
#         func(*args, **kwargs)
#         print('After execution')
#     return inner



# @decorator
# def wish(name):
#     print(f"Hello {name}")
# wish('Ram')

# todo : Example 3

# def decorator(func):
#     def inner(*args, **kwargs):
#         print('Before execution')
#         func(*args, **kwargs)
#         print('After execution')
#     return inner



# @decorator
# def wish(a,b):
#     print(f"{a} + {b} = {a+b}")
# wish(100,200)


# todo : Example 4

# def check_balance(func):
#     def wrapper(object , amount):
#         if  amount > object.balance:
#             print('Insufficient Balance')
#             return
#         print("Balance check successful")
#         return func(object,amount)
#     return wrapper
        



# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance

#     @check_balance
#     def withdraw(self,amount):
#         self.balance -= amount
#         print(f"{amount} has been debited")
#         print(f"Available Balance : {self.balance}")

# object = BankAccount("Ram",50000)
# object.withdraw(10000)
# object.withdraw(10000000)