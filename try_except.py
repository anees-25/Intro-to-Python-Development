
x = 42  # Assigning the value 42 to variable x
y = 0  # Assigning the value 0 to variable y
print()  # Printing a newline character
try:  # Starting a try block
    print(x / y)  # Attempting to divide x by y
except ZeroDivisionError as e:  # Handling ZeroDivisionError exception
    print('Not allowed to divide by zero')  # Printing an error message
else:  # Executing this block if no exception was raised in the try block
    print('Something else went wrong')  # Printing a message indicating an unexpected error
finally:  # Executing this block regardless of whether an exception was raised or not
    print('This is our cleanup code')  # Printing a cleanup message
print()  # Printing a newline character