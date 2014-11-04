from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app.auth.decorators import login_required

twitter = Blueprint('twitter', __name__, url_prefix='/twitter')

@twitter.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@twitter.route('/')
@twitter.route('/index')
@login_required
def twitter_index():
    return render_template('twitter/index.html')
