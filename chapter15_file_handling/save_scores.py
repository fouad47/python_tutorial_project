# Saving game scores
player = "Alex"
score = 999

# We use the 'with' keyword. It is a magic trick that AUTOMATICALLY closes the file for us!
# 'a' means Append mode. It adds new text to the end without deleting the old text.
with open("scores.txt", "a") as f:
    # We write the player's name, their score, and \n (which means "New Line").
    f.write(player + " scored " + str(score) + "\n")
    
print("Score saved successfully! 🏆")

print("\nAll saved scores:")

# We open the file in Read ('r') mode using 'with'.
with open("scores.txt", "r") as f:
    # Read everything and print it.
    print(f.read())
