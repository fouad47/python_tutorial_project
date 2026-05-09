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
