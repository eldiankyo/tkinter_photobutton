import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('Photo Button Demo')

def download_clicked():
    showinfo(title='Information', message='Download button clicked!')

download_icon = tk.PhotoImage(file='./download.png')
download_button = ttk.Button(root, image=download_icon, command=download_clicked).pack()

root.mainloop()