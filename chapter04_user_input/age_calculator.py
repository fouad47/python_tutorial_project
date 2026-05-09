# Age calculator

# Ask for the age. Warning: input() ALWAYS gives us text (a String), even if we type numbers.
age_text = input("How old are you? ")

# We must use int() to change the text into a real math number (Integer).
age = int(age_text)

# Now we can do math! We add 1 to the age.
next_year_age = age + 1

# Print the result.
print("Next year, you will be", next_year_age, "years old! 🎂")
