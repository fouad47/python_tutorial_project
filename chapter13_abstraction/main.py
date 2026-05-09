# We import special tools to create Abstract classes.
from abc import ABC, abstractmethod

# An Abstract class is an empty blueprint. You cannot build an object from it directly.
class Shape(ABC):
    
    # @abstractmethod means "Whoever inherits from me MUST write their own draw() code".
    @abstractmethod
    def draw(self):
        pass # The word 'pass' means do nothing. It's left blank on purpose.

# Circle inherits from Shape, so it MUST implement the draw method.
class Circle(Shape):
    def draw(self):
        print("Drawing a round circle! ⭕")

# Square inherits from Shape, so it MUST implement the draw method.
class Square(Shape):
    def draw(self):
        print("Drawing a square box! ⬛")

# We build our shapes and draw them!
c = Circle()
c.draw()

s = Square()
s.draw()
