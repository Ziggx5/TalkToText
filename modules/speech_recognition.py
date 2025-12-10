import speech_recognition as sr
import threading
from customtkinter import *


recogniser = sr.Recognizer()

def start_listening(text_box, start_button, sound_bar):
    global listening
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box, start_button, sound_bar,))
    thread.start()

def recognition_handler(text_box, start_button, sound_bar):
    start_button.configure(state = "disabled")
    text_box.delete("0.0", "end")
    last_text = ""

    with sr.Microphone() as source:
        while listening:
            try:
                audio = recogniser.listen(source)
                volume_strength = recogniser.energy_threshold * recogniser.dynamic_energy_ratio
                level = min(volume_strength / 5000, 1)
                sound_bar.set(level)
                text = recogniser.recognize_google(audio)
                if text != last_text:
                    text_box.insert("end", f" {text}")
                    last_text = text
            except sr.WaitTimeoutError:
                text_box.insert("end", "No input")
            except Exception as e:
                text_box.insert("end", e)

def stop_listening(start_button):
    global listening
    listening = False
    start_button.configure(state = "enabled")