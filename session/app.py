from flask import Flask, render_template, request, redirect, session, make_response
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.permanent_session_lifetime = timedelta(minutes=5)  # Session expires after 5 minutes

@app.route('/')
def home():
    return "Welcome to the Flask Session and Cookie Demo!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect('/dashboard')
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome {session["username"]}! <a href="/logout">Logout</a>'
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/set_cookie')
def set_cookie():
    response = make_response('Cookie has been set!')
    response.set_cookie('user_id', '12345', secure=True, httponly=True, samesite='Lax')
    return response

@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get('user_id')
    if user_id:
        return f'User ID from cookie: {user_id}'
    return 'No cookie found.'

if __name__ == '__main__':
    app.run(debug=True)