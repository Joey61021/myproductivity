from datetime import datetime

from managers import database_manager
from menus import metric_menu
from utilities import colors
from utilities.create import menu, widget
from utilities.utils import convert_date, get_color

widget_size = 40


def show():
    if not database_manager.date_logged(datetime.now().strftime('%d-%m-%Y')):
        metric_menu.show()
        return

    base = menu.create("Overview")

    label_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')
    button_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')

    widget.label(label_frame, "Overview", widget_size*1.5, 'white').pack(padx=0, pady=10)

    entries = database_manager.get_entries()
    curr_entry = 0

    # TODO - correct overview widget orientation
    #  if row != round(len(entries)/7)+1 else convert_date(entries[len(entries) - 1][0]).weekday()-1

    for row in range(0, round(len(entries)/7)+1):
        for col in range(0, 7):
            try:
                widget.button(button_frame, str(entries[curr_entry][0]), widget_size, False, get_color(int(entries[curr_entry][1])), 'white', None).grid(row=row, column=col, padx=1, pady=1)
            except Exception:  # noqa
                widget.button(button_frame, "No data", widget_size, False, colors.button_null, 'white', None).grid(row=row, column=col, padx=1, pady=1)
            curr_entry += 1
