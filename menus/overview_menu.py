import datetime
from datetime import datetime

from future.backports.datetime import timedelta

from managers import database_manager
from menus import metric_menu
from utilities import colors, utils
from utilities.create import menu, widget
from utilities.utils import get_color

widget_size = 40


def show():
    if not database_manager.date_logged(datetime.now().strftime(utils.date_format)):
        metric_menu.show()
        return

    base = menu.create("Overview")

    label_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')
    button_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')

    widget.label(label_frame, "Overview", widget_size*1.5, 'white').pack(padx=0, pady=10)

    entries = sorted(database_manager.get_entries(), key=lambda x: datetime.strptime(x[0], utils.date_format))
    total_days = (utils.convert_date(entries[len(entries)-1][0])-(utils.convert_date(entries[0][0]))).days

    curr_date = utils.convert_date(entries[0][0])
    curr_entry = 0

    def date_logged(date):
        for entry in entries:
            if str(date) == entry[0]:
                return True
        return False

    rows = round(total_days/7)+1
    for row in range(0, rows):
        for col in range(0 if row != 0 else utils.convert_date(entries[0][0]).weekday()+1, 7 if row != rows-1 else utils.convert_date(entries[len(entries)-1][0]).weekday()+1):
            if date_logged(curr_date):
                widget.button(button_frame, str(entries[curr_entry][0]), widget_size, False, get_color(int(entries[curr_entry][1])), 'white', None).grid(row=row, column=col, padx=1, pady=1)
                curr_entry += 1
            else:
                widget.button(button_frame, "No data", widget_size, False, colors.button_null, 'white', None).grid(row=row, column=col, padx=1, pady=1)
            curr_date = curr_date + timedelta(days=1)
