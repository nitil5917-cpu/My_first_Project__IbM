import sqlite3

# Database connect karo
conn = sqlite3.connect("users.db")  # same file name
cursor = conn.cursor()

print("Current Users in DB:")

# Users table se data fetch karo
cursor.execute("SELECT * FROM users")
for r in cursor.fetchall():
    print(r)

conn.close()
