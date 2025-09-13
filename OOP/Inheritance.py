# Single Inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class programmer(Person):
#     def printprogram(self):
#         return (f"Programmer Name: {self.name} \nage: {self.age}")
# person3 = programmer("Umer",24)

# print(person3.printprogram())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name: {self.name} \nage: {self.age}")
# class programmer(Person):
#     def printprogram(self):
#         return (f"Programmer Name: {self.name} \nage: {self.age}")
# person1 = Person("Ahmed", 30)
# person2 = Person("Ali", 20)
# person3 = programmer("Umer",24)
# person1.display()
# person2.display()
# print(person3.printprogram())


# Multiple inheritance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_info(self):
#         return (f"Person Name: {self.name} \nage: {self.age}")
# class Student:
#     def __init__(self, student_id):
#         self.student_id = student_id

#     def student_info(self):
#         return f"Student ID: {self.student_id}"
    
# class Developer(Person, Student):
#     pass

# person3 = Developer("Umer",24)

# print(person3.student_info())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_info(self):
#         return (f"Person Name: {self.name} \nage: {self.age}")
# class Student:
#     def __init__(self, student_id):
#         self.student_id = student_id

#     def student_info(self):
#         return f"Student ID: {self.student_id}"
    
# class Developer(Person, Student):
#     language = "Python"
#     def print_language(self):
#         return self.language

# person3 = Developer("Umer",24)

# print(person3.print_language())


# Base class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Single inheritance class
# class Programmer(Person):
#     def printprogram(self):
#         return f"Programmer Name: {self.name}\nAge: {self.age}"

# # Another class
# class Student:
#     def __init__(self, student_id):
#         self.student_id = student_id

#     def student_info(self):
#         return f"Student ID: {self.student_id}"

# # Multiple inheritance class
# class Developer(Programmer, Student):
#     def __init__(self, name, age, student_id):
#         Programmer.__init__(self, name, age)
#         Student.__init__(self, student_id)

#     def display(self):
#         return f"{self.printprogram()}\n{self.student_info()}"

# # Usage
# dev = Developer("Umer", 24, "S12345")
# print(dev.display())


# class Person:
#     var = 9
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_info(self):
#         return (f"Person Name: {self.name} \nage: {self.age}")
# class Student:
#     var = 8
#     def __init__(self, student_id):
#         self.student_id = student_id

#     def student_info(self):
#         return f"Student ID: {self.student_id}"
    
# class Developer(Person, Student):
#     language = "Python"
#     def print_language(self):
#         return self.language

# person3 = Developer("Umer",24)

# print(person3.var)


# and now we change order of Multiple inheritance then check var
# class Person:
#     var = 9
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_info(self):
#         return (f"Person Name: {self.name} \nage: {self.age}")
# class Student:
#     var = 8
#     def __init__(self, student_id):
#         self.student_id = student_id

#     def student_info(self):
#         return f"Student ID: {self.student_id}"
    
# class Developer(Student, Person):
#     language = "Python"
#     def print_language(self):
#         return self.language

# person3 = Developer(24)

# print(person3.var)
y = "this is string"
dir(y)

