from customtkinter import *
from modules.speech_recognition import start_listening, stop_listening
from modules.file_loader import image_loader_handler, icon_image_loader
from modules.copy_logic import copy_to_clipboard
from PIL import *
import os

def start_ui():
    app = CTk()
    images = image_loader_handler()
    icon_photo = icon_image_loader()
    app.geometry("550x430")
    app.title("TalkToText")
    app.resizable(False, False)
    app.configure(fg_color = "#323232")
    app.iconphoto(True, icon_photo)

    text_box = CTkTextbox(app, width = 350, height = 380, font = ("TkTextFont", 15), wrap = "word")
    text_box.place(x = 10, y = 10)

    status_label = CTkLabel(app, text = "Stopped...", font = ("TkTextFont", 15))
    status_label.place(x = 10, y = 395)

    start_button = CTkButton(app, text = "Start", fg_color = "#3d3d3d", corner_radius = 5, image = images["start.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: start_listening(text_box, start_button, status_label))
    start_button.place(x = 380, y = 10)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#3d3d3d", corner_radius = 5, image = images["stop.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: stop_listening(start_button, status_label))
    stop_button.place(x = 380, y = 50)

    clear_button = CTkButton(app, text = "Copy", fg_color = "#3d3d3d", corner_radius = 5, image = images["copy.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: copy_to_clipboard(app, text_box))
    clear_button.place(x = 380, y = 90)

    reset_button = CTkButton(app, text = "Reset", fg_color = "#3d3d3d", corner_radius = 5, image = images["reset.png"], compound = "left", width = 150, height = 30, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: text_box.delete("1.0", "end"))
    reset_button.place(x = 380, y = 130)

    app.mainloop()
