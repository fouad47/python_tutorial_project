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
