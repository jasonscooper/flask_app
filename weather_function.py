# Using forecast.io API
import forecastio
# Using geopy package
from geopy.geocoders import Nominatim

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	api_key = os.environ['FORECAST_API_KEY']
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	return "{} and {}°".format(forecast.summary, forecast.temperature)




