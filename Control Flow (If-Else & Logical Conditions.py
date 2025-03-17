### **Python Control Flow (If-Else & Logical Conditions) - Notes**   

#### **1. Python Conditions**   
# Python supports standard logical conditions:   
# - `==` (Equals)   
# - `!=` (Not Equals)   
# - `<` (Less than)   
# - `<=` (Less than or equal to)   
# - `>` (Greater than)   
# - `>=` (Greater than or equal to)   
# These are used in **if statements** and **loops**.   

#### **2. If Statement**   
a = 33  
b = 200  

# Check if b is greater than a  
if b > a:  
    print("b is greater than a")  # Output: b is greater than a  

# Indentation is required in Python. No indentation will cause an error.   

#### **3. Elif Statement**   
# Checks another condition if the first one is False.  
a = 33  
b = 33  

# Compare values of a and b  
if b > a:  
    print("b is greater")  
elif a == b:  
    print("a and b are equal")  # Output: a and b are equal  

#### **4. Else Statement**   
# Catches anything **not** covered by previous conditions.  
a = 200  
b = 33  

# Compare values of a and b  
if b > a:  
    print("b is greater")  
elif a == b:  
    print("a and b are equal")  
else:  
    print("a is greater")  # Output: a is greater  

# Else can be used without `elif`.   

#### **5. Short-Hand If**   
# One-line `if` statement:  
if a > b: 
    print("a is greater")  

#### **6. Short-Hand If-Else (Ternary Operator)**   
a = 2  
b = 330  

# Use ternary operator to print based on condition  
print("A") if a > b else print("B")  # Output: B  

# Can also have multiple conditions:  
print("A") if a > b else print("=") if a == b else print("B")  

#### **7. Logical Operators**   
# Used to combine conditions.  
# - **And (`and`)**   
if a > b and c > a:  
    print("Both conditions are True")  

# - **Or (`or`)**   
if a > b or a > c:  
    print("At least one condition is True")  

# - **Not (`not`)**   
if not a > b:  
    print("a is NOT greater than b")  

#### **8. Nested If**   
# An `if` inside another `if`.  
x = 41  

# Check if x is greater than 10  
if x > 10:  
    print("Above ten,")  

    # Check if x is also greater than 20  
    if x > 20:  
        print("and also above 20!")  
    else:  
        print("but not above 20.")  

#### **9. The `pass` Statement**   
# Use `pass` to avoid errors in empty statements.  
if b > a:  
    pass  # Placeholder (Does nothing)  

### **Summary**   
# - Use `if`, `elif`, and `else` for conditional checks.   
# - Logical operators: `and`, `or`, `not` for combining conditions.   
# - `pass` allows empty code blocks without errors.   
# - Use **short-hand if** for simple one-liners.   
# - **Nested if** helps in multi-level conditions.