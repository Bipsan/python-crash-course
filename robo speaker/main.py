import os

print("welcome to robospeaker 1.1. Created by Bipsan")
while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
        os.system("say 'bye bye friend'")
        break
    command = f"say {x}"
    os.system(command)