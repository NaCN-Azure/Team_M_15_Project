import sqlite3
import db.db_config as db
import db.Bike as Bike
import db.Order as Order
import db.Report as Report
import db.User as User

query = """
    SELECT city, COUNT(*) FROM "order" 
    GROUP BY city
"""
x= db.query_data(query)
print(x)