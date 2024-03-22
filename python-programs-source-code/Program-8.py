from abc import ABC, abstractmethod

# Define an abstract class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @abstractmethod
    def display_details(self):
        pass

# Define a subclass of Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year
    
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Define another subclass of Vehicle
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    
    def display_details(self):
        print(f"Truck Details:\nMake: {self.make}\nModel: {self.model}\nCapacity: {self.capacity} tons")

# Create instances of subclasses and display details
car = Car("Toyota", "Camry", 2022)
truck = Truck("Ford", "F-150", 5)

car.display_details()
print()
truck.display_details()
