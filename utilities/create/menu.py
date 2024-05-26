import os
import tkinter as tk
from datetime import datetime

import customtkinter as ctk
from PIL import Image

import program
from menus import settings_menu
from utilities import colors
from utilities.create import widget

ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

# Get icon file path
executable_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(executable_dir, "../../media/cog.png")

header_title: ctk.CTkLabel
update_id: str


def run():  # Start root
    root.mainloop()


def create(title):  # Create a menu
    # Menu appearance
    root.title(f"{title} | {program.name} {program.version}")
    # root.iconbitmap('root/media/icon.ico')
    root.attributes('-fullscreen', True)
    root.state('zoomed')

    # Add frames
    header = tk.Frame(root, bg=colors.menu_base)
    content = tk.Frame(root, bg=colors.menu_base)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=1)

    header.grid(row=0, sticky='news')
    content.grid(row=1, sticky='news')

    # Add labels
    global header_title
    header_title = title_label = widget.label(header, f"{program.name} | {datetime.now().strftime('%X')}", 18, 'white')
    title_label.pack(padx=12, pady=10, side="left")

    base = tk.Canvas(master=content, bg=colors.menu_base, borderwidth=0, highlightthickness=0)
    base.pack(pady=80, padx=0, anchor="center")

    button_image = ctk.CTkImage(Image.open(file_path), size=(22, 22))
    widget.button(header, '', button_image, 38, True, colors.button_null, 'white', lambda b=base: [None, destroy(b), settings_menu.show()][0]).pack(padx=12, pady=10, side="right")

    stop_update_loop()
    global update_id
    update_id = None
    update_time()

    return base


def update_time():
    text = f"{program.name} | {datetime.now().strftime('%X')}"
    header_title.configure(text=text)
    global update_id
    update_id = root.after(1000, update_time)


def stop_update_loop():
    try:
        root.after_cancel(update_id)
    except NameError:
        return


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
