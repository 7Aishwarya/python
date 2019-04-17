class Employee:
    def __init__(self, paydays, lop):
        self.paydays = paydays
        self.lop = lop
 
    def getSalary(self):
        final_sal = self.paydays - self.lop
        return final_sal
 
class Faculty:
    def teach(self, course):
        pass
 
class Visitor:
    def calculateFees(startTime, EndTime):
        pass
    
class Clerk(Employee):
    
    def prepareBalancesheet(self):
        pass
 
class RegularFaculty(Employee, Faculty):
 
    def prepareAttenceReport():
        pass
 
 
class VisitingFaculty(Faculty, Visitor):
    pass
 
class Examiner(Visitor):
    def examine():
        pass
