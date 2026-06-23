
import sqlite3

# Connect to database
conn = sqlite3.connect("brightbuddies.db")

cursor = conn.cursor()

# -------------------------
# STUDENT TABLE
# -------------------------
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

# -------------------------
# TUTOR TABLE
# -------------------------
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

# -------------------------
# BOOKING TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor TEXT,
    name TEXT,
    email TEXT,
    phone TEXT,
    date TEXT,
    message TEXT
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("BrightBuddies Database Created Successfully!")

