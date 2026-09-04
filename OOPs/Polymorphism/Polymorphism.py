# Polymorphism

class Bank:
    def __init__(self , cname , acc_no , balance):
        self.cname = cname
        self._acc_no = acc_no   # Protected member
        self.__balance = balance    # Private member

    def display(self):
        print(f"Customer Name : {self.cname}")
        print(f"Account Number : {self._acc_no}")
        print(f"Balance : {self.__balance}")

    @property     # getter property
    def balance(self):
        return self.__balance

    @balance.setter     # setter property
    def balance(self,new_balance):
        self.__balance = new_balance



obj = Bank("Ram" , 1234 , 98000)
obj.display()
# Accessing protected Member outside the class , using " objectname.protected_member_VariableName "
print(f"Account Number : {obj._acc_no}")  
# Accessing private Member outside the class using getter property (using the method's name as variable)  
print(f"Balance : {obj.balance}")

# Assigning new value for private member using setter property.
obj.balance = 1000000


# Printing data after modifying private member
print("After Modifying private member's value")
print(f"Account Number : {obj._acc_no}")
print(f"Balance : {obj.balance}")