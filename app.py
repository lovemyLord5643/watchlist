from glob import escape
from flask import Flask, url_for
app = Flask(__name__)

@app.route("/user/<name>")
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='Roger'))
    print(url_for('user_page', name='Jesus'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'


 