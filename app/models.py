from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from hashlib import md5

class User(UserMixin, db.Model):
    '''creates instances of users 
    
    Arguments:
        UserMixin {[type]} -- [description]
        db {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # relationship link
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # python method to print class to the console
    def __repr__(self):
        return '<user {}>'.format(self.username)

    # generate password hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # verify password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)





# tracks of user in user session
@login.user_loader
def load_user(id):
    return User.query.get(int(id))








# remember to add category property
class Post(db.Model):
    '''creates instances of posts
    
    Arguments:
        db {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''


    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # EAT time specific
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # establish relationship with user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    

# remember to add comments
# class Comment(db.model):



