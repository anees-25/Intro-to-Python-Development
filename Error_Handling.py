##Defining Terms
#Error handling:
# is about making our code resilient and user-friendly, preventing unexpected crashes.e.g:Entering a wrong PIN at an ATM prompts "Invalid PIN" instead of swallowing our card—it handles the error gracefully.

# Debugging is about finding and fixing mistakes in our code to make it work correctly.e.g: If our car won't start, wou check the battery, fuel, or engine to find and fix the issue.
# In short:
# Error Handling is about dealing with expected mistakes (like a wrong PIN) smoothly.
# Debugging is about finding and fixing unexpected problems (like a car that won’t start).

# Error types:
# Syntax Error
# Definition: An error that occurs when the rules of the language are broken; it prevents the program from running.
#Example: Forgetting to close quotes in a sentence—like writing Hello, world instead of "Hello, world."—makes it unreadable.
# Code:
#This code won't run at all
# x = 42           # Correct: Assigns the value 42 to variable x.
# y = 206          # Correct: Assigns the value 206 to variable y.
# if x == y        # Syntax Error: Missing colon (:) at the end of the if statement.
#  print('Success!!')  # Incorrect indentation: The print statement should be indented properly.

# 2. Runtime Error
# Definition: An error that occurs while the program is running, causing it to crash unexpectedly.
# Example: Trying to divide a number by zero is like asking a calculator to divide 10 by 0—it results in an error once you try it.
#Code:
# x = 10      # Correct: Assigns the value 10 to variable x.
# y = 0       # Correct: Assigns the value 0 to variable y.
# print(x/y)  # Runtime Error: Division by zero, which is not allowed in mathematics.
# Catching runtime Error
# try:  # Start a block where you "try" to run the code that may raise an error.
#     print(x/y)  # Attempts to divide x by y. If y is zero, a ZeroDivisionError will be raised.
# except ZeroDivisionError as e:  # Catches specifically the "division by zero" error.
#     # The error message is stored in 'e', which you can use for logging (not shown here).
#     print('Sorry, something went wrong')  # Prints a user-friendly message.
# except:  # Catches any other types of exceptions that aren't ZeroDivisionError.
#     print('Something really went wrong')
# finally:  # This block always executes, no matter if an error was raised or not.
#     print('This always runs on success or failure')

# 3. Logic Error
# Definition: An error where the program runs without crashing but produces incorrect results due to flawed logic.
# Example: Setting an alarm for 7 PM instead of 7 AM—everything works, but you wake up too late because the time was wrong.
#Code:
#This code won't run at all
# x = 88  # Correct: Assigns the value 88 to variable x.
# y = 42  # Correct: Assigns the value 42 to variable y.

# if x < y:  # Logic Error: The condition checks if x is less than y, but x (88) is actually greater than y (42).
#     print(str(x) + ' is greater than ' + str(y))  # Incorrect output since the condition is wrong.
# (Note: To fix the logic error, we should change the condition to if x > y:)