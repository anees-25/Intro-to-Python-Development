# def get_initial(name):  # Define a function that takes 'name' as a parameter
#     initial = name[0:1].upper()  # Extract the first character of 'name' and convert it to uppercase
#     return initial  # Return the uppercase initial

# first_name = input('Enter your first name:')  # Prompt the user to enter their first name
# first_name_initial = get_initial(first_name)  # Call the function with the input and store the result
# print('Your initial is: ' + first_name_initial)  # Print the user's initial


# Adding a force_uppercase Parameter for Conditional Uppercasing
# def get_initial(name, force_uppercase= True):  # Define a function with parameters 'name' and 'for
# ce_uppercase'
#     if force_uppercase:  # Check if 'force_uppercase' is True
#         initial = name[0:1].upper()  # Extract the first character and convert it to uppercase
#     else:  # If 'force_uppercase' is False
#         initial = name[0:1]  # Extract the first character without converting to uppercase
#     return initial  # Return the initial (uppercase or original)

# first_name = input('Enter your first name:')  # Prompt the user to enter their first name
# first_name_initial = get_initial(first_name, False)  # Call the function with the input and 'force_uppercase' set to False
# print('Your initial is: ' + first_name_initial)  # Print the user's initial


# Adding Default Parameter and Using Keyword Arguments for Clarity
def get_initial(name, force_uppercase=True):  # Define a function with two parameters: 'name' (string) and 'force_uppercase' (boolean, default is True)
    if force_uppercase:  # Check if 'force_uppercase' is True
        initial = name[0:1].upper()  # Extract the first character from 'name' and convert it to uppercase
    else:  # If 'force_uppercase' is False
        initial = name[0:1]  # Extract the first character from 'name' without converting to uppercase
    return initial  # Return the processed initial (uppercase or original)

first_name = input('Enter your first name:')  # Prompt the user to input their first name and store it in 'first_name'
first_name_initial = get_initial(name=first_name, force_uppercase=False)  # Call 'get_initial', passing the user's first name and setting 'force_uppercase' to False
print('Your initial is: ' + first_name_initial)  # Print a message along with the user's initial (processed based on the 'force_uppercase' value)

