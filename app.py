from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

ACCOUNTS = [
    {"username": "admin", "password": "password"},
    {"username": "user", "password": "password"}
]

@app.route('/')
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    for account in ACCOUNTS:
        if account['username'] == username and account['password'] == password:
            session['username'] = username
            return render_template('_content.html', username=username)

    return render_template('_login_form.html', error="Invalid credentials")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)