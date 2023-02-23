import requests 
from db import activities, emosocio_competencies

url = "http://localhost:5000/create_activity"

#with open('db.json') as f:
  #data = json.load(f)

for js in activities:
  x = requests.post(url, json = js)

url="http://localhost:5000/create_emosocio_competence"

for js in emosocio_competencies:
  x = requests.post(url, json = js)