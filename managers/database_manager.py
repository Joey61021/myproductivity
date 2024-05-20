import sqlite3
from datetime import datetime

from utilities import logger, utils

file_name = "db.sql"
db = sqlite3.connect(file_name)


def connect():
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (

    date STRING, 
    metric INTEGER

    )''')

    db.commit()
    cursor.close()


def get_entries():
    cursor = db.cursor()

    cursor.execute('''SELECT * FROM entries''')
    retval = cursor.fetchall()

    cursor.close()
    return retval


def log_day(metric):
    cursor = db.cursor()

    cursor.execute('''INSERT OR IGNORE INTO entries (date, metric) VALUES (?, ?)''',
                   (datetime.now().strftime(utils.date_format), metric))
    db.commit()
    cursor.close()

    logger.connection(f'Values {datetime.now().strftime(utils.date_format)}, {metric} has been entered into table "entries"')


def date_logged(date):
    for entry in get_entries():
        if date == entry[0]:
            return True
    return False
