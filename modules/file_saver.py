from modules.file_loader import get_project_root
import os

def create_file(file_name):
    root = get_project_root()
    save_folder = os.path.join(root, "saves")
    create = open(f"{save_folder}/{file_name}.txt", "x")