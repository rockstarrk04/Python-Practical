# Types of Methods in OOPs
'''
1.instance method
2.class method
3.static method
'''


# todo : Instance Method

# class Bank:
#     def __init__(self , cname , acc_no , balance):
#         self.cname = cname   # instance variable
#         self.acc_no = acc_no  # instance variable
#         self.balance = balance   # instance variable

#     # instance method
#     def display(self):
#         print(f"Customer name : {self.cname}")
#         print(f"Account Number : {self.acc_no}")
#         print(f"Balance Amount : {self.balance}")

# # creating object for this class
# obj = Bank("Ram" , 1234 , 50000)

# # calling instance method using object reference
# obj.display()  


# todo : class Method
#? class method is used to access and modify the class members (variables declared inside a class)
#? this is achieved by using @classmenthod (should be placed above the class method)


# class Student : 
#     school_name = "Global School"

#     def __init__(self , name , standard ):
#         self.name = name
#         self.standard = standard

#     @classmethod
#     def change_school_name(cls , new_name):
#         Student.school_name = new_name

# # creating object for this class
# Student1 = Student("Ram" , 10)
# print(f"Before changing school name : {Student.school_name}")

# # calling the class method using the classname.methodname(argument)
# Student.change_school_name("Super School")
# print(f"Before changing school name : {Student.school_name}")

        
# todo : static method
#? static method is neither a class method nor instance method but it can be supportive for both methods
#? here , cls or self is not required to pass as first parameter inside the static method

class Bank:

    @staticmethod
    def is_pin_valid(pin):
        if len(str(pin)) == 4 and str(pin).isdigit():
            print('Valid')
        else:
            print('Invalid')


Bank.is_pin_valid(1234)