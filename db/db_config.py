import sqlite3
def get_connect():                  # To connect with the database_old
    return sqlite3.connect("database.db")
#   as db:
    #     cursor = db.cursor()
    #     cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    # 	id integer PRIMARY KEY,
    # 	username text NOT NULL,
    # 	password text NOT NULL);""")
    # return db

def query_data(sql):        # This method means to search the data from db, return with list with dict element
    database = get_connect()
    try:
        cursor = database.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        database.close()

def insert_or_delete_data(sql):
    database = get_connect()
    try:
        cursor = database.cursor()
        cursor.execute(sql)
        database.commit()
    finally:
        database.close()

# class db_config():
#     with sqlite3.connect("database_old.db") as db:
#         cursor = db.cursor()
#         cursor.execute("""CREATE TABLE IF NOT EXISTS users(
#     	id integer PRIMARY KEY,
#     	username text NOT NULL,
#     	password text NOT NULL);""")
#
#
#     def login (username, password):
#         with sqlite3.connect("database_old.db") as db:
#             cursor = db.cursor()
#             cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
#             print(cursor.fetchall())
#             db.close()
#             print("New user added to db")
#             return 0