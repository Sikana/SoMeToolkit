from functools import wraps
from flask import g, flash, redirect, url_for, request

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash('Please sign in to view this page.')
            return redirect(url_for('auth.login', nex=request.path))
        return func(*args, **kwargs)
    return decorated_function
