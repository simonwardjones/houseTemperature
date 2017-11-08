# Temperature model
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from random import random
import os
from datetime import datetime 
import sys
# Just to check it is runnning
print("Script to Get temperature from firebase")

# Fetch the service account key JSON file contents
print(os.getcwd())
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(__location__ )
cred = credentials.Certificate(__location__+'/tempKey.json')

# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://temp-85c6b.firebaseio.com/'
})

# Set the reference to temperature
def getMostRecentTemp():
	# Set up the the temp reference	
	temp_ref = db.reference('/temperature')
	query = temp_ref.order_by_child('timestamp')
	# Get the most recent entry
	recentData = query.limit_to_last(1).get()

	# get the time satmp and temperature dict
	recentDataDict = list(recentData.items())[0][1]

	#Re-fromate the trimestamp
	recentDataDict["timestamp"] = recentDataDict["timestamp"]/1000

	# Add readable time
	utc_time = datetime.utcfromtimestamp(recentDataDict["timestamp"])
	#utc_time =  datetime.now()
	recentDataDict["readableTime"] = utc_time.strftime("%Y-%m-%d %H:%M:%S (UTC)")
	return recentDataDict

def getTemperatureSeries():
	# Set up the the temp reference	
	temp_ref = db.reference('/temperature')
	query = temp_ref.order_by_child('timestamp')
	# Get the most recent entry
	recentData = query.get()

	# get the time satmp and temperature dict
	temp_dict = list(recentData.items())

	# Get the temp and timestamp part in array
	#recentDataArray = [ [r[1]["timestamp"],r[1]["temperature"]] for r in temp_dict ]
	recentDataArray = [ KeyDict[1] for KeyDict in temp_dict ]

	#Re-fromate the trimestamp
	#recentDataDict["timestamp"] = recentDataDict["timestamp"]/1000

	return recentDataArray
	#
