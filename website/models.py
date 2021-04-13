from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

blog_list = db.Table('blog_list', 
  db.collumn('user_id', db.Integer, db.ForeignKey('user.id')),
  db.collumn('array_id', db.Integer, db.ForeignKey('blogarray.id'))
)

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
    bloglist_rel = db.relationship('blog_array', secondary=blog_list, backref=db.backref('blogs'), lazy='dynamic')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Blogarray(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  blog_rel = db.relationship('Blog', backref='blog')

  
class Blog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  pic = db.Column(db.String(150))
  title = db.Column(db.String(150))
  content =  db.Column(db.String(1000))
  post_date = db.DateTime(timezone=True)
  
  array_id = db.Column(db.Integer, db.ForeignKey('blog_array.id'))

