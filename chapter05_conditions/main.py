# We create a variable 'weather' and set it to "sunny".
weather = "sunny"

# 'if' checks if a condition is True. We use == to check if two things are exactly equal.
if weather == "raining":
    # This code only runs if weather is "raining".
    print("Take an umbrella! ☔")
    
# 'elif' means "Else If". It checks another condition if the first one was False.
elif weather == "snowing":
    # This code only runs if weather is "snowing".
    print("Wear a jacket! 🧥")
    
# 'else' runs if ALL the conditions above were False.
else:
    # Since weather is "sunny" (not raining and not snowing), this line will run!
    print("Wear sunglasses! 🕶️")
