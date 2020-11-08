import flask
from flask import render_template

import data

app = flask.Flask(__name__)

@app.route("/")
def main_page():
    print("Здесь будет главная")
    return render_template("index.html", tours=data.tours, departure_destinations=data.departures)


@app.route("/departures/<departure>/")
def departures(departure):
    print("Здесь будет направление")
    tours_by_departure = {}
    for id, tour in data.tours.items():
        if tour["departure"] == departure:
            tours_by_departure[id] = tour
    return render_template('departure.html', departure_data=tours_by_departure, departure_destinations=data.departures, destination=data.departures.get(departure))


@app.route("/tours/<int:id>/")
def tours(id):
    print("Здесь будет тур")
    return render_template("tour.html", tour_data=data.tours.get(id), departure=data.departures[data.tours.get(id)['departure']], departure_destinations=data.departures)


@app.route("/data")
def all_data():
    return render_template("data.html", tours_data=data.tours)


@app.route("/data/tours/<int:tour_id>/")
def tours_data(tour_id):
    return render_template("tour_data.html", tour_data=data.tours.get(tour_id))


@app.route("/data/departures/<departure>/")
def departure_data(departure):
    tours_by_departure = {}
    for id, tour in data.tours.items():
        if tour["departure"] == departure:
            tours_by_departure[id] = tour
    return render_template("departure_data.html", departure_data=tours_by_departure, destination=data.departures.get(departure))


if __name__ == "__main__":
    app.run()

