from modules.file_loader import get_project_root
import os

def create_file(file_name, status_label):
    root = get_project_root()
    save_folder = os.path.join(root, "saves")
    try:
        create = open(f"{save_folder}/{file_name}.txt", "x")
        status_label.configure(text = "Successfully created", text_color = "green")
    except:
        status_label.configure(text = "File already exist", text_color = "red")