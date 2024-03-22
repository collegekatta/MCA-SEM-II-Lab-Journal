# Custom exception for odd age
class OddAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"AgeError: Age '{self.age}' is odd. Please enter an even age."

# Custom exception for even age
class EvenAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"AgeError: Age '{self.age}' is even. Please enter an odd age."

def check_age(age):
    if age % 2 == 0:
        raise EvenAgeError(age)
    else:
        raise OddAgeError(age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Please enter a valid integer.")
except OddAgeError as odd_error:
    print(odd_error)
except EvenAgeError as even_error:
    print(even_error)
