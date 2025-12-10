import threading
from vosk import Model, KaldiRecognizer
import pyaudio
from modules.file_loader import get_parent_path
import os
import time

parent_path = get_parent_path()
vosk_path = os.path.join(parent_path, "vosk-model-small-en-us-0.15")

model = Model(vosk_path)
recogniser = KaldiRecognizer(model, 16000)

def start_listening(text_box, start_button, sound_bar):
    global listening, mic, stream
    mic = pyaudio.PyAudio()
    stream = mic.open(rate = 16000, channels = 1, format = pyaudio.paInt16, input = True, frames_per_buffer = 8192)
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box, start_button, sound_bar,))
    thread.start()

def recognition_handler(text_box, start_button, sound_bar):
    start_button.configure(state = "disabled")
    text_box.delete("0.0", "end")
    last_text = ""
    stream.start_stream()
    print(vosk_path)

    while listening:
        try:
            data = stream.read(4096, exception_on_overflow=False)
            if recogniser.AcceptWaveform(data):
                text = recogniser.Result()
            else:
                text = "No data"

            #level = min(volume_strength / 5000, 1)
            #sound_bar.set(level)
            if text != last_text:
                text_box.insert("end", f" {text}")
                last_text = text
        except Exception as e:
            text_box.insert("end", e)

def stop_listening(start_button):
    global listening, mic, stream
    listening = False
    time.sleep(0.5)
    mic = None
    stream = None
    start_button.configure(state = "enabled")
    print("stopped")