# Testing a login system

# This function simulates checking a username and password.
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

print("Starting Login Test...")

# Test 1: We try the right password. We expect it to return True.
result1 = login("admin", "1234")

if result1 == True:
    print("✅ Correct Login Test Passed!")
else:
    print("❌ Correct Login Test Failed!")

# Test 2: We try a wrong password. We expect it to return False!
result2 = login("admin", "wrong!")

if result2 == False:
    print("✅ Wrong Password Test Passed! (It correctly blocked the user)")
else:
    print("❌ Wrong Password Test Failed!")
