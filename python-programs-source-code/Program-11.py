class MathOperations:
    def add(self, a=None, b=None, *args):
        if a is not None and b is not None:
            return a + b
        elif a is not None and b is None:
            return a
        elif a is None and b is not None:
            return b
        else:
            return sum(args)

# Create an instance of the MathOperations class
math = MathOperations()

# Function overloading demonstration
print("Function overloading demonstration")
print("Addition:", math.add(5, 3))            # Adding two numbers
print("Single Value:", math.add(5))            # Returning single value
print("No Value:", math.add())                 # Returning 0
print("Multiple Values:", math.add(1, 2, 3, 4)) # Adding multiple values

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real) - (self.imaginary * other.imaginary),
                             (self.real * other.imaginary) + (self.imaginary * other.real))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Create instances of ComplexNumber class
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 4)

# Operator overloading demonstration
print("\n===================================================")
print("Operator overloading demonstration")
print("Addition:", c1 + c2)  # Addition using overloaded '+'
print("Subtraction:", c1 - c2)  # Subtraction using overloaded '-'
print("Multiplication:", c1 * c2)  # Multiplication using overloaded '*'
