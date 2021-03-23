from src import app, db
from src.forms import weatherForm
from flask import redirect, url_for, flash, Flask, render_template, request
from src.models import weatherReport, City

@app.route('/', methods=['GET'])
def weatherUpdate1():
    cities = City.query.all()
    return render_template('home.html',report=None, cities = cities, ureport= weatherReport)

@app.route('/result', methods=['POST'])
def weatherUpdate():
    city=request.form["city"]
    cities = City.query.all()
    report = weatherReport(city)
    print(report)
    return render_template('home.html', report=report, cities = cities, ureport= weatherReport)

@app.route('/addcity', methods=['POST'])
def addcity():
    city=request.form["add_city"]
    report = weatherReport(city)
    if report['cod'] == 200:
        c = City(city_name=city)
        db.session.add(c)
        db.session.commit()
    else:
        flash("City Not Found", category='danger')
    return redirect(url_for('weatherUpdate1'))      

    