from flask import Blueprint

web_bp = Blueprint('web', __name__, url_prefix='/web')


@web_bp.route('/monkey')
def monkey():
    return "hello monkey"
