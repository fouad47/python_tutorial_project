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
