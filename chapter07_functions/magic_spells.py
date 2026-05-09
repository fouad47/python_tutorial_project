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
