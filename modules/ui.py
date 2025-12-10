from customtkinter import *
from modules.speech_recognition import start_listening, stop_listening
from modules.file_loader import image_loader_handler
from modules.copy_logic import copy_to_clipboard
from PIL import *
import os

def start_ui():
    app = CTk()
    images = image_loader_handler()
    app.geometry("550x400")
    app.title("TalkToText")
    app.resizable(False, False)
    app.configure(fg_color = "#323232")

    text_box = CTkTextbox(app, width = 350, height = 380, font = ("TkTextFont", 15))
    text_box.place(x = 10, y = 10)

    sound_bar_label = CTkLabel(app, text = "Mic strength:")
    sound_bar_label.place(x = 380, y = 340)

    sound_bar = CTkProgressBar(app, width = 150, progress_color = "green")
    sound_bar.place(x = 380, y = 370)
    sound_bar.set(0)

    start_button = CTkButton(app, text = "Start", fg_color = "#3d3d3d", corner_radius = 5, image = images["start.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: start_listening(text_box, start_button, sound_bar))
    start_button.place(x = 380, y = 10)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#3d3d3d", corner_radius = 5, image = images["stop.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: stop_listening(start_button))
    stop_button.place(x = 380, y = 50)

    clear_button = CTkButton(app, text = "Copy", fg_color = "#3d3d3d", corner_radius = 5, image = images["copy.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: copy_to_clipboard(app, text_box))
    clear_button.place(x = 380, y = 90)

    reset_button = CTkButton(app, text = "Reset", fg_color = "#3d3d3d", corner_radius = 5, image = images["reset.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: text_box.delete("1.0", "end"))
    reset_button.place(x = 380, y = 130)

    app.mainloop()
