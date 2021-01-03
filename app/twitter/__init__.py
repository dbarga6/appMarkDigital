from flask import Blueprint

blueprint = Blueprint(
    'twitter_blueprint',
    __name__,
    url_prefix='/twitter',
    template_folder='templates',
    static_folder='static'
)
