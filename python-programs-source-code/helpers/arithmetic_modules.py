def add(a, b):
    """Function to perform addition."""
    return a + b

def subtract(a, b):
    """Function to perform subtraction."""
    return a - b

def multiply(a, b):
    """Function to perform multiplication."""
    return a * b

def divide(a, b):
    """Function to perform division."""
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b
