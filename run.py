import json, requests, pickle
url = "http://localhost:5000/predictions"
data = json.dumps({'id':'139'}) 
r = requests.post(url, data)

print(r.json())
