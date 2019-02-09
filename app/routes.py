from app import app
from flask import render_template


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