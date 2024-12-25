#To get current date and time we need  to use the datetime library
# import datetime
#The now function returns current date and time as a datetime object
# current_datetime = datetime.datetime.now()
#We must connvert the datetime object to a string
#before we can concatenate it to another string
# print('Today is:' + str(current_datetime))

from datetime import datetime, timedelta
today= datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was:' + str(yesterday))

## more Examples
# from datetime import datetime, timedelta
# today= datetime.now()
# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print('Last week was:' + str(last_week))

# from datetime import datetime, timedelta
# # Get the current date and time
# current_datetime = datetime.now()

# # Add 5 days and 3 hours to the current datetime
# future_datetime = current_datetime + timedelta(days=5, hours=3)

# print("Current Date and Time:", current_datetime)
# print("Future Date and Time:", future_datetime)

# from datetime import datetime, timedelta
# # Get the current date and time
# current_datetime = datetime.now()

# # Add 5 days and 3 hours to the current datetime
# future_datetime = current_datetime + timedelta(days=5, hours=10, weeks=5, )

# print("Current Date and Time:", current_datetime)
# print("Future Date and Time:", future_datetime)


# from datetime import datetime, timedelta
# today= datetime.now()
# print('Day: ' + str(today.day))
# print('Month: ' + str(today.month))
# print('Year: ' + str(today.year))
# print('Hour: ' + str(today.hour))
# print('Minute: ' + str(today.minute))


# The strptime() function in Python is used to convert a string into a datetime object.
# from datetime import datetime

# # Define a date string in a specific format
# date_string = "2022-01-01"

# # Define the format of the date string
# date_format = "%Y-%m-%d"

# # Convert the date string to a datetime object
# date_object = datetime.strptime(date_string, date_format)

# # Now you can use the date_object for further operations
# print(date_object)  # Output: 2022-01-01 00:00:00

#More example
# from datetime import datetime, timedelta
# birthday= input('When is your birthday (dd/mm/yyyy)')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print('Birthday:' + str(birthday_date))
# #Day before birthday
# one_day= timedelta(days=1)
# birthday_eve = birthday_date - one_day
# print('Day befor bithday:' + str(birthday_eve))
