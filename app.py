from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# -------------------------
# HOME PAGE
# -------------------------

@app.route('/')
def home():
    return render_template('index.html')


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

    conn = sqlite3.connect('brightbuddies.db', timeout=10)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    (name, email, phone, grade, subject, password)
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

    conn = sqlite3.connect('brightbuddies.db', timeout=10)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tutors
    (name, email, phone, qualification, subject, experience, about, password)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email, phone, qualification, subject, experience, about, password))

    conn.commit()
    conn.close()

    return redirect(url_for('tutor_dashboard'))


@app.route('/tutor-dashboard')
def tutor_dashboard():
    return render_template('tutor_dashboard.html')


@app.route('/find_tutors')
def find_tutors():
    return render_template('index.html')


# -------------------------
# LOGIN SECTION
# -------------------------

@app.route('/login_student', methods=['POST'])
def login_student():

    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('brightbuddies.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE email=? AND password=?",
        (email, password)
    )

    student = cursor.fetchone()

    conn.close()

    if student:
        return redirect(url_for('student_dashboard'))
    else:
        return "Invalid Student Email or Password"


@app.route('/login_tutor', methods=['POST'])
def login_tutor():

    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('brightbuddies.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tutors WHERE email=? AND password=?",
        (email, password)
    )

    tutor = cursor.fetchone()

    conn.close()

    if tutor:
        return redirect(url_for('tutor_dashboard'))
    else:
        return "Invalid Tutor Email or Password"


# -------------------------
# ADMIN SECTION
# -------------------------

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')


# -------------------------
# RUN APP
# -------------------------

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001, debug=True)