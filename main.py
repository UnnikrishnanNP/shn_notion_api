import os
import speech_recognition as sr
import gtts 
from playsound import playsound

r = sr.Recognizer()
ACTIVATION_COMMAND = "Hello"

def audio_to_text():
    with sr.Microphone() as source:
        print("Heyy")
        audio = r.listen(source)
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError:
        print("Request Error")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        temp = "./temp.mp3"
        tts.save(temp)
        playsound(temp)
        os.remove(temp)
    except AssertionError:
        print("Assertion error")

    

if __name__ == "__main__":
    while True:
        command = audio_to_text()
        if ACTIVATION_COMMAND in command.lower():
            print("Activated")
            play_sound("What can i do for you?")

            note = audio_to_text()
            if note:
                play_sound(note)




