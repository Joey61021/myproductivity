from datetime import datetime

from managers import database_manager
from menus import overview_menu
from utilities import colors, utils
from utilities.create import menu, widget
from utilities.utils import get_color

widget_size = 50
metric = [['0', '0', '1', '1', '2', '2', '3'],
          ['0', '1', '1', '2', '2', '3', '4'],
          ['1', '1', '2', '2', '3', '4', '4'],
          ['1', '2', '2', '3', '4', '4', '5'],
          ['2', '2', '3', '4', '4', '5', '5'],
          ['2', '3', '4', '4', '5', '5', '6'],
          ['3', '4', '4', '5', '5', '6', '6']]


def show():
    base = menu.create("Metric")

    label_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')
    button_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')

    widget.label(label_frame, f'Log productivity for {datetime.now().strftime(utils.date_format)}', widget_size, 'white').pack(padx=0, pady=20)

    for row in range(0, len(metric)+1):
        cols = len(metric[row-1])
        for col in range(0, cols+1):
            if row == 0 and col == 0:
                continue
            if row == 0 or col == 0:
                text = f'{round((cols-col+1)/cols*100)}%\nTasks' if row == 0 else f'{round(row/(len(metric[col-1]))*100)}%\nSocial'
                widget.button(button_frame, text, widget_size, True, colors.button_null, colors.button_null, None).grid(row=row, column=col, padx=1, pady=1)
            else:
                widget.button(button_frame, "", widget_size, True, get_color(int(metric[row-1][col-1])), 'white',
                              lambda m=metric[row-1][col-1]: log_metric(m)).grid(row=row, column=col, padx=1, pady=1)


def log_metric(value):
    database_manager.log_day(int(value))
    overview_menu.show()
