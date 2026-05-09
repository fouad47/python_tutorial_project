# Blueprint for a Bird
class Bird:
    # It has a make_sound method
    def make_sound(self):
        print("Tweet tweet! 🐦")

# Blueprint for a Duck
class Duck:
    # It ALSO has a make_sound method, but it does something different!
    def make_sound(self):
        print("Quack quack! 🦆")

# A function that takes ANY animal and calls its make_sound method.
# It doesn't care if it's a Bird or a Duck!
def play_sound(animal):
    animal.make_sound()

# Create the objects
birdie = Bird()
ducky = Duck()

# Same function call, but we get different behaviors! This is Polymorphism.
play_sound(birdie)
play_sound(ducky)
