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
    overview_frame = menu.create_frame(base, colors.menu_frame, 0, 20, 'top')

    widget.label(label_frame, f'Log productivity for {datetime.now().strftime(utils.date_format).replace("-", "/")}', widget_size, 'white').pack(padx=0, pady=20)

    widget.label(overview_frame, f"Changed your mind?", widget_size/1.5, 'white').pack(padx=10, pady=10, side='left')
    widget.button(overview_frame, "Go back", None, widget_size/1.5, False, colors.button_green, 'white', lambda: [None, overview_menu.show(), menu.destroy(base)][0]).pack(padx=10, pady=10, side='right')

    for row in range(0, len(metric)+1):
        cols = len(metric[row-1])
        for col in range(0, cols+1):
            if row == 0 and col == 0:
                continue
            if row == 0 or col == 0:
                text = f'{round((cols-col+1)/cols*100)}%\nTasks' if row == 0 else f'{round(row/(len(metric[col-1]))*100)}%\nSocial'
                widget.button(button_frame, text, None, widget_size, True, colors.button_null, colors.button_null, None).grid(row=row, column=col, padx=1, pady=1)
            else:
                widget.button(button_frame, "", None, widget_size, True, get_color(int(metric[row-1][col-1])), 'white',
                              lambda m=metric[row-1][col-1]: log_metric(m)).grid(row=row, column=col, padx=1, pady=1)


def log_metric(value):
    if not database_manager.date_logged(datetime.now().strftime(utils.date_format)):
        database_manager.log_day(int(value))
        overview_menu.show()
