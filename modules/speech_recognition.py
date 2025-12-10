import threading
from vosk import Model, KaldiRecognizer
import pyaudio
from modules.file_loader import get_parent_path
import os
import time
import json

parent_path = get_parent_path()
vosk_path = os.path.join(parent_path, "vosk-model-small-en-us-0.15")

model = Model(vosk_path)
recogniser = KaldiRecognizer(model, 16000)

def start_listening(text_box, start_button, status_label):
    global listening, mic, stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate = 16000, channels = 1, format = pyaudio.paInt16, input = True, frames_per_buffer = 8192)
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box, start_button, status_label,))
    thread.start()

def recognition_handler(text_box, start_button, status_label):
    start_button.configure(state = "disabled")
    text_box.delete("0.0", "end")
    status_label.configure(text = "Listening...")
    stream.start_stream()
    print(vosk_path)

    while listening:
        try:
            data = stream.read(4096, exception_on_overflow=False)
            if recogniser.AcceptWaveform(data):
                text = json.loads(recogniser.Result())
                text_box.insert("end", f" {text["text"]}")

        except Exception as e:
            text_box.insert("end", e)

def stop_listening(start_button, status_label):
    global listening, mic, stream
    listening = False
    time.sleep(0.5)
    mic = None
    stream = None
    start_button.configure(state = "enabled")
    status_label.configure(text = "Stopped...")
