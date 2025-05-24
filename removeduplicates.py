import os
import hashlib
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def file_hash(filepath, chunk_size=8192):
    """
    Calculate the MD5 hash of a file for duplicate detection.
    Reads the file in chunks to handle large files efficiently.
    """ 
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_and_move_duplicates(src_folder, dest_folder):
    """
    Find duplicate images in src_folder (including subfolders) and move them to dest_folder.
    Duplicates are detected by comparing file hashes.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder) # Create destination folder if it doesn't exist

    hashes = {} # Dictionary to store unique file hashes
    for root, _, files in os.walk(src_folder):  # Recursively walk through all subfolders
        for name in files:
        # Check if the file is an image by extension
            if name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                filepath = os.path.join(root, name)
                h = file_hash(filepath)
                if h in hashes:
                    print(f"Duplicate found: {filepath}")
                    try:
                        shutil.move(filepath, os.path.join(dest_folder, name)) # Move duplicate file
                    except Exception as e:
                        print(f"Could not move file: {filepath}. Reason: {e}")
                else:
                    hashes[h] = filepath # Store hash of unique file

def select_folders_and_run():
    """
    Show a GUI for the user to select source and destination folders,
    then run the duplicate finder.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask user to select the source folder
    src_folder = filedialog.askdirectory(title="Select Source Folder")
    if not src_folder:
        messagebox.showinfo("Cancelled", "No source folder selected.")
        return
    
    # Ask user to select the destination folder
    dest_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not dest_folder:
        messagebox.showinfo("Cancelled", "No destination folder selected.")
        return
    
    # Run the duplicate finder and show completion message
    find_and_move_duplicates(src_folder, dest_folder)
    messagebox.showinfo("Done", "Duplicate search and move complete.")

if __name__ == "__main__":
    select_folders_and_run()