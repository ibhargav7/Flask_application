from src import app
from flask import redirect, url_for, flash, Flask, render_template


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')