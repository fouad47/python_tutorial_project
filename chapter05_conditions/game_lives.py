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
