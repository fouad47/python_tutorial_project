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

files["walkthrough.md"] = """# 🗺️ Python for Kids - Project Walkthrough

Welcome to the Python Storybook Walkthrough! This guide will take you step-by-step through all 21 chapters of this adventure.

## 🌟 How to Use This Project
- **Step 1:** Start at **Chapter 1** and work your way up to **Chapter 21**.
- **Step 2:** Open the `README.md` in each chapter folder first. It tells a fun story and explains the concept.
- **Step 3:** Open the Python files (like `main.py`). We have added comments to **every single line of code** to explain exactly how it works.
- **Step 4:** Run the code! Open your terminal, go into the chapter folder, and type `python main.py`.

## 📚 Chapter Guide
- **Chapters 1-7:** Core Programming (Printing, Variables, Inputs, Conditions, Loops, Functions).
- **Chapters 8-13:** Object-Oriented Programming (OOP) - Learn to build Blueprints and Objects!
- **Chapters 14-17:** Advanced Core (Exceptions, File Saving, Modules).
- **Chapter 18:** Test Automation - Write code that tests other code!
- **Chapter 19:** Data Science - Read CSV files and draw graphs using pandas.
- **Chapter 20:** AI Basics - Create smart chat bots and recommenders.
- **Chapter 21:** Final Project - A massive Robot Academy combining everything!

Have fun coding! 🚀
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
"""

files["chapter01_what_is_programming/main.py"] = """
# Welcome to Chapter 1!
# Here we will learn how to make the computer talk.

# The print() function is a command. It tells the computer to show text on the screen.
# Notice the text is inside double quotes (""). This tells Python it's a message, not a command.
print("Hello, world! I am learning Python! 🚀")

# Expected Output:
# Hello, world! I am learning Python! 🚀
"""

files["chapter01_what_is_programming/robot_says_hello.py"] = """
# Let's make a robot say hello!

# This command prints the robot's sound.
print("Beep boop! 🤖")

# This command prints the robot's introduction.
print("Hello! I am Robo, your new coding friend.")

# This command asks a question.
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
"""

files["chapter02_print_and_comments/main.py"] = """
# This symbol (#) makes a single-line comment! 
# The computer will NOT read this line. It is just for humans.

# Here we use print() to show a message.
print("I can print anything!") 

'''
This symbol (three single quotes) makes a multi-line comment.
You can write a whole story inside here!
The computer will completely ignore all these lines.
'''

# This will print normally because it doesn't have a # in front of it.
print("Comments are cool because they help us remember what code does.")

# Expected Output:
# I can print anything!
# Comments are cool because they help us remember what code does.
"""

files["chapter02_print_and_comments/robot_intro.py"] = """
# Let's write a story about our robot using prints and comments.

# The robot says hello.
print("Hi, I am Super-Bot! 🦸‍♂️")

# The robot tells us about its powers.
print("I can calculate things super fast!")
print("I can play games with you!")

# Practice: Try to print your own name below!
# print("My name is...")
"""

# CHAPTER 3
files["chapter03_variables/README.md"] = """# Chapter 3: Variables and Data Types 📦
Variables are like magical boxes where we can store things!
You can put numbers, words (strings), or True/False (booleans) in them.
"""

files["chapter03_variables/main.py"] = """
# Let's create some boxes (variables)!

# The variable 'player_name' is a box holding text (a String).
player_name = "Alex"      

# The variable 'player_age' is a box holding a whole number (an Integer).
player_age = 10           

# The variable 'player_score' holds a decimal number (a Float).
player_score = 95.5       

# The variable 'is_winner' holds a True or False value (a Boolean).
is_winner = True          

# Now, we use print() to open the boxes and show what's inside!
# Notice we use a comma (,) to print the text AND the variable together.
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

# We create a variable called 'score' and set its value to 0.
score = 0

# We print the starting score.
print("Starting score:", score)

# You find a magic coin! Let's print a message.
print("You found a magic coin! 🪙")

# We take the old score (0), add 10, and save it back into the 'score' box.
score = score + 10

# We print the new score.
print("New score:", score)
"""

# CHAPTER 4
files["chapter04_user_input/README.md"] = """# Chapter 4: User Input 🎤
Instead of us giving the computer data, what if the computer asks US for data?
We use `input()` to ask questions!
"""

files["chapter04_user_input/main.py"] = """
# We print a welcoming message.
print("Hello! I want to know about you.")

# The input() function asks the user a question and waits for them to type an answer.
# Whatever they type gets stored in the variable 'color'.
color = input("What is your favorite color? ")

# We print their answer back to them!
print("Wow, I love", color, "too! 🎨")
"""

files["chapter04_user_input/name_greeting.py"] = """
# Name greeting app

# Ask for the user's name and save it in the 'name' variable.
name = input("Please type your name: ")

# Print a nice greeting using their name.
print("Hello,", name, "! You are going to be a great programmer! 🌟")
"""

files["chapter04_user_input/age_calculator.py"] = """
# Age calculator

# Ask for the age. Warning: input() ALWAYS gives us text (a String), even if we type numbers.
age_text = input("How old are you? ")

# We must use int() to change the text into a real math number (Integer).
age = int(age_text)

# Now we can do math! We add 1 to the age.
next_year_age = age + 1

# Print the result.
print("Next year, you will be", next_year_age, "years old! 🎂")
"""

files["chapter04_user_input/quiz_game.py"] = """
# Mini quiz game

# Print a welcome message.
print("Welcome to the Mini Quiz!")

# Ask a math question and save their answer in the 'answer' variable.
answer = input("What is 5 + 5? ")

# Show them what they typed.
print("You answered:", answer)

# Tell them the correct answer.
print("If you said 10, you are correct! 🎉")
"""

# CHAPTER 5
files["chapter05_conditions/README.md"] = """# Chapter 5: Conditions 🚦
Conditions are how computers make decisions.
If it's raining, take an umbrella. Else, wear sunglasses!
"""

files["chapter05_conditions/main.py"] = """
# We create a variable 'weather' and set it to "sunny".
weather = "sunny"

# 'if' checks if a condition is True. We use == to check if two things are exactly equal.
if weather == "raining":
    # This code only runs if weather is "raining".
    print("Take an umbrella! ☔")
    
# 'elif' means "Else If". It checks another condition if the first one was False.
elif weather == "snowing":
    # This code only runs if weather is "snowing".
    print("Wear a jacket! 🧥")
    
# 'else' runs if ALL the conditions above were False.
else:
    # Since weather is "sunny" (not raining and not snowing), this line will run!
    print("Wear sunglasses! 🕶️")
"""

files["chapter05_conditions/game_lives.py"] = """
# We ask for lives, use input(), and wrap it in int() to turn it into a number right away!
lives = int(input("How many lives do you have left in the game? "))

# Check if lives are greater than (>) 3.
if lives > 3:
    print("You are doing great! You get a gold star! ⭐")
    
# Check if lives are greater than (>) 0.
elif lives > 0:
    print("Be careful! You are running low on lives. ⚠️")
    
# If lives are not greater than 0, it means lives are 0 or less.
else:
    print("Game Over! Try again. 💔")
"""

# CHAPTER 6
files["chapter06_loops/README.md"] = """# Chapter 6: Loops 🔁
Loops let the computer do the same thing over and over again very fast, without getting tired!
"""

files["chapter06_loops/main.py"] = """
# A 'for' loop is used when we know exactly how many times we want to repeat something.
print("Counting to 5:")

# range(1, 6) gives us numbers from 1 up to 5 (it stops before 6).
# 'number' becomes 1, then 2, then 3, then 4, then 5.
for number in range(1, 6):
    # This prints the current number.
    print(number)

print("---")

# A 'while' loop keeps repeating AS LONG AS a condition is True.
energy = 3

# Keep looping while energy is greater than 0.
while energy > 0:
    # Print the jumping message and the current energy.
    print("Robot is jumping! Energy left:", energy, "⚡")
    
    # We must decrease energy by 1, otherwise the loop will never stop! (Infinite loop)
    energy = energy - 1
    
# This prints after the loop finishes.
print("Robot is tired and needs to sleep. 🛌")
"""

files["chapter06_loops/robot_tasks.py"] = """
# This is a List (a collection of items). We will learn more about lists in Chapter 8.
tasks = ["Clean room", "Do homework", "Play games"]

# We use a for loop to go through each task in the list, one by one.
# 'task' will hold the current item.
for task in tasks:
    # Print the current task.
    print("Robot is doing:", task, "✅")
    
# Print completion message.
print("All tasks finished! Beep boop!")
"""

# CHAPTER 7
files["chapter07_functions/README.md"] = """# Chapter 7: Functions 🪄
A function is like a magical spell. You create the spell once, and then you can use it anytime by saying its name!
"""

files["chapter07_functions/main.py"] = """
# We use 'def' to create (define) a function. This is our magic spell.
# We name it 'say_hello'. The empty parentheses () mean it doesn't need any ingredients.
def say_hello():
    # Everything indented inside is what the spell actually does.
    print("Hello there, wizard! 🧙‍♂️")

# To use the spell, we just type its name with parentheses! This is called "calling" the function.
say_hello()

# We can call it as many times as we want!
say_hello() 
"""

files["chapter07_functions/magic_spells.py"] = """
# Functions can take 'parameters'. Think of them as ingredients for the spell.
# Here, 'name' and 'health_points' are the ingredients.
def heal_player(name, health_points):
    # The function uses the ingredients to print a special message.
    print(name, "drinks a potion and heals for", health_points, "HP! 🧪")

# We call the function and give it the ingredients ("Alex" and 50).
heal_player("Alex", 50)

# We call it again with different ingredients!
heal_player("Sam", 20)

# Functions can also 'return' (give back) an answer instead of just printing.
def multiply(a, b):
    # We use 'return' to give the math answer back to whoever called the function.
    return a * b

# We call the function, and save the returned answer in the 'result' variable.
result = multiply(4, 5)

# We print the result.
print("The magical math result is:", result)
"""

# CHAPTER 8
files["chapter08_lists_and_dictionaries/README.md"] = """# Chapter 8: Lists and Dictionaries 🎒
Lists are like a backpack where you can put many items in order.
Dictionaries are like a magical book where every word has a meaning.
"""

files["chapter08_lists_and_dictionaries/main.py"] = """
# A List uses square brackets []. It holds items in order.
foods = ["Pizza", "Burger", "Ice Cream"]

# We use square brackets with a number (index) to get an item.
# In Python, counting ALWAYS starts at 0. So foods[0] is the FIRST item.
print("My favorite food is:", foods[0])

# We can use .append() to add a new item to the END of the list.
foods.append("Apple")
print("All foods:", foods)

# A Dictionary uses curly brackets {}. It pairs a 'Key' with a 'Value'.
# "Alex" is the key, and 10 is the value.
ages = {"Alex": 10, "Sam": 12, "Mia": 9}

# We look up a value by using the Key inside square brackets.
print("Alex is", ages["Alex"], "years old.")
"""

files["chapter08_lists_and_dictionaries/toy_collection.py"] = """
# Here we create a dictionary to map toy names (Keys) to what they are (Values).
toys = {
    "Buzz": "Space Ranger 🚀",
    "Woody": "Cowboy 🤠",
    "Rex": "Dinosaur 🦖"
}

print("Let's look in the toy box!")

# We can loop through a dictionary using .items().
# It gives us the Key (toy_name) and Value (toy_desc) one by one.
for toy_name, toy_desc in toys.items():
    print(toy_name, "is a", toy_desc)
    
print("Adding a new toy...")

# To add a new pair to the dictionary, we assign a Value to a new Key.
toys["Slinky"] = "Dog 🐕"

# len() tells us the Length (how many items) are in the dictionary.
print("Now we have", len(toys), "toys!")
"""

# CHAPTER 9
files["chapter09_class_and_object/README.md"] = """# Chapter 9: Class and Object 🏗️
A Class is like a blueprint or a factory.
An Object is the actual thing built from that blueprint!
This is called Object Oriented Programming (OOP).
"""

files["chapter09_class_and_object/main.py"] = """
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
"""

files["chapter09_class_and_object/car_factory.py"] = """
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
"""

# CHAPTER 10
files["chapter10_encapsulation/README.md"] = """# Chapter 10: Encapsulation 🔒
Encapsulation means keeping things safe and hidden.
Like a secret diary with a lock! Only you can change what's inside.
"""

files["chapter10_encapsulation/main.py"] = """
# Blueprint for a Piggy Bank
class PiggyBank:
    def __init__(self):
        # We use two underscores (__) to make a variable PRIVATE (hidden).
        # Nobody from the outside can touch this variable directly!
        self.__money = 0 
        
    # This is a "Getter" method. It safely allows us to SEE the hidden money.
    def get_money(self):
        return self.__money
        
    # This is a "Setter" method. It safely allows us to ADD money, but with rules.
    def add_money(self, amount):
        # The rule: You can only add money if the amount is greater than 0!
        if amount > 0:
            self.__money += amount
            print("Added", amount, "coins!")
        else:
            # If someone tries to steal money by adding negative coins, we block them!
            print("You can't add negative coins!")

# We build a PiggyBank object.
bank = PiggyBank()

# We safely use the setter to add 50 coins.
bank.add_money(50)

# We safely use the getter to look at our money.
print("I have", bank.get_money(), "coins in my piggy bank. 🐷")
"""

files["chapter10_encapsulation/secret_toy_box.py"] = """
# Blueprint for a locked box
class SecretToyBox:
    def __init__(self):
        # The toy is hidden inside a private variable.
        self.__secret_toy = "Golden Robot"
        
    # A method to open the box, but it requires a password!
    def open_box(self, password):
        # We check if the password is correct.
        if password == "1234":
            print("The secret toy is:", self.__secret_toy, "🏆")
        else:
            print("Wrong password! The box stays closed. 🔒")

# We build the box.
box = SecretToyBox()

# We try a bad password. It won't work.
print("Trying wrong password:")
box.open_box("0000")

# We try the good password. It works!
print("Trying right password:")
box.open_box("1234")
"""

# CHAPTER 11
files["chapter11_inheritance/README.md"] = """# Chapter 11: Inheritance 🧬
Inheritance is when a child gets features from a parent!
Just like you might have your dad's eyes or mom's hair.
"""

files["chapter11_inheritance/main.py"] = """
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
"""

files["chapter11_inheritance/animal_to_dog.py"] = """
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
"""

# CHAPTER 12
files["chapter12_polymorphism/README.md"] = """# Chapter 12: Polymorphism 🦸‍♂️
Polymorphism is a big word that means "many forms".
It means different objects can use the same method name, but do it differently!
"""

files["chapter12_polymorphism/main.py"] = """
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
"""

files["chapter12_polymorphism/superheroes.py"] = """
# Superhero 1
class Superman:
    def attack(self):
        print("Superman shoots laser eyes! 🔴_🔴")

# Superhero 2
class Batman:
    def attack(self):
        print("Batman throws a batarang! 🦇")

# A list holding different types of superheroes.
heroes = [Superman(), Batman()]

print("Heroes, attack!")

# We loop through the list and tell each hero to attack.
# Each hero attacks in their own unique way!
for hero in heroes:
    hero.attack()
"""

# CHAPTER 13
files["chapter13_abstraction/README.md"] = """# Chapter 13: Abstraction 📺
Abstraction means hiding complex things and only showing the simple buttons!
Like a TV remote: you press power, and the TV turns on. You don't need to know the complex electronics inside.
"""

files["chapter13_abstraction/main.py"] = """
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
"""

files["chapter13_abstraction/remote_control.py"] = """
# Importing abstraction tools
from abc import ABC, abstractmethod

# Abstract class for any remote control
class RemoteControl(ABC):
    # Every remote must have a power button!
    @abstractmethod
    def press_power(self):
        pass

# A TV remote implements the power button for a TV.
class TVRemote(RemoteControl):
    def press_power(self):
        print("Turning TV on... showing cartoons! 📺")

# A Drone remote implements the power button for a Drone.
class DroneRemote(RemoteControl):
    def press_power(self):
        print("Starting drone propellers... ready to fly! 🚁")

# Testing the remotes
my_tv_remote = TVRemote()
my_tv_remote.press_power()

my_drone_remote = DroneRemote()
my_drone_remote.press_power()
"""

# CHAPTER 14
files["chapter14_exception_handling/README.md"] = """# Chapter 14: Exception Handling 🛡️
Sometimes code has mistakes or errors (exceptions).
Instead of crashing, we can use a shield (try/except) to catch the error safely!
"""

files["chapter14_exception_handling/main.py"] = """
print("Let's divide 10 by a number!")

# We use 'try:' to wrap dangerous code that might crash.
try:
    # 10 divided by 0 is impossible in math! This will cause an error (ZeroDivisionError).
    result = 10 / 0
    print(result)
    
# 'except' acts like a safety net. It catches the specific error so the program doesn't crash!
except ZeroDivisionError:
    # We print a friendly message instead of a scary red error.
    print("Oh no! You cannot divide by zero! 🚫")
    
# 'finally' is a block that ALWAYS runs, no matter what happened above.
finally:
    print("Math operation finished.")
"""

files["chapter14_exception_handling/game_input.py"] = """
# Wrong game input handling
print("Welcome to the guessing game!")

# We wrap the input in a try block.
try:
    # If the user types text (like 'hello') instead of a number, int() will crash!
    guess = int(input("Guess a number from 1 to 10: "))
    print("You guessed:", guess)
    
# If int() crashes, it creates a ValueError. We catch it here.
except ValueError:
    # We scold the user nicely!
    print("Oops! That was not a number. Please type a number next time! 😅")
"""

# CHAPTER 15
files["chapter15_file_handling/README.md"] = """# Chapter 15: File Handling 💾
We can teach our Python program to read and write actual files on your computer!
This is how games save your progress.
"""

files["chapter15_file_handling/main.py"] = """
# Writing to a file
# open() takes the file name and the mode. 'w' means Write mode (creates a new file).
file = open("secret_message.txt", "w")

# We use .write() to put text inside the file.
file.write("Python is awesome! 🐍")

# We MUST close the file when we are done so it saves properly!
file.close()
print("Message saved to file!")

# Reading from a file
# 'r' means Read mode. It opens an existing file so we can look inside.
file2 = open("secret_message.txt", "r")

# We use .read() to extract all the text and save it in a variable.
content = file2.read()

# Don't forget to close!
file2.close()

# Print out what we read.
print("Reading file:", content)
"""

files["chapter15_file_handling/save_scores.py"] = """
# Saving game scores
player = "Alex"
score = 999

# We use the 'with' keyword. It is a magic trick that AUTOMATICALLY closes the file for us!
# 'a' means Append mode. It adds new text to the end without deleting the old text.
with open("scores.txt", "a") as f:
    # We write the player's name, their score, and \\n (which means "New Line").
    f.write(player + " scored " + str(score) + "\\n")
    
print("Score saved successfully! 🏆")

print("\\nAll saved scores:")

# We open the file in Read ('r') mode using 'with'.
with open("scores.txt", "r") as f:
    # Read everything and print it.
    print(f.read())
"""

# CHAPTER 16
files["chapter16_modules/README.md"] = """# Chapter 16: Modules and Packages 🧰
Modules are like toolboxes.
Instead of building a hammer from scratch, you just bring in a toolbox that already has a hammer!
"""

files["chapter16_modules/robot_parts.py"] = """
# This is a custom module! A module is just a regular Python file with useful functions.
# We will use these tools in another file.

def build_arm():
    print("Building a strong robot arm! 💪")

def build_leg():
    print("Building a fast robot leg! 🦵")
"""

files["chapter16_modules/main.py"] = """
# Python has built-in modules. 'random' is a module for generating random things.
import random

# We use the randint function from the random module to pick a number between 1 and 10.
number = random.randint(1, 10)

# Print the random number.
print("The random number is:", number, "🎲")
"""

files["chapter16_modules/toolbox.py"] = """
# We can import OUR OWN module! We just type the name of the file (without .py).
import robot_parts

print("Robot Factory is open!")

# We use the dot (.) to access the tools inside the module.
robot_parts.build_arm()
robot_parts.build_leg()

print("Robot is ready to go! 🤖")
"""

# CHAPTER 17
files["chapter17_collections/README.md"] = """# Chapter 17: Collections and Advanced Python 🪄
Collections are special ways to hold data.
Sets hold unique items.
Tuples are like lists, but locked (cannot be changed).
"""

files["chapter17_collections/main.py"] = """
# Tuples use parentheses (). They are like locked lists.
colors = ("Red", "Green", "Blue")

# You can read them just like lists.
print("Tuple color:", colors[0])

# But you CANNOT change them! (Uncommenting the line below would cause an error).
# colors[0] = "Yellow"

# Sets use curly brackets {}. They automatically delete duplicates!
magic_bag = {"apple", "banana", "apple"} 

# When we print it, 'apple' will only show up once!
print("Set magic bag:", magic_bag)
"""

files["chapter17_collections/magic_organizer.py"] = """
# A regular list of numbers.
numbers = [1, 2, 3, 4, 5]

# List comprehension: A fast, magical way to make a new list from an old one in one line!
# It says: "Multiply 'num' by 2, for every 'num' inside the 'numbers' list."
doubled = [num * 2 for num in numbers]

print("Original:", numbers)
print("Doubled :", doubled, "✨")

# Lambda is a tiny, one-line function without a name.
# It takes 'a' and 'b', and returns 'a + b'.
add_magic = lambda a, b: a + b

# We use our tiny lambda function.
print("Magic Addition:", add_magic(10, 5))
"""

# CHAPTER 18
files["chapter18_test_automation_basics/README.md"] = """# Chapter 18: Test Automation Basics for Kids 🤖✅
What is Testing? Checking if a toy or app works properly.
What is Automation? Having a robot check it for us very fast!
"""

files["chapter18_test_automation_basics/calculator.py"] = """
# This is the toy/app we are going to test.

# A simple addition function.
def add(a, b):
    return a + b

# A simple subtraction function.
def subtract(a, b):
    return a - b
"""

files["chapter18_test_automation_basics/main.py"] = """
# Automation basics overview
print("Automation is like a robot checking homework again and again. 📝")
print("Instead of a human doing it slowly, the robot does it instantly!")
print("Run the test files in this folder to see the magic!")
"""

files["chapter18_test_automation_basics/calculator_test.py"] = """
# We import the calculator so we can test its functions.
import calculator

print("Starting Automation Test for Calculator 🤖...")

# Test Case 1: Addition
expected_result = 5 # We EXPECT 2 + 3 to equal 5.
actual_result = calculator.add(2, 3) # We ACTUALLY run the function to see what it gives.

# If the actual result matches what we expected, the test PASSES!
if actual_result == expected_result:
    print("✅ Add Test Passed!")
else:
    print("❌ Add Test Failed! Expected", expected_result, "but got", actual_result)

# Test Case 2: Subtraction
expected_sub = 10 # We EXPECT 15 - 5 to equal 10.
actual_sub = calculator.subtract(15, 5)

if actual_sub == expected_sub:
    print("✅ Subtract Test Passed!")
else:
    print("❌ Subtract Test Failed!")
"""

files["chapter18_test_automation_basics/login_test.py"] = """
# Testing a login system

# This function simulates checking a username and password.
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

print("Starting Login Test...")

# Test 1: We try the right password. We expect it to return True.
result1 = login("admin", "1234")

if result1 == True:
    print("✅ Correct Login Test Passed!")
else:
    print("❌ Correct Login Test Failed!")

# Test 2: We try a wrong password. We expect it to return False!
result2 = login("admin", "wrong!")

if result2 == False:
    print("✅ Wrong Password Test Passed! (It correctly blocked the user)")
else:
    print("❌ Wrong Password Test Failed!")
"""

files["chapter18_test_automation_basics/game_score_test.py"] = """
# Testing game score logic

# Function that gives bonus points if score is 100 or higher.
def get_bonus(score):
    if score >= 100:
        return 50
    return 0

print("Testing Bonus Logic...")

# We test with a score of 120. We expect a bonus of 50.
bonus = get_bonus(120)

if bonus == 50:
    print("✅ Bonus applied correctly for high score!")
else:
    print("❌ Bonus test failed.")
"""

# CHAPTER 19
files["chapter19_data_science_basics/README.md"] = """# Chapter 19: Data Science Basics for Kids 📊
Data Science is like being a detective! You look at lots of clues (data) to find patterns.
"""

files["chapter19_data_science_basics/scores.csv"] = """Student,Score
Alex,85
Sam,92
Mia,78
Leo,95
Zoe,88
"""

files["chapter19_data_science_basics/main.py"] = """
# Introduction to Data Science
print("Data Science is amazing! 📈")
print("We use data science to find averages, maximums, and build charts.")
print("Run the game_score_analysis.py file to see data science in action.")
"""

files["chapter19_data_science_basics/game_score_analysis.py"] = """
# Pandas is a powerful toolbox for reading tables of data (like Excel or CSV).
import pandas as pd

# Matplotlib is a toolbox for drawing graphs.
import matplotlib.pyplot as plt

print("Loading student scores data...")

# We use pandas to read the CSV file and turn it into a DataFrame (a data table).
df = pd.read_csv("scores.csv")

print("\\nHere is the data table:")
# This prints the whole table neatly!
print(df)

print("\\nCalculating average score...")
# We select the "Score" column, and use .mean() to find the average.
average = df["Score"].mean()
print("The average score is:", average)

print("\\nWho got the highest score?")
# We select the "Score" column, and use .max() to find the biggest number.
highest = df["Score"].max()
print("The highest score is:", highest, "🏆")

print("\\nClose the graph window to finish the program.")

# We tell pandas to draw a 'bar' chart. The x-axis is Student, the y-axis is Score.
df.plot(kind='bar', x='Student', y='Score', color='skyblue')

# We add a title and labels to the chart.
plt.title("Student Game Scores")
plt.ylabel("Score")

# Finally, we show the chart on the screen!
plt.show()
"""

# CHAPTER 20
files["chapter20_ai_basics/README.md"] = """# Chapter 20: AI Basics for Kids 🧠
Artificial Intelligence (AI) means teaching a computer to think or make guesses!
"""

files["chapter20_ai_basics/main.py"] = """
print("Welcome to Artificial Intelligence!")
print("AI can recognize faces, predict weather, and recommend games.")
print("Check out the files in this folder for fun AI examples.")
"""

files["chapter20_ai_basics/guessing_ai.py"] = """
# We import 'random' to simulate an AI making a guess.
import random

# A function that guesses your mood.
def guess_mood():
    # A list of possible moods.
    moods = ["Happy 😃", "Excited 🤩", "Sleepy 😴"]
    
    # random.choice() picks one item from the list randomly.
    print("My AI brain predicts you are feeling:", random.choice(moods))

# Call the function.
guess_mood()
"""

files["chapter20_ai_basics/game_recommender.py"] = """
# A very basic rule-based AI recommender.
# Real AI uses math, but this is a simple version using 'If' conditions!

def recommend_game(likes_action, likes_puzzle):
    # If they like action but no puzzles:
    if likes_action == "yes" and likes_puzzle == "no":
        return "Super Smash Action!"
        
    # If they like puzzles but no action:
    elif likes_puzzle == "yes" and likes_action == "no":
        return "Brain Teaser Puzzle 3000!"
        
    # If they like both, or neither:
    else:
        return "Minecraft! (Good for everything)"

print("AI Game Recommender")

# We ask the user questions and use .lower() to force the text into lowercase.
# This way, if they type "YES" or "yes", it works perfectly.
action = input("Do you like action? (yes/no): ").lower()
puzzle = input("Do you like puzzles? (yes/no): ").lower()

# We pass their answers to our AI function.
prediction = recommend_game(action, puzzle)

# We print the result.
print("🤖 AI Recommends: You should play ->", prediction)
"""

files["chapter20_ai_basics/smart_chatbot.py"] = """
# A simple rule-based Chatbot

print("Hello! I am ChatBot-Mini. Talk to me!")

# A 'while True' loop runs forever! It keeps the chatbot awake.
while True:
    # We ask the user to type a message.
    message = input("You: ").lower()
    
    # If they type 'quit', we use 'break' to escape the infinite loop!
    if message == "quit":
        print("Bot: Goodbye! 👋")
        break
        
    # We use 'in' to check if a specific word is hidden inside their message.
    elif "hello" in message or "hi" in message:
        print("Bot: Hello human! 🤖")
        
    elif "how are you" in message:
        print("Bot: My circuits are feeling great today! ⚡")
        
    elif "joke" in message:
        print("Bot: Why did the computer squeak? Because someone stepped on its mouse! 🐁😂")
        
    # A catch-all response if the bot doesn't understand.
    else:
        print("Bot: Hmm, I am still learning. Tell me more!")
"""

# CHAPTER 21
files["chapter21_mini_project/README.md"] = """# Chapter 21: Final Mini Project 🎓
Congratulations on reaching the final chapter!
Here we combine everything: OOP, User Input, Automation, and Logic!
"""

files["chapter21_mini_project/main.py"] = """
# Final project intro!
print("Get ready for the Final Mini Project! 🎉")
print("Run robot_academy.py to start.")
"""

files["chapter21_mini_project/robot_academy.py"] = """
# Robot Academy System
# Combines OOP, Exceptions, Loops, Input, File Handling, and Automation

# 1. OOP: We create a blueprint for a Robot Student.
class RobotStudent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.score = 0
        
    # A method to increase their score.
    def study(self):
        self.score += 10
        print(self.name, "studied hard! Score is now", self.score)
        
    # 2. File Handling & Exceptions: A safe method to save their data.
    def save_data(self):
        try:
            # We open the file in Append mode.
            with open("academy_records.txt", "a") as f:
                # We write the formatted string.
                f.write(f"Robot {self.name} (Model {self.model}) - Score: {self.score}\\n")
            print("Data saved successfully! 💾")
        except Exception as e:
            # If the file system fails, we catch the error safely.
            print("Could not save data!", e)

# 3. User Input: We ask the user to create their robot.
print("🎓 Welcome to Robot Academy 🎓")
name = input("Enter new robot name: ")
model = input("Enter robot model (e.g., T-800): ")

# Build the object using their input!
new_robot = RobotStudent(name, model)

# 4. Loops: An interactive menu that runs until they choose to exit.
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
        # 'break' escapes the while loop!
        break
        
    else:
        print("Invalid choice! Try again.")

# 5. Automation: A simple check at the very end to make sure the score isn't corrupted.
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
        f.write(content.strip() + "\n")

print(f"Kids Python Project V2 (with exhaustive comments) generated successfully in '{base_dir}' folder!")
