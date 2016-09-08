from flask import Flask, render_template, request
import weather_function
app = Flask(__name__)

# weather_report = "The weather in San Diego is {}".format(weather_function.get_weather(address))

@app.route("/")
def index():
	address = request.values.get('address')
	forecast = None
	if address:
		forecast = weather_function.get_weather(address)
	return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run()