# class - Template
# Object _ Instance of the class 

# class Employee:
#     no_of_employees = 8
#     pass
# Ahmed = Employee()
# Ali = Employee()
# print(Ahmed.no_of_employee)


# class Employee:
#     no_of_leaves = 8
#     def details(self):
#         return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
# Ali = Employee()
# Ahmed = Employee()

# Ali.name = "Ali"
# Ali.salary = 500
# Ali.role = "Instructor"

# Ahmed.name = "Ahmed"
# Ahmed.salary = 1000
# Ahmed.role = "Info Desk Helper"

# print(Ahmed.details())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name: {self.name} \nage: {self.age}")
# person1 = Person("Ahmed", 30)
# person2 = Person("Ali", 20)
# person1.display()
# person2.display()


# Class Methods as Alternative Constuctor
# class Cars:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def Display(self):
#         return f"The Car name is {self.name}.\nThe model is {self.model}.\nThe color is {self.color}"

#     @classmethod
#     def from_dasd(cls, string):
#         param = string.split("-")
#         return cls(param[0], param[1], param[2])

# car1 = Cars.from_dash("Ferarri-2022-Blue")
# car2 = Cars("Toyota", "2017", "White")
# car3 = Cars("Honda", "2015", "Red")

# print(car3.model)            # Should print: 2015
# print(car2.Display())        # Displays details of car2
# print(car1.model)            # Should print: 2022
# OR
# class Cars:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def Display(self):
#         return f"The Car name is {self.name}.\nThe model is {self.model}.\nThe color is {self.color}"

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

# car1 = Cars.from_dash("Ferarri-2022-Blue")
# car2 = Cars("Toyota", "2017", "White")
# car3 = Cars("Honda", "2015", "Red")

# print(car3.model)            # Should print: 2015
# print(car2.Display())        # Displays details of car2
# print(car1.model)            # Should print: 2022


# Static Method
# class Cars:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def Display(self):
#         return f"The Car name is {self.name}.\nThe model is {self.model}.\nThe color is {self.color}"

#     @staticmethod
#     def printgood(string):
#         print("This is good" + string)

# car1 = Cars("Toyota", "2017", "White")
# car3 = Cars("Honda", "2015", "Red")

# print(car1.model)            
# print(car3.model)          

# car1.printgood(" Model")