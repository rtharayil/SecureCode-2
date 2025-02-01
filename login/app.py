from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Initialize the database
def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user', 'user123')")
    conn.commit()
    conn.close()

# Vulnerable login function (SQL Injection prone)
def vulnerable_login(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    return result

# Secure login function (using parameterized queries)
def secure_login(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_type = request.form['login_type']

        if login_type == 'vulnerable':
            user = vulnerable_login(username, password)
            if user:
                session['username'] = user[1]
                return redirect(url_for('admin'))
            else:
                message = "Vulnerable Login Failed! Invalid credentials."
        elif login_type == 'secure':
            user = secure_login(username, password)
            if user:
                session['username'] = user[1]
                return redirect(url_for('admin'))
            else:
                message = "Secure Login Failed! Invalid credentials."

    return render_template('index.html', message=message)

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    # Simulate critical customer information
    customers = [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210"},
        {"id": 3, "name": "Alice Johnson", "email": "alice@example.com", "phone": "555-555-5555"}
    ]
    
    return render_template('admin.html', username=session['username'], customers=customers)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)