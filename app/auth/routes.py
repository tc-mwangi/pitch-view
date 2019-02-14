from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
from app import db
from app.auth import bp
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from werkzeug.urls import url_parse
from app.models import User, Post



@bp.route('/login', methods=['GET', 'POST'])
def login():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    title = 'Sign In'
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password          (form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
            
        return redirect(url_for('main.index'))
        
      
    return render_template('auth/login.html', title=title, form=form)

@bp.route('/logout')
def logout():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    '''[summary]
    
    Returns:
        [type] -- [description]
    '''

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', title='Register', form=form)

