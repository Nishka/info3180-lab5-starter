from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "37TK4iAJ5yXgrWi2Kx5YqmgzehGP2f5bpTuIjH9JRGFhMt432y6MJu7uHPFPKeowuFIIB9W"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj1:passwod@localhost/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
