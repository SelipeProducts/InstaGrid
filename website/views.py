from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User, Profile, Blogs, Blogarray, Bloglist
import datetime

from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  profile = Profile.query.filter_by(id = current_user.profile_id).first()

  # if request.method == 'POST':
  #   note = request.form.get('note')

  #   if len(note) < 1:
  #     flash('Note is too short!', category='error')
  #   else:
  #     new_note = Note(data=note, user_id=current_user.id)
  #     db.session.add(new_note)
  #     db.session.commit()
  #     flash('Note added!', category='success')

  return render_template("home.html", user=current_user, profile=profile)


@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
      if note.user_id == current_user.id:
          db.session.delete(note)
          db.session.commit()

  return jsonify({})



@views.route('/profile', methods=['GET', 'POST'])
def profile():
  profile = Profile.query.filter_by(id=current_user.profile_id).first()

  # user = User.query.filter_by(email=email).first()
  if request.method == 'POST':
    f = request.files['pic']
    f.save(f.filename)

    bio = request.form.get('bio')
    url = request.form.get('url')
    pic = request.form.get('pic')

    print("Pic Notes:", pic)

    ###try to fix if mutiple profiles are being added
    if profile is not None:
      #if true if var exists
      update_profile = Profile.query.filter_by(id=current_user.profile_id).first()
      update_profile.bio = bio
      update_profile.url = url
      update_profile.pic = pic
      db.session.commit()

    else:
      new_profile = Profile(bio=bio, url=url, pic=pic)
      db.session.add(new_profile)
      db.session.commit()

      profile = Profile.query.filter_by(bio=bio).first()

    user = User.query.filter_by(id=current_user.id).first()

    user.profile_id = profile.id

    db.session.commit()

    

    return render_template('profile.html', user=current_user, profile=profile)

  bio = "Add a bio"
  url = "Add a url"
  pic = "profile_pic.jpg"
  temp_profile = Profile(bio=bio, url=url, pic=pic)
  db.session.add(temp_profile)
  db.session.commit()

  print(temp_profile)

  return render_template('profile.html', user=current_user, profile=temp_profile)


@views.route('/blogs', methods=['GET', 'POST'])
def blogs():
  # creating temp data
  # temp_blog = Blogs(title = "Title1", content="ABC", date=datetime.datetime.utcnow)
  # temp_blog2 = Blogs(title = "Title2", content="ABC", date=datetime.datetime.utcnow)
  # temp_blog3 = Blogs(title = "Title3", content="ABC", date=datetime.datetime.utcnow)
  # db.session.add(temp_blog)
  # db.session.add(temp_blog2)
  # db.session.add(temp_blog3)
  # db.session.commit()

  # blog1 = Blogs.query.filter_by(title='Title1').first()
  # blog2 = Blogs.query.filter_by(title='Title2').first()
  # blog3 = Blogs.query.filter_by(title='Title3').first()


  # blog_array = Blogarray(blog_id=blog1.title, array_id=0)

  # profile = Profile.query.filter_by(id=current_user.profile_id).first()
  # profile.bloglist_id = "Bloglist id......."

  # blog_list = Bloglist(blogarray_id= )
  

  return render_template('blogs.html', user=current_user)