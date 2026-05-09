# Parent Class
class Animal:
    def __init__(self, name):
        # Every animal has a name.
        self.name = name
        
    def sleep(self):
        # Every animal can sleep.
        print(self.name, "is sleeping. Zzz...")

# Child Class inheriting from Animal
class Dog(Animal):
    def bark(self):
        # Only dogs can bark!
        print(self.name, "says Woof Woof! 🐶")

# We build a Dog object and pass the name "Buddy".
# It uses the __init__ from the Animal class!
my_dog = Dog("Buddy")

# We use the inherited sleep method.
my_dog.sleep()

# We use the Dog's specific bark method.
my_dog.bark()
