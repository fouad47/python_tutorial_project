# This is the Parent Class. It has basic features.
class Animal:
    # A simple method that all animals can do.
    def eat(self):
        print("I am eating! 🍽️")

# This is the Child Class. We put the parent name in parentheses: Cat(Animal).
# This means Cat gets ALL the features of Animal for free!
class Cat(Animal):
    # Cat has its own special method that Animal doesn't have.
    def meow(self):
        print("Meow! 🐱")

# We create a Cat object.
kitty = Cat()

# We can call the eat method because Cat INHERITED it from Animal.
kitty.eat()   

# We can call the meow method because it belongs to Cat.
kitty.meow()
