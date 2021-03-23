from json import loads
from src import db
import requests
from flask import request,flash

class City(db.Model):
    city_name = db.Column(db.String(100), nullable=False, primary_key=True )

def weatherReport(city):
    api_key = "2a12d94d9078ebeebb34ccf5564f0cee"
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    print(api)
    response = requests.get(api)
    data = response.json()
    return data



