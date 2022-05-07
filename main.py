from datetime import datetime
import os
import speech_recognition as sr
import gtts 
from playsound import playsound
import configparser
from notion import NotionClient

config = configparser.RawConfigParser()
config.read('config.ini')

token = config['notion']['token']
database = config['notion']['database']

client = NotionClient(token,database)
r = sr.Recognizer()
ACTIVATION_COMMAND = "hello"

def get_audio():
    with sr.Microphone() as source:
        print("Heyy")
        audio = r.listen(source)
    return audio

def get_text(audio):
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
        audio = get_audio()
        command = get_text(audio)

        if ACTIVATION_COMMAND in command.lower():
            print("Activated")
            play_sound("What can i do for you?")

            note = get_audio()
            note = get_text(note)

            now = datetime.now().astimezone().isoformat()
            res = client.create_page(note,now)
            if res.status_code == 200:
                print("Stored data")




