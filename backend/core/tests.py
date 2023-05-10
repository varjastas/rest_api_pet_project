import requests
import json

inp = \
'''Enter the path to json. Format:
[
  {
    "model_name": {
      "field": data,
      "field2": "data"
      ...
    }
  },
  ...
  {
    "model_name_n": {
      "field": data,
      "field2": "data"
      ...
    }
  }
]
'''
json_name = input(inp)
with open(json_name, encoding="UTF-8") as f:
    data = json.load(f)

session = requests.Session()
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*"
}
session.headers.update(headers)

#Creating the table from json
URL = "http://localhost:8000" 
s = session.post(f"{URL}/import/", json=data)
print(s.content)


#Getting all model objects 
s = session.get(f"{URL}/detail/Catalog")
print(s.json())

#Getting specified model object
s = session.get(f"{URL}/detail/Product/1")
print(s.json())