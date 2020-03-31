class Person:

    def __init__(self, name, hair_color, height):
        self.name = name
        self.hair_color = hair_color
        self.height = height

    def printing_name(self):
        print(self.name)

    def printing_hair_color(self):
        print(self.hair_color)

    def printing_height(self):
        print(self.height)

class Employee(Person):
    def __init__(self, name, hair_color, height, employee_id):
        Person.__init__(self, name, hair_color, height)
        self.employee_id = employee_id

    def printing_employee_id(self):
        print(self.employee_id)

Joe = Person("Joe", "Brown", "5'10\"")

bob_the_employee = Employee("Bob", "Green", "6-0", "A123")

bob_the_employee.printing_employee_id()

bob_the_employee.printing_name()

