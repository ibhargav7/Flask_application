from json import loads
from src import db
import requests

class city:
    city = db.Column(db.Integer(), nullable=False, unique=True )
    country = db.Column(db.String(length=30), nullable=False)
class data:
    def __init__(self,data):
        self.time = data['dt']
        self.city = data['name']
        self.country= data['sys']['country']
        self.main = data['weather'][0]['main']
        self.descreption = data['weather'][0]['description']
        self.icon = data['weather'][0]['icon']
        self.temp = data['main']['temp']
        self.feels_like = data['main']['feels_like']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.pressure = data['main']['pressure']
        self.humidity = data['main']['humidity']
        self.sea_level = data['main']['sealevel']
def weatherReport(city):
    api_key = "2a12d94d9078ebeebb34ccf5564f0cee"
    api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    print(api)
    response = requests.get(api)
    data = response.json()
    return data

    
