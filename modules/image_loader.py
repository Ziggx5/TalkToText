import os
import sys
from PIL import *
from customtkinter import *

def image_loader_handler():
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    parent_path = os.path.dirname(base_path)
    images_path = os.path.join(parent_path, "images")
    images = {}
    
    for file_name in os.listdir(images_path):
        file_path = os.path.join(images_path, file_name)
        open_image = Image.open(file_path)
        images[file_name] = CTkImage(light_image = open_image, dark_image = open_image, size = (15, 15))
    
    return images