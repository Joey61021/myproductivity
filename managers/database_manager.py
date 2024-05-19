import sqlite3

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
