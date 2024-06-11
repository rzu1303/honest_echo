from flask import render_template
from flask_login import login_user, logout_user, current_user
from application.auth.forms import LoginForm
from application.auth import bp


@bp.route('/login')
def login():
    print("test3")
    form = LoginForm()
    return render_template('auth/login.html', title='Sign In', form=form)
