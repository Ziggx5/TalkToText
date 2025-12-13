import os
import sys
from PIL import *
from customtkinter import *

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
def image_loader_handler():
    root = get_project_root()
    print(root)
    images_path = os.path.join(root, "images")
    print(images_path)
    images = {}
    
    for file_name in os.listdir(images_path):
        file_path = os.path.join(images_path, file_name)
        open_image = Image.open(file_path)
        images[file_name] = CTkImage(light_image = open_image, dark_image = open_image, size = (15, 15))
    
    return images

def icon_image_loader():
    root = get_project_root()
    icon_path = os.path.join(root, "images", "icon.png")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)

    return icon_photo