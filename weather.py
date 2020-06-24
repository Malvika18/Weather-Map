import requests
from pprint import pprint
city = input('Enter Your City:')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=55f72319e4bb6dd474e22e194a411d60&units=metric'.format(city)
res = requests.get(url)
data= res.json()

temp =data['main']['temp']
humidity= data['main']['humidity']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Humidity : {}'.format(humidity))
print('Wind Speed : {} m/sec'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))


# print(res)
# pprint(data)