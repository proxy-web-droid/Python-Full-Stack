#!/usr/bin/env python3
import sqlite3, os, json

ROOT = os.path.dirname(os.path.dirname(__file__))
db_path = 'database.db' if os.path.exists(os.path.join(ROOT, 'database.db')) else 'databse.db'
db_full = os.path.join(ROOT, db_path)
out_dir = os.path.join(ROOT, 'exports')
os.makedirs(out_dir, exist_ok=True)

print('Using DB:', db_full)
conn = sqlite3.connect(db_full)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def fetch_and_write(query, out_file):
    try:
        rows = cur.execute(query).fetchall()
        data = [dict(r) for r in rows]
        with open(os.path.join(out_dir, out_file), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print('Wrote', out_file, 'rows=', len(data))
    except Exception as e:
        print('Error fetching', out_file, e)

fetch_and_write('SELECT id,name,email,created_at FROM users', 'users.json')
fetch_and_write('SELECT id,username,created_at FROM Newtable', 'newtable.json')

conn.close()
print('Exports written to', out_dir)
