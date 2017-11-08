# temperture controller
from flask import render_template
from . import routes
from ..models.temperature import  getMostRecentTemp , getTemperatureSeries
import json


@routes.route("/temperature")
def get_temperature():
	"""EndPoint for temperature"""
	temperature = 20
	mostrecentData = getMostRecentTemp()
	return json.dumps(mostrecentData)


@routes.route("/temperatureSeries")
def get_temperature_series():
	"""EndPoint for teperatureSeries"""
	mostrecentDataSeries = getTemperatureSeries()
	return json.dumps(mostrecentDataSeries)
