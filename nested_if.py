country = input("What country do you live in?")  # Prompting the user to enter their country
if country.lower() == 'Canada':  # Checking if the country is Canada (case-insensitive)
    province = input("What province/state do you live in?")  # Prompting the user to enter their province/state
    if province in ('Alberta', 'Nunavut', 'Yukon'):  # Checking if the province/state is Alberta, Nunavut, or Yukon
        tax = 0.05  # Assigning the tax rate as 5% (0.05)
    elif province == "Ontario":  # Checking if the province/state is Ontario
        tax = 0.13  # Assigning the tax rate as 13% (0.13)
    else:  # If the province/state is not Alberta, Nunavut, Yukon, or Ontario
        tax = 0.15  # Assigning the tax rate as 15% (0.15)
else:  # If the country is not Canada
    tax = 0.0  # Assigning the tax rate as 0% (0.0)
print(tax)  # Printing the tax rate