# We can import OUR OWN module! We just type the name of the file (without .py).
import robot_parts

print("Robot Factory is open!")

# We use the dot (.) to access the tools inside the module.
robot_parts.build_arm()
robot_parts.build_leg()

print("Robot is ready to go! 🤖")
