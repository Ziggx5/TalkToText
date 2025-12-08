import speech_recognition as sr
import threading
from customtkinter import *


recogniser = sr.Recognizer()

def start_listening(text_box, start_button):
    global listening
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box, start_button,))
    thread.start()

def recognition_handler(text_box, start_button):
    start_button.configure(state = "disabled")
    text_box.delete("0.0", "end")
    last_text = ""
    with sr.Microphone() as source:
        while listening:
            try:
                audio = recogniser.listen(source)
                text = recogniser.recognize_google(audio, language="sl-SI")
                text_box.insert("end", f" {text}")
            except sr.WaitTimeoutError:
                text_box.insert("end", "No input")
            except Exception as e:
                text_box.insert("end", e)

def stop_listening(start_button):
    global listening
    listening = False
    start_button.configure(state = "enabled")