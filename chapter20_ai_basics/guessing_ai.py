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
