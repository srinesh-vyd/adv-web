from flask import Flask,url_for,render_template,redirect,request,abort
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('users.db', check_same_thread=False)

@app.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                           (username, password))
            user = cursor.fetchone()
            if user:
                return render_template('secretpage.html')
            else:
                return render_template('login.html',error =True)
    else:
        return render_template('login.html',error = False)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmpassword']

        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (firstname,lastname,username, password) VALUES (?,?,?, ?)",
                           (firstname,lastname,username, password))
        return render_template('thankyou.html')
    
    else:
        return render_template('signup.html')

@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.form['username']
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        return {'exists': user is not None}


if __name__ == '__main__':
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      firstname TEXT NOT NULL,
                      lastname TEXT NOT NULL,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL)''')

    app.run(debug=True)