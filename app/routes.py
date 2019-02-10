from datetime import datetime
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostPitchForm

# A decorator provides mapping between a url and a function.
# you can chain more than one url to the same fuction.
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    

@app.route('/')
@app.route('/index')
@login_required
def index():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''


    title = 'pitch view'
    
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
    return render_template('index.html', title=title, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Sign In'
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password          (form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            
        return redirect(url_for('index'))
        
      
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    '''[summary]
    
    Arguments:
        username {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    user = User.query.filter_by(username=username).first_or_404()
    posts = [
            {'author': user, 'body': 'Test post 1'},
            {'author': user, 'body': 'Test post 2'}     
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/post_pitch', methods=['GET', 'POST'])
@login_required
def post_pitch():
    form = PostPitchForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your pitch has been posted.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('post_pitch.html', title='Post Pitch',
                           form=form)


