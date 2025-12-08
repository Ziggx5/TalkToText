from customtkinter import *
from modules.speech_recognition import start_listening, stop_listening
from modules.image_loader import image_loader_handler
import os

def start_ui():
    app = CTk()
    images = image_loader_handler()
    app.geometry("400x400")
    app.title("TalkToText")
    app.resizable(False, False)
    app.configure(fg_color = "#323232")

    text_box = CTkTextbox(app, width = 300, height = 200)
    text_box.place(x = 10, y = 50)
    
    start_button = CTkButton(app, text = "Start", fg_color = "#3d3d3d", corner_radius = 5, image = images["start.png"], compound = "left", command = lambda: start_listening(text_box, start_button))
    start_button.place(x = 10, y = 10)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#3d3d3d", corner_radius = 5, image = images["stop.png"], compound = "left", command = lambda: stop_listening(start_button))
    stop_button.place(x = 160, y = 10)

    app.mainloop()
