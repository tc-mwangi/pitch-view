from app import app

# A decorator provides mapping between a url and a function.
# you can chain more than one url to the same fuction.
@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'