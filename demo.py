from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    sum = a + b
    return 'sum = %d' %sum

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name = name)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
#    app.debug = True
#    app.run()

