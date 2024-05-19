import os
import tkinter as tk

import customtkinter as ctk

import program
from utilities import colors

ctk.set_default_color_theme("dark-blue")

root = tk.Tk()

# Get icon file path
executable_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(executable_dir, "../../media/icon.ico")


def run():  # Start root
    root.mainloop()


def create(title):  # Create a menu
    # Menu appearance
    root.title(f"{title} | {program.name} {program.version}")
    root.iconbitmap(file_path)
    root.attributes('-fullscreen', True)
    root.state('zoomed')

    header = tk.Frame(root, bg=colors.menu_base)
    content = tk.Frame(root, bg=colors.menu_base)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')

    base = tk.Canvas(master=content, bg=colors.menu_base, borderwidth=0, highlightthickness=0)
    base.pack(pady=80, padx=0, anchor="center")

    return base


# Creates a frame above the base
def create_frame(base, color, padx, pady, side):
    frame = ctk.CTkFrame(master=base, fg_color=color)
    if side:
        frame.pack(padx=padx, pady=pady, side=side)
    else:
        frame.pack(padx=padx, pady=pady)
    return frame


# Destroy frame
def destroy(frame):
    frame.pack_forget()


# Terminate root
def terminate():
    root.destroy()
    quit()
