"""
Creates script folder and the log and screeshots folders
"""
import os
import tkinter as tk
from tkinter import filedialog

#establish target directory
root = tk.Tk()
root.withdraw()
print("where would you like your folder to go?")
file_path = tk.filedialog.askdirectory()

#Setup folders for screenshots and logs as well as empty .py file
def create_automation_script(script_name):
    path = "{0}/{1}".format(file_path, script_name)
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)
        logs = path + "\logs"
        screenshots = path + "\screenshots"
        os.makedirs(logs)
        os.makedirs(screenshots)
        open(path + "\\" + script_name + ".py", "x")
        return True
    else:
        print("Directories already exist")
        return False

script_name = input("enter the name of your new_script: ")
if create_automation_script(script_name):
    print("Folder '{}' created with subdirectories for logs and screenshots and the script .py file.".format(script_name))
else:
    print("No files created.")