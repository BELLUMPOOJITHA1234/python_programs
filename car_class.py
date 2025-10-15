# Define the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.running = False  # to keep track of the car's state

    def start(self):
        if not self.running:
            self.running = True
            print(f"The {self.year} {self.make} {self.model} is now started.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print(f"The {self.year} {self.make} {self.model} has been stopped.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Use the methods
my_car.start()
my_car.stop()
my_car.stop()  # demonstrate stopping when already stopped
