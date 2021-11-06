import os
os.system('cmd /c "pip install tkinter"')
os.system('cmd /c "pip install pytube"')
os.system('cmd /c "pip install --upgrade pytube"')
from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog



ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
tk.messagebox.showinfo(title="message", message="Welcome to youtube downloader")
l=[]
link = simpledialog.askstring(title="input",
                                  prompt="Enter youtube link or enter 0 to stop taking input")

while(link!="0"):
    l.append(link)
    link = simpledialog.askstring(title="input",
                                  prompt="Enter youtube link or enter 0 to stop taking input")
dir= simpledialog.askstring(title="input",
                                  prompt="Enter the absolute directory to store the downloaded videos")
i=1
for li in l:
    youtube = YouTube(li)
    youtube.streams.filter(file_extension='mp4').get_highest_resolution().download(dir)
    tk.messagebox.showinfo(title="message", message="video {} downloaded".format(i))
    i=i+1;
tk.messagebox.showinfo(title="message", message="all videos are downloaded.....")
