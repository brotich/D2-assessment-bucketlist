from flask import Blueprint

sample_mod = Blueprint('sample', __name__, url_prefix='/sample')


@sample_mod.route('/', methods=('GET',))
def sample_route():
    return 'endpoint works', 200
