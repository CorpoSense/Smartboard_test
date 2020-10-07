from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad2438f83788a4e4225f5ef0db61a266'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-random-salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['FLASK_ADMIN_SWATCH'] = 'Darkly'
uploads_dir = os.path.join(app.instance_path, 'uploads')
'''os.makedirs(uploads_dir)'''



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

admin = Admin(app, template_mode='bootstrap3')

from application import routes
