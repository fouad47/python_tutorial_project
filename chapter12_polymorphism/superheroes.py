# Superhero 1
class Superman:
    def attack(self):
        print("Superman shoots laser eyes! 🔴_🔴")

# Superhero 2
class Batman:
    def attack(self):
        print("Batman throws a batarang! 🦇")

# A list holding different types of superheroes.
heroes = [Superman(), Batman()]

print("Heroes, attack!")

# We loop through the list and tell each hero to attack.
# Each hero attacks in their own unique way!
for hero in heroes:
    hero.attack()
