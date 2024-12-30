# //Modules in Python
#A module is a single Python file that contains code, such as functions, classes, and variables, which you can use in other Python programs by importing it.

# Example of a Custom Module: helpers.py
def display(message, is_warning=False):  # Define a function with parameters 'message' and 'is_warning' (default is False)
    if is_warning:  # Check if 'is_warning' is True
        print('Warning!!')  # Print "Warning!!" if the condition is True
    print(message)  # Print the value of 'message'

    # Note: Use this module in using_module.py file

