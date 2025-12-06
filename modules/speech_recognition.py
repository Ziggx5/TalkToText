import speech_recognition as sr
import threading

recogniser = sr.Recognizer()

def start_listening(text_box):
    thread = threading.Thread(target = recognition_handler, args = (text_box,))
    thread.start()

def recognition_handler(text_box):
    print("yo")
    with sr.Microphone() as source:
        try:
            text_box.insert("end", "Listening...")
            audio = recogniser.listen(source, timeout = 3)
            text = recogniser.recognize_google(audio, language = "sl-SI")
            text_box.insert("end", text)
        except sr.WaitTimeoutError:
            text_box.insert("end", "No input")
        except Exception as e:
            text_box.insert("end", e)