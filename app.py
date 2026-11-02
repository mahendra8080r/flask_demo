from flask import Flask, render_template  # Flask core imports
import sqlite3                             # built-in SQLite database

app = Flask(__name__)  # create Flask app instance

DB_PATH = "students.db"  # database file path

def init_db():
    """Create table and insert sample data if not exists."""
    conn = sqlite3.connect(DB_PATH)       # connect to SQLite DB
    cursor = conn.cursor()

    # create students table if not already present
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT    NOT NULL,
            city TEXT    NOT NULL
        )
    """)

    # insert sample records only if table is empty
    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO students (name, city) VALUES (?, ?)",
            [
                ("Mahendra Rathod", "Nagpur"),
                ("Ravi Sharma",     "Pune"),
                ("Priya Patil",     "Mumbai"),
            ]
        )

    conn.commit()   # save changes
    conn.close()    # close connection

@app.route("/")
def index():
    """Fetch all students from DB and send to frontend."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, city FROM students")  # fetch all rows
    students = cursor.fetchall()   # returns list of tuples
    conn.close()
    return render_template("index.html", students=students)  # pass data to HTML

if __name__ == "__main__":
    init_db()                              # initialize DB on startup
    app.run(host="0.0.0.0", port=5000)    # host=0.0.0.0 enables remote URL access
