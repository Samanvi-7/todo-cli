import sqlite3
from datetime import datetime

def create_connection(): #creating new db connection
    return sqlite3.connect("todos.db")

def create_table():
    conn=create_connection() #establising a db connection
    cursor=conn.cursor() #creating a cursor object to interact with db
    #creating a table 
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL ,
                   created_at TEXT NOT NULL)
                   ''')
    conn.commit() #commiting changes to the db
    conn.close() #closing the connection to the db


def create_todo(name):
    conn=create_connection() #establishing a db connection
    cursor=conn.cursor() #creating a cursor obj 
    created = str(int(datetime.now().timestamp())) #to generate timestamp for when task is created 
    #here datetime.now() is a function which returns the current date and time as an datetime object and .timestamp() is a method which converts the datetime object to a timestap which is a float value so we are using type conversion and converting it to an int and then finally to a str
    insert='''INSERT INTO todo(name,created_at) VALUES(?,?)'''  # '?' is a place holder
    cursor.execute(insert,(name,created))
    conn.commit()
    conn.close()
# Here , table creation query is a static query that dosent change based on user i/p and since its structure is known and fixed it can be written directly into execute method but for inserting data and deleting.. such operations involve dynamic data so its much safer to create a seperate variable to hold the query .  """


def delete_todo(task_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todo WHERE name = ?", (task_name,))
    conn.commit()
    conn.close()

def get_all_todos():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM todo")
    todos = cursor.fetchall() # Fetches all results from the executed SQL statement
    conn.close()
    return todos # Returns the list of all tasks and it should be placed after the db connection is closed to ensure the db conn is closed properly before the function exists and returns the list of tasks
