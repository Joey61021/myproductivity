from datetime import datetime
from utilities import colors


def convert_date(date):
    return datetime.strptime(date, '%d-%m-%Y').date()


def get_color(value):
    if value == 0:
        return colors.button_lime
    elif value == 1:
        return colors.button_green
    elif value == 2:
        return colors.button_yellow
    elif value == 3:
        return colors.button_orange
    elif value == 4:
        return colors.button_pink
    elif value == 5:
        return colors.button_red
    elif value == 6:
        return colors.button_wine_red
