from pprint import pprint
from flask import render_template, redirect, url_for, flash
from app import app, tools


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/<city>")
def weather(city):
    data: int | dict = tools.get_weather(city)
    if type(data) is int:
        flash(f"Wrong city name: {city}")
        return redirect(url_for("index"))
 
    pprint(data)
    return render_template("weather.html", data = data)
