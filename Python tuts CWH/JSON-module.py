# 8-12-2020
# JSON module
# JavaScript Object Notation
# Used in web for mrssage sending and receiving
# load(): This method is used to load data from a JSON file into a python dictionary.
# Loads( ): This method is used to load data from a JSON variable into a python dictionary.
# dump():This method is used to load data from the python dictionary to the JSON file.
# dumps(): This method is used to load data from the python dictionary to the JSON variable.
import json

data =' {"var1":"mmw", "var2":"94"} '
print(data)
# print(data["var1"])  #It will throw an error
# print(data["var2"])  #It will throw an error
json_data = json.loads(data) # json.loads() takes string as an input and json.load() take file
print(json_data)
print(json_data["var1"])
print(json_data["var2"])

info = {
    "codefor" : "entrepreneur",
    "Be the" : "best of you",
    "coder" : "forever",
    "notTrue" : False
}

dump_info = json.dumps(info,sort_keys = True) #sort_keys parameter sorts the keys according to datatype
print(dump_info)
