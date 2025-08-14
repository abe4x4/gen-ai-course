"""
exercises.py
Step 1: Python Fundamentals Exercises
Practice your Python skills with these exercises.
"""

# =============================
# 1. CALCULATOR
# =============================
# Create a simple calculator that adds, subtracts, multiplies, or divides two numbers
def calculator():
    print("=== Simple Calculator ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero!"
    else:
        result = "Invalid operation!"

    print("Result:", result)

# Uncomment the line below to run the calculator
# calculator()

# =============================
# 2. NUMBER GUESSING GAME
# =============================
# The computer randomly picks a number, and the user tries to guess it
import random

def number_guessing_game():
    print("\n=== Number Guessing Game ===")
    number_to_guess = random.randint(1, 20)
    attempts = 5

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess == number_to_guess:
            print("Congratulations! You guessed it right!")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"Game over! The number was: {number_to_guess}")

# Uncomment to play the game
# number_guessing_game()

# =============================
# 3. LIST MANIPULATION EXERCISE
# =============================
# Create a list of 5 favorite fruits, add one fruit, remove one, and print all
def list_exercise():
    fruits = ["apple", "banana", "cherry", "mango", "grapes"]
    print("\nOriginal list:", fruits)

    # Add a fruit
    fruits.append("orange")
    print("Added orange:", fruits)

    #

