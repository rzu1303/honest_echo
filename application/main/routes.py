from flask import render_template
from application.main import bp
from application.auth.forms import LoginForm

@bp.route('/')
@bp.route('/index')
def index():
    print("test2")
    form = LoginForm()
    user = {'username': 'Arzu'}

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