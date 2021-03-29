import json
import requests

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=548cdd3727af44c4f7e62aae9db8b6c7' % zip)

data = r.json()

print(data['weather'][0]['description'])