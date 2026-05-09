# Blueprint for a Piggy Bank
class PiggyBank:
    def __init__(self):
        # We use two underscores (__) to make a variable PRIVATE (hidden).
        # Nobody from the outside can touch this variable directly!
        self.__money = 0 
        
    # This is a "Getter" method. It safely allows us to SEE the hidden money.
    def get_money(self):
        return self.__money
        
    # This is a "Setter" method. It safely allows us to ADD money, but with rules.
    def add_money(self, amount):
        # The rule: You can only add money if the amount is greater than 0!
        if amount > 0:
            self.__money += amount
            print("Added", amount, "coins!")
        else:
            # If someone tries to steal money by adding negative coins, we block them!
            print("You can't add negative coins!")

# We build a PiggyBank object.
bank = PiggyBank()

# We safely use the setter to add 50 coins.
bank.add_money(50)

# We safely use the getter to look at our money.
print("I have", bank.get_money(), "coins in my piggy bank. 🐷")
