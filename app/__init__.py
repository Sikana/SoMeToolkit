from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

mongo = MongoClient()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.auth.controllers import auth
app.register_blueprint(auth)

from app.twitter.controllers import twitter
app.register_blueprint(twitter)

from app import main
