"""
exercises.py
Step 2: OOP Practice Exercises
"""

# 1. CREATE A CLASS
# Create a class `Car` with attributes: brand, model, year
# Add a method to display car info
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Test
car1 = Car("Tesla", "Model 3", 2022)
car1.car_info()

# 2. INHERITANCE EXERCISE
# Create class ElectricCar inheriting from Car
# Add battery_size attribute and a method to show battery info
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def battery_info(self):
        print(f"{self.brand} {self.model} has a {self.battery_size}-kWh battery.")

ecar = ElectricCar("Tesla", "Model S", 2023, 100)
ecar.car_info()
ecar.battery_info()

# 3. POLYMORPHISM EXERCISE
# Create classes Circle and Square with a method area()
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print("Area:", shape.area())

# 4. ENCAPSULATION EXERCISE
# Create class StudentGrades with private attribute __grades (list)
# Add methods: add_grade(), get_average()
class StudentGrades:
    def __init__(self):
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

student = StudentGrades()
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)
print("Average grade:", student.get_average())
