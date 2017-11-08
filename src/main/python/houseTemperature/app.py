#!venv/bin/python
from flask import Flask
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)

# import the Controllers package
from .controllers import routes

# to see what is in the Controllers package run print(dir(controllers))
# print(type(controllers))

# Now the routes blueprint is set up register the blueprints
app.register_blueprint(routes)

