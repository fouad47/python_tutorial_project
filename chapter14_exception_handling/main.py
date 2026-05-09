print("Let's divide 10 by a number!")

# We use 'try:' to wrap dangerous code that might crash.
try:
    # 10 divided by 0 is impossible in math! This will cause an error (ZeroDivisionError).
    result = 10 / 0
    print(result)
    
# 'except' acts like a safety net. It catches the specific error so the program doesn't crash!
except ZeroDivisionError:
    # We print a friendly message instead of a scary red error.
    print("Oh no! You cannot divide by zero! 🚫")
    
# 'finally' is a block that ALWAYS runs, no matter what happened above.
finally:
    print("Math operation finished.")
