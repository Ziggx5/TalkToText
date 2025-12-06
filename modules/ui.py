from customtkinter import *
from modules.speech_recognition import start_listening

def start_ui():
    app = CTk()
    app.geometry("700x500")
    app.title("TalkToText")
    app.grid_columnconfigure(0, weight = 1)
    app.grid_rowconfigure(0, weight = 1)    

    text_box = CTkTextbox(app, width = 500, height = 300)
    text_box.grid(row = 0, column = 0, pady = (0, 80))
    
    start_button = CTkButton(app, text = "Start", command = start_listening(text_box))
    start_button.place(x = 10, y = 10)

    app.mainloop()
