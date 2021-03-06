from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User, Blog

from datetime import date
from . import db
import json

import os
from werkzeug.utils import secure_filename

import jinja2


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  # profile = Profile.query.filter_by(id = current_user.profile_id).first()

  # if request.method == 'POST':
  #   note = request.form.get('note')

  #   if len(note) < 1:
  #     flash('Note is too short!', category='error')
  #   else:
  #     new_note = Note(data=note, user_id=current_user.id)
  #     db.session.add(new_note)
  #     db.session.commit()
  #     flash('Note added!', category='success')

  return render_template("home.html", user=current_user, counter = 0)


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
  user = current_user

  # user = User.query.filter_by(email=email).first()
  if request.method == 'POST':
    f = request.files['pic']
    if f.filename != '':
      # f.save(f.filename)
      f.save(os.path.join('website/static', f.filename))

    bio = request.form.get('bio')
    url = request.form.get('url')
    pic = f.filename

    if user:
      #if true if var exists
      if bio !='':
        user.bio = bio
      if url !='':
        user.url = url
      if pic:
        user.pic = pic

      db.session.commit()
      flash('Profile Successfully Updated!', category='success')

    else:
      flash('No user found!', category='error')
      # new_profile = Profile(bio=bio, url=url, pic=pic)
      # db.session.add(new_profile)
      # db.session.commit()
      # profile = Profile.query.filter_by(bio=bio).first()
    # user = User.query.filter_by(id=current_user.id).first()
    # user.profile_id = profile.id
    # db.session.commit()
    #return render_template('profile.html', user=current_user)
  return render_template('profile.html', user=current_user)


@views.route('/blogs', methods=['GET', 'POST'])
def blogs():
  blogs = Blog.query
  if blogs:
    pass
  else:
    #pre filled data
    pic1 = 'coding_notes.jpg'
    title1 = 'Having a notebook when coding is handy!'
    date1 = date(year=2016, month=2, day=3)
    content1 = '<p>Ever start a project and the internal logic has your mind running in circles? Sometimes its best to write down your ideas in a notebook to simplify the planning and development process</p> <p>We dont remember everything that pops up in our head. Having things jotted down helps us to not have to remember key ideas.</p>'

    pic2 = 'coding_glasses.jpg'
    title2 = 'Did not realize how much I needed glasses!'
    date2 = date(year=2020, month=2, day=16)
    content2 = ' <p> I had a prescription for glasses from 2016 but around 2019 I broke my only pair of glasses. Fast farward to 2021 and I barely got a new pair of glasses with an updated prescription.</p> <p>Im not blind blind but that doesnt make reading code without my glasses any easier. Now the text in my code is in HD hopefully I can find bugs easier!</p>'

    pic3 = 'coding_python1.jpg'
    title3 = 'From Java to Python'
    date3 = date(year=2021, month=3, day=21)
    content3 = '<p> Coding is one of my passions. If only I had practiced constantly and not taken random breaks. I first learned how to program in a Java Series held at CSULA. I learned everything from OOP to Data Structures and Algorithms. But Java (for me) wasnt the best language to solve different problems.</p> <p>Reinspired to improve my development skills I am now learning Python. I first started with beginner projects that just use the console. This include a hangman, cryptography, and search algorithm projects. Now I am working with Flask with Python.</p>'


    blog1 = Blog(pic=pic1, title=title1, post_date=date1, content=content1, user_id=current_user.id)
    blog2 = Blog(pic=pic2, title=title2, post_date=date2, content=content2, user_id=current_user.id)
    blog3 = Blog(pic=pic3, title=title3, post_date=date3, content=content3, user_id=current_user.id)

    db.session.add(blog1)
    db.session.add(blog2)
    db.session.add(blog3)

    db.session.commit()
    
    # env = jinja2.Environment()
    # env.filters['strftime'] = strf_time



  return render_template('blogs.html', user=current_user)


@views.route('/blogs/<indiv>')
def blogs_indiv(indiv):
  blog_indiv = Blog.query.filter_by(id=indiv).first()


  #html give page blog specific info
  return render_template('blogs_indiv.html', user=current_user,  blog = blog_indiv)


@views.route('/create', methods=['GET', 'POST'])
def create_blog():
  user = current_user
  if request.method == 'POST':
    f = request.files['pic']
    if f.filename != '':
      f.save(os.path.join('website/static', f.filename))

    title = request.form.get('title')
    content = request.form.get('content')
    pic = f.filename

        #user = User.query.filter_by(email=email).first()
    
    if user:
      new_blog = Blog(pic=pic, content=content, title=title, user_id=current_user.id)

      db.session.add(new_blog)
      db.session.commit()
      flash('Blog Successfully Created!', category='success')


    

  
  return render_template('create.html', user=current_user)
