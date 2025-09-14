"""
Topic: Inheritance in Python (Single & Multiple)

Explanation:
Inheritance is a core concept in Object-Oriented Programming (OOP) that allows a class 
(called a child or subclass) to inherit properties and behaviors (attributes and methods) 
from another class (called a parent or superclass). This promotes code reusability and 
logical organization.

Single Inheritance: A class inherits from one parent.
Multiple Inheritance: A class can inherit from two or more classes.
Method Resolution Order (MRO): Python determines the order in which parent classes 
   are checked when calling a method or accessing an attribute. The order depends on how 
   you define the parent classes: `class Child(A, B)` means A is checked before B.
Constructor Handling: When using multiple inheritance, you must explicitly call 
   the __init__ methods of parent classes unless using super() with cooperative design.

Key Takeaways:
- Use inheritance to avoid repeating code.
- Be careful with attribute name conflicts in multiple inheritance.
- Understand MRO to predict behavior in complex hierarchies.
- Always initialize all required attributes in child classes.
"""


# ========================================
# 1. Single Inheritance - Basic Example
# ========================================

class Person:
    """Base class representing a person."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Programmer(Person):
    """Child class inheriting from Person."""
    
    def print_program(self):
        return f"Programmer Name: {self.name}\nAge: {self.age}"


# Create object
prog = Programmer("Umer", 24)
print("=== Single Inheritance ===")
print(prog.print_program())


# ========================================
# 2. Adding Methods in Parent Class
# ========================================

class PersonWithDisplay(Person):
    """Extended version with display method."""
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class ProgrammerEnhanced(PersonWithDisplay):
    """Uses enhanced Person class."""
    
    def print_program(self):
        return f"Programmer Name: {self.name}\nAge: {self.age}"


# Create instances
person1 = PersonWithDisplay("Ahmed", 30)
person2 = PersonWithDisplay("Ali", 20)
prog2 = ProgrammerEnhanced("Umer", 24)

print("\n=== With Display Method ===")
person1.display()
person2.display()
print(prog2.print_program())


# ========================================
# 3. Multiple Inheritance - Simple Case
# ========================================

class Student:
    """Represents a student with ID."""
    
    def __init__(self, student_id):
        self.student_id = student_id

    def student_info(self):
        return f"Student ID: {self.student_id}"


class Developer(ProgrammerEnhanced, Student):
    """Combines Programmer and Student (inherits both)."""
    
    language = "Python"

    def print_language(self):
        return f"Preferred Language: {self.language}"


# Note: We haven't initialized Student.__init__ yet → will cause error if used
# Let's fix that below


# ========================================
# 4. Multiple Inheritance with Proper Init
# ========================================

class DeveloperFull(Programmer, Student):
    """
    Correctly initializes both parent classes.
    Demonstrates manual constructor chaining.
    """
    
    def __init__(self, name, age, student_id):
        # Explicitly initialize both parents
        Programmer.__init__(self, name, age)
        Student.__init__(self, student_id)

    def display(self):
        """Combine output from both parents."""
        return f"{self.print_program()}\n{self.student_info()}"


dev = DeveloperFull("Umer", 24, "S12345")
print("\n=== Multiple Inheritance (Proper Init) ===")
print(dev.display())
print(dev.print_language())


# ========================================
# 5. Method Resolution Order (MRO) - Attribute Conflict
# ========================================

class PersonMRO:
    var = 9  # Class variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentMRO:
    var = 8  # Same name → conflict!
    
    def __init__(self, student_id):
        self.student_id = student_id


# Case 1: Person first → var = 9
class DeveloperMRO(PersonMRO, StudentMRO):
    def get_var(self):
        return self.var


# Case 2: Student first → var = 8
class DeveloperMROReversed(StudentMRO, PersonMRO):
    def get_var(self):
        return self.var


dev1 = DeveloperMRO("Ali", 25)
dev2 = DeveloperMROReversed("Ahmed", 30)

print("\n=== Method Resolution Order (MRO) ===")
print("DeveloperMRO(Person, Student):", dev1.var)           # Output: 9
print("DeveloperMROReversed(Student, Person):", dev2.var)   # Output: 8

# Optional: View the search order
print("MRO for DeveloperMRO:", [cls.__name__ for cls in DeveloperMRO.__mro__])
print("MRO for DeveloperMROReversed:", [cls.__name__ for cls in DeveloperMROReversed.__mro__])
