import sqlite3
import db.db_config as db
import db.User as User

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute("select * from User where user_type = 1")
# print(cursor.fetchall())
# cursor.close()
# conn.close()

x= db.query_data(User.getUserInfo(3))
print(x)