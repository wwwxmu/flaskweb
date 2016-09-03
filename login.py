from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'shiyanlou' and  request.form['psw'] == 'shiyanlou':
            session['username'] = request.form['username']
            session['psw'] = request.form['psw']
            return redirect(url_for('index'))
        else:
            flash('login failed!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('psd', None)
    return redirect(url_for('index'))

app.secret_key = 'f\xa4\x9d\x8a?\x01[\x8ba\xec\xd4N\x95\xc0\x85\xa8\xd4%\x15\xad\xd9a\x87\xbf'

if __name__ == '__main__':
    app.debug = True
    app.run()
