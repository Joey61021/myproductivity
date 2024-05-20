import datetime

from managers import database_manager
from menus import overview_menu
from utilities import logger
from utilities.create import menu

author = "Joey"
version = '1.0.0'
name = "myProductivity"


if __name__ == '__main__':
    logger.info(f"{name} {version} starting for day: {datetime.datetime.now().day}/{datetime.datetime.now().month}...")

    logger.connection("Connecting to database...")
    database_manager.connect()
    logger.connection("Connection made to database")

    logger.info("Attempting to display start menu...")
    overview_menu.show()

    menu.run()
