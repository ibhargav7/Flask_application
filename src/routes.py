from src import app
from src.forms import weatherForm
from src.models import city,data
from flask import redirect, url_for, flash, Flask, render_template, request
from src.models import weatherReport

@app.route('/', methods=['GET','POST'])

def weatherUpdate():
    form = weatherForm()
    if form.validate_on_submit():
        return redirect(url_for("weatherUpdate1"))

    return render_template('home.html', form=form)
@app.route('/result', methods=['GET','POST'])
def weatherUpdate1():
    form = weatherForm()
    city=request.form.get("city_name")
    report = weatherReport(city)
    return render_template('report.html', report=report, form=form)
@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        if search_word == '':
            pass
        else:
            data = city.query.filter(city.city.like(search_word))
    return render_template('home.html', city=data)
