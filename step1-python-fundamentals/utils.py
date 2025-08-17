"""
utils.py - Optional utilities for Step 1
"""

# Print a separator line for clarity
def print_separator(title=""):
    print("\n" + "="*50)
    if title:
        print(title)
        print("="*50)

# Safe integer input
def safe_input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input, returning 0")
        return 0

# Safe float input
def safe_input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input, returning 0.0")
        return 0.0
