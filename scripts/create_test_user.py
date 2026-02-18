#!/usr/bin/env python3
"""Create a test user with a known password (password is shown only on stdout).

The user's password is not stored in plaintext; it's hashed using Werkzeug.
"""
import os
import sqlite3
from werkzeug.security import generate_password_hash

ROOT = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT, 'database.db')

TEST_EMAIL = 'test@example.com'
TEST_NAME = 'Test User'
TEST_PASSWORD = 'TestPass123'

def main():
    if not os.path.exists(DB_PATH):
        print('Database not found at', DB_PATH)
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    existing = conn.execute('SELECT id FROM users WHERE email = ?', (TEST_EMAIL,)).fetchone()
    if existing:
        print(f'User already exists: {TEST_EMAIL} (id={existing[0]})')
        conn.close()
        print('Credentials:')
        print('  email:', TEST_EMAIL)
        print('  password:', TEST_PASSWORD)
        return

    pw_hash = generate_password_hash(TEST_PASSWORD)
    cur = conn.execute('INSERT INTO users (name, email, password_hash) VALUES (?,?,?)', (TEST_NAME, TEST_EMAIL, pw_hash))
    conn.commit()
    uid = cur.lastrowid
    conn.close()
    print('Created test user:', TEST_EMAIL, 'id=', uid)
    print('Credentials:')
    print('  email:', TEST_EMAIL)
    print('  password:', TEST_PASSWORD)

if __name__ == '__main__':
    main()
