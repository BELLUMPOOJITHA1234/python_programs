class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method 'make_sound'")

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp! Chirp!"

# Demonstrating polymorphism
print("\n--- Polymorphism Demonstration ---")
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(f"An animal makes sound: {animal.make_sound()}")

