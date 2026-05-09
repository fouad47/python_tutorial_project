# Robot Academy System
# Combines OOP, Exceptions, Loops, Input, File Handling, and Automation

# 1. OOP: We create a blueprint for a Robot Student.
class RobotStudent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.score = 0
        
    # A method to increase their score.
    def study(self):
        self.score += 10
        print(self.name, "studied hard! Score is now", self.score)
        
    # 2. File Handling & Exceptions: A safe method to save their data.
    def save_data(self):
        try:
            # We open the file in Append mode.
            with open("academy_records.txt", "a") as f:
                # We write the formatted string.
                f.write(f"Robot {self.name} (Model {self.model}) - Score: {self.score}\n")
            print("Data saved successfully! 💾")
        except Exception as e:
            # If the file system fails, we catch the error safely.
            print("Could not save data!", e)

# 3. User Input: We ask the user to create their robot.
print("🎓 Welcome to Robot Academy 🎓")
name = input("Enter new robot name: ")
model = input("Enter robot model (e.g., T-800): ")

# Build the object using their input!
new_robot = RobotStudent(name, model)

# 4. Loops: An interactive menu that runs until they choose to exit.
while True:
    print("\nMenu:")
    print("1. Study (Gain Points)")
    print("2. Save Data")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        new_robot.study()
        
    elif choice == "2":
        new_robot.save_data()
        
    elif choice == "3":
        print("Goodbye! System shutting down... 🔌")
        # 'break' escapes the while loop!
        break
        
    else:
        print("Invalid choice! Try again.")

# 5. Automation: A simple check at the very end to make sure the score isn't corrupted.
print("\n--- Running Automation Check ---")
if new_robot.score >= 0:
    print("✅ System Check Passed: Final score is valid.")
else:
    print("❌ System Check Failed.")
