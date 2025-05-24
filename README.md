# PhotoDuplicates

PhotoDuplicates is a simple Windows tool to help you find and move duplicate image files from a selected folder (including all subfolders) to a destination folder. It uses file hashing to detect duplicates and provides a graphical interface for easy folder selection.

## Features

- Detects duplicate images by content (not just filename)
- Supports JPG, JPEG, PNG, GIF, BMP, and TIFF formats
- Recursively scans all subfolders
- Simple graphical interface for selecting source and destination folders
- Moves duplicates to a folder you choose

## How to Use

### 1. Run the Program

- If you have Python installed, run:
  ```
  python removeduplicates.py
  ```
- If you have the executable (`removeduplicates.exe`), just double-click it.

### 2. Select Folders

- When prompted, select the **source folder** (where your photos are).
- Next, select the **destination folder** (where duplicates will be moved).
