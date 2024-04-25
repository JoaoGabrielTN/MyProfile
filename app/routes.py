from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm


@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html')

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'João'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/test')
def test():
    return render_template('test.html')