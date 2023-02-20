import json
import requests 

url = "http://localhost:5000/create_activity"

with open('db.json') as f:
  data = json.load(f)

for js in data:
    x = requests.post(url, json = js)