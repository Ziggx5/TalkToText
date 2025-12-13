import time
import threading

def start_timer(state, timer_label):
    global time_running
    time_running = state
    thread = threading.Thread(target = timer_handler, args = (state, timer_label,))
    thread.start()

def timer_handler(state, timer_label):
    global time_running
    start = time.time()
    while time_running:
        time.sleep(1)
        end = time.time()
        result = int(end - start)
        timer_label.configure(text = f"Time: {result} sec")
