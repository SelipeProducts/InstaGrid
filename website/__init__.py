from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from datetime import datetime

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['UPLOAD_FOLDER'] = 'website/static/'

    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_PATH'] = 'website/static'
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Blog

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    #Custom Filter for Jinja 
    def strf_time(my_time):
      # time_str = my_time.strftime('%B %d, %Y')
      date_to_str = datetime
      print(my_time)
      print('Type:', type(my_time))
      return my_time

    app.jinja_env.filters['strftime'] = strf_time


    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')  