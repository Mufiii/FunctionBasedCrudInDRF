import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None) :
  data = {}
  if id is not None :
    data = {'id':id}
  json_data = json.dumps(data)
  r = requests.get(url = URL , data=json_data)
  data = r.json()
  print(data)
  
# get_data()

def post_data():
  data = {
    'name': 'Muhammed yassin',
    'roll': 123,
    'city': 'malappuram'
  }
  json_data = json.dumps(data)
  response = requests.post( url=URL , data=json_data)
  data = response.json()
  print(data)
  
# post_data()


def update_data():
  data = {
    'id':4,
    'name': 'Muhammed FARHAN',
    'roll': 125,
    'city': 'Kondotty'
  }
  json_data = json.dumps(data)
  response = requests.put( url=URL , data=json_data)
  data = response.json()
  print(data)
  
# update_data()

def delete_data():
  data = {'id':4}
  
  json_data = json.dumps(data)
  response = requests.delete( url=URL , data=json_data)
  data = response.json()
  print(data)
  
delete_data()