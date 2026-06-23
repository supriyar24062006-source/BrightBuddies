import sqlite3

conn = sqlite3.connect("brightbuddies.db")
cursor = conn.cursor()

print("=== Tutors ===")
cursor.execute("SELECT * FROM tutors")
print(cursor.fetchall())

print("\n=== Students ===")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

print("\n=== Bookings ===")
cursor.execute("SELECT * FROM bookings")
print(cursor.fetchall())

conn.close()