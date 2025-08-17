# Step 2: Object-Oriented Programming (OOP) & Intermediate Python Concepts

This step introduces **OOP in Python**, which is essential for building scalable AI projects, modular code, and eventually generative AI models and agents.

---

## Topics Covered

### 1. Classes and Objects
- Defining classes
- Creating objects
- Attributes vs methods

### 2. Inheritance
- Subclasses inherit properties and methods from parent classes
- Using `super()` to call parent constructor

### 3. Encapsulation
- Private attributes (`__attribute`)
- Getter and setter methods
- Hiding internal data

### 4. Polymorphism
- Same method name behaves differently in different classes
- Example: `speak()` method in multiple Animal subclasses

### 5. Modules and Packages
- Organizing code into separate files
- Importing classes or functions from modules
- Example: `from utils import Person`

---

## Exercises

1. **Car Class**
   - Attributes: brand, model, year
   - Method: car_info()

2. **ElectricCar Subclass**
   - Inherits Car
   - Adds battery_size
   - Method: battery_info()

3. **Polymorphism**
   - Classes: Circle, Square
   - Method: area()
   - Iterate over different shapes

4. **Encapsulation**
   - Class: StudentGrades
   - Private attribute: __grades
   - Methods: add_grade(), get_average()

---

## Instructions

1. Run `basics_oop.py` to see examples.
2. Run `exercises.py` and experiment with each exercise.
3. Modify, extend, and create new objects to strengthen understanding.
4. Commit progress regularly:

```bash
git add .
git commit -m "Completed Step 2: OOP fundamentals and exercises"
