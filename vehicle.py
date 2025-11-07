# this program is the vehicle class example
# the first program based on the instructions and one of the videos 
# demonstrates defining a class, creating objects, and using methods.

class Vehicle:
    def __init__(self, style, doors, color):
        self.style = style
        self.doors = doors
        self.color = color

    def display_info(self):
        print(f"Vehicle style: {self.style}")
        print(f"Number of doors: {self.doors}")
        print(f"Color: {self.color}")
car1 = Vehicle("Car", 4, "Red")
truck1 = Vehicle("Truck", 2, "Blue")

car1.display_info()
print()
truck1.display_info()
