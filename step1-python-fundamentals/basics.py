"""
basics.py
Step 1: Python Fundamentals
This file covers basic Python concepts for beginners.
Each section has examples and comments to explain what's happening.
"""

# =============================
# 1. VARIABLES AND DATA TYPES
# =============================
# Python variables can store numbers, text, or other data types
# You do not need to declare the type explicitly

# Integer
age = 25
print("Age:", age)

# Float
height = 5.9
print("Height:", height)

# String
name = "Ibrahim"
print("Name:", name)

# Boolean
is_student = True
print("Is student:", is_student)

# =============================
# 2. BASIC OPERATORS
# =============================
a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Integer Division:", a // b)  # 3
print("Modulo (remainder):", a % b) # 1
print("Exponent:", a ** b)          # 1000

# =============================
# 3. CONDITIONAL STATEMENTS
# =============================
if age < 18:
    print("You are a minor")
elif age < 30:
    print("You are a young adult")
else:
    print("You are an adult")

# =============================
# 4. LOOPS
# =============================

# For loop
print("\nFor loop example:")
for i in range(5):  # prints 0,1,2,3,4
    print("Iteration:", i)

# While loop
print("\nWhile loop example:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # same as count = count + 1

# =============================
# 5. FUNCTIONS
# =============================

# Define a function
def greet(name):
    """This function greets the person with their name"""
    return f"Hello, {name}!"

print(greet("Ibrahim"))

# Function with default arguments
def power(base, exponent=2):
    return base ** exponent

print("5 squared:", power(5))       # Uses default exponent=2
print("2^5:", power(2, 5))          # Overrides default

# =============================
# 6. LISTS (ARRAYS)
# =============================
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Access elements
print("First fruit:", fruits[0])

# Add element
fruits.append("orange")
print("Added orange:", fruits)

# Remove element
fruits.remove("banana")
print("Removed banana:", fruits)

# Loop through list
for fruit in fruits:
    print("Fruit:", fruit)

# =============================
# 7. DICTIONARIES (KEY-VALUE PAIRS)
# =============================
person = {
    "name": "Ibrahim",
    "age": 25,
    "city": "Louisville"
}
print("Person dictionary:", person)

# Access value
print("Name:", person["name"])

# Add new key-value
person["profession"] = "AI Developer"
print("Added profession:", person)

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# =============================
# 8. TUPLES (IMMUTABLE LISTS)
# =============================
coordinates = (10, 20)
print("Coordinates:", coordinates)

# =============================
# 9. SETS (UNIQUE ELEMENTS)
# =============================
colors = {"red", "green", "blue", "red"}  # duplicates removed automatically
print("Colors set:", colors)

# Add element
colors.add("yellow")
print("Added yellow:", colors)

# Remove element
colors.discard("green")
print("Removed green:", colors)

# =============================
# 10. FILE I/O (READ & WRITE)
# =============================
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is Step 1 of Python Fundamentals.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("\nFile content:\n", content)

# =============================
# 11. EXCEPTION HANDLING
# =============================
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("That's not a valid number!")
else:
    print("Result is:", y)
finally:
    print("Execution completed.")
