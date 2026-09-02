# Hybrid Inheritance
# Single Level , Multi-level , Multiple , Hierarchical Inheritance

class Bank:
    def __init__(self,cname , balance):
        self.cname = cname
        self.balance = balance

    def display(self):
        print(f"Customer Name : {self.cname}")
        print(f"Balance : {self.balance}")
        return self


class currentBankAccount(Bank):  #! Single Level Inheritance
    def __init__(self, cname, balance, interest):
        super().__init__(cname, balance)
        self.interest = interest

    def display_interest(self):
        print(f"Interest in Current Account : {self.interest}")
        return self


class SavingBankAccount(currentBankAccount):  #! Multi-level Inheritance
    def __init__(self, cname, balance, interest, pin):
        super().__init__(cname, balance, interest)
        self.pin = pin

    def display_pin(self):
        print(f"PIN  : {self.pin}")
        return self

class combineAccount(SavingBankAccount,Bank):   #! Multiple Inheritance
    def __init__(self, cname, balance, interest, pin):
        super().__init__(cname, balance, interest, pin)


obj = combineAccount("Allen" , 98000 , 7 , 2010)
obj.display().display_interest().display_pin()
