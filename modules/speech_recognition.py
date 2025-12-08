import speech_recognition as sr
import threading

recogniser = sr.Recognizer()

def start_listening(text_box):
    global listening
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box,))
    thread.start()

def recognition_handler(text_box):
    text_box.delete("0.0", "end")
    with sr.Microphone() as source:
        while listening:
            try:
                audio = recogniser.listen(source)
                text = recogniser.recognize_google(audio)
                text_box.insert("end", text)
            except sr.WaitTimeoutError:
                text_box.insert("end", "No input")
            except Exception as e:
                text_box.insert("end", e)

def stop_listening():
    global listening
    listening = False