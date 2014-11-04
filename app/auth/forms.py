from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email = TextField('User Name', [Required(), Email()])
    password = PasswordField('Password', [Required()])
