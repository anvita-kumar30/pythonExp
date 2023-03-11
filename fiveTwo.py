class Employee:
    def _init_(self, id):
        super()._init_()
        self.id = id
    def setname(self, name):
        self.name = name
    def getname(self):
        return self.name
    def getid(self):
        return self.id

class Student:
    def _init_(self, id, college):
        super()._init_(id)
        self.college = college
    def getCollege(self):
        return self.college

class lntern(Student, Employee):
    def _init_(self, id, college, period):
        super()._init_(id, college)
        self.period = period
    def setDetails(self, name):
        self.name = name
    def getDetails(self):
        return self.name


intern_one = lntern(1, "TSEC", "1 Year")
intern_one.setDetails("Test User")
print("f'lntern's id is: {intern_one.getid()}")
print(f"lntern college is: {intern_one.getCollege()}")
print("f'lntern's details are:{intern_one.getDetails()}")
