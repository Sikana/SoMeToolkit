from flask import render_template, flash, g, session, redirect, url_for
from app import app

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

