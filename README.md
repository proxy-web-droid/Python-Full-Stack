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
- Option B (gh CLI):
  ```
  gh repo create <repo-name> --public --source=. --remote=origin --push
  ```
VS Code
- Open the project folder in VS Code.
- Install the Python extension.
- Select the interpreter `.venv`.
- Use the Run & Debug panel to run or debug (a sample launch config is in `.vscode/launch.json`).
https://www.linkedin.com/posts/anshika-bhadauriya-591340309_techinternship-maincrafts-activity-7416166912054910976-H1BC?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE6Juz0BGFfsNEmZRh0YlHiT4RNNFjdXETY
