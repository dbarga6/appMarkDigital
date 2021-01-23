from flask import jsonify,render_template, request,redirect,url_for
from app.base import blueprint

from bcrypt import checkpw
from app import db, login_manager
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)


# ruta de inicio de twitter

@blueprint.route('/home')
@login_required
def init():
    return render_template("home.html")

@blueprint.route('/')
def route_default():
    return redirect(url_for('login_blueprint.login'))




@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500