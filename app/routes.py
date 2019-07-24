from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Iago Breno'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Kawhi'},
            'body': 'Excited to play in Los Angeles!'
        },
        {
            'author': {'username': 'LeBron'},
            'body': 'Working hard based on a recovery approach!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)