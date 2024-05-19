from managers import database_manager
from utilities import colors
from utilities.create import menu, widget
from utilities.utils import convert_date, get_color

button_size = 40


def show():
    base = menu.create("Overview")

    frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')

    entries = database_manager.get_entries()
    curr_entry = 0

    for row in range(0, round(len(entries)/7)):
        for col in range(0, 7 if row != round(len(entries)/7)-1 else convert_date(entries[len(entries) - 1][0]).weekday()-1):
            try:
                widget.button(frame, str(entries[curr_entry][0]), button_size, False, get_color(int(entries[curr_entry][1])), 'white', None).grid(row=row, column=col, padx=1, pady=1)
            except Exception:  # noqa
                widget.button(frame, "Empty", button_size, False, colors.button_wine_red, 'white', None).grid(row=row, column=col, padx=1, pady=1)
            curr_entry += 1
