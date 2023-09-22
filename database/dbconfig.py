import pymysql

# This file is more like an serviceImpl connected with database and the python itself
# It looks like a back-end but not a true one
# When use this method which I package, just import it, and send the sql sentence afterwards

def get_connect():                  # To connect with the database
    return pymysql.connect(         # This is my localhost, If you want to test yours, just switch
        host = 'localhost',
        user = 'root',
        password = '123456',
        database = 'bicycle',
        charset='utf8'
    )

def query_data(sql):        # This method means to search the data from db, return with list with dict element
    db = get_connect()
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        db.close()

def insert_or_delete_data(sql):
    db = get_connect()
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    finally:
        db.close()