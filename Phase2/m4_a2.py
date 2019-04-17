class Employee:
    def getFullName(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        return self.first_name+" "+self.last_name
    def getEmail(self,first_name,last_name):
        email = self.first_name+"."+self.last_name+"@company.com"
        return email
    def getPay(self,pay):
        self.pay = pay
        return pay
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.pay = None
emp_1 = Employee()
print(emp_1.getFullName("Mohandas", "Gandhi"))
print(emp_1.getEmail("Mohandas", "Gandhi"))
print(emp_1.getPay(50000))
