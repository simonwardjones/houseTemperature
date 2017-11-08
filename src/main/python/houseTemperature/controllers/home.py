from flask import render_template
from . import routes

# Home page
@routes.route("/")
@routes.route("/home")
def home():
    """render The Homepage"""
    return render_template('home.html')

