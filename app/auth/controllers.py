from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app.auth.models import users
from app.auth.forms import LoginForm
from app.auth.decorators import login_required

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = users.find_one({'email': form.email.data})
        if user and user['password'] == form.password.data:
            session['user'] = user['email']
            flash('Welcome %s!' % user['email'])
            return redirect(url_for('index'))

        flash('Invalid email or password', 'error-message')

    return render_template('auth/login.html', form=form)

