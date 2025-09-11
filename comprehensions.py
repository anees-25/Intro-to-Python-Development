"""
Lambda, Map, Filter, List/Dict/Set Comprehensions, and Zip

This demonstrates:
1. Using lambda with map() and filter()
2. Traditional loops vs list comprehensions
3. Creating dictionaries using zip() and dict comprehensions
4. Working with sets and set comprehensions

Each section includes both traditional loop approaches and Pythonic alternatives.
"""

# ========================================
# 1. Using map() with lambda
# ========================================

# Given list of numbers
nums = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

# Using map() and lambda to square each number
squared_nums = list(map(lambda n: n * n, nums))
print("Squared numbers using map + lambda:", squared_nums)


# ========================================
# 2. Using filter() with lambda
# ========================================

# Filter even numbers using filter() and lambda
even_nums = list(filter(lambda n: n % 2 == 0, nums))
print("Even numbers using filter + lambda:", even_nums)


# ========================================
# 3. Nested Loops vs List Comprehension
# ========================================

# Traditional way: nested for loops to pair letters with numbers
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print("Nested loop result:", my_list)

# Pythonic way: using list comprehension (equivalent)
my_list_comp = [(letter, num) for letter in 'abcd' for num in range(4)]
print("List comprehension (same result):", my_list_comp)


# ========================================
# 4. Using zip() to pair two lists
# ========================================

names = ['Chris', 'Jack', 'Bob', 'Anne']
heros = ['Superman', 'Spiderman', 'Batman', 'Wonder Woman']

# Pair names with heroes using zip()
paired = list(zip(names, heros))
print("Zipped pairs (name, hero):", paired)


# ========================================
# 5. Building a dictionary manually using zip()
# ========================================

heroes_dict = {}
for name, hero in zip(names, heros):
    heroes_dict[name] = hero
print("Manually created dictionary:", heroes_dict)


# ========================================
# 6. Dictionary Comprehension (Pythonic!)
# ========================================

# Create the same dictionary using dict comprehension
heroes_dict_comp = {name: hero for name, hero in zip(names, heros)}
print("Dictionary comprehension result:", heroes_dict_comp)


# ========================================
# 7. Removing duplicates using set()
# ========================================

nums_with_duplicates = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

# Convert to set to remove duplicates
unique_set = set(nums_with_duplicates)
print("Unique values using set():", unique_set)


# ========================================
# 8. Set Comprehension
# ========================================

# Same as above but using set comprehension (more explicit)
unique_set_comp = {num for num in nums_with_duplicates}
print("Set comprehension result:", unique_set_comp)
