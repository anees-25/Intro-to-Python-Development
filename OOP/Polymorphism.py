# ==============================================================================
# POLYMORPHISM 
# ==============================================================================
# What is Polymorphism?
#
# Polymorphism means "many forms". In Python, it lets different objects respond
# to the same method name in their own way. You don't need to know what type of
# object you're dealing with — as long as it has the method you're calling,
# Python will run its version of that method.
#
# This makes your code:
#   - Cleaner (same method name everywhere)
#   - Shorter (loop over many types with one line)
#   - Easier to extend (add new classes without changing old code)
#
# Python uses "Duck Typing": If it walks like a duck and quacks like a duck,
# then it’s a duck. No need for inheritance or interfaces — just use the method!
#
# Example: All vehicles can "drive()", but a Car drives on roads, a Boat on water.
# We call .drive() on each — and each does its own thing. That’s polymorphism!
#
# This file shows:
#   1. Without polymorphism → messy code
#   2. With polymorphism → clean, powerful, Pythonic code
#   3. Real-world example with shapes
#   4. Why it’s so useful in practice
# ==============================================================================

# ========================
# WITHOUT POLYMORPHISM
# ========================
# Imagine we have 3 vehicles. We write separate functions for each.
# This is hard to manage and doesn’t scale!

def drive_car():
    print("Car is driving on roads!")

def drive_bike():
    print("Bike is riding on roads!")

def drive_boat():
    print("Boat is sailing on water!")

# Now if we want to make all vehicles move, we must call each function separately:
print("=== WITHOUT POLYMORPHISM ===")
drive_car()
drive_bike()
drive_boat()

# Problem: Adding a new vehicle? Write a new function. Looping? Impossible without if-statements.
# This gets messy fast when you have 10+ types!


# ========================
# WITH POLYMORPHISM
# ========================
# Now let’s do it the Python way: Same method name, different behavior.

class Car:
    def drive(self):
        print("Car is driving on roads!")

class Bike:
    def drive(self):
        print("Bike is riding on roads!")

class Boat:
    def drive(self):
        print("Boat is sailing on water!")

# Create objects
my_car = Car()
my_bike = Bike()
my_boat = Boat()

# Now call the SAME method on all of them — no if-statements needed!
print("\n=== WITH POLYMORPHISM ===")
my_car.drive()
my_bike.drive()
my_boat.drive()

# MAGIC: Loop over them!
vehicles = [Car(), Bike(), Boat()]
print("\n=== LOOPING WITH POLYMORPHISM ===")
for vehicle in vehicles:
    vehicle.drive()  # Works for ANY object that has .drive() — even if we didn't plan for it!

# This is called DUCK TYPING: "If it has .drive(), it's good enough!"


# ========================
# REAL-WORLD EXAMPLE: SHAPES
# ========================
# Let’s calculate area for different shapes — all using the same method name!

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

# Now create a list of shapes and calculate areas — all with ONE loop!
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

print("\n=== CALCULATING AREAS WITH POLYMORPHISM ===")
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

# Add a new shape? Just define it with .area() — no changes to the loop!
class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

shapes.append(Square(4))
print(f"\nAdded Square: Area = {shapes[-1].area()}")


# ========================
# WHAT IF THE METHOD IS MISSING?
# ========================
# Polymorphism only works if the method exists.
print("\n=== ERROR CASE: Missing Method ===")
class Rock:
    pass  # No drive() method!

rock = Rock()
try:
    rock.drive()  # This will crash!
except AttributeError as e:
    print(f"Error: {e}")
print("→ Always make sure your classes implement the expected methods!")


# ========================
# BONUS: Duck Typing in Action
# ========================
# Even if Rock isn't a vehicle, if we give it .drive(), it works!
class Robot:
    def drive(self):
        print("Robot is rolling silently!")

robot = Robot()
print("\n=== DUCK TYPING: Any object with .drive() works! ===")
robot.drive()  # Works even though Robot is unrelated to Car/Bike/Boat!


# ========================
# CONCLUSION
# ========================
print("\n" + "="*60)
print("KEY TAKEAWAYS:")
print("- Polymorphism = Same method name, different behavior.")
print("- Use loops to process many different objects with one line.")
print("- No need for type checking — Python uses 'duck typing'.")
print("- Easy to extend: Just add a new class with the same method!")
print("- Clean, readable, and Pythonic code!")
print("="*60)