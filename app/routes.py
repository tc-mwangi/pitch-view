from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

# A decorator provides mapping between a url and a function.
# you can chain more than one url to the same fuction.
@app.route('/')
@app.route('/index')
def index():

    title = 'pitch view'
    user = {'username': 'loise'}
    posts = [
        {
            'author': {'username': 'Loise'},
            'body': 'Tis a beautiful day in nairobi'
        },
        {
            'author': {'username': 'June'},
            'body': 'Some ugali please'
        }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Sign In'
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
        
    return render_template('login.html', title=title, form=form)