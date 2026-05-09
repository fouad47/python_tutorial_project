# Testing game score logic

# Function that gives bonus points if score is 100 or higher.
def get_bonus(score):
    if score >= 100:
        return 50
    return 0

print("Testing Bonus Logic...")

# We test with a score of 120. We expect a bonus of 50.
bonus = get_bonus(120)

if bonus == 50:
    print("✅ Bonus applied correctly for high score!")
else:
    print("❌ Bonus test failed.")
