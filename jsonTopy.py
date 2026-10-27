import json

#JSON string 
json_str = '{"name": "Harsh","pincode": 250001,"isAdmin": false,"other": null}'

#converting to python dictionary
parsed_json = json.loads(json_str)

#printing parsed JSON
print(parsed_json)