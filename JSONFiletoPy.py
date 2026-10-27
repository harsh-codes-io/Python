import json

# loading the json file
file = open("test.json",'r')

# parsing the json file data
parsed_json = json.load(file)

#printing the parsed json as python dictionary 
print(parsed_json)