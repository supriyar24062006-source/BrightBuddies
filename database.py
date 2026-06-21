import sqlite3

# Connect to database
conn = sqlite3.connect("brightbuddies.db")

cursor = conn.cursor()

# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    grade TEXT,
    subject TEXT,
    password TEXT NOT NULL
)
""")


# Tutor Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tutors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    qualification TEXT,
    subject TEXT,
    experience INTEGER,
    about TEXT,
    password TEXT NOT NULL
)
""")


# Booking Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    tutor_id INTEGER,
    booking_date TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()
conn.close()

print("BrightBuddies Database Created Successfully!")