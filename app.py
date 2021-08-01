
import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=cc605205b496f4d5334d53adc06d8432'
	city = 'Las Vegas'



	r = requests.get(url.format(city)).json()

	weather = {
		'city' : city,
		'min-temp' : r['main']['temp_min'],
		'max-temp' : r['main']['temp_max'],
		'temperature' : r['main']['temp'],
		'humidity' : r['main']['humidity'],
		'description' : r['weather'][0]['description'],
		'icon' : r['weather'][0]['icon']
	}

	print(weather)

	return render_template('index.html', weather=weather)

# main, description, icon, min/max temp, humidity