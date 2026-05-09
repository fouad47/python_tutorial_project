# Writing to a file
# open() takes the file name and the mode. 'w' means Write mode (creates a new file).
file = open("secret_message.txt", "w")

# We use .write() to put text inside the file.
file.write("Python is awesome! 🐍")

# We MUST close the file when we are done so it saves properly!
file.close()
print("Message saved to file!")

# Reading from a file
# 'r' means Read mode. It opens an existing file so we can look inside.
file2 = open("secret_message.txt", "r")

# We use .read() to extract all the text and save it in a variable.
content = file2.read()

# Don't forget to close!
file2.close()

# Print out what we read.
print("Reading file:", content)
