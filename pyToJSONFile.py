import json

# test.json file will be created if not already exists
file = open("test.json",'w')

#python dictionary
my_dict = {"name":"harsh","age":26,"isAdmin":False}

# creating/writing the dictionary data to json file 
json.dump(my_dict,file)