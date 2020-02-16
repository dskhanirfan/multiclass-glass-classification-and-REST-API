# multiclass-glass-classification-and-REST-API

The glass classification study is important for criminological investigation. At the scene of the crime, the glass left can be used as evidence. USA Forensic science service made the data publically available at UCI. 


# Used Flask to serve a machine learning model as a RESTful webservice

write the following commands in the terminal to start the API:

  export FLASK_APP=operationlize.py
  flask run

On another terminal:
  python operationlize.py
  run the last block of code in notebook to see the API work
  
  url = "http://localhost:5000/predictions"
  data = json.dumps({'id':'139'}) 
  r = requests.post(url, data)
  print(r.json())
