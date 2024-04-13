import os
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ =='__main__':
    a = "Welcome to RoboSpeaker 1.1 created by Ankit"
    speak.Speak(a)
    print("Welcome to RoboSpeaker 1.1 created by Ankit")
    while True:
        x = input("Enter what you want me to speak or press 'q' to exit: ")
        if x == "q":
            break
        speak.Speak(x)
