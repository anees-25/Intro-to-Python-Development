###Python Functions - Summary for Notes 

####1. Defining a Function
# - Use `def` keyword to define a function.  
def greet():
    print("Hello, welcome to Python!")

greet()
# Output:
# Hello, welcome to Python!

####2. Function with Parameters 
# - Functions can accept values as arguments.  
def add(a, b):
    return a + b

print(add(5, 3))  
# Output:
# 8

####3. Default Parameter Values 
# - If no argument is provided, the default value is used.  
def greet(name="Guest"):
    print("Hello,", name)

greet()         # Uses default value  
greet("Alice")  # Uses passed value  
# Output:
# Hello, Guest
# Hello, Alice

####4. Arbitrary Arguments (`*args`)
# - Allows passing multiple positional arguments.  
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  
# Output:
# 10
#### 5. Arbitrary Keyword Arguments (`kwargs`)  
# - Allows passing multiple key-value pairs.  
def person_info(details):
    for key, value in details.items():
        print(key, ":", value)

person_info(name="John", age=30, city="New York")
"""
Output:
name : John
age : 30
city : New York
"""

#### 6. The `return` Statement  
# - Functions can return values.  
def multiply(x):
    return x * 5

print(multiply(3))  
print(multiply(5))  
"""
Output:
15
25
"""
#### 7. The `pass` Statement  
# - Used when defining an empty function.  
def my_function():
    pass  # Placeholder for future code
#### 8. Positional-Only Arguments (`/,`)  
# - Forces arguments to be passed positionally.  
def my_function(x, /):
    print(x)

my_function(3)  
# Output:
# 3
# - Using `my_function(x=3)` will cause an error.

#### 9. Keyword-Only Arguments (`*,`)  
# - Forces arguments to be passed as keywords.  
def my_function(*, x):
    print(x)

my_function(x=3)  
# Output:
# 3
# - Using `my_function(3)` will cause an error.

#### 10. Combining Positional & Keyword-Only  
# - Use `/` for positional-only and `*` for keyword-only.  
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)
# Output:
# 26


### More Examples
# def greet():
#     print("Hello, how are you")
# greet()


# def greet(name):
#     print(f"Hello, {name}! How are you?")

# greet("Alice")
# greet("Bob")


# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# greet("Alice")
# greet("Bob", "


# def info(details):
#     for key, value in details.items():
#         print(key, ":", value)
# info(name= "anees", age= "23")


# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "mango"]
# my_function(fruits)
