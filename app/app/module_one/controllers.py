## ---- Module_one routes ---- ##
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
#from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
#from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
#from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
front_end = Blueprint('fronte', __name__, url_prefix='/front_end')

# Set the route and accepted methods
@front_end.route('/')
def signin():
    return render_template('front_end/index.html');
