#!/usr/bin/env python3
import sqlite3, os, csv

ROOT = os.path.dirname(os.path.dirname(__file__))
db_path = 'database.db' if os.path.exists(os.path.join(ROOT, 'database.db')) else 'databse.db'
db_full = os.path.join(ROOT, db_path)
out_dir = os.path.join(ROOT, 'exports')
os.makedirs(out_dir, exist_ok=True)

print('Using DB:', db_full)
conn = sqlite3.connect(db_full)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def fetch_and_write_csv(query, out_file, fieldnames):
    try:
        rows = cur.execute(query).fetchall()
        with open(os.path.join(out_dir, out_file), 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                row = dict(r)
                # Ensure only requested fields are written
                writer.writerow({k: row.get(k) for k in fieldnames})
        print('Wrote', out_file, 'rows=', len(rows))
    except Exception as e:
        print('Error fetching', out_file, e)

fetch_and_write_csv('SELECT id,name,email,created_at FROM users', 'users.csv', ['id','name','email','created_at'])
fetch_and_write_csv('SELECT id,username,created_at FROM Newtable', 'newtable.csv', ['id','username','created_at'])

conn.close()
print('CSV exports written to', out_dir)
