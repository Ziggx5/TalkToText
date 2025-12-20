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

        seconds = result % 60
        minutes = (result // 60) % 60
        hours = result // 3600


        timer_label.configure(text = f"Time: {hours:02}h {minutes:02}m {seconds:02}s")
