from modules.file_loader import get_project_root
import os

def create_file(file_name, status_label):
    root = get_project_root()
    save_folder = os.path.join(root, "saves")
    path = os.path.join(save_folder, f"{file_name}.txt")
    try:
        with open(path, "x"):
            pass
        status_label.configure(text = "Successfully created", text_color = "green")
        current_file = path
        return path
    except FileExistsError:
        status_label.configure(text = "File already exists", text_color = "red")

def save_file(current_file, text_box):
    if not current_file:
        return
    with open (current_file, "w") as f:
        f.write(text_box)