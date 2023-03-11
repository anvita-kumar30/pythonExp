class Employee:
    employee_count = 0
    def _init_(self,  id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    @classmethod
    def set_employee_count(cls):
        cls.employee_count += 1

emp1 = Employee(1)
emp1.set_name("Aayush Wadhwani")
emp1.set_employee_count()
emp2 = Employee(2)
emp2.set_name("Chirag Lulla")
emp2.set_employee_count()
emp3 = Employee(3)
emp3.set_name("Kunal Budhrani")
emp3.set_employee_count()
print("The name and Id of all Employees are:")
print("f'Name ={emp1.get_name()}\tlD ={emp1.get_id()}")
print("f'Name ={emp2.get_name()}\tlD ={emp2.get_id()}")
print("f'Name ={emp3.get_name()}\tlD ={emp3.get_id()}")
print("The total number of employee are ", Employee.employee_count)
