# Blueprint for a locked box
class SecretToyBox:
    def __init__(self):
        # The toy is hidden inside a private variable.
        self.__secret_toy = "Golden Robot"
        
    # A method to open the box, but it requires a password!
    def open_box(self, password):
        # We check if the password is correct.
        if password == "1234":
            print("The secret toy is:", self.__secret_toy, "🏆")
        else:
            print("Wrong password! The box stays closed. 🔒")

# We build the box.
box = SecretToyBox()

# We try a bad password. It won't work.
print("Trying wrong password:")
box.open_box("0000")

# We try the good password. It works!
print("Trying right password:")
box.open_box("1234")
