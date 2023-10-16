## pyttsx3 library
# https://thepythoncode.com/article/convert-text-to-speech-in-python#Offline_Text_to_Speech
import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# convert this text to speech
text = input("please write text here to speech : ")
engine.say(text)
engine.say(text)
engine.say(text)

# play the speech
engine.runAndWait()


