class Customer:
    def __init__(self, cId, Name, TNo, Add):
        self.cID = cID
        self.Name = Name
        self.TNo = TNo
        self.Add = Add
        
    def discount(self):
        pass
class Regular_Customer(Customer):
    def discount(self):
        print("You are offered a discount for being a regular customer")
 
class Privileged_Customer(Customer):
    def discount(self):
        print("You are offered a membership card based on gifts given")
