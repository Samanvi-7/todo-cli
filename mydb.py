import sqlite3
from datetime import datetime


def create_todo(name):
    conn = sqlite3.connect("todos.db")


    cursor = conn.cursor()

    created = str(int(datetime.now().timestamp()))

    insert = """Insert into todo (name, created_at)  values(?,?) """
    cursor.execute(insert, (name, created))

    conn.commit()
    conn.close()
