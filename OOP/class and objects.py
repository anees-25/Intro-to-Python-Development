# class - Template
# Object _ Instance of the class 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name} \nage: {self.age}")
person1 = Person("Ahmed", 30)
person2 = Person("Ali", 20)
person1.display()
person2.display()