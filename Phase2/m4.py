class Employee:
    def display(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        email = self.first_name+"."+last_name+"@company.com"
        print("First name is : ",self.first_name)
        print("Last name is : ",self.last_name)
        print("Pay is : ",pay)
        print("Email is : ",email)
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.pay = None
e = Employee()
e.display("Mohandas", "Gandhi", 50000)   
