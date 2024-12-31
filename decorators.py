# //What are Decorators in Python?
# A decorator in Python is a design pattern that allows you to modify or extend the behavior of a function or method without changing its code. It’s a powerful and flexible feature of Python used to wrap functions and add extra functionality.
def logger(func):  # Define a decorator function named 'logger' that takes another function as an argument
    def wrapper():  # Define an inner function (wrapper) to modify or extend the behavior of 'func'
        print('Logging execution')  # Print a message before executing the original function
        func()  # Call the original function passed to the decorator
        print('Done logging')  # Print a message after executing the original function
    return wrapper  # Return the wrapper function as the modified version of 'func'

@logger  # Apply the 'logger' decorator to the 'sample' function
def sample():  # Define a simple function named 'sample'
    print('-- Inside sample function')  # Print a message to indicate the function's main behavior
