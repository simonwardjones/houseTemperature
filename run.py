from sys import path
path.append("src/main/python")

from houseTemperature.app import app
app.run(debug=True, host='0.0.0.0', port=5000)

