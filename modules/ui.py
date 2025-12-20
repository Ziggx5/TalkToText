from customtkinter import *
from modules.speech_recognition import start_listening, stop_listening
from modules.file_loader import image_loader_handler, icon_image_loader
from modules.copy_logic import copy_to_clipboard
from modules.load_inputs import load_all_inputs
from modules.timer import start_timer
from PIL import *
import os

def start_ui():
    app = CTk()
    images = image_loader_handler()
    icon_photo = icon_image_loader()
    devices = load_all_inputs()
    app.geometry("550x430")
    app.title("TalkToText")
    #app.iconphoto(True, icon_photo)
    app.resizable(False, False)
    app.configure(fg_color = "#323232")

    selected_input_index = 0

    def input_return(value):
        nonlocal selected_input_index
        selected_input_index = devices[value]

        return selected_input_index
    
    
    text_box = CTkTextbox(app, width = 350, height = 380, font = ("TkTextFont", 15), wrap = "word", fg_color= "#1d1e1e")
    text_box.place(x = 10, y = 10)

    status_label = CTkLabel(app, text = "Idle...", font = ("TkTextFont", 15), text_color = "white")
    status_label.place(x = 10, y = 395)

    timer_label = CTkLabel(app, text = "Time:", font = ("TkTextFont", 15), text_color = "white")
    timer_label.place(x = 220, y = 395)

    input_label = CTkLabel(app, text = "Input device:", font = ("TkTextFont", 15), text_color = "white")
    input_label.place(x = 380, y = 360)

    start_button = CTkButton(app, text = "Start", fg_color = "#3d3d3d", text_color = "white", corner_radius = 5, image = images["start.png"], compound = "left", width = 150, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: (start_listening(text_box, start_button, status_label, selected_input_index), start_timer(True, timer_label)))
    start_button.place(x = 380, y = 10)

    stop_button = CTkButton(app, text = "Stop", fg_color = "#3d3d3d", text_color = "white", corner_radius = 5, image = images["stop.png"], compound = "left", width = 150, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: (stop_listening(start_button, status_label), start_timer(False, timer_label)))
    stop_button.place(x = 380, y = 50)

    clear_button = CTkButton(app, text = "Copy", fg_color = "#3d3d3d", text_color = "white", corner_radius = 5, image = images["copy.png"], compound = "left", width = 150, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: copy_to_clipboard(app, text_box))
    clear_button.place(x = 380, y = 90)

    reset_button = CTkButton(app, text = "Reset", fg_color = "#3d3d3d", text_color = "white", corner_radius = 5, image = images["reset.png"], compound = "left", width = 150, font = ("TkTextFont", 15), hover_color= "gray", command = lambda: (text_box.delete("1.0", "end"), timer_label.configure(text = "Time:")))
    reset_button.place(x = 380, y = 130)

    select_microphone = CTkOptionMenu(app, fg_color = "#3d3d3d", text_color = "white", corner_radius = 5, width = 150, height = 30, button_color = "#3d3d3d", button_hover_color = "gray", dynamic_resizing = False, font = ("TkTextFont", 15), values = list(devices.keys()), command = input_return)
    select_microphone.place(x = 380, y = 390)
    
    app.mainloop()
