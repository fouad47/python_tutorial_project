# Blueprint for a Car
class Car:
    # The setup function that sets brand and speed.
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    # A method that makes the car drive.
    def drive(self):
        print("The", self.brand, "drives at", self.speed, "km/h! 🏎️")

# Create Car objects from the blueprint.
car1 = Car("Ferrari", 300)
car2 = Car("Mini Cooper", 150)

# Make the cars drive.
car1.drive()
car2.drive()
