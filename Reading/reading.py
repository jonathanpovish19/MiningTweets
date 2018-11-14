import json

with open('python.json') as json_file:  
    data = json.load(json_file)
print(data)