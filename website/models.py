from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    notes = db.relationship('Note')

class Profile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  pic = db.Column(db.String(150))
  bio = db.Column(db.String(150))
  url = db.Column(db.String(150))
  bloglist_id = db.Column(db.Integer, db.ForeignKey('bloglist.id'))
  user = db.relationship('User')

class Bloglist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  blogarray_id = db.Column(db.Integer, db.ForeignKey('blogarray.id'))
  profile = db.relationship('Profile')

class Blogarray(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
  array_id = db.Column(db.Integer, db.ForeignKey('bloglist.id')) #should be same for allot 
  bloglist = db.relationship('Bloglist')
  bloglist = db.relationship('Blog')

class Blog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  pic = db.Column(db.String(150))
  title = db.Column(db.String(150))
  content =  db.Column(db.String(1000))
  post_date = db.DateTime(timezone=True)
  blogarray =  db.relationship('Blogarray')