from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__,'views')

@views.route('/index')
def home():
    return render_template('index.html')

@views.route('/')
def root():
    return redirect('/index', 302)