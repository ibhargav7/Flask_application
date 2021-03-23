from src import app
from src.forms import weatherForm
from flask import redirect, url_for, flash, Flask, render_template, request
from src.models import weatherReport, cities

@app.route('/', methods=['GET'])
def weatherUpdate1():
    print(cities)
    form = weatherForm()
    if form.validate_on_submit():
        return redirect(url_for("weatherUpdate1"))
    return render_template('home.html',report=None, cities = cities, ureport= weatherReport)

@app.route('/result', methods=['POST'])
def weatherUpdate():
    city=request.form["city"]
    report = weatherReport(city)
    print(report)
    return render_template('home.html', report=report, cities = cities, ureport= weatherReport)

"""@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        if search_word == '':
            pass
        else:
            data = City.query.filter(city.city.like(search_word))
    return render_template('home.html', city=data)
"""