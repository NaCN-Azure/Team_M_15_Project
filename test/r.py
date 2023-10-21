import sqlite3
conn = sqlite3.connect('../database.db')
cursor = conn.cursor()
query = "SELECT city, COUNT(*) FROM \"order\" GROUP BY city"
cursor.execute(query)
results = cursor.fetchall()
print(results)