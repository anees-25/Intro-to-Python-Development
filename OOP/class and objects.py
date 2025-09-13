"""
This script demonstrates:
1. Defining classes and creating objects
2. Using instance variables and methods
3. The __init__ constructor
4. Class methods (@classmethod) for alternative constructors
5. Static methods (@staticmethod)
6. Real-world examples with Cars and Employees

Each concept is clearly commented for future reference.
"""


# ========================================
# 1. Basic Class and Object
# ========================================

class Employee:
    """A simple class to represent an employee with a fixed number of leaves."""
    
    # Class variable shared by all instances
    no_of_leaves = 8
    
    pass  # Placeholder for empty class body


# Creating objects (instances) of the Employee class
ahmed = Employee()
ali = Employee()

# Assigning instance attributes
ahmed.name = "Ahmed"
ahmed.salary = 1000
ahmed.role = "Info Desk Helper"

ali.name = "Ali"
ali.salary = 500
ali.role = "Instructor"

# Access class variable
print("Number of leaves (shared):", Employee.no_of_leaves)


# ========================================
# 2. Adding Methods to Class - Instance Method
# ========================================

class EmployeeDetails:
    """Class with instance method to display employee info."""

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def details(self):
        """Returns formatted string with employee information."""
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


# Create employees using constructor
ali = EmployeeDetails("Ali", 500, "Instructor")
ahmed = EmployeeDetails("Ahmed", 1000, "Info Desk Helper")

print("\nEmployee Details:")
print(ali.details())
print(ahmed.details())


# ========================================
# 3. __init__ Constructor and Display Method
# ========================================

class Person:
    """Represents a person with name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        """Prints the person's name and age."""
        print(f"Name: {self.name}\nAge: {self.age}")


# Create person objects
person1 = Person("Ahmed", 30)
person2 = Person("Ali", 20)

print("\nPerson Info:")
person1.display()
person2.display()


# ========================================
# 4. Class Method as Alternative Constructor
# ========================================

class Car:
    """Represents a car with name, model, color."""

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        """Returns formatted description of the car."""
        return f"The Car name is {self.name}.\nThe model is {self.model}.\nThe color is {self.color}"

    @classmethod
    def from_dash(cls, string):
        """
        Alternative constructor to create Car from a dash-separated string.
        Example: "Ferrari-2022-Blue"
        Uses *args unpacking for cleaner code.
        """
        return cls(*string.split("-"))


# Creating cars using different ways
car1 = Car.from_dash("Ferrari-2022-Blue")   # via classmethod
car2 = Car("Toyota", "2017", "White")      # direct
car3 = Car("Honda", "2015", "Red")         # direct

print("\nCars Created:")
print("Car 3 Model:", car3.model)
print(car2.display())
print("Car 1 Model:", car1.model)


# ========================================
# 5. Static Method - Utility Function
# ========================================

class UtilityCar:
    """Same Car class but with a static method for utility messages."""

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        return f"The Car name is {self.name}.\nModel: {self.model}, Color: {self.color}"

    @staticmethod
    def print_good(suffix):
        """Static method: doesn't use class or instance data. Used for general messages."""
        print("This is good" + suffix)


# Test static method
util_car = UtilityCar("Toyota", "2017", "White")
print("\nStatic Method Demo:")
print("Car Model:", util_car.model)
util_car.print_good(" Model")