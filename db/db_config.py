import sqlite3

class db_config():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    	id integer PRIMARY KEY, 
    	username text NOT NULL, 
    	password text NOT NULL);""")
               
    
    def login (username, password):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
            print(cursor.fetchall())
            db.close()
            print("New user added to db")
            return 0