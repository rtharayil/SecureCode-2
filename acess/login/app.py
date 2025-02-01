from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3
from faker import Faker

app = Flask(__name__)
app.secret_key = 'supersecretkey'
fake = Faker()

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Modify the CREATE TABLE statement to include the 'email' column
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)''')
    
    # Now we can insert users with email values
    c.execute("INSERT OR IGNORE INTO users (username, password, email) VALUES ('admin', 'admin123', 'admin@example.com')")
    c.execute("INSERT OR IGNORE INTO users (username, password, email) VALUES ('user', 'user123', 'user@example.com')")


    
    # Create a table for customers if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS customers 
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, credit_card TEXT)''')
    
    # Check if the customers table is empty and populate it with fake data
    c.execute("SELECT COUNT(*) FROM customers")
    if c.fetchone()[0] == 0:
        for _ in range(1000):  # Add 10 random customers
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            credit_card = fake.credit_card_number()
            c.execute("INSERT INTO customers (name, email, phone, credit_card) VALUES (?, ?, ?, ?)", 
                      (name, email, phone, credit_card))
    
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

# Fetch all customers from the database
def get_customers():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()
    return customers

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        
   
        user = secure_login(username, password)
        if user:
            session['username'] = user[1]
            session['user_id'] = user[0]  # Store user ID to identify the user

            if user[1] is "admin":
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('profile', user_id=user[0]))
        else:
            message = "Secure Login Failed! Invalid credentials."

    return render_template('index.html', message=message)

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    # Fetch all customers, no access control, any logged-in user can see all customers' details
    customers = get_customers()
    return render_template('admin.html', username=session['username'], customers=customers)

@app.route('/profile/<int:user_id>')
def profile(user_id):
    if 'username' not in session:
        return redirect(url_for('index'))
    
    # Broken access control: Users can view any profile, not just their own
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE id=?", (user_id,))
    customer = c.fetchone()
    conn.close()

    if customer:
        # Display secret information like credit card (which should be restricted)
        return render_template('profile.html', customer=customer)
    else:
        flash("Profile not found.")
        return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
