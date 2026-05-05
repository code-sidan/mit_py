class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, eid, salary):
        super().__init__(name, age)
        self.eid = eid
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, eid, salary, dept):
        super().__init__(name, age, eid, salary)
        self.dept = dept

    def show(self):
        print(self.name, self.age, self.eid, self.salary, self.dept)

m = Manager("sid", 18, 1, 50000, "IT")
m.show()