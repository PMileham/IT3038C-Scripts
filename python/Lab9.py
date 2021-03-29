import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()
for widget in range(len(data)):

    print("{} is {}.".format(data[widget]["name"], data[widget]["color"]))