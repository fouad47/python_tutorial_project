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
