from flask import Flask, render_template
from grovepi import *
import math

app = Flask(__name__)
temp_sensor = 3
ultrasonic_ranger = 4
buzzer = 6
pinMode(buzzer, "OUTPUT")

@app.route("/getTemp")
def getTemp():
	temp = dht(temp_sensor, 0)
	return str(temp)

@app.route("/getDist")
def getDist():
	dist = ultrasonicRead(ultrasonic_ranger)
	if dist < 10:
		analogWrite(buzzer, 0)
	if dist >= 10 and dist < 15:
		analogWrite(buzzer, 15)
	if dist >= 15 and dist < 20:
		analogWrite(buzzer, 25)
	if dist >= 20:
		analogWrite(buzzer, 50)
	return str(dist)
	
@app.route("/")
def getStatus():
	try:
		[temp, hum] = dht(temp_sensor, 0)
		dist = ultrasonicRead(ultrasonic_ranger)
		if dist < 10:
			analogWrite(buzzer, 0)
		if dist >= 10 and dist < 15:
			analogWrite(buzzer, 15)
		if dist >= 15 and dist < 20:
			analogWrite(buzzer, 25)
		if dist >= 20:
			analogWrite(buzzer, 50)
		templateData = {'temp': temp, 'dist': dist}
		return render_template('assign2-b.html', **templateData)
	except:
		print("An error has occured")
		
if __name__ == '__main__':
	app.run(debug=True, port=1200, host='0.0.0.0')

