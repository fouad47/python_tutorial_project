import os

base_dir = "kids_python_project"
os.makedirs(base_dir, exist_ok=True)

files = {}

# ROOT FILES
files["README.md"] = """# 🚀 Python Storybook for Kids
Welcome to the most fun Python learning project! 
Here you will learn programming from zero to hero. You will build games, program robots, and learn about AI!

## 🛠️ How to Setup
1. **Install Python**: Go to python.org and download the latest version.
2. **Install VS Code**: Download Visual Studio Code from code.visualstudio.com (or Cursor).
3. **Run a file**: Open terminal in VS Code, go to the chapter folder, and type `python main.py`

Let's start learning and have fun! 🎈
"""

files["requirements.txt"] = """pandas
matplotlib
scikit-learn
"""

# CHAPTER 1
files["chapter01_what_is_programming/README.md"] = """# Chapter 1: What is Programming? 🤖
Imagine you have a robot friend. But your friend only speaks a special language. 
Programming is just learning how to talk to your computer or robot to give it instructions!
Python is one of the easiest languages to learn.

## What you learned:
- We learned what programming is.
- We learned how to say hello to the computer!

## Practice Exercise:
Change the `main.py` to say hello to your pet!

## Mini Challenge:
Can you make the robot say 3 different greetings in `robot_says_hello.py`?
"""

files["chapter01_what_is_programming/main.py"] = """
# Welcome to Chapter 1!
# Here we will learn how to make the computer talk.

# This is our first command. It tells the computer to print a message.
print("Hello, world! I am learning Python! 🚀")

# Expected Output:
# Hello, world! I am learning Python! 🚀
"""

files["chapter01_what_is_programming/robot_says_hello.py"] = """
# Let's make a robot say hello!
print("Beep boop! 🤖")
print("Hello! I am Robo, your new coding friend.")
print("Are you ready to learn?")

# Expected Output:
# Beep boop! 🤖
# Hello! I am Robo, your new coding friend.
# Are you ready to learn?
"""

# CHAPTER 2
files["chapter02_print_and_comments/README.md"] = """# Chapter 2: Print Statements and Comments 🖨️
`print()` is how we show things on the screen.
Comments are notes we write for ourselves. The computer ignores them completely!

## What you learned:
- Using print() for text
- Using # for single-line comments
- Using ''' for multi-line comments

## Practice Exercise:
Write a comment explaining your favorite food.

## Mini Challenge:
Print a picture of a cat using multiple print() statements and text symbols!
"""

files["chapter02_print_and_comments/main.py"] = """
# This is a single line comment! The computer will NOT read this line.

print("I can print anything!") # This prints a message.

'''
This is a multi-line comment.
You can write a whole story here.
The computer will ignore it all.
'''
print("Comments are cool because they help us remember what code does.")

# Expected Output:
# I can print anything!
# Comments are cool because they help us remember what code does.
"""

files["chapter02_print_and_comments/robot_intro.py"] = """
# Let's write a story about our robot using prints and comments.
print("Hi, I am Super-Bot! 🦸‍♂️")

# Here the robot explains its powers
print("I can calculate things super fast!")
print("I can play games with you!")

# Expected Output:
# Hi, I am Super-Bot! 🦸‍♂️
# I can calculate things super fast!
# I can play games with you!
"""

# CHAPTER 3
files["chapter03_variables/README.md"] = """# Chapter 3: Variables and Data Types 📦
Variables are like magical boxes where we can store things!
You can put numbers, words (strings), or True/False (booleans) in them.

## What you learned:
- Strings (Text)
- Integers (Whole numbers)
- Booleans (True/False)

## Practice Exercise:
Create a variable for your pet's name.

## Mini Challenge:
Make variables for two numbers, add them together, and print the result!
"""

files["chapter03_variables/main.py"] = """
# Let's create some boxes (variables)!

player_name = "Alex"      # This box holds a String (text)
player_age = 10           # This box holds an Integer (whole number)
player_score = 95.5       # This box holds a Float (decimal number)
is_winner = True          # This box holds a Boolean (True or False)

# Let's open the boxes and print what's inside!
print("Player Name:", player_name)
print("Player Age:", player_age)
print("Is the player a winner?", is_winner)

# Expected Output:
# Player Name: Alex
# Player Age: 10
# Is the player a winner? True
"""

files["chapter03_variables/game_score.py"] = """
# Let's make a simple game score system
score = 0
print("Starting score:", score)

# You find a magic coin!
print("You found a magic coin! 🪙")
score = score + 10
print("New score:", score)

# Expected Output:
# Starting score: 0
# You found a magic coin! 🪙
# New score: 10
"""

# CHAPTER 4
files["chapter04_user_input/README.md"] = """# Chapter 4: User Input 🎤
Instead of us giving the computer data, what if the computer asks US for data?
We use `input()` to ask questions!

## What you learned:
- Taking user input
- Converting string to integers

## Practice Exercise:
Ask the user for their favorite superhero.

## Mini Challenge:
Make an app that asks for two numbers and multiplies them!
"""

files["chapter04_user_input/main.py"] = """
# The computer will wait for you to type something and press Enter!

print("Hello! I want to know about you.")

# Asking for text
color = input("What is your favorite color? ")
print("Wow, I love", color, "too! 🎨")

# Expected Output:
# Hello! I want to know about you.
# What is your favorite color? [User types 'Blue']
# Wow, I love Blue too! 🎨
"""

files["chapter04_user_input/name_greeting.py"] = """
# Name greeting app
name = input("Please type your name: ")
print("Hello,", name, "! You are going to be a great programmer! 🌟")
"""

files["chapter04_user_input/age_calculator.py"] = """
# Age calculator
# Input always gives us a string (text). We must turn it into an int (number) to do math.
age_text = input("How old are you? ")
age = int(age_text)

next_year_age = age + 1
print("Next year, you will be", next_year_age, "years old! 🎂")
"""

files["chapter04_user_input/favorite_game.py"] = """
# Favorite game selector
game = input("What is your favorite video game? ")
print(game, "is an awesome game! I like playing it too! 🎮")
"""

files["chapter04_user_input/quiz_game.py"] = """
# Mini quiz game
print("Welcome to the Mini Quiz!")
answer = input("What is 5 + 5? ")

print("You answered:", answer)
print("If you said 10, you are correct! 🎉")
"""

# CHAPTER 5
files["chapter05_conditions/README.md"] = """# Chapter 5: Conditions 🚦
Conditions are how computers make decisions.
If it's raining, take an umbrella. Else, wear sunglasses!

## What you learned:
- if, elif, else
- Comparison operators like > and <

## Practice Exercise:
Check if a number is greater than 10.

## Mini Challenge:
Create a traffic light program: green means go, red means stop!
"""

files["chapter05_conditions/main.py"] = """
# If, Elif (Else If), and Else
weather = "sunny"

if weather == "raining":
    print("Take an umbrella! ☔")
elif weather == "snowing":
    print("Wear a jacket! 🧥")
else:
    print("Wear sunglasses! 🕶️")

# Expected Output:
# Wear sunglasses! 🕶️
"""

files["chapter05_conditions/game_lives.py"] = """
# Game lives and rewards
lives = int(input("How many lives do you have left in the game? "))

if lives > 3:
    print("You are doing great! You get a gold star! ⭐")
elif lives > 0:
    print("Be careful! You are running low on lives. ⚠️")
else:
    print("Game Over! Try again. 💔")
"""

# CHAPTER 6
files["chapter06_loops/README.md"] = """# Chapter 6: Loops 🔁
Loops let the computer do the same thing over and over again very fast, without getting tired!

## What you learned:
- for loops
- while loops

## Practice Exercise:
Print your name 5 times using a for loop.

## Mini Challenge:
Make a countdown from 10 to 1 for a rocket launch!
"""

files["chapter06_loops/main.py"] = """
# The 'for' loop: useful when we know how many times to repeat.
print("Counting to 5:")
for number in range(1, 6):
    print(number)

print("---")

# The 'while' loop: keeps going until a condition is false.
energy = 3
while energy > 0:
    print("Robot is jumping! Energy left:", energy, "⚡")
    energy = energy - 1
    
print("Robot is tired and needs to sleep. 🛌")

# Expected Output:
# Counting to 5:
# 1
# 2
# 3
# 4
# 5
# ---
# Robot is jumping! Energy left: 3 ⚡
# Robot is jumping! Energy left: 2 ⚡
# Robot is jumping! Energy left: 1 ⚡
# Robot is tired and needs to sleep. 🛌
"""

files["chapter06_loops/robot_tasks.py"] = """
# Robot repeating tasks
tasks = ["Clean room", "Do homework", "Play games"]

# Let's loop through each task in our list
for task in tasks:
    print("Robot is doing:", task, "✅")
    
print("All tasks finished! Beep boop!")
"""

# CHAPTER 7
files["chapter07_functions/README.md"] = """# Chapter 7: Functions 🪄
A function is like a magical spell. You create the spell once, and then you can use it anytime by saying its name!

## What you learned:
- Creating functions
- Parameters (Spell ingredients)
- Return values

## Practice Exercise:
Create a function that says "Good morning!"

## Mini Challenge:
Create a function that takes two numbers and returns the biggest one!
"""

files["chapter07_functions/main.py"] = """
# Creating a function (our magic spell)
def say_hello():
    print("Hello there, wizard! 🧙‍♂️")

# Calling the function (casting the spell)
say_hello()
say_hello() # We can do it as many times as we want!

# Expected Output:
# Hello there, wizard! 🧙‍♂️
# Hello there, wizard! 🧙‍♂️
"""

files["chapter07_functions/magic_spells.py"] = """
# Functions can take 'parameters' (ingredients for the spell)
def heal_player(name, health_points):
    print(name, "drinks a potion and heals for", health_points, "HP! 🧪")

heal_player("Alex", 50)
heal_player("Sam", 20)

# Functions can also 'return' (give back) an answer
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("The magical math result is:", result)
"""

# CHAPTER 8
files["chapter08_lists_and_dictionaries/README.md"] = """# Chapter 8: Lists and Dictionaries 🎒
Lists are like a backpack where you can put many items in order.
Dictionaries are like a magical book where every word has a meaning.

## What you learned:
- Lists (ordered items)
- Dictionaries (Keys and values)

## Practice Exercise:
Make a list of your top 3 favorite movies.

## Mini Challenge:
Make a dictionary of your family members and their ages!
"""

files["chapter08_lists_and_dictionaries/main.py"] = """
# List of favorite foods
foods = ["Pizza", "Burger", "Ice Cream"]
print("My favorite food is:", foods[0]) # 0 is the first item!

# Adding an item
foods.append("Apple")
print("All foods:", foods)

# Dictionary of student ages
ages = {"Alex": 10, "Sam": 12, "Mia": 9}
print("Alex is", ages["Alex"], "years old.")

# Expected Output:
# My favorite food is: Pizza
# All foods: ['Pizza', 'Burger', 'Ice Cream', 'Apple']
# Alex is 10 years old.
"""

files["chapter08_lists_and_dictionaries/toy_collection.py"] = """
# Toy collection using a dictionary
toys = {
    "Buzz": "Space Ranger 🚀",
    "Woody": "Cowboy 🤠",
    "Rex": "Dinosaur 🦖"
}

print("Let's look in the toy box!")
for toy_name, toy_desc in toys.items():
    print(toy_name, "is a", toy_desc)
    
print("Adding a new toy...")
toys["Slinky"] = "Dog 🐕"
print("Now we have", len(toys), "toys!")
"""

# CHAPTER 9
files["chapter09_class_and_object/README.md"] = """# Chapter 9: Class and Object 🏗️
A Class is like a blueprint or a factory.
An Object is the actual thing built from that blueprint!
This is called Object Oriented Programming (OOP).

## What you learned:
- Blueprint concept (Class)
- Creating objects
- Constructors (__init__)

## Practice Exercise:
Create a blueprint (Class) for a Pet.

## Mini Challenge:
Build a `House` class with a color and number of rooms!
"""

files["chapter09_class_and_object/main.py"] = """
# Blueprint for a Robot
class Robot:
    # The constructor (__init__) runs when we create a new Robot
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def introduce(self):
        print("Hello! I am", self.name, "and I am", self.color)

# Creating Objects (actual robots)
robot1 = Robot("R2D2", "Blue and White")
robot2 = Robot("Wall-E", "Yellow")

robot1.introduce()
robot2.introduce()

# Expected Output:
# Hello! I am R2D2 and I am Blue and White
# Hello! I am Wall-E and I am Yellow
"""

files["chapter09_class_and_object/car_factory.py"] = """
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def drive(self):
        print("The", self.brand, "drives at", self.speed, "km/h! 🏎️")

# Let's make some cars from our factory
car1 = Car("Ferrari", 300)
car2 = Car("Mini Cooper", 150)

car1.drive()
car2.drive()
"""

# CHAPTER 10
files["chapter10_encapsulation/README.md"] = """# Chapter 10: Encapsulation 🔒
Encapsulation means keeping things safe and hidden.
Like a secret diary with a lock! Only you can change what's inside.

## What you learned:
- Private variables (using double underscore __)
- Getter methods (to safely read)
- Setter methods (to safely write)

## Practice Exercise:
Create a `Wallet` class with secret money.

## Mini Challenge:
Create a password-protected journal!
"""

files["chapter10_encapsulation/main.py"] = """
class PiggyBank:
    def __init__(self):
        # Two underscores make it secret/private!
        self.__money = 0 
        
    # Getter method to see the money safely
    def get_money(self):
        return self.__money
        
    # Setter method to add money safely
    def add_money(self, amount):
        if amount > 0:
            self.__money += amount
            print("Added", amount, "coins!")
        else:
            print("You can't add negative coins!")

bank = PiggyBank()
bank.add_money(50)
print("I have", bank.get_money(), "coins in my piggy bank. 🐷")

# Expected Output:
# Added 50 coins!
# I have 50 coins in my piggy bank. 🐷
"""

files["chapter10_encapsulation/secret_toy_box.py"] = """
class SecretToyBox:
    def __init__(self):
        self.__secret_toy = "Golden Robot"
        
    def open_box(self, password):
        if password == "1234":
            print("The secret toy is:", self.__secret_toy, "🏆")
        else:
            print("Wrong password! The box stays closed. 🔒")

box = SecretToyBox()
print("Trying wrong password:")
box.open_box("0000")

print("Trying right password:")
box.open_box("1234")
"""

# CHAPTER 11
files["chapter11_inheritance/README.md"] = """# Chapter 11: Inheritance 🧬
Inheritance is when a child gets features from a parent!
Just like you might have your dad's eyes or mom's hair.

## What you learned:
- Parent and child classes
- Code reuse (not writing the same code twice)

## Practice Exercise:
Create a `Vehicle` parent class and a `Bike` child class.

## Mini Challenge:
Make a `Bird` class that inherits from `Animal`, and give it a `fly()` method!
"""

files["chapter11_inheritance/main.py"] = """
# Parent Class
class Animal:
    def eat(self):
        print("I am eating! 🍽️")

# Child Class inherits from Animal
class Cat(Animal):
    def meow(self):
        print("Meow! 🐱")

kitty = Cat()
kitty.eat()   # Kitty gets this from the parent!
kitty.meow()  # Kitty's own special power!

# Expected Output:
# I am eating! 🍽️
# Meow! 🐱
"""

files["chapter11_inheritance/animal_to_dog.py"] = """
class Animal:
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print(self.name, "is sleeping. Zzz...")

class Dog(Animal):
    def bark(self):
        print(self.name, "says Woof Woof! 🐶")

my_dog = Dog("Buddy")
my_dog.sleep() # Inherited!
my_dog.bark()
"""

# CHAPTER 12
files["chapter12_polymorphism/README.md"] = """# Chapter 12: Polymorphism 🦸‍♂️
Polymorphism is a big word that means "many forms".
It means different objects can use the same method name, but do it differently!

## What you learned:
- Same method, different behavior

## Practice Exercise:
Create different instruments that all have a `play()` method.

## Mini Challenge:
Create different robots that all have a `work()` method but do different jobs!
"""

files["chapter12_polymorphism/main.py"] = """
class Bird:
    def make_sound(self):
        print("Tweet tweet! 🐦")

class Duck:
    def make_sound(self):
        print("Quack quack! 🦆")

def play_sound(animal):
    animal.make_sound()

birdie = Bird()
ducky = Duck()

# Same function, different behavior!
play_sound(birdie)
play_sound(ducky)

# Expected Output:
# Tweet tweet! 🐦
# Quack quack! 🦆
"""

files["chapter12_polymorphism/superheroes.py"] = """
class Superman:
    def attack(self):
        print("Superman shoots laser eyes! 🔴_🔴")

class Batman:
    def attack(self):
        print("Batman throws a batarang! 🦇")

heroes = [Superman(), Batman()]

print("Heroes, attack!")
for hero in heroes:
    hero.attack() # Same command, different attacks!
"""

# CHAPTER 13
files["chapter13_abstraction/README.md"] = """# Chapter 13: Abstraction 📺
Abstraction means hiding complex things and only showing the simple buttons!
Like a TV remote: you press power, and the TV turns on. You don't need to know the complex electronics inside.

## What you learned:
- Abstract classes
- Hidden implementation

## Practice Exercise:
Create an abstract class called `GameConsole` with a `play_game()` method.

## Mini Challenge:
Make an abstract `Phone` class with a `make_call()` method, and implement an `iPhone` and `Android` class!
"""

files["chapter13_abstraction/main.py"] = """
from abc import ABC, abstractmethod

# Abstract class (like an empty blueprint)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass # Empty! Children must fill this in.

class Circle(Shape):
    def draw(self):
        print("Drawing a round circle! ⭕")

class Square(Shape):
    def draw(self):
        print("Drawing a square box! ⬛")

c = Circle()
c.draw()
s = Square()
s.draw()

# Expected Output:
# Drawing a round circle! ⭕
# Drawing a square box! ⬛
"""

files["chapter13_abstraction/remote_control.py"] = """
from abc import ABC, abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def press_power(self):
        pass

class TVRemote(RemoteControl):
    def press_power(self):
        print("Turning TV on... showing cartoons! 📺")

class DroneRemote(RemoteControl):
    def press_power(self):
        print("Starting drone propellers... ready to fly! 🚁")

my_tv_remote = TVRemote()
my_tv_remote.press_power()

my_drone_remote = DroneRemote()
my_drone_remote.press_power()
"""

# CHAPTER 14
files["chapter14_exception_handling/README.md"] = """# Chapter 14: Exception Handling 🛡️
Sometimes code has mistakes or errors (exceptions).
Instead of crashing, we can use a shield (try/except) to catch the error safely!

## What you learned:
- try, except, finally

## Practice Exercise:
Try to open a file that doesn't exist, and catch the error.

## Mini Challenge:
Create a safe division program that catches `ZeroDivisionError`!
"""

files["chapter14_exception_handling/main.py"] = """
print("Let's divide 10 by a number!")

try:
    # Try doing something risky
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    # If it crashes, catch the error here safely!
    print("Oh no! You cannot divide by zero! 🚫")
finally:
    # This always runs
    print("Math operation finished.")

# Expected Output:
# Let's divide 10 by a number!
# Oh no! You cannot divide by zero! 🚫
# Math operation finished.
"""

files["chapter14_exception_handling/game_input.py"] = """
# Wrong game input handling
print("Welcome to the guessing game!")

try:
    guess = int(input("Guess a number from 1 to 10: "))
    print("You guessed:", guess)
except ValueError:
    print("Oops! That was not a number. Please type a number next time! 😅")
"""

# CHAPTER 15
files["chapter15_file_handling/README.md"] = """# Chapter 15: File Handling 💾
We can teach our Python program to read and write actual files on your computer!
This is how games save your progress.

## What you learned:
- Reading files
- Writing files
- Saving data

## Practice Exercise:
Write a program that saves your favorite movie to a file.

## Mini Challenge:
Create a digital diary that asks for your mood and saves it to a text file!
"""

files["chapter15_file_handling/main.py"] = """
# Writing to a file
# 'w' means write mode (creates or overwrites a file)
file = open("secret_message.txt", "w")
file.write("Python is awesome! 🐍")
file.close()
print("Message saved to file!")

# Reading from a file
# 'r' means read mode
file2 = open("secret_message.txt", "r")
content = file2.read()
file2.close()
print("Reading file:", content)

# Expected Output:
# Message saved to file!
# Reading file: Python is awesome! 🐍
"""

files["chapter15_file_handling/save_scores.py"] = """
# Saving game scores
player = "Alex"
score = 999

# 'a' means append (add to the end, without deleting old stuff)
with open("scores.txt", "a") as f:
    f.write(player + " scored " + str(score) + "\\n")
    
print("Score saved successfully! 🏆")

print("\\nAll saved scores:")
with open("scores.txt", "r") as f:
    print(f.read())
"""

# CHAPTER 16
files["chapter16_modules/README.md"] = """# Chapter 16: Modules and Packages 🧰
Modules are like toolboxes.
Instead of building a hammer from scratch, you just bring in a toolbox that already has a hammer!

## What you learned:
- Importing files
- Reusing code

## Practice Exercise:
Import the built-in `math` module and find the square root of 16.

## Mini Challenge:
Create a file called `my_math.py` with an addition function, and import it into another file!
"""

files["chapter16_modules/robot_parts.py"] = """
# This is a module! It holds useful tools.
def build_arm():
    print("Building a strong robot arm! 💪")

def build_leg():
    print("Building a fast robot leg! 🦵")
"""

files["chapter16_modules/main.py"] = """
# Importing built-in Python modules
import random

number = random.randint(1, 10)
print("The random number is:", number, "🎲")
"""

files["chapter16_modules/toolbox.py"] = """
# Importing our own module!
import robot_parts

print("Robot Factory is open!")
robot_parts.build_arm()
robot_parts.build_leg()
print("Robot is ready to go! 🤖")

# Expected Output:
# Robot Factory is open!
# Building a strong robot arm! 💪
# Building a fast robot leg! 🦵
# Robot is ready to go! 🤖
"""

# CHAPTER 17
files["chapter17_collections/README.md"] = """# Chapter 17: Collections and Advanced Python 🪄
Collections are special ways to hold data.
Sets hold unique items.
Tuples are like lists, but locked (cannot be changed).

## What you learned:
- Sets, Tuples
- List comprehensions
- Basic lambda

## Practice Exercise:
Create a set of your 3 favorite colors. Try adding a duplicate color!

## Mini Challenge:
Use a list comprehension to generate a list of squares for numbers 1 to 5.
"""

files["chapter17_collections/main.py"] = """
# Tuples (Locked list)
colors = ("Red", "Green", "Blue")
print("Tuple color:", colors[0])

# Sets (No duplicates!)
magic_bag = {"apple", "banana", "apple"} 
print("Set magic bag:", magic_bag) # Notice 'apple' only appears once!

# Expected Output:
# Tuple color: Red
# Set magic bag: {'banana', 'apple'} 
"""

files["chapter17_collections/magic_organizer.py"] = """
# List comprehension: A fast magical way to make lists
numbers = [1, 2, 3, 4, 5]

# Let's double all numbers easily!
doubled = [num * 2 for num in numbers]
print("Original:", numbers)
print("Doubled :", doubled, "✨")

# Lambda (A tiny spell function in one line)
add_magic = lambda a, b: a + b
print("Magic Addition:", add_magic(10, 5))
"""

# CHAPTER 18
files["chapter18_test_automation_basics/README.md"] = """# Chapter 18: Test Automation Basics for Kids 🤖✅

## What is Testing?
a. Checking if a toy works properly
b. Finding mistakes or bugs!

## Manual Testing vs Automation Testing
a. **Manual Testing**: Human checking (slow)
b. **Automation Testing**: Robot checking (super fast!)

## Why Automation?
a. Fast
b. Repeatable
c. Robots never get tired!

## What Can Be Automated?
a. Login checking
b. Calculator checking
c. Game score validation

## Basic Testing Concepts
a. **Test Case**: The thing we want to check
b. **Expected Result**: What SHOULD happen
c. **Actual Result**: What REALLY happened
d. **Pass and Fail**: Yay or Nay!

We will act like a robot checking homework over and over again!

## Practice Exercise:
Run `calculator_test.py` and see the results!

## Mini Challenge:
Create a function that multiplies by 2, and write an automation test for it!
"""

files["chapter18_test_automation_basics/calculator.py"] = """
# This is the toy we are going to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

files["chapter18_test_automation_basics/main.py"] = """
print("Automation is like a robot checking homework again and again. 📝")
print("Instead of a human doing it slowly, the robot does it instantly!")
print("Run the test files in this folder to see the magic!")
"""

files["chapter18_test_automation_basics/calculator_test.py"] = """
import calculator

print("Starting Automation Test for Calculator 🤖...")

# Test Case 1: Addition
expected_result = 5
actual_result = calculator.add(2, 3)

if actual_result == expected_result:
    print("✅ Add Test Passed!")
else:
    print("❌ Add Test Failed! Expected", expected_result, "but got", actual_result)

# Test Case 2: Subtraction
expected_sub = 10
actual_sub = calculator.subtract(15, 5)

if actual_sub == expected_sub:
    print("✅ Subtract Test Passed!")
else:
    print("❌ Subtract Test Failed!")
"""

files["chapter18_test_automation_basics/login_test.py"] = """
# Testing a login system
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

print("Starting Login Test...")

# Test 1: Right password
result1 = login("admin", "1234")
if result1 == True:
    print("✅ Correct Login Test Passed!")
else:
    print("❌ Correct Login Test Failed!")

# Test 2: Wrong password
result2 = login("admin", "wrong!")
if result2 == False:
    print("✅ Wrong Password Test Passed! (It correctly blocked the user)")
else:
    print("❌ Wrong Password Test Failed!")
"""

files["chapter18_test_automation_basics/game_score_test.py"] = """
# Testing game score logic
def get_bonus(score):
    if score >= 100:
        return 50
    return 0

print("Testing Bonus Logic...")

bonus = get_bonus(120)
if bonus == 50:
    print("✅ Bonus applied correctly for high score!")
else:
    print("❌ Bonus test failed.")
"""

# CHAPTER 19
files["chapter19_data_science_basics/README.md"] = """# Chapter 19: Data Science Basics for Kids 📊
Data Science is like being a detective! You look at lots of clues (data) to find patterns.

## What you learned:
- What is Data Science
- Reading CSV files (tables of data)
- Finding highest scores and averages
- Drawing simple graphs

## Practice Exercise:
Add a new student to `scores.csv` and run the analysis script again.

## Mini Challenge:
Make a new CSV file for "Toy Sales" and calculate the average sales!
"""

files["chapter19_data_science_basics/scores.csv"] = """Student,Score
Alex,85
Sam,92
Mia,78
Leo,95
Zoe,88
"""

files["chapter19_data_science_basics/main.py"] = """
# Data science helps us count scores and find the highest one!
print("Data Science is amazing! 📈")
print("Run the game_score_analysis.py file to see data science in action.")
"""

files["chapter19_data_science_basics/game_score_analysis.py"] = """
# Note: You need pandas and matplotlib installed! (pip install pandas matplotlib)
import pandas as pd
import matplotlib.pyplot as plt

print("Loading student scores data...")
# Read the CSV file into a Table (DataFrame)
df = pd.read_csv("scores.csv")

print("\\nHere is the data table:")
print(df)

print("\\nCalculating average score...")
average = df["Score"].mean()
print("The average score is:", average)

print("\\nWho got the highest score?")
highest = df["Score"].max()
print("The highest score is:", highest, "🏆")

print("\\nClose the graph window to finish the program.")
# Let's draw a simple chart! (It will pop up on your screen)
df.plot(kind='bar', x='Student', y='Score', color='skyblue')
plt.title("Student Game Scores")
plt.ylabel("Score")
plt.show()
"""

# CHAPTER 20
files["chapter20_ai_basics/README.md"] = """# Chapter 20: AI Basics for Kids 🧠
Artificial Intelligence (AI) means teaching a computer to think or make guesses!
Machine Learning is how AI learns from data instead of strict rules.

## What you learned:
- What is AI
- Simple prediction ideas
- Smart robot basics

## Practice Exercise:
Change the `guessing_ai.py` to guess favorite colors instead of moods!

## Mini Challenge:
Upgrade the ChatBot to tell a new joke!
"""

files["chapter20_ai_basics/main.py"] = """
print("Welcome to Artificial Intelligence!")
print("AI can recognize faces, predict weather, and recommend games.")
"""

files["chapter20_ai_basics/guessing_ai.py"] = """
# A simple "AI" that guesses what you want based on random choice
import random

def guess_mood():
    moods = ["Happy 😃", "Excited 🤩", "Sleepy 😴"]
    print("My AI brain predicts you are feeling:", random.choice(moods))

guess_mood()
"""

files["chapter20_ai_basics/game_recommender.py"] = """
# A very basic rule-based AI recommender
def recommend_game(likes_action, likes_puzzle):
    if likes_action == "yes" and likes_puzzle == "no":
        return "Super Smash Action!"
    elif likes_puzzle == "yes" and likes_action == "no":
        return "Brain Teaser Puzzle 3000!"
    else:
        return "Minecraft! (Good for everything)"

print("AI Game Recommender")
action = input("Do you like action? (yes/no): ").lower()
puzzle = input("Do you like puzzles? (yes/no): ").lower()

prediction = recommend_game(action, puzzle)
print("🤖 AI Recommends: You should play ->", prediction)
"""

files["chapter20_ai_basics/smart_chatbot.py"] = """
# A simple rule-based Chatbot
print("Hello! I am ChatBot-Mini. Talk to me!")

while True:
    message = input("You: ").lower()
    
    if message == "quit":
        print("Bot: Goodbye! 👋")
        break
    elif "hello" in message or "hi" in message:
        print("Bot: Hello human! 🤖")
    elif "how are you" in message:
        print("Bot: My circuits are feeling great today! ⚡")
    elif "joke" in message:
        print("Bot: Why did the computer squeak? Because someone stepped on its mouse! 🐁😂")
    else:
        print("Bot: Hmm, I am still learning. Tell me more!")
"""

# CHAPTER 21
files["chapter21_mini_project/README.md"] = """# Chapter 21: Final Mini Project 🎓
Congratulations on reaching the final chapter!
Here we combine everything: OOP, User Input, Automation, and Logic!

## Project: Robot Academy System
This project brings together:
- Classes and Objects (RobotStudent)
- File Handling (Saving to academy_records.txt)
- User Input (Menus and typing names)
- Exception Handling (Safe saving)
- Simple Automation Test

You did it! You are a Python Programmer now! 🎉
"""

files["chapter21_mini_project/main.py"] = """
# Run the robot_academy.py to see the final project!
print("Get ready for the Final Mini Project! 🎉")
print("Run robot_academy.py")
"""

files["chapter21_mini_project/robot_academy.py"] = """
# Robot Academy System
# Combines OOP, Exceptions, Loops, Input, File Handling, and Automation

class RobotStudent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.score = 0
        
    def study(self):
        self.score += 10
        print(self.name, "studied hard! Score is now", self.score)
        
    def save_data(self):
        try:
            with open("academy_records.txt", "a") as f:
                f.write(f"Robot {self.name} (Model {self.model}) - Score: {self.score}\\n")
            print("Data saved successfully! 💾")
        except Exception as e:
            print("Could not save data!", e)

print("🎓 Welcome to Robot Academy 🎓")
name = input("Enter new robot name: ")
model = input("Enter robot model (e.g., T-800): ")

new_robot = RobotStudent(name, model)

while True:
    print("\\nMenu:")
    print("1. Study (Gain Points)")
    print("2. Save Data")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        new_robot.study()
    elif choice == "2":
        new_robot.save_data()
    elif choice == "3":
        print("Goodbye! System shutting down... 🔌")
        break
    else:
        print("Invalid choice! Try again.")

# Simple automation check at the end
print("\\n--- Running Automation Check ---")
if new_robot.score >= 0:
    print("✅ System Check Passed: Final score is valid.")
else:
    print("❌ System Check Failed.")
"""

# Write all files
for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")

print(f"Kids Python Project generated successfully in '{base_dir}' folder!")
