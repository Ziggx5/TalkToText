import pyaudio

def load_all_inputs():
    mic = pyaudio.PyAudio()
    devices = {}

    for i in range (mic.get_device_count()):
        mic_info = mic.get_device_info_by_index(i)

        if mic_info["maxInputChannels"] >= 1:
            device_name = mic_info['name']
            devices[device_name] = i

    return devices