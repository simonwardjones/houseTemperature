from flask import render_template
from . import routes

# Home page
@routes.route("/zoegs")
def zoegs():
    """render The Homepage"""
    return render_template('zoegs.html')

