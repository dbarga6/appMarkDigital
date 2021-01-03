from flask import Blueprint

blueprint = Blueprint(
    'mongodb_blueprint',
    __name__,
    url_prefix='/mongodb',
    template_folder='templates',
    static_folder='static'
)
