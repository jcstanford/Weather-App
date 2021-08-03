
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'

db = SQLAlchemy(app)

class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)


def get_weather_data(city):

	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=cc605205b496f4d5334d53adc06d8432&units=imperial'
	r = requests.get(url).json()
	return r


@app.route('/')
def index_get():

	cities = City.query.all()

	city = 'Las Vegas'

	weather_data = [ ]

	for city in cities:

		r = get_weather_data(city.name)

		weather = {
			'city' : city.name,
			'temperature' : r['main']['temp'],
			'humidity' : r['main']['humidity'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon']
		}

		weather_data.append(weather)

	return render_template('index.html', weather_data=weather_data)



@app.route('/', methods=['POST'])
def index_post():

	err_msg = ''
	new_city = request.form.get('city')

	if new_city:
		# check to see if city already exists in our sqlite database
		existing_city = City.query.filter_by(name=new_city).first()

		if not existing_city:
			new_city_data = get_weather_data(new_city)

			if new_city_data['cod'] == 200:
				new_city_obj = City(name=new_city)
				db.session.add(new_city_obj)
				db.session.commit()
			else:
				err_msg = 'City does not exist!'

		else:
			err_msg = 'City already submitted to database'

	if err_msg:
		flash(err_msg, 'error')
	else:
		flash('City added successfully!')

	return redirect(url_for('index_get'))

















