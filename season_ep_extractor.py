import os
import re
import tkinter as tk
from tkinter import filedialog

def rename_files(directory):
    for filename in os.listdir(directory):
        match = re.search(r'S(\d+)E(\d+)', filename)
        if match:
            season_episode = match.group(0)
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{season_episode}{file_extension}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed file {filename} to {new_filename}")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        rename_files(directory)

root = tk.Tk()
button = tk.Button(root, text="Select Directory", command=browse_directory)
button.pack()
root.mainloop()
