from utilities import colors
from utilities.create import menu, widget
from utilities.utils import get_color

button_size = 75
metric = [['0', '0', '1', '1', '2', '2', '3'],
          ['0', '1', '1', '2', '2', '3', '3'],
          ['1', '1', '2', '2', '3', '3', '4'],
          ['1', '2', '2', '3', '3', '4', '5'],
          ['2', '2', '3', '3', '4', '5', '5'],
          ['2', '3', '3', '4', '5', '5', '6'],
          ['3', '3', '4', '5', '5', '6', '6']]


def show():
    base = menu.create("Metric")

    frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')

    for row in range(0, len(metric)):
        for col in range(0, len(metric[row])):
            widget.button(frame, "", button_size, True, get_color(int(metric[row][col])), 'white', None).grid(row=row, column=col, padx=1, pady=1)
