from customtkinter import *
from modules.speech_recognition import start_listening, stop_listening
from modules.image_loader import image_loader_handler
import os

def start_ui():
    app = CTk()
    images = image_loader_handler()
    app.geometry("500x400")
    app.title("TalkToText")
    app.resizable(False, False)
    app.configure(fg_color = "#323232")

    text_box = CTkTextbox(app, width = 300, height = 380, font = ("TkTextFont", 15))
    text_box.place(x = 10, y = 10)
    
    start_button = CTkButton(app, text = "Start", fg_color = "#3d3d3d", corner_radius = 5, image = images["start.png"], compound = "left", width = 150, hover_color= "gray", command = lambda: start_listening(text_box, start_button))
    start_button.place(x = 330, y = 10)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#3d3d3d", corner_radius = 5, image = images["stop.png"], compound = "left", width = 150, hover_color= "gray", command = lambda: stop_listening(start_button))
    stop_button.place(x = 330, y = 50)

    clear_button = CTkButton(app, text = "Clear", fg_color = "#3d3d3d", corner_radius = 5, image = images["clear.png"], compound = "left", width = 150, hover_color= "gray", command = lambda: text_box.delete("0.0", "end"))
    clear_button.place(x = 330, y = 90)

    app.mainloop()
