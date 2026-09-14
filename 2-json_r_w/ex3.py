import json
with open("data.json","r") as file_obj:
    person = json.load(file_obj)
print(person)