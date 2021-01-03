from flask import Blueprint

blueprint = Blueprint(
    'nlp_blueprint',
    __name__,
    url_prefix='/nlp',
    template_folder='templates',
    static_folder='static'
)
