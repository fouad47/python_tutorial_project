# Importing abstraction tools
from abc import ABC, abstractmethod

# Abstract class for any remote control
class RemoteControl(ABC):
    # Every remote must have a power button!
    @abstractmethod
    def press_power(self):
        pass

# A TV remote implements the power button for a TV.
class TVRemote(RemoteControl):
    def press_power(self):
        print("Turning TV on... showing cartoons! 📺")

# A Drone remote implements the power button for a Drone.
class DroneRemote(RemoteControl):
    def press_power(self):
        print("Starting drone propellers... ready to fly! 🚁")

# Testing the remotes
my_tv_remote = TVRemote()
my_tv_remote.press_power()

my_drone_remote = DroneRemote()
my_drone_remote.press_power()
