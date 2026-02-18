from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

APP_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(APP_DIR, 'database.db')

app = Flask(__name__, template_folder='Template', static_folder='Static')
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret-change-me')


def get_db_connection():
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row
  return conn


def init_db():
  conn = get_db_connection()
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      password_hash TEXT NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    '''
  )
  # Create students table for CRUD operations
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      course TEXT NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    '''
  )
  conn.commit()
  conn.close()


@app.route('/')
def index():
  return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')

  # POST: create user
  name = request.form.get('name', '').strip()
  email = request.form.get('email', '').strip().lower()
  password = request.form.get('password', '')

  if not name or not email or not password:
    return 'Missing fields', 400
  if len(password) < 6:
    return 'Password too short', 400

  password_hash = generate_password_hash(password)

  try:
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, email, password_hash) VALUES (?,?,?)',
           (name, email, password_hash))
    conn.commit()
    conn.close()
  except sqlite3.IntegrityError:
    return 'Email already registered', 409

  return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')

  email = request.form.get('email', '').strip().lower()
  password = request.form.get('password', '')

  conn = get_db_connection()
  user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
  conn.close()

  if user and check_password_hash(user['password_hash'], password):
    session['user_id'] = user['id']
    return redirect('/dashboard')

  return 'Invalid credentials', 401


@app.route('/dashboard')
def dashboard():
  uid = session.get('user_id')
  if not uid:
    return redirect('/login')
  conn = get_db_connection()
  user = conn.execute('SELECT id, name, email, created_at FROM users WHERE id = ?', (uid,)).fetchone()
  # include a short list of students for quick access (no sensitive data)
  newusers = conn.execute('SELECT id, name AS username, created_at FROM users ORDER BY created_at DESC LIMIT 5').fetchall()
  students_preview = conn.execute('SELECT id, name, email, course FROM students ORDER BY created_at DESC LIMIT 5').fetchall()
  conn.close()
  if not user:
    return redirect('/login')
  return render_template('dashboard.html', user=user, newusers=newusers, students_preview=students_preview)


### Student management routes (CRUD) ###


def require_login():
  if not session.get('user_id'):
    return False
  return True


@app.route('/students')
def students():
  if not require_login():
    return redirect('/login')
  conn = get_db_connection()
  rows = conn.execute('SELECT id, name, email, course, created_at FROM students ORDER BY id DESC').fetchall()
  conn.close()
  students = [dict(r) for r in rows]
  return render_template('student.html', students=students)


@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
  if not require_login():
    return redirect('/login')
  if request.method == 'GET':
    return render_template('add_student.html')

  name = request.form.get('name', '').strip()
  email = request.form.get('email', '').strip().lower()
  course = request.form.get('course', '').strip()

  if not name or not email or not course:
    return 'Missing fields', 400

  try:
    conn = get_db_connection()
    conn.execute('INSERT INTO students (name, email, course) VALUES (?,?,?)', (name, email, course))
    conn.commit()
    conn.close()
  except sqlite3.IntegrityError:
    return 'Email already exists for another student', 409

  return redirect('/students')


@app.route('/students/edit/<int:sid>', methods=['GET', 'POST'])
def edit_student(sid):
  if not require_login():
    return redirect('/login')
  conn = get_db_connection()
  student = conn.execute('SELECT id, name, email, course FROM students WHERE id = ?', (sid,)).fetchone()
  conn.close()
  if not student:
    return 'Student not found', 404

  if request.method == 'GET':
    return render_template('edit_student.html', student=student)

  # POST -> update student
  name = request.form.get('name', '').strip()
  email = request.form.get('email', '').strip().lower()
  course = request.form.get('course', '').strip()

  if not name or not email or not course:
    return 'Missing fields', 400

  try:
    conn = get_db_connection()
    conn.execute('UPDATE students SET name = ?, email = ?, course = ? WHERE id = ?', (name, email, course, sid))
    conn.commit()
    conn.close()
  except sqlite3.IntegrityError:
    return 'Email already exists for another student', 409

  return redirect('/students')


@app.route('/students/delete/<int:sid>', methods=['POST'])
def delete_student(sid):
  if not require_login():
    return redirect('/login')
  conn = get_db_connection()
  conn.execute('DELETE FROM students WHERE id = ?', (sid,))
  conn.commit()
  conn.close()
  return redirect('/students')


@app.route('/logout')
def logout():
  session.pop('user_id', None)
  return redirect('/login')


@app.route('/api/users')
def api_users():
  # Return basic user list for real-time fetch (no passwords)
  conn = get_db_connection()
  rows = conn.execute('SELECT id, name, email, created_at FROM users ORDER BY created_at DESC').fetchall()
  conn.close()
  users = [dict(r) for r in rows]
  return jsonify(users)


if __name__ == '__main__':
  init_db()
  app.run(host='0.0.0.0', port=5000, debug=True)

                      
 
           
              
            
             
  