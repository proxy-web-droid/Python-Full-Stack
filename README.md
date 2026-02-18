# Python-Full-Stack
Python full stack development
Flask + HTML/CSS + SQLite (Beginner friendly)

This is a minimal starter showing:
- Frontend: plain HTML/CSS (templates/index.html)
- Backend: Flask (app.py) serving / and /api/hello
- Database: SQLite (instance/app.db), initialized with `flask init-db`
- Editor: VS Code
- Browser: use for testing the UI

Quick start (macOS / Linux)
1. Create a Python virtual env:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Initialize the SQLite DB:
   ```
   flask init-db
   ```
4. Run the app:
   ```
   python app.py
   ```
   or
   ```
   FLASK_APP=app.py flask run
   ```
5. Open http://127.0.0.1:5000/ in your browser. The page fetches `/api/hello` and displays the message retrieved from SQLite.

Git & GitHub
- Initialize local git:
  ```
  git init
  git add .
  git commit -m "Initial commit"
  ```
- Option A (GitHub web UI): create a new repo on github.com, copy the remote URL, then:
  ```
  git remote add origin https://github.com/<you>/<repo>.git
  git branch -M main
  git push -u origin main
  ```
# Python-Full-Stack

A minimal full-stack example using Flask (backend), plain HTML/CSS templates (frontend), and SQLite (database). This repo implements registration, login, a simple dashboard, and a small API for fetching registered users.

What we built
- Frontend: templates located in the `Template` folder — `login.html`, `register.html`, and `dashboard.html`.
- Backend: `app. py` (Flask) with routes `/register`, `/login`, `/dashboard`, `/logout`, and `/api/users`.
- Database: SQLite database created at `database.db` (the app will also handle an existing `databse.db` if present). The app creates two tables: `users` and `Newtable` (simple username/password store).

Key features
- Passwords are hashed using Werkzeug (`generate_password_hash` / `check_password_hash`).
- Client-side registration form includes validation and submits via POST (fetch). Successful registration stores the user in `users` and a username entry in `Newtable`.
- The dashboard displays the current user and a list of usernames from `Newtable`.
- A JSON endpoint `/api/users` returns the list of registered users (without password hashes) for real-time fetch.
- If a pre-existing DB file is invalid, the app backs it up (adds `.bak` suffix) and creates a fresh database automatically.

Files of interest
- `app. py` — main Flask app and DB initialization (note: filename contains a space in this workspace).
- `Template/login.html` — login form template.
- `Template/register.html` — registration form with client-side validation and fetch submit.
- `Template/dashboard.html` — dashboard template that lists registered usernames.
- `database.db` — SQLite database file created at runtime (or `databse.db` if you had a misspelled file).

Quick start (Linux/macOS)
1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
2. Install dependencies (either with `requirements.txt` if you add one, or directly):
```bash
pip install flask werkzeug
```
3. Run the app (this runs `init_db()` on startup to create required tables):
```bash
python "app. py"
```
4. Visit the app in your browser:
   - Registration: http://127.0.0.1:5000/register
   - Login: http://127.0.0.1:5000/login
   - Dashboard (after login): http://127.0.0.1:5000/dashboard

Environment
- Optionally set `FLASK_SECRET` to a production secret before running the app:
```bash
export FLASK_SECRET="your-production-secret"
```

Notes and troubleshooting
- The app expects templates in the `Template` directory and static assets in `Static`. If you move folders, update `app. py` accordingly.
- If you see `sqlite3.DatabaseError: file is not a database`, the app will back up the problematic DB file to `database.db.bak` (or `.bakN`) and create a fresh database.
- The repo currently installs minimal dependencies at runtime; consider adding a `requirements.txt` with pinned versions for reproducible installs.

Want me to:
- add a `requirements.txt` and a simple `Makefile` for quick setup? Reply and I'll add them.

---
Updated to reflect the current full-stack implementation (Flask backend, HTML templates, SQLite database).
