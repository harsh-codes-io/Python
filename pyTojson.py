import json 

#python dictionary
my_dict = {"name":"harsh","age":26,"isAdmin":False}

#converting to json string
json_str = json.dumps(my_dict)

#printing json string
print(json_str)