import pyttsx3
import sys

# engine = pyttsx3.init()

if (sys.argv[1] == "-m"):
    voices = pyttsx3.init().getProperty('voices')
    engine.setProperty("rate", 145) 
    engine.say(sys.argv[2])
    engine.runAndWait()

elif (sys.argv[1] == "-f"):
    f = open(sys.argv[2], "r")
    engine.say(f.read())
    engine.runAndWait()

else:
    print("Error: <Invalid voice type>")


