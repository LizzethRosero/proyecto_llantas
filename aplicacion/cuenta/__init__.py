from flask import Blueprint

cuenta = Blueprint('cuenta', __name__, template_folder='templates')

from . import routes