"""
basics_oop.py
Step 2: Python OOP & Intermediate Concepts
"""

# =============================
# 1. CLASS & OBJECT BASICS
# =============================

class Person:
    """A simple class representing a person"""
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def greet(self):
        """Print a greeting"""
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")

# Create objects
person1 = Person("Ibrahim", 25)
person2 = Person("Alice", 30)

person1.greet()
person2.greet()

# =============================
# 2. INHERITANCE
# =============================

class Student(Person):
    """Student inherits from Person"""
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # call parent constructor
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

student1 = Student("Bob", 20, "S12345")
student1.greet()   # inherited method
student1.study()   # own method

# =============================
# 3. ENCAPSULATION
# =============================

class BankAccount:
    """Example of encapsulation"""
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Ibrahim", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance accessed via getter:", account.get_balance())

# =============================
# 4. POLYMORPHISM
# =============================

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.speak()  # each object responds differently

# =============================
# 5. MODULES AND PACKAGES
# =============================
# You can save this class in a separate file e.g., utils.py and import it
# Example:
# from utils import Person
