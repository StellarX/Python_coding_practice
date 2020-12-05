import json


with open("a.json") as f_obj:
    data = json.load(f_obj)

print(data)


