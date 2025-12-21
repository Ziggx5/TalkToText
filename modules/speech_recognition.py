import threading
from vosk import Model, KaldiRecognizer
import pyaudio
from modules.file_loader import get_project_root
from modules.load_inputs import load_all_inputs
import os
import time
import json

root = get_project_root()
vosk_path = os.path.join(root, "vosk-model")

def start_listening(text_box, start_button, status_label, selected_input_index):
    global listening, mic, stream
    devices = load_all_inputs()
    print(selected_input_index)
    mic = pyaudio.PyAudio()
    stream = mic.open(rate = 16000, channels = 1, format = pyaudio.paInt16, input_device_index = selected_input_index, input = True, frames_per_buffer = 8192)
    listening = True
    thread = threading.Thread(target = recognition_handler, args = (text_box, start_button, status_label, selected_input_index,))
    thread.start()

def recognition_handler(text_box, start_button, status_label, selected_input_index):
    start_button.configure(state = "disabled")
    status_label.configure(text = "Listening...")
    model = Model(vosk_path)
    recogniser = KaldiRecognizer(model, 16000)
    stream.start_stream()

    while listening:
        try:
            data = stream.read(4096, exception_on_overflow = False)
            if recogniser.AcceptWaveform(data):
                text_box.focus_set()
                text = json.loads(recogniser.Result())
                text_box.insert("end", f" {text['text']}")

        except Exception as e:
            text_box.insert("end", e)

def stop_listening(start_button, status_label):
    global listening, mic, stream
    listening = False
    time.sleep(0.5)
    stream.stop_stream()
    stream.close()
    mic.terminate()
    mic = None
    stream = None
    start_button.configure(state = "enabled")
    status_label.configure(text = "Stopped...")
