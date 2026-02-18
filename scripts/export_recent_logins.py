#!/usr/bin/env python3
"""
Export recent login data from the project's SQLite DB to exports/recent_logins.csv.

The script will use the `last_login` column if present; otherwise it falls back
to `created_at` as a proxy for recent activity.
"""
import csv
import os
import sqlite3

ROOT = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(ROOT, 'database.db')
OUT_DIR = os.path.join(ROOT, 'exports')
OUT_FILE = os.path.join(OUT_DIR, 'recent_logins.csv')

os.makedirs(OUT_DIR, exist_ok=True)

def has_column(conn, table, column):
    cur = conn.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    return column in cols

def main():
    if not os.path.exists(DB_PATH):
        print('Database not found at', DB_PATH)
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    use_last = has_column(conn, 'users', 'last_login')

    if use_last:
        q = 'SELECT id, name, email, last_login, created_at FROM users ORDER BY last_login DESC NULLS LAST'
    else:
        # fallback: use created_at as proxy for recent activity
        q = 'SELECT id, name, email, created_at as last_login, created_at FROM users ORDER BY created_at DESC'

    rows = conn.execute(q).fetchall()
    conn.close()

    with open(OUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'email', 'last_login', 'created_at'])
        for r in rows:
            writer.writerow([r['id'], r['name'], r['email'], r['last_login'], r['created_at']])

    print('Wrote', OUT_FILE)

if __name__ == '__main__':
    main()
