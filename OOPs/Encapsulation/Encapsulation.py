#  Encapsulation in Python 

class Bank:
    def __init__(self , cname , acc_no , balance):
        self.cname = cname      # Public Member
        self._acc_no = acc_no   # Protected Member
        self.__balance = balance    # Private Member

    def display(self):
        print("Accessing the members inside the class")
        print(f"Customer Name : {self.cname}")
        print(f"Account Number : {self._acc_no}")
        print(f"Balance : {self.__balance}")

obj = Bank("Ram" , 12345 , 60000)
obj.display()

print("\nAccessing the members outside the class")
print(f"Customer Name : {obj.cname}")   # accessed public member
print(f"Account Number : {obj._acc_no}")  # accessed protected member (but it is not recommended)
# print(f"Balance : {obj.__balance}")   # can't Accecc Private member


#? Name Mangling
'''
    Syntax:
        objectname._classname__variablename
'''

# using Name Mangling its possible to access private members
print(f"Accessing Private Member Using Name Mangling : {obj._Bank__balance}")
    