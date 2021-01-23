from app.login.forms import LoginForm,CreateAccountForm
from flask import jsonify,render_template, request,redirect,url_for
from app.login.models import User
from bcrypt import checkpw
from app import db, login_manager
from app.login import blueprint
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and checkpw(password.encode('utf8'), user.password):
            login_user(user)
            return redirect(url_for('login_blueprint.route_default'))
        return render_template('errors/page_403.html')
    if not current_user.is_authenticated:
        return render_template(
            'login.html',
            login_form=login_form,
            create_account_form=create_account_form
        )
    return  redirect(url_for('base_blueprint.init'))



@blueprint.route('/create_user', methods=['POST'])
def create_user():
    user = User(**request.form)
    db.session.add(user)
    db.session.commit()
    return jsonify('success')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'
## Errors

@blueprint.route('/')
def route_default():
    return redirect(url_for('login_blueprint.login'))