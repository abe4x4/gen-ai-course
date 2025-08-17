"""
utils.py - Optional utilities for Step 2
"""

# Print object info
def print_object_info(obj):
    print(f"Type: {type(obj)}")
    print(f"Attributes: {dir(obj)}")

# Safe method call
def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error calling function {func.__name__}: {e}")
        return None
