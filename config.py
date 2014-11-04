import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'This will be changed in production.'

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'impossibru'

THREADS_PER_PAGE = 8

