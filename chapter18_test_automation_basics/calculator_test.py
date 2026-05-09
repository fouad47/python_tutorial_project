# We import the calculator so we can test its functions.
import calculator

print("Starting Automation Test for Calculator 🤖...")

# Test Case 1: Addition
expected_result = 5 # We EXPECT 2 + 3 to equal 5.
actual_result = calculator.add(2, 3) # We ACTUALLY run the function to see what it gives.

# If the actual result matches what we expected, the test PASSES!
if actual_result == expected_result:
    print("✅ Add Test Passed!")
else:
    print("❌ Add Test Failed! Expected", expected_result, "but got", actual_result)

# Test Case 2: Subtraction
expected_sub = 10 # We EXPECT 15 - 5 to equal 10.
actual_sub = calculator.subtract(15, 5)

if actual_sub == expected_sub:
    print("✅ Subtract Test Passed!")
else:
    print("❌ Subtract Test Failed!")
