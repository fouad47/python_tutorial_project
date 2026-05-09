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
