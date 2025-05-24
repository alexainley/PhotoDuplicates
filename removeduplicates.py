import os
import hashlib
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def file_hash(filepath, chunk_size=8192):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_and_move_duplicates(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    hashes = {}
    for root, _, files in os.walk(src_folder):
        for name in files:
            if name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                filepath = os.path.join(root, name)
                h = file_hash(filepath)
                if h in hashes:
                    print(f"Duplicate found: {filepath}")
                    shutil.move(filepath, os.path.join(dest_folder, name))
                else:
                    hashes[h] = filepath

def select_folders_and_run():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    src_folder = filedialog.askdirectory(title="Select Source Folder")
    if not src_folder:
        messagebox.showinfo("Cancelled", "No source folder selected.")
        return

    dest_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not dest_folder:
        messagebox.showinfo("Cancelled", "No destination folder selected.")
        return

    find_and_move_duplicates(src_folder, dest_folder)
    messagebox.showinfo("Done", "Duplicate search and move complete.")

if __name__ == "__main__":
    select_folders_and_run()