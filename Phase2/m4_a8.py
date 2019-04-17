class Employee:
    @classmethod
    def from_string(cls,emp_string):
        t = emp_string.split('-')
        fname=t[0]
        lname=t[1]
        pay=t[2]
        print("First name=",fname)
        print("Last name=",lname)
        print("Pay=",pay)
        
    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
emp_1_str = "John-Abrahim-50000"
emp_1 = Employee.from_string(emp_1_str)



