import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'brightbuddies.db')


def init_db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()


init_db()

# -------------------------
# HOME PAGE
# -------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------
# ABOUT PAGE
# -------------------------
@app.route('/about')
def about():
    return render_template('about_us.html')


# -------------------------
# CONTACT PAGE
# -------------------------
@app.route('/contact')
def contact():
    return render_template('contact_us.html')


# -------------------------
# FIND TUTORS (25 TUTORS + SEARCH)
# -------------------------
@app.route('/find_tutors')
def find_tutors():

    search = request.args.get('search', '').lower()

    tutors = [
        {"name": "Rahul Sharma", "subject": "Maths (Class 6–10)", "rating": "4.2"},
        {"name": "Priya Singh", "subject": "Science (Class 6–10)", "rating": "4.6"},
        {"name": "Arjun Patel", "subject": "Python (Degree)", "rating": "4.9"},
        {"name": "Sneha Reddy", "subject": "English (Class 1–5)", "rating": "3.8"},
        {"name": "Vikram Rao", "subject": "Physics (Class 11–12)", "rating": "4.1"},
        {"name": "Ananya Das", "subject": "Chemistry (Class 11–12)", "rating": "4.7"},
        {"name": "Kiran Kumar", "subject": "Biology (Class 8–10)", "rating": "3.5"},
        {"name": "Meera Nair", "subject": "Hindi (Class 1–10)", "rating": "4.0"},
        {"name": "Suresh Babu", "subject": "Social Studies (Class 6–10)", "rating": "2.9"},
        {"name": "Divya Menon", "subject": "Computer Science (Degree)", "rating": "5.0"},
        {"name": "Ravi Teja", "subject": "Maths (Degree)", "rating": "4.3"},
        {"name": "Kavya Sharma", "subject": "English Literature (Degree)", "rating": "3.9"},
        {"name": "Manoj Singh", "subject": "Physics (Degree)", "rating": "4.4"},
        {"name": "Pooja Verma", "subject": "Chemistry (Class 6–10)", "rating": "3.2"},
        {"name": "Akash Gupta", "subject": "Coding (Python/Java)", "rating": "4.8"},
        {"name": "Neha Iyer", "subject": "Primary School Tutor", "rating": "3.6"},
        {"name": "Siddharth Rao", "subject": "Advanced Maths", "rating": "4.5"},
        {"name": "Lakshmi Devi", "subject": "EVS (Class 1–5)", "rating": "2.8"},
        {"name": "Tarun Mehta", "subject": "Web Development", "rating": "5.0"},
        {"name": "Ishita Jain", "subject": "Accountancy (Degree)", "rating": "4.1"},
        {"name": "Amit Kumar", "subject": "Maths (Class 1–5)", "rating": "3.0"},
        {"name": "Riya Sen", "subject": "Science (Class 1–5)", "rating": "3.7"},
        {"name": "John Mathew", "subject": "Physics (Degree)", "rating": "4.6"},
        {"name": "Deepa Rani", "subject": "Chemistry (Degree)", "rating": "4.2"},
        {"name": "Vishal Singh", "subject": "Programming (C/C++)", "rating": "4.9"}
    ]

    # SEARCH FILTER
    if search:
        tutors = [
            t for t in tutors
            if search in t["name"].lower() or search in t["subject"].lower()
        ]

    return render_template("find_tutors.html", tutors=tutors, search=search)
 


# -------------------------
# STUDENT SECTION
# -------------------------
@app.route('/student-login')
def student_login():
    return render_template('student_login.html')


@app.route('/student-register')
def student_register():
    return render_template('student_register.html')


@app.route('/register_student', methods=['POST'])
def register_student():

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    grade = request.form['grade']
    subject = request.form['subject']
    password = request.form['password']

    conn = sqlite3.connect(DB_PATH, timeout=10)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, email, phone, grade, subject, password)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, phone, grade, subject, password))

    conn.commit()
    conn.close()

    return redirect(url_for('student_dashboard'))


@app.route('/student-dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')


# -------------------------
# TUTOR SECTION
# -------------------------
@app.route('/tutor-login')
def tutor_login():
    return render_template('tutor_login.html')


@app.route('/tutor-register')
def tutor_register():
    return render_template('tutor_register.html')


@app.route('/register_tutor', methods=['POST'])
def register_tutor():

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    qualification = request.form['qualification']
    subject = request.form['subject']
    experience = request.form['experience']
    about = request.form['about']
    password = request.form['password']

    conn = sqlite3.connect(DB_PATH, timeout=10)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tutors (name, email, phone, qualification, subject, experience, about, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email, phone, qualification, subject, experience, about, password))

    conn.commit()
    conn.close()

    return redirect(url_for('tutor_dashboard'))


@app.route('/tutor-dashboard')
def tutor_dashboard():
    return render_template('tutor_dashboard.html')


# -------------------------
# BOOK TUTOR
# -------------------------
@app.route('/book_tutor', methods=['GET', 'POST'])
def book_tutor():
    if request.method == 'GET':
        return render_template('booking_form.html')

    tutor = request.form.get('tutor')
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    message = request.form.get('message')

    conn = sqlite3.connect(DB_PATH, timeout=10)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tutor TEXT,
            name TEXT,
            email TEXT,
            phone TEXT,
            date TEXT,
            message TEXT
        )
    ''')

    cursor.execute(
        "INSERT INTO bookings (tutor, name, email, phone, date, message) VALUES (?, ?, ?, ?, ?, ?)",
        (tutor, name, email, phone, date, message)
    )

    conn.commit()
    conn.close()

    return render_template('booking_success.html', tutor=tutor, name=name)


# -------------------------
# LOGIN SECTION
# -------------------------
@app.route('/login_student', methods=['POST'])
def login_student():

    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE email=? AND password=?", (email, password))
    student = cursor.fetchone()

    conn.close()

    if student:
        return redirect(url_for('student_dashboard'))
    return "Invalid Student Email or Password"


@app.route('/login_tutor', methods=['POST'])
def login_tutor():

    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tutors WHERE email=? AND password=?", (email, password))
    tutor = cursor.fetchone()

    conn.close()

    if tutor:
        return redirect(url_for('tutor_dashboard'))
    return "Invalid Tutor Email or Password"


# -------------------------
# ADMIN
# -------------------------
@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')


# -------------------------
# RUN APP
# -------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)