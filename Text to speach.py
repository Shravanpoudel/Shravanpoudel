#First install pyttsx from pip install 
import pyttsx3
text =  pyttsx3.init()
while True:
 t = input("what you want to convert to speech:\n")
 text.say(t)
 text.runAndWait()
 if t=="Q":
    break

