from flask import Blueprint
routes = Blueprint('routes', __name__)

# import the submodules here so they get called in the app.py
# the sub modules reference the routes object we just made
from . import home
from . import temperature
from . import zoegs