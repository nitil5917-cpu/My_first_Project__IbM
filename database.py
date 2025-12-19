import sqlite3

conn = sqlite3.connect("users.db") 
cursor = conn.cursor()

print("Current Users in DB:")

cursor.execute("SELECT * FROM users")
for r in cursor.fetchall():
    print(r)

conn.close()

