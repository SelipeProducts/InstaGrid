from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# blog_list = db.Table('blog_list', 
#   db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#   db.Column('array_id', db.Integer, db.ForeignKey('blog_array.id'))
# )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    bio = db.Column(db.String(150))
    url = db.Column(db.String(150))
    pic = db.Column(db.String(150))
    notes = db.relationship('Note', backref='note_creater')
    blogs = db.relationship('Blog', backref='blog_creator')
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
class Blog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  pic = db.Column(db.String(150))
  title = db.Column(db.String(150))
  content =  db.Column(db.String(1000))
  post_date = db.DateTime(timezone=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
