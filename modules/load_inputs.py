import pyaudio

def load_all_inputs():
    mic = pyaudio.PyAudio()
    devices = []
    device_index = []
    short_name = []

    for i in range (mic.get_device_count()):
        mic_info = mic.get_device_info_by_index(i)

        if mic_info["maxInputChannels"] >= 1:
            device_name = mic_info['name']
            devices.append(device_name)
            device_index.append(i)

            if len(device_name) > 10:
                short_name.append(f"{device_name[:10]}...")
            else:
                short_name.append(device_name)

    return devices, device_index, short_name