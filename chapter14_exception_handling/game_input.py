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
