# Decorator function to convert a string to uppercase
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Decorator function to add a prefix to a string
def prefix_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return prefix + result
        return wrapper
    return decorator

# Decorator function to add a suffix to a string
def suffix_decorator(suffix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + suffix
        return wrapper
    return decorator

# Function with multiple decorators chained
@suffix_decorator("!!!")
@prefix_decorator("Result: ")
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

# Using the decorated function
print(greet("Alice"))
