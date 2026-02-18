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
   # Python-Full-Stack

   A minimal full-stack example using Flask (backend), HTML templates (frontend), and SQLite (database).

   This project provides user registration/login and a secure, session-protected student management CRUD interface (add/view/edit/delete students). Passwords are stored hashed and all student routes require a logged-in user.

   Quick overview
   - Templates: located in the `Template/` folder (login, register, dashboard, student management pages).
   - Static assets: `Static/style.css` (responsive styles).
   - App: `app.py` — Flask application. Starts the DB on first run and exposes routes for auth and student CRUD.
   - Database: `database.db` (SQLite) in the project root. The app creates `users` and `students` tables automatically.
   - Export: `scripts/export_recent_logins.py` writes `exports/recent_logins.csv`.

   Getting started
   1. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   3. Start the app (this calls `init_db()` automatically to create missing tables):
   ```bash
   python app.py
   ```
   4. Open the app in your browser:
     - Register: http://127.0.0.1:5000/register
     - Login: http://127.0.0.1:5000/login
     - Dashboard (after login): http://127.0.0.1:5000/dashboard
     - Students manager: http://127.0.0.1:5000/students

   Notes
   - Only logged-in users can access `/students`, `/students/add`, `/students/edit/<id>`, and `/students/delete/<id>`. Direct URL access without login redirects to `/login`.
   - Passwords are hashed via Werkzeug; the app uses Flask `session` for authentication.

   Export recent logins
   Run the export script to generate a CSV of recent user activity:
   ```bash
   python scripts/export_recent_logins.py
   ```
   Output is written to `exports/recent_logins.csv`.

   Project structure (important files)
   - `app.py` — Flask app and routes.
   - `Template/` — HTML templates used by the app.
   - `Static/style.css` — global, responsive stylesheet.
   - `scripts/export_recent_logins.py` — export helper.
   - `requirements.txt` — Python dependencies.

   Security
   - Passwords are never stored as plaintext.
   - Session-based access control prevents unauthenticated CRUD operations.

   If you want, I can:
   - Create a test user automatically for quicker testing.
   - Run the server and open the students page in your browser.
```bash

python "app. py"

