import customtkinter as ctk

font = "century gothic"


def label(master, text, size, text_color):
    result = ctk.CTkLabel(master=master, text=text, text_color=text_color, bg_color="transparent")

    if text.startswith('*') and text.endswith('*'):
        result.configure(text=text[1:-1], font=(font, size, 'bold'))
    else:
        result.configure(font=(font, size))

    return result


def button(master, text, size, squared, fg_color, hover_color, command):
    result = ctk.CTkButton(master=master, text=text, height=size, width=size * 4,
                           fg_color=fg_color, hover_color=hover_color)
    if squared:
        result.configure(height=size * 1.33, width=size * 1.33)
    if text.startswith('*') and text.endswith('*'):
        result.configure(text=text[1:-1], font=(font, size * 0.33, 'bold'))
    else:
        result.configure(font=(font, size * 0.33))
    if command is not None:
        result.configure(command=command)
    return result


def entry(master, text, size):
    result = ctk.CTkEntry(master=master, height=size, width=size * 4)
    if text:
        result.configure(placeholder_text=text)
    return result


def create_labeled_entry(master, frame_color, text, size, text_color, placeholder_text):
    frame = ctk.CTkFrame(master=master, fg_color=frame_color)
    frame.pack(pady=5, padx=10)

    label(frame, text, size*0.33, text_color).pack(padx=5, pady=5, side='left')
    result = entry(frame, placeholder_text, size)
    return result


def combobox(master, items):
    result = ctk.CTkComboBox(master=master, values=items)
    return result


def create_labeled_combobox(master, frame_color, text, items, size):
    frame = ctk.CTkFrame(master=master, fg_color=frame_color)
    frame.pack(pady=5, padx=10)

    label(frame, text, size*0.33, 'white').pack(padx=5, pady=5, side='left')
    result = combobox(frame, items)
    return result
