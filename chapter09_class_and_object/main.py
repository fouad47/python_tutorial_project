# We use 'class' to create a blueprint. Let's make a Robot blueprint.
class Robot:
    # The __init__ function is the "constructor". It runs automatically when a new Robot is built.
    # 'self' means "this specific robot we are building right now".
    def __init__(self, name, color):
        # We attach the given name and color to the robot itself.
        self.name = name
        self.color = color
        
    # This is a method (a function inside a class). It makes the robot talk.
    def introduce(self):
        print("Hello! I am", self.name, "and I am", self.color)

# We use the blueprint to build an actual Object (a real robot!).
# "R2D2" and "Blue and White" get passed to the __init__ function.
robot1 = Robot("R2D2", "Blue and White")

# We build a second object.
robot2 = Robot("Wall-E", "Yellow")

# We tell the robots to use their introduce method.
robot1.introduce()
robot2.introduce()
