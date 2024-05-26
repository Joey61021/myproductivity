from menus import overview_menu
from utilities import colors
from utilities.create import menu, widget

widget_size = 40


def show():
    base = menu.create("Metric")

    label_frame = menu.create_frame(base, colors.menu_base, 0, 0, 'top')
    overview_frame = menu.create_frame(base, colors.menu_frame, 0, 20, 'top')

    widget.label(label_frame, "Settings", widget_size, 'white').pack(padx=0, pady=20)

    widget.label(overview_frame, f"Changed your mind?", widget_size/1.5, 'white').pack(padx=10, pady=10, side='left')
    widget.button(overview_frame, "Go back", None, widget_size/1.5, False, colors.button_green, 'white', lambda: [None, overview_menu.show(), menu.destroy(base)][0]).pack(padx=10, pady=10, side='right')
