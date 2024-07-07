import pyttsx3

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Sarvesh")
    while True:
        command = pyttsx3.init()
        x = input("Enter what you want me to speak: ")
        if x == "q":
            print("bye bye friends")
            break
        command.say(x)
        command.runAndWait()
