# Python For Loops - Summary for Notes
# 1. For Loop Concept
# Used to iterate over sequences (list, tuple, dictionary, set, string).
# Works like an iterator, executing statements for each item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. Looping Through a String
Strings are iterable, so we can loop through characters.

for x in "banana":
  print(x)
3. The break Statement
Stops the loop when a condition is met.

for x in fruits:
  if x == "banana":
    break
  print(x)
4. The continue Statement
Skips the current iteration and continues with the next.

for x in fruits:
  if x == "banana":
    continue
  print(x)
5. The range() Function
Used to loop a specified number of times.

for x in range(6):  # Output: 0 to 5
  print(x)
With start & end: range(2, 6) → (2,3,4,5)
With step: range(2, 30, 3) → (2,5,8,...,29)
6. Else in For Loop
Executes after the loop only if no break occurs.

for x in range(6):
  print(x)
else:
  print("Loop finished!")
7. Nested Loops
A loop inside another loop.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
8. The pass Statement
Used when a loop must be present but should do nothing.

for x in [0, 1, 2]:
  pass


# Python While Loops - Summary for Notes
# 1. While Loop
# Executes a block of code as long as the condition is True.
# Always increment the variable inside the loop to avoid infinite loops.

i = 1  
while i < 6:  # Loop runs while i is less than 6  
    print(i)  
    i += 1  # Increment i to avoid an infinite loop  

# Output:
# 1
# 2
# 3
# 4
# 5
2. The break Statement
Used to stop the loop even if the condition is still True.

i = 1  
while i < 6:  
    print(i)  
    if i == 3:  # Stop when i reaches 3  
        break  
    i += 1  

# Output:
# 1
# 2
# 3
3. The continue Statement
Skips the current iteration and moves to the next.

i = 0  
while i < 6:  
    i += 1  
    if i == 3:  # Skip printing 3  
        continue  
    print(i)  

# Output:
# 1
# 2
# 4
# 5
# 6
4. The else Statement
Runs when the loop condition becomes false.
Does not execute if the loop is exited with break.

i = 1  
while i < 6:  
    print(i)  
    i += 1  
else:  
    print("i is no longer less than 6")  

# Output:
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6