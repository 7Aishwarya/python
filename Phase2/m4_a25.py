class Department:
    def __init__(self, name):
        self.name = name
    def addcourse(self, course):
        pass
class Institution(Department):
    def __init__(self, name):
        self.name = name
    def event(self, visitor):
        self.visitor = visitor
        print("Visitor: ", self.visitor)
    def recruit(self, employee = []):
        self.employee.append()
    def add_dept(self, name):
        super().__init__(self.name)
        print("Department added")
    
class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.id = self.name + "@"+ "123"
    def set_designation(self, designation):
        self.designation = designation
    def __str__(self):
        return self.id + ":" + self.name + ":" + self.designation
 
class Visitor:
    def __init__(self, name):
        self.vis_name = name
 
class RegularFaculty:
    def __init__(self, deptname):
        self.deptname = deptname
    def teach(self,course):
        self.course = course
class Course:
    def __init__(self, coursename):
        self.coursename = coursename
d1 = Department("Computer")
e1 = Employee('John', "Clerk")
print(e1)
v1 = Visitor("Bill Gates")
inst = Institution("Institute of Technology")
inst.add_dept(d1)
inst.event(v1)
